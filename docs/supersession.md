---
title: Supersession & Temporal Model
type: concept
tags: [knowledge-management]
description: "How a fact gets superseded while nothing is lost — the temporal/status frontmatter contract, claim-level history convention, reconciliation rules, and retrieval integration."
status: current
as_of: 2026-09-12
supersedes: SCHEMA.md
confidence: high
---

# Supersession & Temporal Model

The vault ingests many notes on the same fast-moving topic (agents, harnesses, models, evals)
across different dates with **no ordering and no supersession**, so a June claim and a September
claim about the same thing sit side by side with equal weight. This document defines how a fact is
**superseded without being lost**: the agent always knows which version is *current*, *most recent*,
and *most relevant*, yet can still retrieve the full history on request.

**Design principle — keep information, rank it.** We never delete a superseded note. We *close its
validity window* and point it at its replacement, exactly as temporal knowledge graphs do:
"when new information contradicts an existing fact, the old fact is marked invalid (not deleted), so
history is preserved" (Zep/Graphiti). This is a **bi-temporal** model: we track both *valid time*
(when a claim was true in the world) and *transaction time* (when the vault learned it).

This spec composes with two parallel efforts and does not change either's surface:
- **T1 retrieval** (`docs/retrieval-protocol.md`) already reserves a **status gate** and reads
  `status`/`date` from `INDEX.tsv`. This doc defines the exact values it gates on.
- **T2 schema** (`SCHEMA.v2.md`) already **reserves** the temporal fields under section 2. This doc
  is the authoritative definition of their vocabulary and semantics; T2 points here.

---

## 1. Frontmatter fields

All fields are **optional and additive**. A note with none of them behaves exactly as today
(retrieval treats a missing `status` as `current` — see §5), so we can roll the model out
incrementally without touching the ~540 existing notes.

```yaml
status: current            # current | superseded | historical | deprecated
as_of: 2026-08-14          # YYYY-MM-DD — date the note's claims were TRUE AS OF (valid-time)
supersedes: old-note-slug  # bare slug(s) this note replaces        (string or list)
superseded_by: new-slug    # bare slug that replaces this note      (string)
confidence: high           # high | medium | low
```

### `status` — retrieval visibility / supersession state (single axis)

| value | meaning | retrieval |
|---|---|---|
| `current` | The live, authoritative version of this topic. **Default** — an omitted `status` is treated as `current`. | shown |
| `superseded` | A newer note now carries the current view of the **same topic**. Kept for provenance; must set `superseded_by`. | gated out by default; shown on history request |
| `historical` | Describes a state of the world that was true then and is intentionally kept as a time-slice (e.g. "the agent-memory landscape as of 2026-06"). Not wrong, just not current. | gated out by default; shown on history / timeline request |
| `deprecated` | The note's guidance is now considered wrong or harmful and should not be acted on, but is retained so the record and any inbound links survive. | gated out by default; shown only if explicitly asked |

`status` is **single-axis** (supersession/visibility), never a topic or type — those live in `tags`
and `type` (T2 §4 faceting rule).

### `as_of` — valid-time anchor

The date the note's claims were **true as of** — *valid time* in bi-temporal terms ("when the fact
was true in the real world"), as distinct from `date`/`ingested`, which are *transaction time*
("when the system learned the fact"). Use `as_of` for recency ranking and for ordering a topic's
history; it is the field a note author bumps when they re-verify or refresh a living note without
re-ingesting it. When absent, retrieval falls back to `date` → `ingested` (already the INDEX.tsv
date-precedence). Format `YYYY-MM-DD`.

### `supersedes` / `superseded_by` — the supersession edge

A directed edge between two notes on the same topic. `new` sets `supersedes: old`; `old` sets
`superseded_by: new`. They are **inverses and should always be set as a pair** (the reconciliation
procedure in §4 does exactly that).

**Format: bare slug, not a `[[wikilink]]`.** This is deliberate and matters for composition:
- The vault has a **hard rule** (CLAUDE.md, SCHEMA.v2 §2) that `[[wikilinks]]` must never appear in
  YAML — they break PyYAML and the TAG-INDEX generator.
- T2 already reserved these as bare slugs (`supersedes: old-note-slug`), and T1's `INDEX.tsv`
  builder reads a slug, not a link.

So the machine-facing edge is a bare slug (`superseded_by: on-policy-distillation-aha-neural-avb`),
and **human/Obsidian navigability is preserved in the body** via a `## Supersession` line with the
real `[[wikilink]]` (see §3). `supersedes` may be a YAML list when one note absorbs several.
(If a project later wants the edge clickable in Obsidian's frontmatter graph, the *quoted* form
`superseded_by: "[[slug]]"` is YAML-safe — the vault already quotes `raw: "[[...]]"` — but then the
index builder must strip the brackets; bare slug is the recommended canonical form.)

### `confidence` — trust in the claim

`high | medium | low`. Orthogonal to recency: a brand-new note can be `low` (single unverified X
post) and an old note `high` (a paper you've re-checked). Retrieval may use it as a minor tiebreaker
and to caveat answers; §4 uses it when two same-date notes conflict.

### Interaction with T2's reserved set

T2 `SCHEMA.v2.md` §2 listed a first-pass `status: draft | living | stable | superseded`. Those extra
values are **note-maturity**, an axis orthogonal to supersession, and folding two axes into one field
is what makes retrieval ambiguous. Resolution, so both tasks stay consistent:

| T2 first-pass value | canonical `status` here | maturity, if still wanted |
|---|---|---|
| `draft` | `current` (retrievable) | `confidence: low` |
| `living` | `current` | (living is the normal state of a `concept`/evergreen note) |
| `stable` | `current` | `confidence: high` |
| `superseded` | `superseded` | — |

i.e. **`status` carries supersession only** (`current | superseded | historical | deprecated`), and
maturity is expressed through `confidence` (or, if a project insists, a separate `maturity:` field —
never overloaded onto `status`). This is a strict subset of what T1's gate already drops, so nothing
in the retrieval protocol has to change. Recommendation: T2 adopts this 4-value vocabulary verbatim.

---

## 2. Two shapes of change

A fact can change in two structurally different ways. Handle them differently:

1. **A whole note is replaced** by a newer note on the same topic (two files) → **note-level
   supersession** via `status` + `superseded_by` (§4).
2. **A fact changes inside one living note** (one file that should stay evergreen — an entity page,
   a `concept`, a landscape) → **claim-level supersession** via dated claim lines (§3).

Prefer claim-level history for evergreen/`concept`/entity notes: it lets a single note carry its own
history **without spawning duplicates**, which is the root cause of the accumulation problem.
Note-level supersession is for the common ingest case where each source became its own bookmark and
a cluster of them now covers one topic.

---

## 3. Claim-level convention (history inside a living note)

Inside a `concept`, entity, or any note marked `status: current` that you intend to keep evergreen,
record changing facts as **dated claim lines** and keep an explicit updates block. This lets the
note stay singular while remaining honest about what changed.

**Dated claim line** — prefix a claim with its valid-time and, when it changes, strike or mark the
old one rather than deleting it:

```markdown
- **[2026-09-05]** On-policy distillation is the frontier default for post-training small models.
- **[2026-05-13]** ~~Off-policy distillation from a frontier teacher is the recommended approach.~~ (superseded 2026-09-05)
```

**`## Status & updates` block** — a reverse-chronological changelog at the foot of a living note,
each entry dated with valid-time:

```markdown
## Status & updates
- **2026-09-05** — Replaced the distillation recommendation (on-policy now default). confidence: high
- **2026-06-02** — Initial synthesis from the 2026-06 landscape. confidence: medium

## Supersession
- supersedes: [[on-policy-distillation-must-read]]   <!-- body wikilink; frontmatter carries the bare slug -->
```

Rules:
- The note's frontmatter `as_of` = the date of the **newest** claim line, so recency ranking tracks
  the freshest fact in the note.
- Never delete a superseded claim line; strike it (`~~…~~`) and annotate `(superseded YYYY-MM-DD)`.
- When a claim is *contested* (two sources disagree and both are currently plausible), keep both
  dated lines and mark them (see §4 "both-valid").

---

## 4. Reconciliation rules

### 4a. Detecting that two notes cover the same topic

A pair of notes is **same-topic** when **all three** hold (this is exactly what
`scripts/detect-duplicates.py` computes):

1. **Shared primary entity / anchor.** They share ≥ 1 **anchor** token: either a **topic-specific
   tag** — one used in **≤ 3% of notes** (≤ ~16 notes today), so generic connectors like `agents`
   (279), `claude-code` (105), `multi-agent` (48) are excluded — or a shared **`entities/` slug**
   (e.g. `graphiti`, `deepseek`). This is the "shared primary entity" gate.
2. **Tag overlap.** tag-set **Jaccard ≥ 0.40** *or* **≥ 4 shared tags**.
3. **Title/description similarity.** token **Jaccard ≥ 0.20** over title + description (stopwords
   removed). *Strong-overlap fallback:* a pair also qualifies on tag Jaccard ≥ 0.55 alone (+ anchor).

Clustering is done **per anchor** (connected components *within* one anchor's notes), then components
are merged only when their membership overlaps by **≥ 50%**. This confines chaining to a single
specific topic, so a note tagged both `graph-engineering` and `loop-engineering` cannot chain two
distinct topics into one blob. Thresholds are the tunable constants at the top of the detector.

### 4b. Resolving a cluster

Given a same-topic cluster:

1. **Pick the current note.** The member with the **newest `as_of`** (fallback `date` → `ingested`)
   becomes `status: current`.
2. **Supersede the rest, retain them.** Every older member gets `status: superseded` and
   `superseded_by: <current-slug>`; the current note gets `supersedes: [<older-slugs>]`. **No note is
   deleted or moved** — "supersede, don't archive" (SCHEMA.v2 §5).
3. **Time-slices stay historical.** A member that is an intentional dated snapshot
   (e.g. `...-landscape-2026`, a "state as of" note) gets `status: historical`, not `superseded` —
   it is kept as a retrievable point-in-time record.
4. **Both-valid / contested is flagged, never deleted.** If the top two are within **14 days** of
   each other, or make genuinely **contradictory** claims that are both currently plausible, do
   **not** auto-supersede: leave both `current`, add a body note linking them, and (optionally)
   mark the lower-`confidence` one for review. Contradiction surfacing is a feature (CLAUDE.md
   "Contradiction Detector"), not something to silence.
5. **Prefer merge for evergreen topics.** If the cluster is really one concept fragmented across many
   bookmarks, the higher-value move is to fold them into one `concept` note using §3 claim-level
   history and supersede the fragments into it. The detector flags dense clusters; a human/curator
   decides merge-vs-supersede.

**This document specifies the procedure; applying it is a separate task (T6-style).** The detector is
read-only and writes only its report.

---

## 5. Retrieval integration (T1)

`docs/retrieval-protocol.md` already defines the hook; this pins the exact behavior so the two
compose with zero ambiguity.

**Status gate (default).** Before scoring the grep hits, **drop** rows whose `status ∈ {superseded,
historical, deprecated}` (and any legacy `archived`). **Empty `status` = treat as `current`** — the
field is unpopulated across the existing corpus, and retrieval must never stall waiting for it.

**Same-topic tiebreak.** Among survivors covering the same topic, if one is `status: current`, prefer
it regardless of date (an explicitly-blessed current note beats a merely-newer un-triaged one).

**Recency uses valid-time.** The recency term uses `as_of` when present, else `date` → `ingested`
(the existing INDEX.tsv date precedence). Recency stays a **tiebreaker among topically-equal notes**
(the protocol's `2^(-days_old/120)`, half-life 120d), not a driver — so a note being newer never
outranks a more relevant one.

**Confidence (minor).** May act as a small tiebreaker and should caveat answers drawn from
`confidence: low` notes.

**History on request.** When (and only when) the user asks for *history / evolution / "what did we
used to think" / a timeline* — or asks *"how did X change"* — **re-include** the gated rows and
present the cluster **oldest → newest by `as_of`**, following `superseded_by` forward and `supersedes`
backward to walk the chain. This is the "keep information, rank it" payoff: the default answer is the
current fact; the history is one explicit question away and never lost.

**Index.** `status` and the effective date are already columns in `INDEX.tsv`; populating `status`/
`as_of` on notes makes the gate live with no change to `scripts/build-search-index.py`. (If the
builder does not yet prefer `as_of` for the date column, that is a one-line precedence addition.)

---

## 6. Tooling

- **`scripts/detect-duplicates.py`** — READ-ONLY. Scans `processed/*.md`, builds same-topic clusters
  with the §4a heuristic, and writes **`docs/supersession-candidates.md`** proposing which note in
  each cluster should be `current` and which `superseded`. It modifies **no note**. Rerun after any
  ingest batch: `python3 scripts/detect-duplicates.py`.
- Applying status/edges to notes from that report is a **separate, human-reviewed** step — kept out
  of the detector on purpose so analysis can never corrupt the vault.

## Sources

- Zep, *What Is a Temporal Knowledge Graph?* — facts are marked invalid, not deleted; four edge
  timestamps (valid-from/valid-to/observed/recorded); current vs historical vs provenance queries.
  https://www.getzep.com/ai-agents/temporal-knowledge-graph/
- Rasmussen et al., *Zep: A Temporal Knowledge Graph Architecture for Agent Memory*, arXiv:2501.13956
  — bi-temporal edge model with validity intervals for agent memory. https://arxiv.org/abs/2501.13956
- Neo4j, *Graphiti: Knowledge graph memory for an agentic world* — edge invalidation / validity
  windows over deletion. https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/
- *Bitemporal Modeling* (Software Patterns Lexicon) — valid-time vs transaction-time; supersede by
  marking rows expired and adding a new row, never deleting; recreate state at any decision point.
  https://softwarepatternslexicon.com/bitemporal-modeling/
