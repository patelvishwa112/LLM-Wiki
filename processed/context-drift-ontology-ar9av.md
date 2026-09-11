---
tags: ["agents", "ontology", "security", "knowledge-graph", "agent-ops"]
source: https://x.com/_ar9av/status/2094477621593858344
date: 2026-08-31
type: bookmark
description: "Arnav Gupta: context drift is org-ontology drift; 'wrong' is a relationship not an action property; write the org graph outside the model and diff it."
author: _ar9av
summary: "Arnav Gupta: context drift is org-ontology drift; 'wrong' is a relationship not an action property; write the org graph outside the model and diff it."
raw: "[[raw/_ar9av_2094477621593858344]]"
---

# Context Drift Is an Ontology Problem

Arnav Gupta (@_ar9av), Prismor. Seven years in retrieval (hotel ontology vs eleven names). Same `read_file(contracts/q3-renewal.pdf)` is routine at a 4-person startup and reportable at an insurer. Verdict is **subject × entitlements × data tier × approved use-case × owner** — state the agent never sees.

## Three named layers all model the task

Harness / context engineering / domain ontology. None models the **organization the task runs inside**. A hotel ontology holds months; an org ontology holds about a week (permissions, MCP installs, model swap, summarization quietly becoming reasoning).

Drift here is two clocks: org moves, agent's copy does not. You only compute a gap if both pictures live **outside** the model.

## Where it lands (Prismor)

One org graph; six enforcement discovery points, one judge. Typed edges (untrusted_content then private_data then external_comms as **path** vs co-occurrence). Session subgraph synthesized once, deny-by-omission after. Narrow agents are tractable to diff; a whole-toolbelt agent has no baseline.

Keep outside the model: graph on disk, resolve scope once / enforce per call, named accountable human, log state transitions not statements, check records not memory.

Vendor OSS: https://github.com/PrismorSec/prismor. Extract the **org-graph-outside-the-window** thesis.

## Related

- [[why-every-ai-accountant-fails-eya0]]
- [[graphiti-knowledge-graph-agent-memory]]
- [[llm-as-judge-architectures-runtime-joshrosen]]
