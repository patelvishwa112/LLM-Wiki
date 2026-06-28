---
tags:
- agents
- agent-memory
- knowledge-graphs
- entity-resolution
source: https://x.com/pauliusztin_/status/2058163537114259691
raw: '[[raw/pauliusztin__2058163537114259691]]'
date: 2026-05-23
type: bookmark
description: Unified Memory Layers — Entity Resolution vs Deduplication
---

# Unified Memory Layers — Entity Resolution vs Deduplication

## Summary
Paul Iusztin shares hard-won insights from building unified memory layers with knowledge graphs. The key discovery: most people conflate entity resolution with deduplication, but the best memory systems separate naming from identity. He studied how mem0, cognee, and Neo4j approach this and developed a two-stage pipeline.

## Key Takeaways

**1. Resolution (What should we call this?)**
- Handles typos, acronyms, and surface-form similarity
- Uses exact, fuzzy, and semantic matching against names of nodes of the same type
- Examples: "NYC" → "New York City", "JP Morgan" → "JPMorgan Chase"
- Only updates canonical names — no graph merges happen yet
- Similar names alone are NOT strong enough evidence that two entities are identical

**2. Deduplication (Is this the same real-world entity?)**
- Embeds full entity context and compares against existing nodes
- Uses semantic + fuzzy similarity across the full context
- Three outcomes based on similarity score:
  - High confidence (≥0.95) → auto-merge
  - Medium confidence (>0.85) → human review
  - Low confidence (≤0.85) → new node

**The core design principle: evidence strength = permission strength**
- Weak evidence → new node
- Strong evidence → merge
- Uncertain evidence → review queue

This prevents false merges that silently corrupt the graph as memory scales.

## Connections
- [[graphiti-knowledge-graph-agent-memory]] — Temporal knowledge graphs for agent memory
- [[quarq-agent-memory-architecture]] — Agent memory architecture patterns
- [[autobrowse-browser-agent-memory]] — Browser agent memory systems
- Orchestration with PrefectIO for durability and cost reduction
- Entity resolution pipeline mirrors the broader agent memory problem of knowing when to merge vs. keep separate
