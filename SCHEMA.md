---
title: Wiki Schema
created: 2026-05-22
updated: 2026-05-22
type: meta
tags: [schema]
sources: []
---

# Wiki Schema

## Domain

Anthropic AI Research — a comprehensive knowledge base of all publications, blog posts,
research papers, engineering articles, and features published by Anthropic (anthropic.com).
Covers 2021–present.

## Conventions

- File names: lowercase, hyphens, no spaces (e.g., `constitutional-ai.md`)
- Every wiki page starts with YAML frontmatter
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- **Provenance markers:** On pages that synthesize 3+ sources, append `^[raw/articles/source-file.md]`
  at the end of paragraphs whose claims come from a specific source.

## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
confidence: high | medium | low
contested: true  # optional
contradictions: [other-page-slug]  # optional
---
```

## Tag Taxonomy

**Research Areas (top-level):**
- alignment
- interpretability
- safety
- societal-impacts
- economic-research

**Alignment sub-topics:**
- rlhf, constitutional-ai, scalable-oversight, deceptive-alignment,
  agentic-misalignment, reward-hacking, alignment-faking, sycophancy

**Interpretability sub-topics:**
- circuits, features, superposition, sparse-autoencoders, induction-heads,
  persona-vectors, introspection

**Safety sub-topics:**
- jailbreaks, classifiers, red-teaming, biosecurity, cybersecurity,
  model-welfare, misuse, sabotage, rsp

**Societal-impacts sub-topics:**
- education, government, enterprise, persuasion, regulation, partnership

**Capability / product tags:**
- agents, claude-code, mcp, computer-use, extended-thinking, scaling-laws

**Content Types:**
- research-paper, blog-post, engineering, feature, policy, model-card,
  system-card, transcript

**Models:**
- claude-1, claude-2, claude-3, claude-3.5, claude-4, opus, sonnet, haiku

**Meta:**
- comparison, timeline, controversy, prediction, overview, schema, anthropic

**Rule:** Every tag on a page must appear in this taxonomy. Add new tags here first.

## Page Thresholds

- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions or minor details
- **Split a page** when it exceeds ~200 lines — break into sub-topics
- **Archive a page** when content is fully superseded — move to `_archive/`

## Entity Pages

One page per notable entity (person, org, model, tool). Include:
- Overview
- Key facts and dates
- Relationships to other entities ([[wikilinks]])
- Source references

## Concept Pages

One page per concept or topic. Include:
- Definition / explanation
- Current state of knowledge
- Open questions or debates
- Related concepts ([[wikilinks]])

## Comparison Pages

Side-by-side analyses. Include:
- What is being compared and why
- Dimensions of comparison (table preferred)
- Verdict or synthesis
- Sources

## Update Policy

When new information conflicts with existing content:
1. Check dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter
4. Flag for user review

## Source Capturing

When ingesting a URL:
1. Capture the raw source to `raw/articles/` using `web_extract`
2. Add raw frontmatter with `source_url`, `ingested` date, `sha256`
3. Extract: title (og:title), description (og:description), category
4. Create or update wiki pages for entities and concepts mentioned
5. Update index.md
6. Log the action

For arXiv papers, also capture from arxiv.org abstract page.
For transformer-circuits.pub papers, capture directly.
For assets.anthropic.com PDFs, note the URL but PDFs may not be extractable.
