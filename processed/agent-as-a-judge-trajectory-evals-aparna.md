---
tags: ["evals", "agents", "llm-judges", "observability", "arize", "trajectories", "agent-harness", "production"]
source: https://x.com/aparnadhinak/status/2075688574960488558
date: 2026-07-11
type: bookmark
author: aparnadhinak
description: "Aparna on paper→product Agent-as-a-Judge: trajectory failures, DevAI results, Swiss-cheese eval stack, Arize AX/Signal."
summary: "Aparna on paper→product Agent-as-a-Judge: trajectory failures, DevAI results, Swiss-cheese eval stack, Arize AX/Signal."
raw: "[[raw/aparnadhinak_2075688574960488558]]"
---

# Agent-as-a-Judge — Trajectory Evals

**Source:** [X Article @aparnadhinak](https://x.com/aparnadhinak/status/2075688574960488558) (co-authored @seldo)

## Summary

**Timeline:** Zhuge et al. (Meta/KAUST, Oct 2024, Schmidhuber senior) → ICML 2025 → You et al. survey (Jan 2026: procedural / reactive / self-evolving judges) → productized mid-2026 (~20 months paper→ship).

**Thesis:** LLM-as-a-judge fits single-turn 2023 apps. Agents fail in **trajectories** (loops, forgotten context, silent bad tool results, false “done”) while final answers still look fine. Column-mapped judges decide where failure lives before inspection.

**DevAI evidence:** agent judge ~90% alignment with expert consensus vs ~70% plain LLM judge; often beat individual experts; $31 vs ~$1,300 human time; ~50× faster. Memory on the judge hurt (error propagation); fresh evidence per requirement worked.

**Stack:** Swiss cheese — deterministic checks → LLM judges → **agent judges** → human spot-checks. Arize AX (sandbox agent judge on traces, NL instructions, no column mapping) + Signal (continuous production failure clustering). Caveats: nondeterminism, cost at scale, trajectory-length bias; still need human validation.

**Outlook:** eval as **flywheel** inside the agent, not external report card.

## Why it matters

Canonical argument for trajectory-level evals and agent judges in production agent stacks—pairs with loop-engineering and trace-mining notes.

## Related

- [[four-loops-ai-engineering-taxonomy-aparna]]
- [[writing-good-skills-measured-rulebook-aparna]]
- [[continual-learning-replit-agent-vibench]]
- [[improving-agents-data-mining-traces]]
- [[langchain-fireworks-trace-judge-100x-cheaper]]
- [[how-to-become-applied-ai-engineer-eyad-khrais]]
