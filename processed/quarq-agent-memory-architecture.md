---
tags: [llm, agent-architecture, memory, continual-learning, retrieval, open-source, faiss, rag]
type: bookmark
description: "Quarq open-source memory-first agent architecture with four-layer continual learning design."
source: https://x.com/quarqlabs/status/2059320863070286177
raw: "[[raw/quarqlabs_2059320863070286177]]"
author: QuarqLabs (@quarqlabs)
date: 2026-05-26
scraped: 2026-05-27
repo: https://github.com/quarqlabs/agent-oss
---

# We Are Open Sourcing Quarq Agent — A Memory-First Agent Architecture

QuarqLabs' memory-first AI agent, now open-source. Designed for continual learning across conversations with a 4-layer architecture that goes far beyond simple chat history storage.

## The 4-Layer Architecture

| Layer | Problem | Solution |
|-------|---------|----------|
| **1. Query** | Finding right evidence | Multi-hypothesis search across vector + keyword indexes, merged and deduplicated |
| **2. Storage** | Organizing by type | 3 memory types: Semantic (facts), Episodic (events), Procedural (instructions) |
| **3. Reasoning** | Preventing hallucination | Temporal safeguards, numerical safeguards, entity isolation, evidence insufficiency detection |
| **4. Learning** | Keeping memory accurate | Async background model reviews interactions, creates/updates/removes memories |

## Memory Types

- **Semantic:** FAISS + JSON — preferences, possessions, relationships, attributes
- **Episodic:** FAISS + JSON — conversations, meetings, purchases, decisions
- **Procedural:** JSON rules — formatting preferences, tone guidelines, project conventions

## Design Principles

1. **Retrieve Broadly, Reason Narrowly** — aggressive search, conservative reasoning
2. **Evidence Beats Confidence** — admit uncertainty over invention
3. **Time Is First-Class** — dedicated temporal reasoning safeguards
4. **Async Learning** — no latency penalty for memory improvement
5. **Context Is a Resource** — only load relevant info into prompt

## Key Takeaways

1. Storage is the easy part — retrieval, reasoning, and maintenance are the real memory challenges
2. Vector + keyword hybrid retrieval consistently outperforms either alone
3. Separating memory by type (semantic/episodic/procedural) keeps reasoning context-aware
4. Explicit reasoning constraints prevent hallucinated recall even with correct evidence available
5. Background async learning prevents memory from going stale without user-facing latency
6. **Status:** Archived research project, not maintained — but valuable reference architecture

## Relevance to Our Work
Directly applicable to Hermes' memory system. The 3-type memory taxonomy maps well to what we need: user profile (semantic), conversation history (episodic), and agent rules/skills (procedural). The hybrid retrieval + explicit reasoning safeguards pattern is worth adopting.
