---
tags: ["rag", "knowledge-graph", "graphrag", "agents", "retrieval", "dspy", "mcp", "anthropic", "microsoft", "agent-memory", "second-brain", "prompt-engineering"]
source: https://x.com/sprytixl/status/2078778799064584535
date: 2026-07-20
type: bookmark
author: sprytixl
title: "Graph Engineering vs RAG — relationships over text chunks"
description: "Creator roundup arguing Graph Engineering (GraphRAG-style KGs) beats vanilla RAG on global/causal questions; cites Microsoft GraphRAG, DSPy/STORM, KG scaling laws, LaunchNotes+Claude/MCP. Skeptical of overclaiming Stanford/Anthropic 'replaced RAG'."
summary: "Creator roundup arguing Graph Engineering (GraphRAG-style KGs) beats vanilla RAG on global/causal questions; cites Microsoft GraphRAG, DSPy/STORM, KG scaling laws, LaunchNotes+Claude/MCP. Skeptical of overclaiming Stanford/Anthropic 'replaced RAG'."
raw: "[[raw/sprytixl_2078778799064584535]]"
---

# Graph Engineering vs RAG — relationships over text chunks

## Why it matters

Compact field guide (with links) for **when chunk RAG fails** — multi-hop / global / causal questions — and what people mean by **Graph Engineering**: extract entities+relations, store triples, query structure, ground answers. Useful bibliography even if the packaging is hype-heavy.

## Thesis

- Regular RAG searches **text**; Graph Engineering searches **relationships**.
- Local lookup (“about entity X”) can work with chunks; global themes and causation need explicit graph structure.
- Headline metrics (as attributed to Microsoft GraphRAG / ChatP&ID paper arXiv:2603.22528): **~18% better accuracy, ~85% lower cost** vs regular RAG — treat as domain-specific, not universal.

## Stack of citations (as linked)

| Source | Role in argument |
|--------|------------------|
| Microsoft GraphRAG | Text → KG; local vs global Qs |
| DSPy (arXiv:2310.03714) | Model as node in **pipeline** graph |
| STORM (arXiv:2402.14207) | Research workflow as structured steps |
| KG scaling (arXiv:2505.16276) | Right graph > bigger model (26 OSS models) |
| TACL relational memory | Explicit relations → fewer logical errors |
| KEPLER | LM + KG embeddings joint training |
| Anthropic LaunchNotes Graph + MCP | GitHub/Jira/Linear graph; 5× incident detect, −50% meetings (case study) |
| LLM-assisted KGE (arXiv:2307.06917) | LLMs good at extract/normalize; schema/dedup need humans |

## Pipeline + five prompt stages

Extract → normalize/dedupe → query → grounded answer → maintenance. Prompts are **stage-local**, not a substitute for the graph.

## Claude / MCP framing

1. Extract graph from text  
2. NL → graph query → explain  
3. MCP as durable transport to graph DBs  

## Five “businesses” (author list)

Due diligence, sales intel, eng intel, research intel, personal knowledge OS — with income ranges that are **unverified marketing**.

## Skeptical read

- Creator funnel (“DMs open,” income angle); diagrams in Firecrawl dump were repeated placeholders.
- Reply critique (in-thread): **does not prove** Stanford/Anthropic “replaced RAG.” DSPy/STORM are pipeline/research graphs, not GraphRAG clones. LaunchNotes is one customer story.
- “18%/85%” should be traced to the specific GraphRAG/ChatP&ID setup, not treated as a law of nature.
- Honest paper line kept: **zero-shot full graph gen still needs human schema/dedup review**.

## Key takeaways

- Prefer graphs when the question needs **paths and global structure**, not nearest chunks.
- Distinguish **knowledge graph** (world) from **control/pipeline graph** (system) — same word, different layers (see [[loops-vs-graphs-polygres-infinite-context-daleverett]], [[graph-engineering-14-step-roadmap-0xcodez]]).
- Keep the linked primary sources; discount monistic “everyone moved to Graph Engineering” rhetoric.

## Related

- [[loops-vs-graphs-polygres-infinite-context-daleverett]]
- [[graph-engineering-14-step-roadmap-0xcodez]]
- [[how-vector-database-works]]
- [[production-rag-agents-technmak]]
- [[cerebras-knowledge-base-hybrid-search-mcp]]
- [[gbrain-markdown-git-brain-mem0]]
- [[graphiti-knowledge-graph-agent-memory]]
- [[open-knowledge-format-okf-google]]
- [[agent-memory-landscape-2026]]
- [[are-you-still-tuning-llms-by-hand-gepa]]
- [[automate-writing-llm-prompts-dspy]]
