---
tags:
  - continual-learning
  - agent-harness
  - observability
  - evals
  - trace-data
  - harness-engineering
  - langchain
  - langsmith
  - training
  - production-traces
source: https://x.com/vtrivedy10/status/2074509344155066517
date: 2026-07-07
type: bookmark
description: "Viv Trivedy (LangChain) — traces as the substrate for continual learning, harness engineering, and post-training; Scaling Dreaming, LangSmith Engine, and Harness→FT→Harness funnel."
raw: "[[raw/vtrivedy10_2074509344155066517]]"
---

# Improving Agents is a Data Mining Problem

**Author:** Viv Trivedy (@Vtrivedy10), LangChain Labs  
**Context:** AI Engineer World Fair 2026 talk — slide walkthrough with commentary

## Core thesis

Continual learning, harness engineering, and post-training are not separate disciplines — they share one substrate: **curating data at scale from agent traces** to run experiments and close improvement loops. Every continual-learning company is effectively an observability company (and vice versa) because traces are the currency of long-horizon agent improvement.

## Practical recipe

1. Ship a decent agent to kickstart the data flywheel.
2. Mine traces to see what to fix.
3. Curate evals (treat evals as training data — hill-climb until behaviors transfer).
4. Run targeted experiments along axes you care about.

**Scaling Dreaming:** integrating experience back via SFT/RL, harness changes (instructions, tools, orchestration), and memory/context stores — at scale over long horizons.

## Trace mining at scale

Agents are opaque vs traditional code; traces bridge understanding. Volume creates **cost** (tokens) and **context** (finding signals in millions of long traces) problems — hence specialized agents/models for curation. Open, fine-tuned trace judges can beat closed frontier models on narrow mining tasks at far lower cost; at high volume, owned inference can beat per-token APIs.

**LangSmith Engine:** compound agents that read traces, detect issues, propose code fixes, generate evals, update memory stores, and iterate agents over time.

## Model–task–harness fit

Fit functions include fine-tuning (SFT, RL, DPO) and **harness engineering** (auto-research with eval scores as the metric). Example: **13.7% lift** on Terminal Bench 2.0 from harness adjustments driven by correctness metrics and trace behavior — traces densify feedback beyond scalar rewards.

**Recommended funnel:** Harness Engineering → Fine-Tuning → Harness Engineering  
- Harness first: fast, high-bandwidth knowledge transfer; strong in-context learning on capable base models.  
- Fine-tune when harness hits an intelligence ceiling or for distillation / high-volume inference.  
- Harness again after FT to generalize new capabilities across tasks.

## Why it matters

Unifies the production agent stack under one leverage point: **trace-derived data**. Pairs directly with cheaper trace judges, production eval loops, and harness-first iteration before heavier training — the same loop Hermes-style vaults and harnesses need for durable self-improvement without silent degradation.

## Related

- [[langchain-fireworks-trace-judge-100x-cheaper]]
- [[continual-learning-replit-agent-vibench]]
- [[learn-harness-engineering]]
- [[continuous-trace-intelligence-braintrust-topics]]
- [[how-to-give-your-agent-memory]]
- [[2-ways-self-evolving-agents-model-harness]]