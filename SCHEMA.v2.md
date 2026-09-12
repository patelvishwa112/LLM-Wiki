---
title: Wiki Schema v2
type: concept
status: living
as_of: 2026-09-12
tags: [knowledge-management]
description: "Canonical schema for the LLM Wiki — frontmatter contract, type vocabulary, and taxonomy rules. Supersedes SCHEMA.md."
supersedes: SCHEMA.md
---

# Wiki Schema v2 (canonical)

> **This file replaces `SCHEMA.md`.** The old schema described an "Anthropic AI Research 2021-present"
> vault with a ~60-tag safety taxonomy, `created`/`updated`/`sources:` frontmatter, and directories
> (`raw/articles/`, `_archive/`) that do not exist. All of that is stale and wrong. This v2 reconciles
> the **real working conventions** (previously only in `CLAUDE.md`) with the structural guidance the old
> schema was meant to provide, and points at the controlled vocabulary in `docs/taxonomy.md`.

## 1. Domain

A **broad, multi-domain second brain** — not a single-topic research archive. Actual coverage, by tag
cluster weight: AI **agents & agent-harness engineering**, **agent loops/orchestration/multi-agent**,
**Claude Code & AI coding tools**, **skills / prompt / context engineering**, **LLM training & post-training
(RL, RLHF, fine-tuning, distillation)**, **inference & ML systems (GPU, serving, cost)**, **evals /
verification / observability**, **mechanistic interpretability & alignment/safety**, **RAG / retrieval /
knowledge graphs**, **quant / trading / finance / prediction markets**, **browser agents**, **world models
& robotics**, **knowledge management / PKM**, and **career / product / startups / creator-economy /
productivity**. The value is in **cross-domain connection**, so notes are filed by *type* and navigated by
*tags*, never siloed by topic folder.

## 2. Frontmatter contract

Every `processed/*.md` note starts with YAML frontmatter. This is the **single source of truth** (merging
the real `CLAUDE.md` conventions with the reserved temporal fields defined in parallel by T3).

```yaml
---
tags: [agents, agent-harness, evals]   # REQUIRED. Controlled vocab only (docs/taxonomy.md). 3-8 tags.
source: https://...                    # REQUIRED. URL back to the original.
date: 2026-08-14                        # REQUIRED. Publication/ingest date (YYYY-MM-DD).
type: bookmark                          # REQUIRED. One of the 6 values in section 3.
description: "One-line summary."        # REQUIRED (OKF). Quote if it contains ': '.
summary: "..."                          # OPTIONAL. Longer summary; duplicate description text if both present.
author: andrewyng                       # OPTIONAL. Source author handle.
raw: "[[raw/andrewyng_2088302050706686198]]"  # OPTIONAL. Wikilink to the raw capture; MUST be quoted.
# ---- reserved temporal fields (T3 — include when known, else omit) ----
status: living                          # RESERVED. draft | living | stable | superseded
as_of: 2026-09-12                       # RESERVED. Date the note's claims were last verified/true-as-of.
supersedes: old-note-slug               # RESERVED. Slug this note replaces.
superseded_by: new-note-slug            # RESERVED. Slug that replaces this note.
confidence: high                        # RESERVED. high | medium | low
---
```

**Hard rules**
- **No `related:` (or any `[[wikilinks]]`) in YAML** — it breaks PyYAML / TAG-INDEX. Put connections in a
  `## Related` section in the **body only**.
- `tags` must be a flat list of **canonical tags from `docs/taxonomy.md`**. See section 4.
- `raw:` values must be **quoted** because `[[...]]` is not valid bare YAML.
- Legacy fields from the old schema (`created`, `updated`, `sources`, `contested`, `contradictions`,
  `title`) are **deprecated**. `title` is optional; use the H1 heading instead. Temporal intent that
  `created`/`updated` carried is now expressed by `date` + `as_of` + `status`.

## 3. `type` vocabulary (6 values)

The `type` field had **14** values including junk. Canonical set is **6**. Migration map (old -> new):

| Canonical `type` | Collapses from | Meaning |
|---|---|---|
| **`bookmark`** | `bookmark` | A saved external link with light distillation. The default for ingested sources. |
| **`article`** | `article`, `paper`, `lecture` | A long-form external source captured/summarized in depth (incl. papers, talks). |
| **`concept`** | `concept`, `overview`, `analysis`, `summary`, `research-synthesis` | An evergreen synthesized concept/topic page that outlives any single source. |
| **`note`** | `note`, `processed-note`, `proposal` | An original short synthesized note / idea / proposal by the vault owner. |
| **`resource`** | `resource` | A curated list/collection of tools or links (a resource hub). |
| **`experiment`** | `experiment` | A hands-on experiment, prototype log, or result writeup. |

Rule of thumb: if it wraps one external URL, it is a `bookmark` (short) or `article` (deep). If it is the
owner's own synthesis across sources it is a `concept` (evergreen) or `note` (atomic/opinion). Entity
profiles live in `entities/` and are outside this `type` set.

## 4. Tag taxonomy rules

- The controlled vocabulary lives in **`docs/taxonomy.md`** — **~121 canonical tags**, organized into topic
  facets (domain > tag). This replaced **1,072** free-form tags (62% of which were used exactly once and
  therefore routed nothing).
- **Every tag on a note MUST appear in `docs/taxonomy.md`.** To introduce a new tag, add it to the taxonomy
  first (with a one-line purpose), then use it. Never coin a tag inline.
- **Faceting:** `tags` is the **TOPIC** facet only. *Type* is the `type` field; *status/recency* is
  `status`/`as_of`. Do **not** encode type or status as tags.
- **One term per concept:** synonyms and near-duplicates are collapsed (e.g. `sub-agents`->`subagents`,
  `loops`->`loop-engineering`, `mechanistic-interpretability`->`interpretability`).
- Target **3-8 tags per note**; beyond that, returns diminish.
- The full legacy->canonical migration is in **`tags-migration.json`** (100% of legacy tags mapped; noise
  mapped to `"__drop__"`). A later task (T6) applies it to notes.

## 5. Page thresholds

- **Create a note** when a source is worth keeping or a concept appears in 2+ sources / is central to one.
- **Add to an existing note** when a source only elaborates something already covered.
- **Do NOT create** a note for passing mentions or trivial detail.
- **Split** a note when it substantially exceeds **~200 lines** — break into sub-topic notes and link them.
- **Supersede, don't archive:** there is no `_archive/`. When a note is fully replaced, set
  `status: superseded` and `superseded_by: <slug>` on the old note and `supersedes: <slug>` on the new one;
  keep both for provenance.

## 6. Structure (authoritative paths)

```
processed/   — synthesized notes with the frontmatter above (this schema governs these)
entities/    — entity profiles (companies, people, tools, models) + TAG-INDEX.md
raw/         — raw scraped sources (author_statusid.md); provenance, referenced via raw: "[[...]]"
docs/        — taxonomy.md (controlled vocab), tag-distribution.txt (ground-truth audit)
index.md     — OKF v0.1 bundle index      Bookmarks Index.md — master topic index
SCHEMA.v2.md — THIS FILE (canonical)       CLAUDE.md — navigation & operating conventions
tags-migration.json — legacy->canonical tag map (consumed by migration task)
```

Referenced but **nonexistent** directories from the old schema (`raw/articles/`, `_archive/`) are not part
of this vault.
