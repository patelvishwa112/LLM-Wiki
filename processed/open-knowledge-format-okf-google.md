---
tags: [agents, knowledge-graph, obsidian, second-brain, agent-harness, standards, google-cloud, open-source]
source: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
date: 2026-06-28
type: concept
author: google-cloud
summary: "OKF v0.1 is Google's vendor-neutral spec for agent-readable knowledge bundles—markdown concepts with YAML frontmatter (required type), index.md for progressive disclosure, and markdown cross-links—formalizing the Karpathy LLM-wiki pattern without a mandatory SDK."
description: "OKF v0.1 is Google's vendor-neutral spec for agent-readable knowledge bundles—markdown concepts with YAML frontmatter (required type), index.md for progressive disclosure, and markdown cross-links—formalizing the Karpathy LLM-wiki pattern without a mandatory SDK."
raw: "[[raw/googlecloud_okf-open-knowledge-format]]"
---

# Open Knowledge Format (OKF)

Google Cloud **Open Knowledge Format v0.1** (June 2026, draft) — a **format**, not a hosted brain. Bundles are git-friendly folders of markdown **concepts** that humans and agents read with `cat` / `read_file`, no proprietary catalog API.

## Spec essentials

| Piece | Rule |
|-------|------|
| Bundle | Directory tree of `.md` files (git repo recommended) |
| Concept | One file = one unit of knowledge; ID = path without `.md` |
| Frontmatter | **Required:** `type` (free-form string). **Recommended:** `title`, `description`, `resource`, `tags`, `timestamp` |
| Navigation | Optional `index.md` per folder (bullet catalog + descriptions); optional `log.md` (dated changelog) |
| Graph | Markdown links; `/bundle-root/path.md` preferred |
| Consumption | Permissive — unknown types, extra YAML keys, broken links OK |

**Producer/consumer split:** enrichment agents (e.g. Google’s BigQuery walker) *write* concepts; any agent *reads* via filesystem + links. Pairs with **pull** recall (gbrain, mem0, etc.), not replacement for thin `CLAUDE.md` / harness memory.

## How agents should use OKF

1. **Progressive disclosure** — Open bundle `index.md` (or synthesize from frontmatter `description`), then load only matching concepts.
2. **Traverse links** — Treat links as directed edges; relationship type lives in prose around the link.
3. **Write back** — Update concepts, append `log.md`, add cross-links; version in git.
4. **Do not dump the bundle** into every session — same discipline as skills-over-push-memory.

## Why it matters

Validates the vault’s existing bet: **markdown + frontmatter + wikilinks + git** as agent infrastructure. Google names the interoperability surface so external tools (Knowledge Catalog, visualizers, future MCP servers) can consume the same corpus without Obsidian-specific glue.

## Related

- [[gbrain-markdown-git-brain-mem0]]
- [[knowledge-system-compounding-obsidian-vellum]]
- [[your-ais-memory-is-quietly-making-it-dumber]]
- [[graphiti-knowledge-graph-agent-memory]]
- [[agent-memory-landscape-2026]]

## Migration path for this vault

**Current shape:** ~326 `processed/` notes, ~569 `raw/` captures, `entities/` profiles, `Bookmarks Index.md` + `TAG-INDEX.md`, Obsidian `[[wikilinks]]`, frontmatter `type: bookmark | concept | …`.

**Already OKF-aligned (~80%):** flat concept files, YAML frontmatter, tags, git distribution, cross-links, human+agent readable.

### Tier 1 — Low effort (1–2 sessions, no mass moves)

**Status: adopted 2026-06-28** (`index.md`, `CLAUDE.md` OKF section, ingestion skills + memory updated).

- Add bundle root `index.md` with `okf_version: "0.1"` in frontmatter (only place index may have YAML per spec) + pointer to `CLAUDE.md` / navigation doc.
- Document OKF mapping in `CLAUDE.md` (processed = concepts, raw = citation/archive layer outside strict bundle if desired).
- Ingestion SOP: ensure every new `processed/` note has `type` + `description` (use `summary` as description or alias in regen script).
- Hermes `wiki-search` / curation skills: explicit “start at index → tags → concept” flow (progressive disclosure).

### Tier 2 — Medium (scripted pass, ~326 files)

**Status: partial 2026-06-28** — `scripts/okf-frontmatter-fix.py` backfilled `description`, stripped invalid frontmatter `related:` → body `## Related`, quoted risky `summary` lines; 0 YAML parse errors remaining.

- **Type normalization:** Map `bookmark` → `Reference`, `concept` → `Reference` or `Playbook`, entity pages → `Entity` (OKF allows any string; pick a small internal enum).
- **Backfill `description`:** Copy from `summary` where missing (one Python pass over `processed/`). **Done 2026-06-28.**
- **Generate OKF-style `processed/index.md`:** Script from frontmatter descriptions. **Done** — `scripts/regenerate-processed-index.py` via `regenerate-okf-indexes.py`.
- **Optional `log.md`:** Append on ingest via `scripts/append-okf-log.py`. **Done** — root `log.md` + ingest SOP.
- **Type normalization:** Deferred — `bookmark` / `concept` remain valid OKF `type` strings unless exporting to a strict consumer.

### Tier 3 — Heavy (only if exporting to non-Obsidian consumers)

- **Link portability:** Dual-write `## Related` with `/processed/slug.md` markdown links alongside `[[wikilinks]]`, or conversion script (regex wikilink → path).
- **`resource` field:** Set `source:` URLs as OKF `resource` where concepts describe external assets.
- **`# Citations` sections:** Point processed notes at `raw/` via bundle-relative paths instead of only `raw:` frontmatter.
- **Restructure:** Only if sharing a *subset* as a public OKF bundle (e.g. agents-only concepts without raw dumps) — split repo or `okf-export/` subtree.

### What you should not do

- Re-folder 300+ notes unless a consumer requires it — OKF does not mandate taxonomy.
- Replace TAG-INDEX — OKF says tag aggregation can be synthesized at consumption time; your regen script already does that.
- Load entire wiki into harness memory — OKF is **pull** knowledge; aligns with cutting push memory.

### Suggested decision

**Adopt Tier 1 now**, Tier 2 when you want Knowledge Catalog / external OKF tooling or a public export. Full Tier 3 only for cross-org bundle exchange.

Spec: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md