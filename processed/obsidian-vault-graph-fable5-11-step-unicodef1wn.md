---
tags:
- graph-engineering
- second-brain
- obsidian
- fable-5
- agents
- agent-memory
- knowledge-graph
- hermes
- cost-optimization
- context-engineering
source: https://x.com/unicodef1wn/status/2080693998180606075
date: 2026-07-25
author: unicode (@unicodef1wn)
type: bookmark
description: "Obsidian second-brain graph for agents (Fable 5): ROUTER + index + atomic nodes + edges + retrieval logic + state. Pretty graph view is for humans; index is the engine. Target 2–3 files per answer vs whole vault."
summary: "Obsidian second-brain graph for agents (Fable 5): ROUTER + index + atomic nodes + edges + retrieval logic + state. Pretty graph view is for humans; index is the engine. Target 2–3 files per answer vs whole vault."
raw: "[[raw/unicodef1wn_2080693998180606075]]"
---

# Graph engineering: Obsidian vault → agent-usable graph (11 steps)

@unicodef1wn on why raw Obsidian piles fail agents: Fable 5 (or similar) burns hundreds of thousands of tokens reading ~2k notes and still often wrong. A second brain is only as good as the **routing graph**, not the vault dump.

Quote: "The pretty graph is for you. The index is for Fable 5."

## Layout

```
vault/
├─ ROUTER.md      # every session, tiny
├─ index.md       # one line per note: name | link | description
├─ nodes/         # one idea per file
├─ routines/      # save + find rules
└─ state.md       # persists across sessions
```

## Stack of ideas

1. Graph = routing structure (router, index, nodes, edges) — not Obsidian's visual web  
2. Whole engine in one folder (portable, legible)  
3. Pile vs graph vs system (system = graph + compounding memory)  
4–8. Build: tiny router (~≤500 tokens), **index first** (highest leverage), atomic nodes, deliberate edges, retrieval as **logic not model calls** (keywords → score index → open 2–3 sections → ≤1 edge)  
9–11. Prove with A/B (tokens/time/correctness); add `state.md` so runs compound; value lives in owned markdown (model-swappable)

## Failure modes

Raw vault; bloated router; missing index; mega-notes; model-as-search; no memory; structure before content.

## Why it matters

Maps cleanly onto OKF/Hermes vault patterns (index-first, processed+raw, TAG-INDEX). Same "addressable knowledge without stuffing context" thesis as thinking-database / infinite-context posts — applied to personal markdown.

## Related

- [[hermes-agent-10x-faster-vault-index]]
- [[open-knowledge-format-okf-google]]
- [[living-wiki-second-brain-hermes-leopardracer]]
- [[gbrain-markdown-git-brain-mem0]]
- [[second-brain-obsidian-night-shift-300-agent-swarm]]
- [[graph-engineering-substance-over-meme-akshay]]
- [[loops-vs-graphs-polygres-infinite-context-daleverett]]
