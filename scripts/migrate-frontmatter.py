#!/usr/bin/env python3
"""
migrate-frontmatter.py  (T6)  -- stdlib only, idempotent.

For each processed/*.md note (excluding the auto-generated index.md):
  * remap every tag via tags-migration.json, drop "__drop__", de-duplicate
    canonical tags (stable order); tags not in the map are kept if already
    canonical, else kept + flagged for review.
  * normalize `type` to the 6-value vocabulary (SCHEMA.v2 sec.3); missing/
    unknown -> `bookmark` (flagged).
  * add `status: current` if absent (existing status preserved).
  * add `as_of:` from existing `date:` (fallback `ingested:`); if neither
    exists, leave `as_of` absent and flag the note. Never invents a date.

Body (everything from the closing `---` onward) is preserved byte-for-byte.
All other frontmatter keys (incl. the malformed `related:` blocks that T7
repairs) are preserved verbatim. Line-transform, not a YAML round-trip.

Default = dry-run (writes nothing). Pass --apply to write notes + report.
"""
import sys, os, re, json, glob, argparse

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED = os.path.join(VAULT, "processed")
MAP_PATH = os.path.join(VAULT, "tags-migration.json")
TAX_PATH = os.path.join(VAULT, "docs", "taxonomy.md")
REPORT_PATH = os.path.join(VAULT, "docs", "migration-report.md")

# ---- SCHEMA.v2 sec.3 : 14 legacy type values -> 6 canonical ----
TYPE_MAP = {
    "bookmark": "bookmark",
    "article": "article", "paper": "article", "lecture": "article",
    "concept": "concept", "overview": "concept", "analysis": "concept",
    "summary": "concept", "research-synthesis": "concept",
    "note": "note", "processed-note": "note", "proposal": "note",
    "resource": "resource",
    "experiment": "experiment",
}
CANON_TYPES = {"bookmark", "article", "concept", "note", "resource", "experiment"}
STATUS_VOCAB = {"current", "superseded", "historical", "deprecated"}

KEYRE = re.compile(r'^[A-Za-z0-9_][\w\-]*:')

def load_map():
    with open(MAP_PATH, encoding="utf-8") as f:
        return json.load(f)

def load_canon():
    txt = open(TAX_PATH, encoding="utf-8").read()
    return set(re.findall(r'\*\*`([^`]+)`\*\*', txt))

def split_note(text):
    """Return (opening_line, fm_lines[], tail_str) or None if no frontmatter."""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None
    close = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            close = i
            break
    if close is None:
        return None
    return lines[0], lines[1:close], "".join(lines[close:])

def group_entries(fm_lines):
    """Group frontmatter into ordered [key, [raw_lines]] entries.
    A new top-level key starts a new entry; block-list items ('- x'),
    indented lines and blanks continue the current entry."""
    entries = []
    for ln in fm_lines:
        if KEYRE.match(ln):
            key = ln.split(":", 1)[0].strip()
            entries.append([key, [ln]])
        else:
            if entries:
                entries[-1][1].append(ln)
            else:
                entries.append([None, [ln]])
    return entries

def parse_scalar(lines):
    v = "".join(lines).split(":", 1)[1]
    return v.strip().strip('"').strip("'").strip()

def parse_tags(lines):
    after = "".join(lines).split(":", 1)[1]
    tags = []
    if "[" in after:  # inline flow list
        inner = after[after.index("[") + 1:]
        if "]" in inner:
            inner = inner[:inner.rindex("]")]
        for part in inner.split(","):
            t = part.strip().strip('"').strip("'").strip()
            if t:
                tags.append(t)
    else:  # block list; items may be at col 0 or indented
        for ln in lines[1:]:
            s = ln.strip()
            if s.startswith("-"):
                t = s[1:].strip().strip('"').strip("'").strip()
                if t:
                    tags.append(t)
    return tags

def remap_tags(tags, tmap, canon):
    out, seen, unknown = [], set(), []
    for t in tags:
        if t in tmap:
            c = tmap[t]
            if c == "__drop__":
                continue
        elif t in canon:
            c = t
        else:
            unknown.append(t)
            c = t
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out, unknown

def emit_tags(tags):
    if not tags:
        return "tags: []\n"
    return "tags:\n" + "".join("  - %s\n" % t for t in tags)

def process(text, tmap, canon):
    """Return (new_text, info). info describes what changed for the report."""
    parts = split_note(text)
    info = {"no_fm": False}
    if parts is None:
        info["no_fm"] = True
        return text, info
    opening, fm_lines, tail = parts
    entries = group_entries(fm_lines)

    keys = [e[0] for e in entries]
    date_val = ingested_val = None
    orig_type = None
    orig_tags = []
    existing_status = None
    for k, lines in entries:
        if k == "date" and date_val is None:
            date_val = parse_scalar(lines)
        elif k == "ingested" and ingested_val is None:
            ingested_val = parse_scalar(lines)
        elif k == "type" and orig_type is None:
            orig_type = parse_scalar(lines)
        elif k == "tags" and not orig_tags:
            orig_tags = parse_tags(lines)
        elif k == "status" and existing_status is None:
            existing_status = parse_scalar(lines)

    new_tags, unknown = remap_tags(orig_tags, tmap, canon)
    final_type = TYPE_MAP.get((orig_type or "").strip(), None)
    type_defaulted = final_type is None
    if type_defaulted:
        final_type = "bookmark"

    # rebuild entries
    out = [opening]
    for k, lines in entries:
        if k == "tags":
            out.append(emit_tags(new_tags))
        elif k == "type":
            out.append("type: %s\n" % final_type)
        else:
            out.append("".join(lines))
    # ensure the last frontmatter line ends with a newline before we append
    if out and not out[-1].endswith("\n"):
        out.append("\n")

    added_status = added_as_of = False
    as_of_val = None
    if "status" not in keys:
        out.append("status: current\n")
        added_status = True
    if "as_of" not in keys:
        as_of_val = date_val or ingested_val
        if as_of_val:
            out.append("as_of: %s\n" % as_of_val)
            added_as_of = True

    new_text = "".join(out) + tail

    info.update({
        "orig_tags": orig_tags,
        "new_tags": new_tags,
        "unknown_tags": unknown,
        "orig_type": orig_type,
        "final_type": final_type,
        "type_defaulted": type_defaulted,
        "no_tags": len(orig_tags) == 0,
        "existing_status": existing_status,
        "added_status": added_status,
        "added_as_of": added_as_of,
        "as_of_val": as_of_val if added_as_of else None,
        "has_as_of_already": "as_of" in keys,
        "date_val": date_val,
        "ingested_val": ingested_val,
        "missing_date": (date_val is None and ingested_val is None),
        "changed": new_text != text,
    })
    return new_text, info

def note_files():
    files = sorted(glob.glob(os.path.join(PROCESSED, "*.md")))
    return [f for f in files if os.path.basename(f) != "index.md"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry-run)")
    ap.add_argument("--samples", type=int, default=0, help="print before/after frontmatter for N sample notes")
    args = ap.parse_args()

    tmap = load_map()
    canon = load_canon()
    files = note_files()

    results = []
    tags_before = tags_after = 0
    vocab_after = set()
    type_final_counts = {}
    type_collapse = {}      # (orig -> final) -> count
    missing_date = []
    review = {"type_defaulted": [], "no_tags": [], "unknown_tags": [],
              "noncanonical_status": [], "no_frontmatter": [], "missing_as_of": []}
    changed = 0

    for path in files:
        name = os.path.basename(path)
        text = open(path, encoding="utf-8").read()
        new_text, info = process(text, tmap, canon)
        results.append((path, new_text, info))
        if info["no_fm"]:
            review["no_frontmatter"].append(name)
            continue
        tags_before += len(info["orig_tags"])
        tags_after += len(info["new_tags"])
        vocab_after.update(info["new_tags"])
        ft = info["final_type"]
        type_final_counts[ft] = type_final_counts.get(ft, 0) + 1
        key = ((info["orig_type"] or "<missing>"), ft)
        type_collapse[key] = type_collapse.get(key, 0) + 1
        if info["type_defaulted"]:
            review["type_defaulted"].append((name, info["orig_type"]))
        if info["no_tags"]:
            review["no_tags"].append(name)
        if info["unknown_tags"]:
            review["unknown_tags"].append((name, info["unknown_tags"]))
        if info["existing_status"] and info["existing_status"] not in STATUS_VOCAB:
            review["noncanonical_status"].append((name, info["existing_status"]))
        if info["missing_date"] and not info["has_as_of_already"]:
            missing_date.append(name)
            review["missing_as_of"].append(name)
        if info["changed"]:
            changed += 1

    n = len([r for r in results if not r[2]["no_fm"]])
    avg_before = tags_before / n if n else 0
    avg_after = tags_after / n if n else 0

    if args.samples:
        printed = 0
        for path, new_text, info in results:
            if info["no_fm"] or not info["changed"]:
                continue
            old = open(path, encoding="utf-8").read()
            def fm(t):
                s = split_note(t)
                return s[0] + "".join(s[1]) if s else "(no frontmatter)"
            print("=" * 70)
            print("SAMPLE:", os.path.basename(path))
            print("---- BEFORE ----")
            print(fm(old), end="")
            print("---- AFTER ----")
            print(fm(new_text), end="")
            printed += 1
            if printed >= args.samples:
                break

    print("\n===== SUMMARY (%s) =====" % ("APPLY" if args.apply else "DRY-RUN"))
    print("notes considered:", len(files), "| with frontmatter:", n,
          "| no-frontmatter skipped:", len(review["no_frontmatter"]))
    print("notes that would change:", changed)
    print("tags before (per-note total): %d  avg %.2f/note" % (tags_before, avg_before))
    print("tags after  (per-note total): %d  avg %.2f/note" % (tags_after, avg_after))
    print("unique canonical vocab present after: %d / 121" % len(vocab_after))
    print("type final counts:", dict(sorted(type_final_counts.items())))
    print("missing dates (no date & no ingested):", len(missing_date))
    print("type-defaulted to bookmark:", len(review["type_defaulted"]))
    print("notes with no tags:", len(review["no_tags"]))
    print("notes with unknown (kept) tags:", len(review["unknown_tags"]))
    print("notes with non-canonical existing status:", len(review["noncanonical_status"]))

    if args.apply:
        for path, new_text, info in results:
            if info["no_fm"]:
                continue
            old = open(path, encoding="utf-8").read()
            if new_text != old:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_text)
        write_report(n, tags_before, tags_after, avg_before, avg_after,
                     vocab_after, type_final_counts, type_collapse,
                     missing_date, review, changed, len(files))
        print("\nWROTE notes + report:", REPORT_PATH)

def write_report(n, tb, ta, ab, aa, vocab, tfc, collapse, missing_date,
                 review, changed, considered):
    L = []
    L.append("# Frontmatter Migration Report (T6)\n")
    L.append("_Generated by `scripts/migrate-frontmatter.py --apply`. Idempotent; safe to re-run._\n")
    L.append("## Scope\n")
    L.append("- Notes considered (`processed/*.md`, excluding `index.md`): **%d**" % considered)
    L.append("- Notes with valid frontmatter processed: **%d**" % n)
    L.append("- Notes without frontmatter (skipped): **%d**%s" %
             (len(review["no_frontmatter"]),
              (" — " + ", ".join(review["no_frontmatter"])) if review["no_frontmatter"] else ""))
    L.append("- Notes changed by this run: **%d**\n" % changed)
    L.append("## Tag vocabulary\n")
    L.append("- Legacy tag vocabulary collapsed: **1072 -> 121** canonical (per `docs/taxonomy.md`).")
    L.append("- Unique canonical tags actually present after migration: **%d / 121**" % len(vocab))
    L.append("- Per-note tag totals: **%d -> %d**" % (tb, ta))
    L.append("- Average tags/note: **%.2f -> %.2f**\n" % (ab, aa))
    L.append("## `type` collapse (14 -> 6)\n")
    L.append("Final `type` counts:\n")
    L.append("| type | count |\n|---|---|")
    for t, c in sorted(tfc.items()):
        L.append("| %s | %d |" % (t, c))
    L.append("\nOld -> new mapping observed:\n")
    L.append("| legacy type | canonical type | notes |\n|---|---|---|")
    for (o, f), c in sorted(collapse.items()):
        L.append("| %s | %s | %d |" % (o, f, c))
    L.append("\n## Notes missing dates (no `date:` and no `ingested:`)\n")
    L.append("`as_of` left absent for these (dates are never invented): **%d**\n" % len(missing_date))
    for nm in sorted(missing_date):
        L.append("- %s" % nm)
    L.append("\n## Review needed (ambiguous / non-standard)\n")
    L.append("### type defaulted to `bookmark` (missing/unknown legacy type): %d" % len(review["type_defaulted"]))
    for nm, ot in sorted(review["type_defaulted"]):
        L.append("- %s (was: %r)" % (nm, ot))
    L.append("\n### notes with no tags: %d" % len(review["no_tags"]))
    for nm in sorted(review["no_tags"]):
        L.append("- %s" % nm)
    L.append("\n### notes with unknown tags kept (not in map, not canonical): %d" % len(review["unknown_tags"]))
    for nm, ut in sorted(review["unknown_tags"]):
        L.append("- %s: %s" % (nm, ", ".join(ut)))
    L.append("\n### notes with non-canonical existing `status` (left untouched): %d" % len(review["noncanonical_status"]))
    for nm, st in sorted(review["noncanonical_status"]):
        L.append("- %s (status: %s)" % (nm, st))
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

if __name__ == "__main__":
    main()
