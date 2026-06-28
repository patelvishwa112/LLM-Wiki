---
source_url: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
spec_url: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
ingested: 2026-06-28
author: google-cloud
title: "Open Knowledge Format (OKF) v0.1"
---

# Open Knowledge Format — sources

## Google Cloud blog (2026-06-12)

Sam McVeety & Amir Hormati — introduces OKF as formalization of Karpathy LLM-wiki pattern.

Key points:
- v0.1 = directory of markdown + YAML frontmatter; git/tarball distribution
- **Concept** = one .md file; path (minus .md) = concept ID
- Required frontmatter: `type` only
- Recommended: title, description, resource, tags, timestamp
- Reserved: `index.md` (directory listing, progressive disclosure), `log.md` (changelog)
- Cross-links: markdown, bundle-root paths `/tables/foo.md` preferred
- Living wiki: agents read/update files; knowledge managed like code
- Reference: BigQuery enrichment agent, HTML visualizer, sample bundles (GA4, Stack Overflow, Bitcoin)
- Knowledge Catalog product can ingest OKF

## SPEC.md v0.1 (summary)

Goals: enrichment agents write; consumption agents read/traverse; exchange across orgs.

Conformance (strict):
1. Parseable YAML frontmatter on every non-reserved .md
2. Non-empty `type` field
3. index.md / log.md follow spec when present

Permissive consumption: unknown types, extra keys, broken links, missing index — must NOT reject bundle.

Conventional body sections: `# Schema`, `# Examples`, `# Citations`

Relationship: LLM wikis, Obsidian, AGENTS.md/CLAUDE.md family, metadata-as-code repos.