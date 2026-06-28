---
okf_version: "0.1"
title: LLM Wiki Knowledge Bundle
description: Agent- and human-readable knowledge graph (bookmarks, concepts, entities) for AI research, agents, harness design, and related domains.
---

# LLM Wiki — bundle index

Progressive disclosure entry for OKF v0.1 consumers. Read this file first; open concepts only as needed.

## Navigation

* [Vault conventions and intelligence ops](CLAUDE.md) — placement rules, ingestion SOP, OKF alignment
* [Bookmarks by topic and A-Z](Bookmarks%20Index.md) — primary human entry; topic sections + tag badges
* [Tag cross-reference](entities/TAG-INDEX.md) — every tag → processed concept slugs
* [Frontmatter schema](SCHEMA.md) — tags, types, page thresholds

## Concepts

* [processed/](processed/) — one markdown file per concept (OKF concept documents). Required frontmatter: `type`. Required for new ingests: `description` (one line; may match `summary`).
* [entities/](entities/) — entity profiles (people, orgs, tools, models) plus TAG-INDEX

## Source material (archive)

* [raw/](raw/) — full scraped captures (X, web, papers). Provenance for processed notes via `raw: "[[raw/...]]"` in concept frontmatter. Not required for minimal OKF export subsets.

## Agent retrieval order

1. This `index.md` or Bookmarks Index (topic fit)
2. `entities/TAG-INDEX.md` for tag → slug list
3. `read_file` on 1–3 `processed/<slug>.md` files
4. Follow `## Related` wikilinks; read `raw/` only when verbatim source matters

Do not load the full bundle into session context.