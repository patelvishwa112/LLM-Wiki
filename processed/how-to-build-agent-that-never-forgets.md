---
tags: ["agents", "memory", "knowledge-graphs", "rag", "architecture", "cron"]
source: https://x.com/rohit4verse/status/2012925228159295810
date: 2026-01-18
type: bookmark
author: "Rohit (@rohit4verse)"
raw: "[[raw/rohit4verse_2012925228159295810]]"
related: []
---

# How to Build an Agent That Never Forgets

## Key Takeaways

- **Memory is infrastructure, not a feature.** Vector similarity is not memory — embeddings measure similarity, not truth. "I love my job" and "I hate my job" embed nearly identically. You need structured memory with conflict resolution, time awareness, and decay.
- **Two production architectures.** File-Based Memory: 3-layer hierarchy (Resources → Items → Categories) with active memorization that rewrites summaries on each update. Context-Graph Memory: hybrid vector store + knowledge graph with subject-predicate-object facts, conflict resolution, and parallel retrieval.
- **Memory must decay.** "Never forget" means "remember what matters." Cron jobs for nightly consolidation, weekly summarization, and monthly re-indexing keep the system from rotting. Without maintenance, agents become confused, slow, and expensive.
- **Tiered retrieval saves tokens.** Don't dump everything into context. Pull category summaries → ask if sufficient → drill into items only if needed. Use time-decay scoring so a recent slightly-less-relevant memory beats a perfect match from six months ago.
- **Five fatal mistakes:** Storing raw conversations forever, blind embedding usage, no memory decay, no write rules, treating memory as chat history. Chat history is ephemeral; memory is a structured representation of what was learned.
- **Agent as OS mental model.** Process management (track concurrent tasks), memory management (allocate/update/free knowledge), I/O management (tools and users). RAM for volatile context, hard drive for persistent indexed knowledge.

## Summary

Rohit describes building a production-grade agent memory system after failing a technical interview on the topic. The core insight: most "agent memory" implementations are just RAG wrappers around vector databases, which fundamentally cannot handle time, context evolution, or conflicting information.

The solution is a dual-architecture approach. File-Based Memory organizes knowledge hierarchically (raw resources → extracted facts → evolving category summaries) with active rewrites that resolve contradictions on write. Context-Graph Memory uses a hybrid vector + knowledge graph with conflict resolution for precision applications. Both require background maintenance cron jobs (nightly consolidation, weekly summarization, monthly re-indexing) to prevent rot.

Retrieval is tiered and scored: synthesized queries, relevance filtering, time-decay ranking, and token-budgeted context assembly. The mental model shifts from "chatbot with history" to "operating system with RAM + hard drive + garbage collection."
