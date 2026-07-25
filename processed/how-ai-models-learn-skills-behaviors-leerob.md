---
tags: ["training", "pretraining", "sft", "rl", "evals", "alignment", "model-spec", "continual-learning", "agents", "agent-memory", "llm-judges", "post-training"]
source: https://x.com/leerob/status/2080467752897146898
date: 2026-07-25
type: bookmark
description: "Lee Robinson lay explainer: pretrain → SFT → RL as book/film/coach; model specs + held-out evals; alignment quirks; agents still use file memory not true continual learning."
author: leerob
summary: "Lee Robinson lay explainer: pretrain → SFT → RL as book/film/coach; model specs + held-out evals; alignment quirks; agents still use file memory not true continual learning."
raw: "[[raw/leerob_2080467752897146898]]"
---

# How do AI models learn new skills and behaviors? (Lee Robinson)

Public-facing primer from Lee Robinson (@leerob) mapping model training to human onboarding and sports coaching. Aimed at non-ML readers; useful vault bridge between post-training mechanics and agent memory limits.

## Core pipeline (human analogy)

| Stage | Human parallel | Model parallel |
|---|---|---|
| Knowledge base | Read every book on basketball | **Pretraining** — predict patterns from huge corpora → book-smart base model |
| Study great play | Film of elite players | **SFT** — imitate desired behavior examples |
| Practice + coach | Play games; coach nudges decisions | **RL** — simulated work + rewards; weights nudged toward better choices |
| Target behavior | Ideal colleague traits | **Model spec / principles / constitution** — alignment target + eval guide |

Knowledge ≠ experience (“book smarts” vs “street smarts”); best systems max both. Coach = feedback that generalizes when alone. Research note: RL on honesty in one domain can transfer truthfulness more broadly.

## Specs, evals, alignment

- Write “correct” behavior down first (spec) for training and testing.
- Measure with practice tests vs **held-out** final exams — benchmarks must not be memorized answer keys.
- Objective checks (tests pass) + **LLM-as-judge** rubrics (like free-response AP grading).
- Intelligence alone fails product: style quirks (“Bottom line:”, LLM slop, over-compressed jargon) → document, penalize, A/B for user preference and outcomes.

## Continual learning gap (agent-relevant)

Weights do **not** update from live chat. Today’s substitute: write rules/skills/files into context. Works surprisingly well; still far from a new colleague who retains skills. Bridges vault notes on amnesiac-intern continual learning, Replit/ViBench loops, and harness-before-pretrain flywheels.

## Why it matters

- Clean separation of **knowledge (pretrain)** vs **behavior (SFT/RL)** for teaching and product design.
- Reminds operators that agent “learning” is mostly **context + skills**, not weight updates — design memory and evals accordingly.
- Model-spec + held-out eval framing pairs with trajectory judges and verifiable RL domains.

## Related

- [[trying-to-actually-define-continual-learning-oneill]]
- [[continual-learning-replit-agent-vibench]]
- [[how-to-build-your-own-llm-from-scratch-5-stage-pipeline]]
- [[rlhf-from-first-principles]]
- [[what-if-harness-comes-before-pretraining-lihanc02]]
- [[training-agents-class-1-sft-by-agent]]
- [[agent-as-a-judge-trajectory-evals-aparna]]
- [[learnings-training-llm-from-scratch]]
