---
tags: ["agent-memory", "agents", "agent-harness", "memory", "forgetting", "kv-cache", "observability", "harness-engineering", "cost-optimization", "context-management"]
source: https://x.com/n01ennn/status/2083971749079581120
date: 2026-08-02
type: bookmark
description: "Memory engineering as cost/utility/control/hardware discipline — Stanford write-path cost, Microsoft utility density, Anthropic file control, Nvidia KV/HBM."
author: n01ennn
summary: "Memory engineering as cost/utility/control/hardware discipline — Stanford write-path cost, Microsoft utility density, Anthropic file control, Nvidia KV/HBM."
raw: "[[raw/n01ennn_2083971749079581120]]"
---

# How to be a Memory Engineer (@n01ennn)

## Key takeaways

- Agent memory fails less from “forgetting” than from **never forgetting on purpose** while ignoring write-path cost, stale data, and hardware pressure.
- Hold four lab lenses at once:
  1. **Stanford** — price the **write path**; measure **energy per correct answer** (accuracy-matched systems can differ ~47× in cost).
  2. **Microsoft** — keep **facts and skills**, not raw logs; optimize **utility density**; model-managed notes can beat dumping history.
  3. **Anthropic** — memory in **files** the agent can read/write/delete → inspect, export, audit, scope, rollback.
  4. **Nvidia** — memory hits **KV cache / HBM**; construction is prefill-heavy background work — rate-limit/batch so live queries aren’t stalled.
- Build order: write path → manual contradiction handling → **forgetting policy before scale** → hardware tuning. Don’t auto-merge contradictions blindly.

## Why it matters

Complements leanxbt’s four-shelf forgetting policy with lab-grounded cost and control. Same cluster as agent-memory landscape and continual-learning notes.

## Note on provenance

Playwright hit X “Something went wrong” on status and article URLs; raw is x_search synthesis. Refresh raw if full article becomes loadable.

## Related

- [[memory-engineering-forgetting-policy-leanxbt]]
- [[agent-memory-four-layer-stack-matthew-gunnin]]
- [[agent-memory-landscape-2026]]
- [[your-ais-memory-is-quietly-making-it-dumber]]
- [[how-to-give-your-agent-memory]]
- [[context-engineering-field-guide-phosphenq]]

## Source

https://x.com/n01ennn/status/2083971749079581120
