---
tags: [orchestration, multi-agent, sakana-ai, models, agent-harness, grpo, collective-intelligence, routing]
source: https://x.com/amitiitbhu/status/2069023290182758497
raw: "[[raw/amitiitbhu_2069023290182758497]]"
date: 2026-06-22
type: bookmark
author: amitiitbhu
summary: "Sakana Fugu orchestrator models route queries across frontier LLMs instead of answering alone: Fugu picks one model via a fast selection head; Fugu-Ultra builds multi-model workflows trained with GRPO, with debate, build-and-debug, and specialist routing emerging at SOTA benchmarks."
---

# Sakana Fugu — Orchestrator Models

By Amit Shekhar (@amitiitbhu), Outcome School / AI education.

## What it is

**Fugu** (Sakana AI) treats the LLM layer as a **conductor**, not a soloist: read the user query, choose which frontier models to involve, define collaboration, synthesize one answer.

## Variants

- **Fugu** — Daily use; **one** best model per query from a lightweight **selection head** on hidden states (no extra generation for routing). ~single-model latency.
- **Fugu-Ultra** — Hard problems; full **agentic workflows** (subtasks, per-step model choice, access control). Slower, higher ceiling.

## Training & architecture notes

- Fugu: SFT with soft targets (KL), then **sep-CMA-ES** on end-to-end tasks.
- Fugu-Ultra: **GRPO** on workflow generation; **intra-workflow isolation** + **persistent shared memory** to avoid orchestration collapse.

## Why it matters

No frontier model dominates every domain. Framing orchestration as **collective intelligence** is an alternative scaling axis to raw parameter count — relevant to harness design, multi-agent routing, and inference-time compute allocation.

Reported highlights include strong **SWE-Bench Pro** scores vs pool models and non-coding stress tests (Rubik's cube, blindfold chess, trading sims, CAD).

## Emergent patterns

1. Debate → aggregate  
2. Build (e.g. GPT) → debug (e.g. Claude)  
3. Dynamic specialist routing per subtask  

## Related

- [[2-ways-self-evolving-agents-model-harness]]
- [[universal-agent-thesis]]
- [[sub-agents-are-a-promising-inference-time-scaling]]
- [[agent-harness-engineering-agentforge]]
- [[what-is-kv-cache-llms]]