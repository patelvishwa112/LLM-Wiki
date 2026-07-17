---
tags: ["okf", "openwiki", "langchain", "second-brain", "knowledge-graph", "agents", "agent-harness", "documentation", "standards", "obsidian"]
source: https://x.com/bracesproul/status/2077799049156338142
date: 2026-07-16
type: bookmark
description: "LangChain OpenWiki 0.2 adopts Google OKF — YAML frontmatter, index.md, logs.md for agent-navigable codebase wikis; deterministic tag/category filters over pure agentic search."
author: bracesproul
summary: "LangChain OpenWiki 0.2 adopts Google OKF — YAML frontmatter, index.md, logs.md for agent-navigable codebase wikis; deterministic tag/category filters over pure agentic search."
raw: "[[raw/bracesproul_2077799049156338142]]"
---

# OpenWiki 0.2 adopts the OKF spec

Brace Sproul (LangChain) announces **OpenWiki 0.2**: the open-source CLI for generating/maintaining **codebase documentation wikis** for coding agents now emits **OKF** (Open Knowledge Format, Google Cloud) structure so large wikis stay navigable.

## Key takeaways

- **OpenWiki role:** Generate a repo wiki, wire it into coding agents (e.g. via AGENTS.md / CLAUDE.md), keep docs updated as code changes.
- **Why structure:** v0.1 was free-form Markdown; hundreds of files need discovery, update, search, and review conventions.
- **OKF in 0.2:** Each page gets YAML front matter (`type` required; `title`, `description`, `resource`, `tags`, `timestamp`, producer fields). Conventions:
  - **`index.md`** — progressive disclosure summary of siblings/subdirs (often from descriptions).
  - **`logs.md`** — changelog of wiki updates after each OpenWiki run (what changed, where to read more).
- **Agent retrieval:** Structured metadata enables **deterministic filters** (e.g. all docs tagged `billing` or category BigQuery tables) instead of only open-ended agentic search — lower latency/tokens for simple lookups.
- **Ecosystem:** Compatible with community OKF viewers/linters; Google open-source OKF wiki visualizer (graph of doc relationships, OpenSWE example). OWOX ecosystem tools article linked.
- **Try:** `npm install -g openwiki@latest` then `openwiki --init`. Upgrade existing installs to OKF on next generate/update. Repo: https://github.com/langchain-ai/openwiki

## Why it matters

Same OKF shape this vault uses (type, description, indexes, log). Validates agent-wiki standards and points at a LangChain-maintained generator for **code** wikis complementary to personal second brains / Hermes vault patterns.

## Related

- [[open-knowledge-format-okf-google]]
- [[hermes-agent-10x-faster-vault-index]]
- [[living-wiki-second-brain-hermes-leopardracer]]
- [[cerebras-knowledge-base-hybrid-search-mcp]]
- [[gbrain-markdown-git-brain-mem0]]
- [[how-to-build-custom-agent-harness-langchain]]
