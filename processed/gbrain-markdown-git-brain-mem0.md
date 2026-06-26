---
tags: [agents, agent-memory, mem0, gbrain, garry-tan, knowledge-graph, obsidian, wikilinks, rag, retrieval, openclaw, hermes, second-brain, git]
source: https://x.com/mem0ai/status/2070541048527609885
date: 2026-06-26
type: bookmark
author: mem0ai
summary: "Mem0 In Context #14 on Garry Tan's GBrain: markdown+git as source of truth, regex/wikilink typed graph (no LLM at write) drives BrainBench P@5 49.1% vs ~11–18% without graph; hybrid search + think mode with gap honesty; overnight dream cycle; brain (world facts) vs Mem0 memory (preferences/session)."
raw: "[[raw/mem0ai_2070541048527609885]]"
---

# GBrain: A Brain in a Git Repo

Mem0's breakdown of **GBrain** (Garry Tan, Apr 2026) — complements their earlier harness memory landscape note.

## Architecture

| Layer | Role |
|-------|------|
| Git markdown | Authoritative, diffable, revertible knowledge |
| Index (PGLite / Postgres+pgvector) | Retrieval downstream of files |
| Regex graph | Typed edges at ingest; multi-hop SQL |
| `search` / `think` | Hybrid RRF retrieval vs cited synthesis + unknowns |
| Dream cycle | Nightly dedup, citations, salience, contradictions |

## Benchmark signal (internal)

Graph contributes ~31 P@5 points over vector+keyword on GBrain's BrainBench v0.20 — relational questions ("who at portfolio companies…") need edges, not cosine alone. Not head-to-head vs Mem0/Zep on shared corpora.

## Brain vs memory (taxonomy)

- **Brain:** external world entities and facts (durable in git).
- **Memory:** how the agent operates — preferences, continuity across resets/tools.

Article positions **Mem0** as the memory side; GBrain as company/personal **brain**. Directly relevant to this vault's Obsidian raw/processed + TAG-INDEX pattern and Hermes MEMORY.md limits.

## Why it matters

Validates **file-first knowledge graphs** (like this wiki) as agent infrastructure, not just note-taking — with explicit gap that harness keyword memory (Hermes FTS5) and semantic Mem0 layer solve different problems.

## Related

- [[agent-memory-landscape-2026]]
- [[memory-is-retained-consequence]]
- [[knowledge-system-compounding-obsidian-vellum]]
- [[openclaw-hermes-supervisor-setup]]
- [[540k-lines-i-didnt-need-garry-tan]]