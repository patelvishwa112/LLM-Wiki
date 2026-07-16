---
tags: ["agent-memory", "rag", "mcp", "enterprise", "cerebras", "cocoindex", "retrieval", "knowledge-base", "hybrid-search", "agents", "agent-harness", "second-brain"]
source: https://x.com/cerebras/status/2077822555159945507
date: 2026-07-16
type: bookmark
description: "Cerebras Knowledge: meet-data-where-it-lives enterprise KB (15k queries/day) — unified Postgres embeddings, hybrid Slack search, CocoIndex code, planner/RRF/rerank, MCP primitives vs full UI pipeline."
author: cerebras
summary: "Cerebras Knowledge: meet-data-where-it-lives enterprise KB (15k queries/day) — unified Postgres embeddings, hybrid Slack search, CocoIndex code, planner/RRF/rerank, MCP primitives vs full UI pipeline."
raw: "[[raw/cerebras_2077822555159945507]]"
---

# How Cerebras built its knowledge base

Cerebras engineers (Isaac Tai, Daniel Kim, Mike Gao) describe **Cerebras Knowledge** — an internal knowledge base used by humans, automations, and agents, answering **15,000+ questions/day** within three months of launch. Full technical writeup on the company blog.

## Key takeaways

- **Meet data where it lives.** Reject “single source of truth” forced centralization. Ingest Slack, GitHub, Confluence/wiki, Jira-style systems, netlists, custom DBs with minimal workflow change.
- **One embeddings table.** Single Postgres schema (document, embedding, metadata, source + timestamps). Every connector lands the same row shape → one query surface. Custom sources = small Python plugins emitting that schema.
- **Slack is the hard path.** Socket Mode bot for real-time events (no polling rate limits). On event: re-fetch entire thread and upsert one row. Hybrid retrieval per thread:
  - Full-text (exact errors, flags, hostnames)
  - Embeddings (paraphrase)
  - IDF (rare tokens beat filler)
  - Age decay (newer wins ties)
- **Distillation, not raw embed.** LLM extracts question / summary / resolution / systems / code refs; embedding the normalized artifact beat embedding raw transcripts.
- **Bursting.** Long threads miss important tangent messages; embed qualifying same-author bursts with thread topic prepended (thresholds: IDF ≥ 4, length ≥ 200 chars, optional reactions).
- **Code via CocoIndex.** Language-aware recursive chunking (class → method → blocks); incremental re-embed on commit; allow/deny path configs; multi-level records per file. Motivated partly by Cursor’s semantic-search findings despite “grep is all you need.”
- **Query path.** Planner LLM selects tools → parallel fan-out (`search`, `search_slack`, `search_code`/ripgrep, `recent_prs`, `who_knows`, `subsystem_index`) → normalize evidence → **RRF (k=60)** across lists → small reranker model → expand winners with neighbor sections → synthesis + citations.
- **MCP vs Web UI.** MCP exposes **LLM-light retrieval primitives** so agents (e.g. Claude Code) orchestrate. Web UI runs full planner → executor → synthesizer for humans.
- **Projects scope search.** Named bundles of channels/repos/docs; shared sources referenced not duplicated. Onboarding picks a default project so new hires get high-signal answers immediately.

## Why it matters

Production-grade enterprise RAG/agent memory pattern: hybrid scorers, thread distillation, incremental code index, project scoping, and split between MCP tools and a full synthesis UI. Directly relevant to second-brain / vault / Hermes-style retrieval and company-wide agent knowledge layers (Glean/Sierra class systems).

## Related

- [[gbrain-markdown-git-brain-mem0]]
- [[open-knowledge-format-okf-google]]
- [[hermes-agent-10x-faster-vault-index]]
- [[agent-memory-landscape-2026]]
- [[how-to-build-agent-that-never-forgets]]
- [[glean-coding-harness-programmatic-tool-calling]]
- [[improving-agents-data-mining-traces]]
- [[continuous-trace-intelligence-braintrust-topics]]
