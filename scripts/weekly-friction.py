#!/usr/bin/env python3
"""weekly-friction.py — the weekly review artifact.

Produces ONE dated briefing the owner actually reads:
    briefings/YYYY-MM-DD-friction.md

It answers two questions:

  1. WHAT CHANGED THIS WEEK — notes added/modified in the last 7 days (via
     `git log`, falling back to file mtime), plus the count of unreconciled
     same-topic clusters currently outstanding.

  2. WHAT CONFLICTS — candidate CONTRADICTIONS between notes on the same topic.
     Same-topic candidate pairs come from reusing scripts/detect-duplicates.py's
     tag+entity clustering; within each cluster we compare sentences that mention
     a shared anchor and carry OPPOSING polarity cues (recommend vs avoid, better
     vs worse, faster vs slower, works vs fails, ...). These are *candidates* for
     the owner to adjudicate (CLAUDE.md "Contradiction Detector": quote both, ask
     the owner to clarify their position) — heuristic, not ground truth.

Default --dry-run prints the full briefing draft to stdout (writes nothing).
--apply writes it to briefings/. Stdlib only.
"""
from __future__ import annotations

import argparse
import datetime
import importlib.util
import re
import subprocess
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
VAULT = SCRIPTS.parent
PROCESSED = VAULT / "processed"
BRIEFINGS = VAULT / "briefings"
TODAY = datetime.date.today()
WINDOW_DAYS = 7

# Opposing polarity cue groups: a pair contradicts when one note's anchor
# sentence hits group[0] and the other's hits group[1] (order-insensitive).
POLARITY = [
    (r"\b(recommend(?:ed|s)?|prefer(?:red|s)?|should use|adopt|default|best|go[- ]to)\b",
     r"\b(avoid|deprecated|don'?t use|do not use|discourage|worst|against|abandon|obsolete|replaced|no longer)\b"),
    (r"\b(faster|fastest|speed[- ]?up|lower latency|cheaper|more efficient)\b",
     r"\b(slower|slowest|slowdown|higher latency|expensive|less efficient|overhead)\b"),
    (r"\b(better|superior|outperform(?:s|ed)?|wins?|improv(?:e|es|ed|ement))\b",
     r"\b(worse|inferior|underperform(?:s|ed)?|loses?|regress(?:es|ion)?|degrad(?:e|es|ed))\b"),
    (r"\b(works?|reliable|robust|scal(?:es|able)|solved)\b",
     r"\b(fails?|unreliable|brittle|doesn'?t scale|broken|unsolved|breaks)\b"),
    (r"\b(necessary|required|essential|must)\b",
     r"\b(unnecessary|optional|overrated|not needed|overkill)\b"),
]
NEG_SPLIT = re.compile(r"(?<=[.!?])\s+|\n+|^\s*[-*]\s+", re.M)


def load_detector():
    spec = importlib.util.spec_from_file_location("detect_duplicates", str(SCRIPTS / "detect-duplicates.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def split_body(text: str) -> str:
    if text.startswith("---"):
        m = re.match(r"^---\s*\n.*?\n---[ \t]*\n?(.*)$", text, re.S)
        if m:
            return m.group(1)
    return text


def sentences(text: str):
    out = []
    for s in NEG_SPLIT.split(text):
        s = s.strip()
        if not s:
            continue
        if "|" in s:                     # table row
            continue
        if s.startswith("#"):            # heading
            continue
        if s.startswith("[[") and s.endswith("]]"):  # bare wikilink line
            continue
        if s.endswith(":"):              # label / lead-in fragment
            continue
        if len(s.split()) < 6:           # too short to carry a real claim
            continue
        out.append(s)
    return out


def changed_this_week():
    """Notes touched in the last WINDOW_DAYS. Prefer git; fall back to mtime."""
    since = (TODAY - datetime.timedelta(days=WINDOW_DAYS)).isoformat()
    try:
        out = subprocess.run(
            ["git", "-C", str(VAULT), "log", f"--since={since}", "--name-only",
             "--pretty=format:", "--", "processed", "entities"],
            capture_output=True, text=True, timeout=60)
        if out.returncode == 0:
            files = sorted({ln.strip() for ln in out.stdout.splitlines()
                            if ln.strip().endswith(".md") and "index.md" not in ln})
            if files:
                return files, "git"
    except (OSError, subprocess.SubprocessError):
        pass
    cutoff = datetime.datetime.now() - datetime.timedelta(days=WINDOW_DAYS)
    files = []
    for folder in ("processed", "entities"):
        d = VAULT / folder
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            if p.name in ("index.md", "TAG-INDEX.md"):
                continue
            try:
                if datetime.datetime.fromtimestamp(p.stat().st_mtime) >= cutoff:
                    files.append(str(p.relative_to(VAULT)))
            except OSError:
                pass
    return files, "mtime"


def find_contradictions(dd):
    """Return list of dicts: {anchor, a_slug, a_sent, b_slug, b_sent, cue}."""
    notes, clusters = dd.notes, dd.clusters
    bodies = {}
    for i, n in enumerate(notes):
        p = VAULT / n["slug"]
        try:
            bodies[i] = split_body(p.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            bodies[i] = ""
    hits = []
    seen_pairs = set()
    for members in clusters:
        anchors = set()
        for i in members:
            anchors |= notes[i]["anchors"]
        for a_i in range(len(members)):
            for b_i in range(a_i + 1, len(members)):
                ni, nj = members[a_i], members[b_i]
                key = (min(ni, nj), max(ni, nj))
                if key in seen_pairs:
                    continue
                shared_anchor = notes[ni]["anchors"] & notes[nj]["anchors"]
                if not shared_anchor:
                    continue
                si, sj = sentences(bodies[ni]), sentences(bodies[nj])
                found = _pair_conflict(si, sj)
                if found:
                    seen_pairs.add(key)
                    hits.append({
                        "anchor": ", ".join(sorted(shared_anchor)[:4]),
                        "a_slug": notes[ni]["slug"], "a_sent": found[0],
                        "b_slug": notes[nj]["slug"], "b_sent": found[1],
                        "cue": found[2],
                    })
    return hits


CUE_STOP = set("""claude code agent agents llm llms model models tool tools data with that this
these those from your when what which will would could should about into more most best them they
their there here also than then very much many some such your ours also more using used use""".split())


def _content(sent):
    return {w for w in re.split(r"[^a-z0-9]+", sent.lower()) if len(w) > 4 and w not in CUE_STOP}


def _pair_conflict(si, sj):
    """A candidate contradiction: one sentence carries a polarity cue, the other
    the opposing cue, AND the two sentences share >=1 substantive content token
    (so they are about the same specific subject, not merely both mention Claude)."""
    for gi, (pa, pb) in enumerate(POLARITY):
        ra, rb = re.compile(pa, re.I), re.compile(pb, re.I)
        pos_a = [s for s in si if ra.search(s)]
        neg_b = [s for s in sj if rb.search(s)]
        neg_a = [s for s in si if rb.search(s)]
        pos_b = [s for s in sj if ra.search(s)]
        for left, right in ((pos_a, neg_b), (neg_a, pos_b)):
            for ls in left:
                lt = _content(ls)
                for rs in right:
                    if len(lt & _content(rs)) >= 2:   # share >=2 substantive tokens
                        return (ls[:240], rs[:240], f"polarity#{gi+1}")
    return None


def build_briefing(dd):
    changed, src = changed_this_week()
    n_clusters = len(dd.clusters)
    contradictions = find_contradictions(dd)

    L = []
    L.append("---")
    L.append(f"title: Weekly Friction Briefing — {TODAY.isoformat()}")
    L.append("type: note")
    L.append("tags: [knowledge-management]")
    L.append('description: "Weekly review: what changed and what conflicts. Auto-drafted by scripts/weekly-friction.py."')
    L.append("status: current")
    L.append(f"as_of: {TODAY.isoformat()}")
    L.append("---")
    L.append("")
    L.append(f"# Weekly Friction Briefing — {TODAY.isoformat()}")
    L.append("")
    L.append("> Auto-drafted by `scripts/weekly-friction.py`. Contradictions are heuristic "
             "*candidates* — read both quotes and decide. Nothing here modifies a note.")
    L.append("")
    L.append("## What changed this week")
    L.append("")
    L.append(f"- **{len(changed)}** note(s) added/modified in the last {WINDOW_DAYS} days (source: {src}).")
    L.append(f"- **{n_clusters}** same-topic clusters currently outstanding "
             "(see `docs/supersession-candidates.md`; reconcile via `scripts/nightly-reconcile.py`).")
    L.append("")
    if changed:
        for f in changed[:60]:
            L.append(f"- `{f}`")
        if len(changed) > 60:
            L.append(f"- … and {len(changed) - 60} more")
        L.append("")
    L.append("## Conflicts to resolve")
    L.append("")
    if not contradictions:
        L.append("_No candidate contradictions surfaced by the polarity heuristic this week._")
        L.append("")
    else:
        L.append(f"**{len(contradictions)}** candidate contradiction(s) — same topic, opposing claims:")
        L.append("")
        for k, c in enumerate(contradictions, 1):
            L.append(f"### {k}. topic: {c['anchor']}  _(cue: {c['cue']})_")
            L.append("")
            L.append(f"- `{c['a_slug']}`:")
            L.append(f"  > {c['a_sent']}")
            L.append(f"- `{c['b_slug']}`:")
            L.append(f"  > {c['b_sent']}")
            L.append("")
            L.append("  **Action:** confirm whether these genuinely conflict; if so, note your "
                     "current position (dated claim line) or supersede the stale one.")
            L.append("")
    L.append("## How to act on this")
    L.append("")
    L.append("- Reconcile outstanding clusters: review `docs/supersession-candidates.md`, "
             "then `python3 scripts/nightly-reconcile.py --apply` (or edit by hand).")
    L.append("- Fix health issues logged in `docs/health.md` (orphans, broken wikilinks).")
    L.append("")
    return "\n".join(L) + "\n", len(changed), len(contradictions)


def main() -> int:
    ap = argparse.ArgumentParser(description="Weekly contradiction/friction briefing.")
    ap.add_argument("--apply", action="store_true", help="write the briefing file (default: dry-run to stdout)")
    ap.add_argument("--dry-run", action="store_true", help="print the draft, write nothing (default)")
    args = ap.parse_args()
    apply = args.apply and not args.dry_run

    dd = load_detector()
    text, n_changed, n_conflict = build_briefing(dd)
    out = BRIEFINGS / f"{TODAY.isoformat()}-friction.md"

    mode = "APPLY" if apply else "DRY-RUN"
    print(f"weekly-friction [{mode}] — {n_changed} changed this week, "
          f"{n_conflict} candidate contradiction(s) -> {out.relative_to(VAULT)}\n")
    if apply:
        BRIEFINGS.mkdir(exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print(f"wrote {out}")
    else:
        print("----- BRIEFING DRAFT (dry-run; not written) -----\n")
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
