---
title: Retrieval Protocol
type: meta
tags: [meta, retrieval, protocol]
description: The full index-first retrieval protocol — tiers, scoring function, token budget, stop rules, web boundary, and a worked example.
---

# Retrieval Protocol

This is the executable retrieval layer for the vault. `ROUTER.md` (root) is the ~350-token always-loaded summary; this file is the full spec. The design goal: **a typical answer touches 2–3 notes, not 540.** Retrieval is **deterministic logic over a compact index** (`grep` + arithmetic), not a model call, not an embedding lookup.

## Why this shape (design rationale)

- The vault is small (≈550 notes) and heavily structured (`tags`, `type`, `date`, `description`). For small, exact-term, structured corpora, lexical search + an agentic refine loop **beats dense embeddings** and needs no vector DB to build, host, or keep fresh — you "throw all that away and use BM25/grep." [Shah, *RAG in an Agentic World*]. BM25/keyword also wins outright on rare identifiers, tags, model names, and proper nouns where an encoder has never seen the string. [sesen.ai, *BM25 vs Embeddings*].
- We keep the retrieval logic in **owned markdown + stdlib Python**, so it is model-swappable and survives with zero infra.
- Embeddings would add recall on pure paraphrase, but the agent's own query reformulation (retry grep with synonyms) recovers most of that gap at a fraction of the cost. [Shah]. If paraphrase recall ever becomes the bottleneck, add a dense sidecar as a *fourth* tier — do not replace tiers 1–3.

## The index: `INDEX.tsv`

Built by `scripts/build-search-index.py` (stdlib only, idempotent). One row per note in `processed/` and `entities/`:

```
slug <TAB> type <TAB> status <TAB> date <TAB> tags <TAB> description
```

- `slug` — vault-relative, ready to open (`processed/foo.md`, `entities/bar.md`).
- `type` — `bookmark | article | concept | comparison | entity | …`.
- `status` — temporal field (T3). Empty today; when populated, `current | deprecated | superseded | historical | …`.
- `date` — `date`, else `ingested`, else `as_of` (`YYYY-MM-DD`), else empty.
- `tags` — comma-joined. Free-form today; a controlled set once T2 lands (the protocol is agnostic to which — it scores whatever tokens are present).
- `description` — one line, ≤160 chars.

The whole file is ~145 KB (~36k tokens) — but **you never read it whole.** You `grep` it. A keyword grep returns a few dozen rows (~1–3k tokens); the routing step that used to cost 33k tokens (`processed/index.md`) now costs ~2k.

Rebuild after any ingest: `python3 scripts/build-search-index.py`.

## Tiered flow

Stop at the first tier that answers the question.

**Tier 0 — ROUTER (always loaded, ~350 tok).** Sets order + stop rules. No vault read.

**Tier 1 — Grep `INDEX.tsv` (~1–3k tok).** Extract 2–4 keywords from the question; prefer terms that look like tags (`agent-memory`, `interpretability`, a model name). Run `grep -iE 'kw1|kw2' INDEX.tsv`. If >~40 hits, add a term (AND-narrow with a second `grep`); if 0 hits, drop to the stem or a synonym and retry. This is the reformulation loop — cheap, deterministic.

**Tier 2 — Score the hits in-context (0 extra tokens).** Apply the scoring function below to the grep output you already have in context. No file opens, no model call — just arithmetic over the TSV columns. Rank; take the top 2–3 slugs.

**Tier 3 — Open ≤3 notes (~0.6–2k tok).** Open only the top-scoring slugs, and within each read only the relevant `##` sections (the `# H1` + the 1–2 sections whose headers match the query), not the whole file. Average note is ~660 tokens; sectional reads are less.

**Tier 4 — Hop ≤1 edge (optional).** If an opened note names a concept you still need, follow **one** `## Related` wikilink. Resolve the wikilink to a slug and open that one note. Do not chain hops.

**Tier 5 — `raw/` only for verbatim.** Open a `raw/*` capture *only* when you need an exact quote or to verify a source. Get the path from the note's `raw:` frontmatter. Raw captures are large; never use them for routing or gist.

**Tier 6 — Web (named gap only).** See the boundary below.

## Scoring function

For each candidate row returned by the grep, with query term set `Q` (lowercased keywords):

```
score = 3.0 * tag_hits          # distinct q-terms that substring-match a tag token   (0..|Q|)
      + 1.0 * desc_hits         # distinct q-terms appearing in the description        (0..|Q|)
      + 0.5 * type_bonus        # +1 if type in {concept, comparison, article}, else 0  (explain/how questions)
      + 2.0 * recency           # recency = 2^(-days_old / 120);  empty date => 0.5

days_old = today - date
```

**Weights & rationale.** Relevance mass (tag + desc + type) dominates; recency is a **tiebreaker among topically-equal notes**, not a driver. This matches the "deep-context agent" profile (favor relevance ≈0.7 over recency ≈0.3) rather than the chatbot profile (recency-heavy). [theneuralbase, *Hybrid recency + relevance*]. Tags are weighted 3× description because tags are curated/controlled (especially post-T2) while descriptions are prose; a tag hit is a stronger topical signal. `type_bonus` gently prefers synthesized concept/comparison notes over raw bookmarks **for explanatory questions**; for "find me the link/source" questions, set `type_bonus = 0` (a bookmark is the right answer).

**Recency decay.** `recency = 2^(-days_old / 120)` → **half-life 120 days**: a 4-month-old note keeps half its recency weight. This suits a research vault where ideas age over months, not days. Tunable: shrink the half-life (e.g. 60) for fast-moving topics, grow it (e.g. 365) for durable reference. A note with no `date` gets a neutral `0.5` so it is neither boosted nor buried.

**Status gate (T3-aware).** Before scoring, **drop** rows with `status ∈ {deprecated, superseded, archived, historical}`. Among survivors, if two notes cover the same topic and one is `status: current`, prefer it regardless of date. **Empty `status` = treat as current** (the field is unpopulated pre-T3; the protocol must not stall waiting for it). Only when the user explicitly asks for *history / evolution / "what did we used to think" / timeline* do you re-include non-current rows and surface them oldest→newest.

**Fusion note.** This is a weighted linear fusion because we control and trust the field scores. If you ever fuse this lexical rank with a second retriever (e.g. a dense sidecar), prefer **Reciprocal Rank Fusion** (`Σ 1/(60 + rank_i)`) instead of summing raw scores — RRF needs no score calibration and reliably beats either retriever alone. [sesen.ai; Spice AI, *RRF*].

## Token budget & stop rules

Hard budget for a typical answer: **≤ ~6k retrieval tokens.**

| Step | Budget |
|---|---|
| ROUTER (Tier 0) | ~0.35k (always loaded) |
| Grep INDEX.tsv (Tier 1) | ~1–3k |
| Score (Tier 2) | 0 |
| Open ≤3 notes (Tier 3) | ~0.6–2k |
| +1 hop (Tier 4, if needed) | ~0.7k |

**Stop rules (in force order):**
1. **3 notes opened → answer now.** Do not open a 4th unless you can name the *specific missing fact* it would supply.
2. **A tier answered the question → stop descending.** Do not "read one more for completeness."
3. **Grep returned 0 after 2 reformulations → the vault likely lacks it →** go to Tier 6 (web) or tell the user it's not in the vault. Do not brute-force by opening notes.
4. **Never** open `processed/index.md`, `Bookmarks Index.md`, or `entities/TAG-INDEX.md` in full during retrieval — that defeats the entire design (33k–50k tokens each). They remain as human-browsable surfaces only.
5. **Never** read `raw/*` for gist. Verbatim only.

## Web vs. vault boundary

Prefer the vault. Go to the web **only** when a gap is *named and specific*:

Go to web when:
- The answer needs a **specific fact/number/quote/date** that the ≤3 opened notes do not contain (e.g. an exact benchmark score, a price, an API signature).
- The question is about events **newer than the top note's `date`** (the vault has a freshness ceiling; a 2026-06 note can't answer "what shipped last week").
- The grep returned **0 hits after two reformulations** — the topic isn't in the vault at all.
- The user explicitly asks to verify/update a vault claim against a live source.

Stay in the vault when:
- The question is conceptual/explanatory and ≥1 scored note covers it — synthesize from the notes.
- You want background, definitions, comparisons, or "what does my vault say about X" — that is exactly what the vault is for.
- A single fact is missing but a `## Related` hop or the note's `source`/`raw:` link plausibly holds it — hop/check first (Tier 4/5) before spending a web call.

Rule of thumb: **the vault answers "what do I know about X"; the web answers "what is true about X right now that my notes can't say."**

## Worked example (real, against this vault)

**Question:** *"What's the current best-practice architecture for giving an AI agent long-term memory?"*

**Tier 1 — grep.** Keywords `{agent, memory, architecture}`. Tag-token grep:
```
grep -iE 'agent-memory|agent memory' INDEX.tsv     # → 32 rows, ~2.5k tokens
```
(vs. reading `processed/index.md` to route = ~33k tokens.)

**Tier 2 — score** (today = 2026-09-12, half-life 120d, `type_bonus`=0, all bookmarks). Applying `3·tag_hits + 1·desc_hits + 2·recency` to the grepped rows:

| slug | date | days | tag_hits | desc_hits | recency | **score** |
|---|---|---|---|---|---|---|
| quarq-agent-memory-architecture | 2026-05-26 | 109 | 3 (agent✓ memory✓ arch✓ via `agent-architecture`) | 3 | 0.53 | **13.1** |
| memory-engineering-forgetting-policy-leanxbt | 2026-08-02 | 41 | 2 | 2 | 0.79 | **9.6** |
| agent-memory-four-layer-stack-matthew-gunnin | 2026-07-02 | 72 | 2 | 2 | 0.66 | **9.3** |
| agent-memory-landscape-2026 | 2026-06-02 | 102 | 2 | 2 | 0.55 | 9.1 |
| how-to-be-a-memory-engineer-n01ennn | 2026-08-02 | 41 | 2 | 1 | 0.79 | 8.6 |

Note the intended behavior: **quarq wins on relevance** (only note matching all three terms, incl. `architecture`) even though it is the *oldest* — recency is a tiebreaker, not a driver. The two newest notes rank 2nd–3rd on relevance + recency.

**Tier 3 — open top 3 sections.** ~2k tokens total:
- `processed/quarq-agent-memory-architecture.md` → sections `## The 4-Layer Architecture`, `## Memory Types`, `## Design Principles`.
- `processed/memory-engineering-forgetting-policy-leanxbt.md` → `## Four shelves`, `## Three forgetting mechanisms`, `## Build order` (the *current*, 2026-08 discipline).
- `processed/agent-memory-four-layer-stack-matthew-gunnin.md` → `## Layers`, `## Coordination invariant` (a concrete production stack).

These three answer the question: a layered memory architecture (quarq's 4 layers / Gunnin's stack) governed by an explicit **forgetting policy** (leanxbt) — synthesized from 3 notes.

**Tier 4 — hop (only if a gap).** If the user then asks "how is this benchmarked?", follow one `## Related` edge from leanxbt → `[[longmemeval-evaluating-agent-memory-across-sessions]]` (or `[[agent-memory-landscape-2026]]`) and open that one note (~0.7k tok). No further hops.

**Tier 6 — web (only if named gap).** Only if they ask for a number the notes lack ("what LongMemEval score did model X get?") or something after 2026-08 → one targeted web search. Otherwise the vault suffices.

**Token path — before vs after:**

| | Route step | Note reads | Total |
|---|---|---|---|
| **Before** (naive) | read `processed/index.md` ~33k (often + TAG-INDEX ~50k) | ~5 full notes ×~0.7k ≈ 3.3k | **~36k–86k** |
| **After** (this protocol) | ROUTER 0.35k + grep 2.5k | 3 sectional reads ≈ 2k | **~5k** |

≈ **7× fewer tokens** vs. the light naive path, ≈ **17×** vs. the full-route path — and the routing step alone drops **33k → 2.5k (~13×)**.

## Maintenance

- After every ingest batch: `python3 scripts/build-search-index.py` (regenerates `INDEX.tsv` from frontmatter; idempotent).
- The index derives entirely from note frontmatter, so it never drifts as long as it's rebuilt — unlike hand-maintained prose indexes. Consider wiring the rebuild into the ingest SOP / a pre-commit or cron so it can't go stale.

## Sources

- Rajiv Shah, *RAG in an Agentic World* — lexical + agentic loop beats embeddings on small/code corpora; no vector DB. https://rajivshah.com/blog/rag-agentic-world.html
- sesen.ai, *BM25 vs Embeddings: Why Hybrid Retrieval Wins* — BM25 wins on rare/exact terms & out-of-domain; RRF k=60; route identifier queries to lexical. https://sesen.ai/blog/bm25-vs-embeddings-hybrid-retrieval
- The Neural Base, *Hybrid recency + relevance* — `w·similarity + w·recency`; exponential recency decay & half-life; deep-context agents favor relevance (~0.7/0.3). https://theneuralbase.com/ai-memory-systems/learn/advanced/hybrid-recency-relevance/
- Spice AI, *Reciprocal Rank Fusion* — `Σ 1/(k+rank)`, k=60, calibration-free fusion. https://spice.ai/learn/reciprocal-rank-fusion
