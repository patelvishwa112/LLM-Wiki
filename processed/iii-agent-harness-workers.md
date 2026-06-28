---
tags:
- agents
- agent-harness
- iii
- agent-architecture
- workers
- orchestration
- policy-engine
- approval-gate
source: https://x.com/mfpiccolo/status/2060069083878408689
raw: '[[raw/mfpiccolo_2060069083878408689]]'
date: 2026-05-28
type: bookmark
author: mfpiccolo
description: How to Build Your Own Agent Harness
---

# How to Build Your Own Agent Harness

By Mike Piccolo (@mfpiccolo) | Founder & CEO @iiidevs

## Key Takeaways

- **Frameworks bundle 12+ concerns that should be independent.** Every serious agent team ends up rewriting its harness because you can't swap one layer without forking the whole framework.
- **The iii model: workers on a shared engine.** Each worker registers functions and triggers on a WebSocket bus. Every harness layer (auth, models catalog, policy engine, approval gate, budget tracker, hook fanout, session storage, context compaction) is a separate swappable worker.
- **Thin vs thick is a slider, not a fork.** A thin harness is 3 workers (orchestrator + provider + auth). A thick harness is all 14. You move the slider by adding/removing workers from config.
- **Fail-closed by construction.** Policy checks time out after 5 seconds and deny by default. No silent passthroughs.
- **Same primitive everywhere.** The harness workers are built on the same iii.trigger() primitive as your business logic. "Build your own harness" decomposes into "write a worker that registers these function IDs."

## Summary

Most agent teams adopt a framework (LangChain, CrewAI, OpenAI Agents SDK) that bundles the turn loop, tools, memory, and orchestration into one monolith. Mike Piccolo argues this is fundamentally wrong. Every long-running agent team eventually rewrites its harness because the framework's policy engine, approval UI, credential store, or budget tracker can't be swapped independently.

iii solves this by decomposing the harness into 14 independent workers on a shared WebSocket engine. Each worker registers functions and triggers on the bus. Replacing any layer (policy engine, model catalog, approval gate) means writing a new worker that registers the same function IDs — the rest of the stack never knows the difference. The harness becomes a composition of installable workers, not a framework you fork.

## Source

https://x.com/mfpiccolo/status/2060069083878408689

## Related

- [[autobrowse-browser-agent-memory]] — Skills as durable agent memory
- [[anshuman-athletickoder-on-building-agents-from-first-princip]] — Agent architecture from first principles
- [[sub-agents-are-a-promising-inference-time-scaling-primitive]] — Skills as reusable sub-agent primitives
- [[hermes-agent-changed-how-i-work]] — Hermes skills as durable memory
- [[coding-agent-harness-eight-pillars]] — Agent harness evaluation framework
