---
tags:
- training
- agents
- rl
- sft
- data-curation
- agent-traces
- distillation
- open-source
- huggingface
- benchmarks
- teacher-model
source: https://x.com/sergiopaniego/status/2070511769315930493
date: 2026-06-26
type: bookmark
author: sergiopaniego
summary: 'OpenThoughts-Agent: open 6-stage agent training data pipeline (100+ ablations)
  — task mix/diversity dominates (~30 pts), GLM-4.7 beats GPT-5.3-Codex as teacher,
  5+ turn traces, don''t rewrite tasks; OpenThinkerAgent-32B 44.8% avg/7 benches;
  8B RL wins on pymethods2test, SFT+RL > SFT or RL alone.'
raw: '[[raw/sergiopaniego_2070511769315930493]]'
description: 'OpenThoughts-Agent: open 6-stage agent training data pipeline (100+
  ablations) — task mix/diversity dominates (~30 pts), GLM-4.7 beats GPT-5.3-Codex
  as teacher, 5+ turn traces, don''t rewrite tasks; OpenThinkerAgent-32B 44.8% avg/7
  benches; 8B RL wins on pymethods2test, SFT+RL > SFT or RL alone.'
---

# OpenThoughts-Agent — Data Recipes for Agentic Models

Open release on **curating agent training data** (not just scaling rollouts).

## Six-stage pipeline

1. Source tasks  
2. Mix  
3. Filter tasks  
4. Generate rollouts  
5. Filter rollouts  
6. Pick the teacher  

## Ablations (high signal)

| Knob | Lesson |
|------|--------|
| Task set | Largest lever (~30 pt swings); **diversity > duplicate rollouts** |
| Teacher | Capability ≠ teachability (Codex weak, GLM-4.7 strong) |
| Trace length | Prefer **5+ turns** |
| Difficulty filter | Small gain |
| Task rewrite/harden | Usually hurts — leave tasks untouched |

## Model outcome

**OpenThinkerAgent-32B** — 44.8% average on 7 benchmarks; generalizes to 4/5 held-out evals without training on them (per authors).

## RL recipe (8B)

**pymethods2test** — Python methods with docstrings + unit tests (Codeforces-style contracts). RL lifts mid-tier SFT more than heavily distilled SFT; **SFT then RL** best.

## Assets

- [HF collection](https://huggingface.co/collections/open-thoughts/openthinker-agent2)
- [Paper 2606.24855](https://huggingface.co/papers/2606.24855)
- [GitHub OpenThoughts-Agent](https://github.com/open-thoughts/OpenThoughts-Agent)

## Related

- [[training-agents-class-1-sft-by-agent]]
- [[continuous-batching-grpo-trl]]
- [[harbor-rl-coding-environments]]
- [[rlhf-from-first-principles]]