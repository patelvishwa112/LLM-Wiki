---
title: "Agent Memory Landscape 2026 — Every Harness, Every Gap"
tags: ["memory", "agents", "hermes", "claude-code", "codex", "copilot", "mem0", "benchmarks", "infrastructure"]
source: https://x.com/mem0ai/status/2061822612398014782
date: 2026-06-02
published: 2026-06-02
authors: ["mem0 (@mem0ai)"]
type: bookmark
raw: "[[raw/mem0ai_2061822612398014782]]"
related: ["[[research-agent-evidence-operator]]", "[[knowledge-system-compounding-obsidian-vellum]]"]
---

# Agent Memory Landscape 2026

Mem0's comprehensive survey of how 9 major agent harnesses handle memory. The thesis: memory is now infrastructure, every harness shipped it, but all break at the same boundary — bounded local storage, keyword retrieval, harness scoping, weak staleness, and isolation gaps.

## Key Takeaways

- **Three tiers of memory, only one in production.** Working memory (context window, resets per session), external memory (vector stores, files, persists across sessions — the only tier in production), parametric memory (encoded in weights — zero deployments in 2026).
- **Hermes sits at ~1,300 tokens of durable memory.** MEMORY.md (2,200 chars) + USER.md (1,375 chars). Consolidation at 80% capacity. FTS5 keyword-only search. Three layers: working memory, skills, session search. Eight pluggable providers including Mem0.
- **Every harness has the same shortcomings.** Claude Code: filename-based retrieval, 25KB cap. Codex: 5K-token summary, grep-only search, 6h idle gate. Copilot: the only one with staleness handling (+7% PR merge rate), but citation schema can't hold preferences. OpenClaw: has semantic search but compaction is model-dependent and inconsistent.
- **Benchmarks are mostly bad.** LoCoMo: grep baseline ~74%. MemoryArena: systems that ace recall benchmarks fail at action-guiding memory. BEAM: only benchmark at 10M+ token production scale. Field needs a new benchmark.
- **Memory is an attack surface.** 57-71% cross-user contamination under normal usage. Poisoning attacks: 6-38% success.
- **The Mem0 solution.** Hybrid (vector + knowledge graph + key-value), multi-signal retrieval (semantic + BM25 + entity linking), ~6,900 tokens / 1.44s per query vs 26K tokens / 17s for full-context. Ships as provider for every harness.

## The 9 Harnesses Compared

| Harness | Storage | Retrieval | Staleness | Scoping | Key Gap |
|---------|---------|-----------|-----------|---------|---------|
| Claude Code | 25KB local markdown | Filename (non-semantic) | None | Repo-only | Can't find by meaning |
| Managed Agents | 100KB/store, immutable | Filesystem mount | Immutable history | Workspace | Not for personal memory |
| Codex | Markdown, 5K token load | Grep (substring) | 30-day prune | Local | Paraphrased facts invisible |
| Copilot | Structured objects | Citation-verified | 28-day expire + rewrite | Repo-only | Can't hold preferences |
| OpenClaw | Markdown + SQLite + embeddings | Hybrid (70% vec / 30% BM25) | None | Local | Compaction inconsistent |
| Hermes | 2,200 chars MEMORY.md | FTS5 (keyword) | None | Local | 800 token cap, no semantics |
| Bedrock | Managed service | 200ms retrieval | INVALID marks + lineage | AWS lock-in | Ecosystem bound |
| Windsurf | Cascade-managed files | Engine-driven | None | Workspace | Not developer-controlled |
| Devin | Human-curated + DeepWiki | Trigger-content | Approval-gated | Devin-only | Friction, non-transferable |

## Hermes-Specific Detail

Three built-in layers:
1. **Working memory:** MEMORY.md (2,200 chars) + USER.md (1,375 chars), ~1,300 tokens combined. §-delimited, utilization gauge, consolidation at 80%. Writes land on disk; system prompt holds frozen snapshot until next session (preserves prefix cache).
2. **Skills:** procedural docs written after 5+ tool-call tasks, curated on schedule.
3. **Session search:** SQLite FTS5 over all sessions, summarized on demand.

Eight pluggable providers. Mem0 provider: removes cap, adds semantic retrieval, server-side extraction, user-scoped writes, circuit breaker.
