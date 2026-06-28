---
tags:
- agents
- agent-harness
- prompt-caching
- kv-cache
- cost-optimization
- langchain
- langsmith
- deep-agents
- observability
- inference
- token-economy
source: https://x.com/its_ao/status/2070556265906917860
date: 2026-06-26
type: bookmark
author: its_ao
summary: 'Alex Olsen (Deep Agents/LangChain): provider-agnostic prompt caching — explicit
  breakpoints + implicit fallback + stable prefix layout; 49–80% token cost cuts on
  real trajectories (Haiku/GPT mini/Gemini flash); LangSmith cache-read metrics; ties
  to KV-cache hit rate as production KPI.'
raw: '[[raw/its_ao_2070556265906917860]]'
description: 'Alex Olsen (Deep Agents/LangChain): provider-agnostic prompt caching
  — explicit breakpoints + implicit fallback + stable prefix layout; 49–80% token
  cost cuts on real trajectories (Haiku/GPT mini/Gemini flash); LangSmith cache-read
  metrics; ties to KV-cache hit rate as production KPI.'
---

# Prompt Caching with Deep Agents

Harness-level **KV / prompt cache** strategy for multi-provider agents — not just enabling the API flag.

## Why it matters for agents

Cost scales with **re-read prefix** every turn (system + tools + skills + history). Cache hit rate ≈ economic viability on long loops (aligns with Manus “KV-cache hit rate” metric).

## Provider fragmentation

| Mechanism | Notes |
|-----------|--------|
| Anthropic | Explicit breakpoints |
| OpenAI | Longest-prefix automatic |
| Gemini | Implicit caching |
| Others | Fireworks, Baseten — check docs |

Features diverge on TTL, prewarm, routing keys → harness must abstract.

## Deep Agents tactics

1. Breakpoints when available  
2. Implicit caching fallback  
3. **Prefix layout** — minimize bust when memory/compaction mutates tail  

`createDeepAgent` ships this; LangChain middleware for `createAgent`.

## Measured deltas

~77–80% on Haiku / GPT-5.4-mini trajectories; ~49% Gemini flash. Gains compound on long horizons.

## Ops requirement

**LangSmith** (or equivalent) must surface cache-read tokens per step — otherwise you can't tell caching from shorter chats.

## Hermes angle

Vault note [[agent-memory-landscape-2026]]: Hermes freezes MEMORY.md snapshot for **prefix cache** across sessions — same economic idea at smaller durable-memory scale.

## Related

- [[opus-48-token-economy-guide]]
- [[harness-is-the-product-context-aware-agents]]
- [[langchain-fireworks-trace-judge-100x-cheaper]]
- [[how-to-give-your-agent-memory]]
- [[agent-memory-landscape-2026]]