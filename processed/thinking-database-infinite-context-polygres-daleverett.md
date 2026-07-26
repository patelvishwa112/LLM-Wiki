---
tags:
- polygres
- postgres
- agent-memory
- agents
- knowledge-graph
- context-management
- databases
- enterprise
- harness-engineering
source: https://x.com/daleverett/status/2080883869281386672
date: 2026-07-25
author: dale (@daleverett)
type: bookmark
description: "Polygres 'thinking database': infinite context = addressable rows/relations/embeddings on demand, not stuffing the company into the prompt. Better context over more context; Postgres as system of thought."
summary: "Polygres 'thinking database': infinite context = addressable rows/relations/embeddings on demand, not stuffing the company into the prompt. Better context over more context; Postgres as system of thought."
raw: "[[raw/daleverett_2080883869281386672]]"
---

# Thinking database / infinite context (Polygres)

@daleverett product vision: historical split was DB stores facts, app retrieves, human thinks. Agents must investigate, remember, connect evidence, decide — but only reason inside the current context window → institutional memory + agent amnesia.

## Claim

Not a DB that replaces the main model — one that **helps it reason**: start at a customer, follow orders/tickets, similar incidents, filter noise, assemble needed evidence.

**Infinite context window** ≠ one giant company prompt. = reach any relevant row, relationship, or embedding **when it matters**. Immediate context stays focused; addressable knowledge = whole DB.

Tagline: **More context is not the goal. Better context is.**

## Systems of record → systems of thought

- Every row available without loading  
- Every relationship followable without pre-expanding  
- Every embedding searchable without export to a side system  
- Selective immediate context; unbounded addressable context  

Polygres: turn Postgres from system of record into a thinking helper. (CTA: free signup limited time.)

## Skeptical read

Vision/product post; thin on architecture vs prior art (tool-using agents + SQL/graph DBs already do partial versions). Durable idea: **retrieval/traversal as the infinite window**, not context stuffing.

## Related

- [[loops-vs-graphs-polygres-infinite-context-daleverett]]
- [[open-knowledge-format-okf-google]]
- [[obsidian-vault-graph-fable5-11-step-unicodef1wn]]
- [[cerebras-knowledge-base-hybrid-search-mcp]]
- [[own-your-intelligence-harrison-chase]]
- [[gbrain-markdown-git-brain-mem0]]
