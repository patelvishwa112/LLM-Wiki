#!/usr/bin/env python3
"""
detect-duplicates.py  —  READ-ONLY same-topic cluster detector for the LLM Wiki.

Scans processed/*.md, groups notes that cover the SAME topic using the
reconciliation heuristic in docs/supersession.md, and writes a candidate
report to docs/supersession-candidates.md.

It NEVER modifies any note. It only reads frontmatter + the H1 title and
writes ONE report file. Stdlib only (no PyYAML, no third-party deps).

Heuristic (see docs/supersession.md for the full rationale + thresholds):

  1. PRIMARY-ENTITY ANCHOR. A tag is an "anchor" (topic-specific) if it is used
     in <= ANCHOR_DF_FRAC of notes; shared entities/ slug tokens also anchor.
     Generic connective tags (agents, claude-code, multi-agent, ...) are NOT
     anchors, so they never by themselves make two notes "the same topic".

  2. PER-ANCHOR CLUSTERING (no global chaining). For each anchor we take the
     notes carrying it and connect a pair when BOTH:
        (a) tag Jaccard >= TAG_JACCARD  OR  shared tag count >= SHARED_TAGS_MIN,
        (b) title+description token Jaccard >= TITLEDESC_JACCARD
     (or the strong fallback: tag Jaccard >= TAG_JACCARD_STRONG).
     Connected components are taken WITHIN that one anchor only, so a note that
     is both "graph-engineering" and "loop-engineering" cannot chain those two
     distinct topics into one blob.

  3. OVERLAP MERGE. Two components are merged only when their membership sets
     overlap by >= MERGE_OVERLAP (Jaccard) -- i.e. they are the same cluster
     seen via two anchors -- never merged by a single shared note.

  Within a cluster the note with the newest effective date (as_of > date >
  ingested) is the proposed CURRENT; the rest are proposed SUPERSEDED and point
  at it via superseded_by. Near-ties and missing dates are FLAGGED for human
  review rather than auto-ranked. Nothing is ever written back to a note.
"""

import os, re, sys, glob, datetime, itertools
from collections import defaultdict

# ---- tunable thresholds (single source of truth) ----------------------------
ANCHOR_DF_FRAC     = 0.03   # tag is topic-specific ("anchor") if used in <= 3% of notes
TAG_JACCARD        = 0.40   # min tag-set Jaccard for the normal gate
TAG_JACCARD_STRONG = 0.55   # tag Jaccard that qualifies a pair on its own
SHARED_TAGS_MIN    = 4      # OR: this many shared tags satisfies the tag gate
TITLEDESC_JACCARD  = 0.20   # min title+description token Jaccard
MERGE_OVERLAP      = 0.50   # merge two components when member-set Jaccard >= this
NEAR_TIE_DAYS      = 14      # top-2 dates within this window -> flag "co-current / review"
# -----------------------------------------------------------------------------

STOP = set("""a an the of for for to in on and or is are be as at by with from this that
these those it its into your you i how why what when which who whom whose we our us they
their them he she his her not no do does can will would could should vault note notes ai
llm llms guide part via using use used new 2025 2026 x post thread""".split())

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)
PROC = os.path.join(VAULT, "processed")
ENT  = os.path.join(VAULT, "entities")
OUT  = os.path.join(VAULT, "docs", "supersession-candidates.md")
TODAY = datetime.date.today()

def split_frontmatter(text):
    if not text.startswith("---"):
        return "", text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    return (m.group(1), m.group(2)) if m else ("", text)

def parse_fm(fm):
    """Tiny YAML-ish parser: scalars + block/inline lists. Good enough for this vault."""
    data, block = {}, None
    for raw in fm.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if block is not None and re.match(r"^\s*-\s+", raw):
            data[block].append(raw.strip()[1:].strip().strip('"\''))
            continue
        block = None
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val == "":
            data[key] = []
            block = key
        elif val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [x.strip().strip('"\'') for x in inner.split(",") if x.strip()] if inner else []
        else:
            data[key] = val.strip().strip('"\'')
    return data

def eff_date(fm):
    for k in ("as_of", "date", "ingested", "published", "updated", "created"):
        v = fm.get(k)
        if isinstance(v, str) and re.match(r"\d{4}-\d{2}-\d{2}", v):
            try:
                return datetime.date.fromisoformat(v[:10])
            except ValueError:
                pass
    return None

def toks(s):
    return {w for w in re.split(r"[^a-z0-9]+", (s or "").lower()) if w and w not in STOP and len(w) > 2}

def h1(body):
    m = re.search(r"^#\s+(.+)$", body, re.M)
    return m.group(1).strip() if m else ""

def jac(a, b):
    return len(a & b) / len(a | b) if (a or b) else 0.0

# ---- entity slugs (for the "shared primary entity" anchor) ------------------
entity_tokens = set()
for p in glob.glob(os.path.join(ENT, "*.md")):
    name = os.path.splitext(os.path.basename(p))[0]
    if name == "TAG-INDEX":
        continue
    entity_tokens.add(name.lower())
    for t in name.lower().split("-"):
        if len(t) > 3 and t not in STOP:
            entity_tokens.add(t)

# ---- load notes -------------------------------------------------------------
notes = []
for p in sorted(glob.glob(os.path.join(PROC, "*.md"))):
    try:
        text = open(p, encoding="utf-8", errors="replace").read()
    except OSError:
        continue
    fm_raw, body = split_frontmatter(text)
    fm = parse_fm(fm_raw)
    tags = fm.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    tags = [t.lower() for t in tags if t]
    slug = os.path.relpath(p, VAULT)
    title = (fm.get("title") if isinstance(fm.get("title"), str) else "") or h1(body) or os.path.basename(p)
    desc = fm.get("description") if isinstance(fm.get("description"), str) else ""
    notes.append({
        "slug": slug,
        "base": os.path.splitext(os.path.basename(p))[0].lower(),
        "tags": set(tags),
        "title": title,
        "desc": desc,
        "date": eff_date(fm),
        "type": fm.get("type", ""),
        "status": fm.get("status", ""),
        "td": toks(title + " " + desc),
    })

N = len(notes)
if N == 0:
    sys.exit("No processed notes found at " + PROC)

# ---- anchor tags: document frequency <= ANCHOR_DF_FRAC * N ------------------
df = defaultdict(int)
for n in notes:
    for t in n["tags"]:
        df[t] += 1
anchor_cutoff = max(2, round(ANCHOR_DF_FRAC * N))
anchor_tags = {t for t, c in df.items() if c <= anchor_cutoff}

for n in notes:
    a = {t for t in n["tags"] if t in anchor_tags}
    a |= (entity_tokens & (set(n["base"].split("-")) | n["tags"] | n["td"]))
    n["anchors"] = a

def similar(i, j):
    A, B = notes[i], notes[j]
    shared = A["tags"] & B["tags"]
    tj = jac(A["tags"], B["tags"])
    if tj >= TAG_JACCARD_STRONG:
        return True, tj
    gate_tag = tj >= TAG_JACCARD or len(shared) >= SHARED_TAGS_MIN
    gate_td = jac(A["td"], B["td"]) >= TITLEDESC_JACCARD
    return (gate_tag and gate_td), tj

# ---- per-anchor connected components (chaining confined to one topic) -------
def components(idxs):
    parent = {i: i for i in idxs}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for a, b in itertools.combinations(idxs, 2):
        ok, _ = similar(a, b)
        if ok:
            parent[find(a)] = find(b)
    comps = defaultdict(set)
    for i in idxs:
        comps[find(i)].add(i)
    return [c for c in comps.values() if len(c) > 1]

by_anchor = defaultdict(list)
for i, n in enumerate(notes):
    for a in n["anchors"]:
        by_anchor[a].append(i)

raw_clusters = []
for a, idxs in by_anchor.items():
    if len(idxs) < 2:
        continue
    raw_clusters.extend(components(idxs))

# ---- overlap-merge: same cluster seen via two anchors -----------------------
merged = []
for c in sorted(raw_clusters, key=len, reverse=True):
    placed = False
    for m in merged:
        if jac(c, m) >= MERGE_OVERLAP:
            m |= c
            placed = True
            break
    if not placed:
        merged.append(set(c))
# dedupe subsets
clusters = []
for c in sorted(merged, key=len, reverse=True):
    if not any(c < d for d in clusters):
        clusters.append(c)
clusters = [sorted(c) for c in clusters if len(c) > 1]

def cl_anchor_summary(members):
    c = defaultdict(int)
    for i in members:
        for a in notes[i]["anchors"]:
            c[a] += 1
    return [a for a, k in sorted(c.items(), key=lambda kv: -kv[1]) if k >= 2]

def rank(members):
    dated = sorted([i for i in members if notes[i]["date"]], key=lambda i: notes[i]["date"], reverse=True)
    undated = [i for i in members if not notes[i]["date"]]
    return dated, undated

def cl_newest(members):
    ds = [notes[i]["date"] for i in members if notes[i]["date"]]
    return max(ds) if ds else datetime.date.min

clusters.sort(key=lambda m: (len(m), cl_newest(m)), reverse=True)

# ---- write report -----------------------------------------------------------
lines = []
w = lines.append
w("---")
w("title: Supersession Candidates (auto-generated)")
w("type: note")
w("tags: [knowledge-management]")
w('description: "READ-ONLY detector output: same-topic note clusters + proposed current/superseded assignment. Regenerate with scripts/detect-duplicates.py."')
w("status: living")
w("as_of: %s" % TODAY.isoformat())
w("---")
w("")
w("# Supersession Candidates")
w("")
w("> **Auto-generated by `scripts/detect-duplicates.py` — do not hand-edit.** "
  "Read-only analysis; no note was modified. See `docs/supersession.md` for the model and thresholds.")
w("")
members_in_clusters = sum(len(c) for c in clusters)
w("- Scanned **%d** processed notes on **%s**." % (N, TODAY.isoformat()))
w("- Anchor cutoff: a tag is topic-specific when used in ≤ **%d** notes (≤ %.0f%% of corpus) → "
  "**%d** anchor tags + **%d** entity tokens. Generic connective tags are excluded." %
  (anchor_cutoff, ANCHOR_DF_FRAC*100, len(anchor_tags), len(entity_tokens)))
w("- Gates: tag Jaccard ≥ **%.2f** (or ≥ %d shared tags) **and** title/desc Jaccard ≥ **%.2f**, "
  "or strong tag Jaccard ≥ **%.2f**; clustered per-anchor then merged at ≥ %.0f%% member overlap." %
  (TAG_JACCARD, SHARED_TAGS_MIN, TITLEDESC_JACCARD, TAG_JACCARD_STRONG, MERGE_OVERLAP*100))
w("- Found **%d** same-topic clusters covering **%d** notes." % (len(clusters), members_in_clusters))
w("")
w("Legend: **CURRENT** = proposed `status: current` (newest `as_of`/`date`). "
  "**superseded** = proposed `status: superseded`, `superseded_by: <current>` (RETAINED, never deleted). "
  "⚠ = needs human review (near-tie or missing date).")
w("")

for ci, members in enumerate(clusters, 1):
    dated, undated = rank(members)
    anchors_sum = cl_anchor_summary(members)
    w("## Cluster %d — %s" % (ci, ", ".join("`%s`" % a for a in anchors_sum[:6]) or "(mixed)"))
    w("")
    flags = []
    if len(dated) >= 2:
        gap = (notes[dated[0]]["date"] - notes[dated[1]]["date"]).days
        if gap <= NEAR_TIE_DAYS:
            flags.append("⚠ top two within %dd — verify which is truly current (may be co-current / both-valid)" % gap)
    if undated:
        flags.append("⚠ %d note(s) undated — cannot rank, review manually" % len(undated))
    for f in flags:
        w("> %s" % f)
    if flags:
        w("")
    w("| role | note | date | type | tags |")
    w("|---|---|---|---|---|")
    if dated:
        cur = dated[0]
        w("| **CURRENT** | `%s` | %s | %s | %s |" % (
            notes[cur]["slug"], notes[cur]["date"], notes[cur]["type"] or "-",
            ", ".join(sorted(notes[cur]["tags"])[:8])))
        for i in dated[1:]:
            w("| superseded | `%s` | %s | %s | %s |" % (
                notes[i]["slug"], notes[i]["date"], notes[i]["type"] or "-",
                ", ".join(sorted(notes[i]["tags"])[:8])))
    for i in undated:
        w("| ⚠ undated | `%s` | (none) | %s | %s |" % (
            notes[i]["slug"], notes[i]["type"] or "-", ", ".join(sorted(notes[i]["tags"])[:8])))
    w("")
    if dated:
        cur_slug = os.path.splitext(os.path.basename(notes[dated[0]]["slug"]))[0]
        w("Proposed edits (additive, NOT applied): on each superseded note set "
          "`status: superseded` + `superseded_by: %s`; on the current note set `status: current`"
          "%s." % (cur_slug, (" + `supersedes:` listing the %d older slug(s)" % (len(dated)-1)) if len(dated) > 1 else ""))
        w("")

open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("Scanned %d notes; %d clusters (%d notes). Report -> %s" % (N, len(clusters), members_in_clusters, os.path.relpath(OUT, VAULT)))
