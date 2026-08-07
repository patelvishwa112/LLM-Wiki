---
tags: ["recursive-self-improvement", "agents", "agent-harness", "harness-engineering", "continual-learning", "agent-memory", "distillation", "trace-data", "verification", "ai-strategy", "knowledge-management"]
source: https://x.com/yisongyue/status/2085043769297277114
date: 2026-08-05
type: bookmark
description: "Knowledge scaling as third axis — distill agent experience into reusable insights (when/why/what fails) that simplify harnesses and train wiser models."
author: yisongyue
summary: "Knowledge scaling as third axis — distill agent experience into reusable insights (when/why/what fails) that simplify harnesses and train wiser models."
raw: "[[raw/yisongyue_2085043769297277114]]"
---

# Knowledge Flywheels (@yisongyue)

## Key takeaways

Three scaling dimensions, not two:

| Axis | Improves |
|------|----------|
| **Model** | The reasoner (data, architecture, compute) |
| **Agent** | What it can do on a task (tools, search, verification, harnesses) |
| **Knowledge** | What the **next** task can build on |

**Knowledge** = reusable insights from agent experience: what works, what fails, **when**, and **why**.

### Experience → knowledge

Systems generate far more experience than they convert. Without curation, architectural constraints, recurring failures, better strategies, and cross-dataset relationships stay tied to one run and get rediscovered.

A **knowledge flywheel** works both ways: experience → abstractions, then abstractions → new situations.

### Evidence cited

- **KSI (knowledge-centric self-improvement)** — disposable agents contribute/critique evidence into a shared KB; better cost/performance than elaborate agent-centric SI on reasoning/coding/terminal.
- **EinsteinArena** — open math + verifier feedback + idea refinement → cumulative SOTA.
- **Asari AI** — inference-stack optimization campaigns leave better code **and** process lessons.
- **Trace2Skill** — execution traces → transferable declarative skills.
- **Cartridges / MeMo** — encode knowledge into reusable learned memory.

### Harness implication

```text
task + model + tools + knowledge → task-specific harness
```

Persistent asset is not one harness but the **knowledge** from which many harnesses are constructed. Move decompositions, checks, and failure modes out of runtime search.

### Wiser models + RSI path

Curate judgment (what generalizes, where rules break) for on-policy distillation — not raw traces. RSI improves **how** the system extracts/tests/organizes knowledge, not only solutions.

Domains of need: vast scientific archives (HuBMAP, DANDI, Gaia) and large software ecosystems.

## Why it matters

Bridges harness engineering, trace mining, memory/skills, and RSI into one “third axis” framing. Complements loop-is-the-moat (verifier+synthetic flywheel) with **knowledge curation** as the compounding substrate.

## Related

- [[loop-is-the-moat-rsi-m0egpt]]
- [[anthropic-recursive-self-improvement]]
- [[improving-agents-data-mining-traces]]
- [[continual-learning-replit-agent-vibench]]
- [[how-to-give-your-agent-memory]]
- [[memory-engineering-forgetting-policy-leanxbt]]
- [[trying-to-actually-define-continual-learning-oneill]]
- [[three-layers-harness-loop-graph-lunarresearcher]]

## Source

https://x.com/yisongyue/status/2085043769297277114
