---
tags: ["agent-memory", "agents", "agent-harness", "context-management", "memory", "forgetting", "procedural-memory", "episodic-memory", "semantic-memory", "verification", "harness-engineering"]
source: https://x.com/leanxbt/status/2083915037635424462
date: 2026-08-02
type: bookmark
description: "Agent memory as four shelves plus engineered forgetting (TTL, eviction by value, supersede) — good memory is a forgetting policy, not a dump."
author: leanxbt
summary: "Agent memory as four shelves plus engineered forgetting (TTL, eviction by value, supersede) — good memory is a forgetting policy, not a dump."
raw: "[[raw/leanxbt_2083915037635424462]]"
---

# Memory Engineering: forgetting policy, not a store (@leanxbt)

## Key takeaways

- Memory is a **flow** (enter → consolidate → live bounded time → leave), not a growing bag of facts.
- Human memory works because it **forgets almost everything with precision**. Most agent memory systems do the opposite and choke.
- Core question is not “should we store this?” but **which shelf, and how fast does that shelf forget?**

## Four shelves (different lifetimes)

| Shelf | Contents | Lifetime |
|-------|----------|----------|
| **Working** | current task, drafts, intermediate reasoning | dies end of turn |
| **Episodic** | specific events (“504 on Tuesday”) | days/weeks, then decay |
| **Semantic** | durable extracted facts (plan, region) | long until contradicted |
| **Procedural** | skills / action sequences | longest |

## Consolidation > raw storage

- Do not write raw dialogue, tool dumps, or full turns into memory.
- On ingest: compress to crisp facts with filter **“Will this matter in a week?”** Most experience never enters — cheapest forgetting.

## Three forgetting mechanisms (all required)

1. **TTL** — each shelf has its own lifetime; untouched records expire.
2. **Eviction by value** — when full, drop least valuable (rarely used, low confidence, unconfirmed) — not only oldest.
3. **Superseding** — new fact contradicts old → replace; do not coexist.

Remove any one and the system fails in a specific way (bloat, overflow, or internal contradiction).

## Retrieval discipline

- Retrieved memory enters the context window — same cutting rules as context engineering.
- Relevance threshold (`RECALL_FLOOR`); irrelevant recall is noise.
- Access extends life (`last_used = now`) — reinforcement without immortality.

## How memory systems die

- **Bloat** — linear growth, slow retrieval, junk in context (no consolidation/TTL/eviction).
- **Rot** — acts on stale facts (no supersede).
- **Contradiction** — inconsistent answers depending on which duplicate surfaces.
- **False immortality** — working drafts leak into semantic and live forever (wrong shelf).

## Build order

1. Define four shelves with wired lifetimes and forgetting rules.
2. Consolidation on ingest (“matters in a week?”).
3. Enable all three forgetting mechanisms from day one.
4. Selective retrieval tied to context budgets.
5. Only then scale volume.

## Closing line

> Memory feels like accumulation… In fact it is **selection over time**. Good memory is not the one that remembers everything but the one that forgets well.

## Why it matters

Direct antidote to “vector store + save everything” degradation. Complements four-layer memory stacks, “memory is retained consequence,” “never forgets” guides, and “memory quietly making it dumber” hygiene essays. Same-author series with the conductor build.

## Related

- [[how-to-build-conductor-multi-agent-leanxbt]]
- [[agent-memory-four-layer-stack-matthew-gunnin]]
- [[agent-memory-landscape-2026]]
- [[memory-is-retained-consequence]]
- [[how-to-give-your-agent-memory]]
- [[how-to-build-agent-that-never-forgets]]
- [[your-ais-memory-is-quietly-making-it-dumber]]
- [[managed-agents-built-in-memory]]
- [[longmemeval-evaluating-agent-memory-across-sessions]]
- [[trying-to-actually-define-continual-learning-oneill]]

## Source

https://x.com/leanxbt/status/2083915037635424462
