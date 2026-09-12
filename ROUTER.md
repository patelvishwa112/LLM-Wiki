---
title: Retrieval Router
type: meta
tags: [meta, retrieval, router]
description: Always-loaded entry point. The exact order an agent retrieves in, and when to stop.
---

# ROUTER — read this first, then stop reading indexes

Answer by touching **2–3 notes, not the vault**. Retrieval is **logic over `INDEX.tsv`**, not model calls. Never load `processed/index.md`, `Bookmarks Index.md`, or `entities/TAG-INDEX.md` whole — 33k–50k tokens each; grep `INDEX.tsv` instead.

## Order (stop at the first tier that answers)

1. **Grep the index.** `grep -iE '<kw1>|<kw2>' INDEX.tsv` (cols: `slug⇥type⇥status⇥date⇥tags⇥description`). Keywords from the question; prefer tag tokens.
2. **Score hits in-context** (no model call; full spec in `docs/retrieval-protocol.md`):
   `score = 3·tag_hits + 1·desc_hits + 0.5·type_bonus + 2·recency`, `recency = 2^(-days_old/120)`.
   Drop `status: deprecated|superseded|archived`; empty status = current.
3. **Open ≤3 notes** — top-scoring slugs, only the relevant `##` sections.
4. **Hop ≤1 edge** — follow one `## Related` wikilink only if a named gap remains.
5. **Web only** for a *named* gap the vault can't fill (see protocol's boundary): a fact/number/date/entity absent from the opened notes, or info newer than the top note's `date`.

## Hard stops
- Opened 3 notes → **answer now**; do not open a 4th without a specific missing fact.
- Never read `raw/*` unless you need a **verbatim** quote/source; cite `raw:` from the note's frontmatter.
- History/evolution asked for? Then and only then surface non-`current` `status` rows.

Rebuild the index after ingests: `python3 scripts/build-search-index.py`.
