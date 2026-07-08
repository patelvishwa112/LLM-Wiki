---
tags:
  - distillation
  - training
  - post-training
  - rl
  - sft
  - agents
  - continual-learning
  - trl
  - gemma
  - deepseek
source: https://x.com/sergiopaniego/status/2074863503312044499
date: 2026-07-08
type: bookmark
author: sergiopaniego
description: "Sergio Paniego maps 2026 frontier distillation into off-policy, on-policy multi-teacher, and self-distillation with lab examples and TRL Class 2 tie-in."
summary: "Sergio Paniego maps 2026 frontier distillation into off-policy, on-policy multi-teacher, and self-distillation with lab examples and TRL Class 2 tie-in."
raw: "[[raw/sergiopaniego_2074863503312044499]]"
---

# Distillation in 2026 frontier post-training

Companion write-up for the **Training an Agent** series (after SFT on traces): how post-training distillation shows up in real 2026 recipes, aligned with live Class 2 mechanics in TRL.

## Three patterns in production

| Stage | Idea | Examples cited |
|-------|------|----------------|
| **Off-policy** | Large IT teacher → smaller student (soft logits or hard generated text) | Gemma 3/4, DeepSeek-R1-Distill → Qwen/Llama via SFT on teacher text |
| **On-policy / multi-teacher** | Domain RL experts (often **same size**, specialized) grade student rollouts token-wise | DeepSeek-V4 (reverse KL), MiMo **MOPD**, GLM-5 stage recovery, Nemotron 3 Ultra (10+ teachers), Qwen3 (~1/10 RL GPU-hours) |
| **Self-distillation** | Teacher is a better *context* of the same weights | Composer 2.5 hint-conditioned privileged teacher; Thinking Machines pre-FT checkpoint for continual learning without forgetting |

## Why labs prefer distillation over pure RL here

Teachers supply **dense per-token feedback**; scalar RL rewards are one score per completion. Reports argue faster convergence on the behaviors that need fixing—Thinking Machines’ on-policy distillation post is cited as the practitioner-friendly version with compute numbers.

## Why it matters for agent training

The series treats distillation as the bridge after trace SFT: compressing capability, merging math/code/agentic RL experts into one deployable model, and stabilizing sequential training without catastrophic drift. Hands-on scripts are in TRL at reproducible scale; theory pointer: Nathan Lambert’s RLHF Book distillation chapter.

## Related

- [[training-agents-class-1-sft-by-agent]]
- [[openthoughts-agent-data-recipes-agentic-models]]
- [[rlhf-from-first-principles]]