---
tags:
  - training
  - rl
  - rlvr
  - rlhf
  - evals
  - alignment
  - agents
  - scaling-laws
  - ai-research
source: https://x.com/tanayj/status/2072766211256119475
date: 2026-07-02
type: bookmark
author: tanayj
description: "Tanay Jaipuria on Dario's unverifiable-task uncertainty—RLVR in math/code, verifier's law, rubric/process/generative rewards, and lab/data/formalization/physical-loop companies."
summary: "Tanay Jaipuria on Dario's unverifiable-task uncertainty—RLVR in math/code, verifier's law, rubric/process/generative rewards, and lab/data/formalization/physical-loop companies."
raw: "[[raw/tanayj_2072766211256119475]]"
---

# Verifiability constraint (RLVR vs unverifiable work)

**@tanayj** ties **Dario Amodei's** Dwarkesh caveat—novels, science discovery, Mars planning lack checkers—to where capability gains stall after **RLVR** wins in **math and code**.

## Verifier's law (Jason Wei)

Trainability tracks **how cheaply you can verify** outputs. RLVR hill-climbing explains SWE-bench / IMO jumps; most economic work has fuzzy or delayed rewards.

## When there's no checker

| Approach | Idea |
|----------|------|
| RLHF / Constitutional AI | Preference or principle-based rewards—alignment more than capability leaps |
| **Rubrics as rewards** | Decompose "good" into checkable items; LLM judge per rubric line (Scale, OpenRubrics) |
| **Generative RM** | Reason-then-score judges |
| **Process RM** | Reward intermediate reasoning steps |

## Commercial patterns

1. **Data + verifiers for labs** — expert rubrics in legal/health/finance; taste-focused players reject preference averaging  
2. **Formalize domains** — Lean-style self-checking; regulated verticals (Pramaana)  
3. **Closed physical loop** — propose in silico, verify in lab (Periodic, Isomorphic, Lila)

## Why it matters

Explains **why agents ace coding evals** but strategic/creative/social work lags—central for interpretability career bets, eval design, and agent harness verification.

## Related

- [[rlhf-from-first-principles]]
- [[langchain-fireworks-trace-judge-100x-cheaper]]
- [[agent-evals-practical-guide]]
- [[design-good-ml-experiments-grigorev]]
- [[zen-and-the-art-of-ai-research]]
- [[claude-fable-map-territory-unknowns-trq212]]