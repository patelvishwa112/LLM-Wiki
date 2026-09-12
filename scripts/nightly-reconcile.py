#!/usr/bin/env python3
"""nightly-reconcile.py — the nightly self-maintenance pass.

Three jobs, all conservative and additive (nothing is ever deleted; the mount
blocks deletion anyway):

  A. SUPERSESSION. Reuses scripts/detect-duplicates.py's same-topic clustering
     (imported directly — single source of truth for the heuristic + thresholds
     in docs/supersession.md). For clusters that are UNAMBIGUOUS it marks the
     older note(s) `status: superseded` + `superseded_by: <newer>` and the newer
     `status: current` + `supersedes: [<older>...]` (both retained). A cluster is
     auto-applied only when ALL of:
        - every member is dated (rankable),
        - the top-two effective dates are > NEAR_TIE_DAYS apart (not co-current),
        - no member looks like an intentional time-slice snapshot
          (…-landscape, -YYYY, "state of/as of", snapshot) — those need a human
          to choose historical-vs-superseded (supersession.md 4b.3).
     Everything else is left for docs/supersession-candidates.md (the detector's
     own report, refreshed each run) — listed, never touched.

  B. HEALTH SWEEP. Finds NEW orphans (processed/entities notes with no inbound
     wikilink) and NEW broken wikilinks (a [[target]] with no matching note), and
     appends them to a running docs/health.md. "New" = not seen on a prior run
     (state kept in docs/.health-state.json so the log doesn't repeat itself).

  C. as_of FLAG. Reports how many notes still lack `as_of`, and lists the
     genuinely UNDATEABLE ones (no as_of AND no date AND no ingested) — those
     break temporal ranking and are the actionable subset.

Default --dry-run (prints findings, writes nothing except the detector's own
read-only candidates report, which is regenerated on import). --apply performs
the frontmatter edits, appends to docs/health.md, and updates the state file.
Stdlib only.
"""
from __future__ import annotations

import argparse
import datetime
import importlib.util
import json
import re
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
VAULT = SCRIPTS.parent
PROCESSED = VAULT / "processed"
ENTITIES = VAULT / "entities"
HEALTH = VAULT / "docs" / "health.md"
STATE = VAULT / "docs" / ".health-state.json"
TODAY = datetime.date.today().isoformat()

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
# slug/title patterns that mark an intentional time-slice (keep as historical, not superseded)
TIMESLICE_RE = re.compile(r"(landscape|snapshot|-20\d{2}\b|\bstate of\b|\bas of\b|\bin 20\d{2}\b)", re.I)


# ---- reuse the detector's clustering (single source of truth) ---------------
def load_detector():
    spec = importlib.util.spec_from_file_location("detect_duplicates", str(SCRIPTS / "detect-duplicates.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # NB: regenerates docs/supersession-candidates.md (read-only detector output)
    return mod


# ---- minimal stdlib frontmatter split / edit --------------------------------
def split_note(text: str):
    """Return (fm_lines:list[str], body:str) or (None, text) if no frontmatter."""
    if not text.startswith("---"):
        return None, text
    m = re.match(r"^---\s*\n(.*?)\n---[ \t]*\n?(.*)$", text, re.S)
    if not m:
        return None, text
    return m.group(1).split("\n"), m.group(2)


def fm_get_scalar(fm_lines, key):
    pat = re.compile(rf"^{re.escape(key)}:\s*(.*)$")
    for ln in fm_lines:
        m = pat.match(ln)
        if m:
            return m.group(1).strip().strip("'\"")
    return None


def fm_set_scalar(fm_lines, key, value):
    """Set/replace a top-level scalar; return new fm_lines (does not mutate input)."""
    out, done = [], False
    pat = re.compile(rf"^{re.escape(key)}:\s*.*$")
    for ln in fm_lines:
        if not done and pat.match(ln):
            out.append(f"{key}: {value}")
            done = True
        else:
            out.append(ln)
    if not done:
        out.append(f"{key}: {value}")
    return out


def rebuild(fm_lines, body):
    fm = "\n".join(l for l in fm_lines if l is not None)
    return "---\n" + fm.rstrip("\n") + "\n---\n" + body.lstrip("\n") if body.strip() else "---\n" + fm.rstrip("\n") + "\n---\n"


def ensure_supersession_body(body: str, line: str) -> str:
    if line in body:
        return body
    if "## Supersession" in body:
        # append under existing section
        return body.rstrip() + "\n" + line + "\n"
    return body.rstrip() + "\n\n## Supersession\n\n" + line + "\n"


# ---- health: orphans + broken links -----------------------------------------
def all_note_stems():
    """Every resolvable wikilink target: basename stems across the vault + a few roots."""
    stems = set()
    for p in VAULT.rglob("*.md"):
        # skip gitignored personal areas
        rel = p.relative_to(VAULT).as_posix()
        if rel.startswith("Career/") or p.name.startswith("PERSONAL"):
            continue
        stems.add(p.stem)
    return stems


def scan_links():
    """Return (inbound_counts:dict[stem->int], broken:list[(src_rel, target)])."""
    stems = all_note_stems()
    inbound = {}
    broken = []
    for folder in (PROCESSED, ENTITIES):
        for p in sorted(folder.glob("*.md")):
            if p.name in ("index.md", "TAG-INDEX.md"):
                continue
            inbound.setdefault(p.stem, inbound.get(p.stem, 0))
    for p in VAULT.rglob("*.md"):
        rel = p.relative_to(VAULT).as_posix()
        if rel.startswith("Career/") or p.name.startswith("PERSONAL"):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        _, body = split_note(text)
        for m in WIKILINK_RE.finditer(text):
            target = m.group(1).split("|")[0].split("#")[0].strip()
            if "/" in target:
                target = target.rsplit("/", 1)[-1]
            if target.endswith(".md"):
                target = target[:-3]
            if not target:
                continue
            if target in inbound:
                inbound[target] += 1
            if target not in stems:
                broken.append((rel, target))
    return inbound, broken


def note_has_as_of(p: Path):
    text = p.read_text(encoding="utf-8", errors="replace")
    fm_lines, _ = split_note(text)
    if fm_lines is None:
        return False, False  # (has_as_of, has_any_date)
    def has(k):
        return fm_get_scalar(fm_lines, k) not in (None, "")
    return has("as_of"), (has("as_of") or has("date") or has("ingested"))


def load_state():
    if STATE.is_file():
        try:
            return json.loads(STATE.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            pass
    return {"orphans": [], "broken": [], "undateable": []}


# ---- health.md append (newest section on top) -------------------------------
HEALTH_HEADER = ("# Vault Health Log\n\n"
                 "> Auto-appended by `scripts/nightly-reconcile.py`. Newest section on top. "
                 "Only NEW findings are logged each run (state in `docs/.health-state.json`).\n\n")


def prepend_health_section(section: str):
    if HEALTH.is_file():
        text = HEALTH.read_text(encoding="utf-8")
        if not text.startswith("# Vault Health Log"):
            text = HEALTH_HEADER + text
        # insert after header block (first blockquote paragraph)
        idx = text.find("\n\n", text.find(">"))
        if idx == -1:
            new = text.rstrip() + "\n\n" + section
        else:
            new = text[:idx + 2] + section + text[idx + 2:]
    else:
        new = HEALTH_HEADER + section
    HEALTH.write_text(new, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Nightly supersession + health reconcile.")
    ap.add_argument("--apply", action="store_true", help="apply edits / append health (default: dry-run)")
    ap.add_argument("--dry-run", action="store_true", help="print findings, write nothing (default)")
    args = ap.parse_args()
    apply = args.apply and not args.dry_run
    mode = "APPLY" if apply else "DRY-RUN"

    dd = load_detector()
    notes, clusters, rank = dd.notes, dd.clusters, dd.rank
    near_tie = dd.NEAR_TIE_DAYS

    print(f"nightly-reconcile [{mode}] — {len(notes)} notes, {len(clusters)} clusters")

    # ---- A. supersession -----------------------------------------------------
    auto, flagged = [], []
    for members in clusters:
        dated, undated = rank(members)
        slugs = [notes[i]["slug"] for i in members]
        timeslice = any(TIMESLICE_RE.search(notes[i]["slug"]) or TIMESLICE_RE.search(notes[i]["title"] or "")
                        for i in members)
        reason = None
        if undated:
            reason = f"{len(undated)} undated member(s)"
        elif len(members) != 2:
            # multi-note clusters fragment several subtopics; supersession.md 4b.5
            # leaves merge-vs-supersede to a human curator. Only clean PAIRS auto-apply.
            reason = f"cluster of {len(members)} notes (curator decides merge-vs-supersede)"
        elif len(dated) < 2:
            reason = "only one dated member"
        else:
            gap = (notes[dated[0]]["date"] - notes[dated[1]]["date"]).days
            if gap <= near_tie:
                reason = f"top-two within {gap}d (co-current)"
            elif timeslice:
                reason = "contains time-slice snapshot (historical-vs-superseded is a human call)"
        if reason:
            flagged.append((slugs, reason))
            continue
        cur = dated[0]
        older = dated[1:]
        auto.append((cur, older))

    print(f"  A. supersession: {len(auto)} unambiguous cluster(s) auto-supersede, "
          f"{len(flagged)} flagged for review (see docs/supersession-candidates.md)")

    n_written = 0  # actual note files modified under --apply
    for cur, older in auto:
        cur_path = VAULT / notes[cur]["slug"]
        cur_stem = cur_path.stem
        older_stems = [Path(notes[i]["slug"]).stem for i in older]
        # current note: status: current + supersedes: [older...]
        cur_text = cur_path.read_text(encoding="utf-8", errors="replace")
        cur_fm, cur_body = split_note(cur_text)
        if apply and cur_fm is not None:
            want = "[" + ", ".join(older_stems) + "]"
            if fm_get_scalar(cur_fm, "status") != "current" or fm_get_scalar(cur_fm, "supersedes") != want:
                new_fm = fm_set_scalar(cur_fm, "status", "current")
                new_fm = fm_set_scalar(new_fm, "supersedes", want)
                new_body = cur_body
                for op in older_stems:
                    new_body = ensure_supersession_body(new_body, f"- supersedes: [[{op}]]")
                cur_path.write_text(rebuild(new_fm, new_body), encoding="utf-8")
                n_written += 1
        # older notes: status: superseded + superseded_by: current
        for i in older:
            op_path = VAULT / notes[i]["slug"]
            op_text = op_path.read_text(encoding="utf-8", errors="replace")
            op_fm, op_body = split_note(op_text)
            op_status = fm_get_scalar(op_fm, "status") if op_fm else None
            if apply and op_fm is not None:
                # never clobber a note already marked superseded/historical/deprecated
                if op_status in ("superseded", "historical", "deprecated"):
                    continue
                new_fm = fm_set_scalar(op_fm, "status", "superseded")
                new_fm = fm_set_scalar(new_fm, "superseded_by", cur_stem)
                new_body = ensure_supersession_body(op_body, f"- superseded by: [[{cur_stem}]]")
                op_path.write_text(rebuild(new_fm, new_body), encoding="utf-8")
                n_written += 1

    for cur, older in auto[:8]:
        print(f"     CURRENT {notes[cur]['slug']}  <= "
              + ", ".join(Path(notes[i]['slug']).stem for i in older))
    if len(auto) > 8:
        print(f"     ... and {len(auto) - 8} more")

    # ---- B. health sweep -----------------------------------------------------
    inbound, broken = scan_links()
    orphans = sorted(s for s, c in inbound.items() if c == 0)
    broken_ids = sorted({f"{src} -> [[{tgt}]]" for src, tgt in broken})
    state = load_state()
    new_orphans = [o for o in orphans if o not in set(state.get("orphans", []))]
    new_broken = [b for b in broken_ids if b not in set(state.get("broken", []))]

    # ---- C. as_of flag -------------------------------------------------------
    missing_as_of, undateable = 0, []
    for p in sorted(PROCESSED.glob("*.md")):
        if p.name == "index.md":
            continue
        has_as_of, has_date = note_has_as_of(p)
        if not has_as_of:
            missing_as_of += 1
        if not has_date:
            undateable.append(str(p.relative_to(VAULT)))
    new_undateable = [u for u in undateable if u not in set(state.get("undateable", []))]

    print(f"  B. health: {len(orphans)} orphans ({len(new_orphans)} new), "
          f"{len(broken_ids)} broken links ({len(new_broken)} new)")
    print(f"  C. as_of: {missing_as_of} notes missing as_of; "
          f"{len(undateable)} undateable ({len(new_undateable)} new)")
    for o in new_orphans[:10]:
        print(f"     new orphan: {o}")
    for b in new_broken[:10]:
        print(f"     new broken: {b}")

    # ---- write outputs (apply only) -----------------------------------------
    if apply:
        L = [f"## {TODAY} (nightly)", ""]
        L.append(f"- Scanned {len(notes)} notes; {len(clusters)} same-topic clusters "
                 f"({len(auto)} auto-superseded, {len(flagged)} flagged for review).")
        L.append(f"- Health: {len(orphans)} orphans total, {len(broken_ids)} broken wikilinks total.")
        L.append(f"- Temporal: {missing_as_of} notes missing `as_of`; {len(undateable)} undateable "
                 f"(no as_of/date/ingested).")
        L.append("")
        if new_orphans:
            L.append(f"### New orphans ({len(new_orphans)})")
            L += [f"- `{o}` — no inbound wikilinks" for o in new_orphans]
            L.append("")
        if new_broken:
            L.append(f"### New broken wikilinks ({len(new_broken)})")
            L += [f"- {b}" for b in new_broken]
            L.append("")
        if new_undateable:
            L.append(f"### New undateable notes ({len(new_undateable)})")
            L += [f"- `{u}` — no as_of/date/ingested" for u in new_undateable]
            L.append("")
        prepend_health_section("\n".join(L) + "\n")

        state = {
            "orphans": sorted(set(state.get("orphans", [])) | set(orphans)),
            "broken": sorted(set(state.get("broken", [])) | set(broken_ids)),
            "undateable": sorted(set(state.get("undateable", [])) | set(undateable)),
            "last_run": TODAY,
        }
        STATE.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
        print(f"\nAPPLY: {n_written} note file(s) edited, appended docs/health.md, updated state.")
    else:
        print("\nDRY-RUN: no note or health edits written "
              "(docs/supersession-candidates.md was refreshed by the read-only detector).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
