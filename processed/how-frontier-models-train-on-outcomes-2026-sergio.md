---
tags: ["training", "rl", "rlvr", "grpo", "post-training", "agents", "distillation", "trl", "verifiable-rewards", "dapo", "deepseek", "huggingface"]
source: https://x.com/sergiopaniego/status/2086805987705417851
date: 2026-08-10
type: bookmark
description: "Sergio Paniego maps 2026 frontier post-training RL — verifiable rewards, GRPO variants (DAPO/GSPO/CISPO), agentic environments, and RL-then-distill pipelines."
author: SergioPaniego
summary: "Sergio Paniego maps 2026 frontier post-training RL — verifiable rewards, GRPO variants (DAPO/GSPO/CISPO), agentic environments, and RL-then-distill pipelines."
raw: "[[raw/sergiopaniego_2086805987705417851]]"
---

# How frontier models train on outcomes in 2026

Companion essay for **Training an Agent Class 3 (RL / GRPO)** (Sergio + Ben). Does not re-teach GRPO; situates class ideas in public frontier lab reports (as of ~Aug 2026). Pairs with prior class notes on SFT traces and distillation.

Originally on Hugging Face Blog.

## Lineage (brief)

1. **RLHF** (InstructGPT) — preference reward model + PPO  
2. **DPO** — preferences without online sampling loop  
3. **Reasoning RL / RLVR** — reward = executable check  
   - o1 (train-time + test-time compute, opaque algo)  
   - Tulu 3 coined **RLVR**  
   - DeepSeek-R1 pure RL + **GRPO** (from DeepSeekMath) + “aha” longer thinking  
   - Llama 4 online RL as pipeline core (filter medium-hard prompts)

## Three patterns

### 1. Rewards you can execute

If you can run a check, you have a reward:

- Qwen3 Reasoning RL: GRPO on **query–verifier pairs**  
- MiMo-7B: 130K verifiable math/code; **test-difficulty-driven** code reward (sparse-reward fix)  
- Magistral: math numerical answers + code tests only  
- Gemma 3: code execution feedback + math ground truth  
- Kimi K2: self-critic, but critic distilled from **on-policy RLVR rollouts**  
- GLM-5: hybrid rule-based + ORMs + GRMs  

Class parallel: MBPP asserts / verifiable vs intentionally broken reward run.

### 2. GRPO became a family

Original GRPO is the teaching base; labs modify it:

| Variant | Lab / note |
|---------|------------|
| DAPO | ByteDance: Clip-Higher, Dynamic Sampling, token-level PG, overlong shaping |
| Dr. GRPO | Fixes length bias favoring long wrong answers |
| GSPO | Qwen: sequence-level ratio/clip (Qwen3 improvements) |
| CISPO | MiniMax: clip IS weights not token updates |
| Magistral | filters **zero-advantage groups** (class metric `frac_reward_zero_std`) |

TRL (Aug 2026): `GRPOTrainer` default `loss_type="dapo"`; plain `"grpo"` marked not recommended (length bias). GSPO via `importance_sampling_level="sequence"`. TRL paper index has configs.

### 3. Reward → environment (agentic RL)

Model acts (files, tools, commands); outcome reward at end of rollout.

- LFM2.5-2.6B: sandbox + GRPO + judge + programmatic checks + safety gate  
- Cursor Composer: RL in diverse dev environments  
- Also: Kimi K3, GLM-5, Nemotron 3 Ultra, MiniMax Forge  

→ **Class 4** topic.

## RL then distillation

Not alternatives — consecutive stages:

1. RL builds domain specialists with outcome rewards  
2. On-policy distillation merges into unified student  

Examples: DeepSeek-V4 (GRPO experts → reverse KL OPD), MiMo-V2-Flash multi-teacher OPD (RL on teachers), LFM2.5 (RLVR teachers then student agentic RL).

## Class scale-up

0.6B class runs show same failure modes (entropy collapse ↔ DAPO Clip-Higher). Length growth: Dr. GRPO fixes objective bias; broken class run paid for length directly — similar curves, different cause.

## Scope limits (honest)

Public reports only; Gemma 4 excluded (no post-train detail); Anthropic/Cohere not surveyed; OpenAI only via o1 post. Pointer to Interconnects frontier recipe reviews (Lambert / Timbers).

## Why it matters

Best single map tying **Training Agents Class 3**, TRL defaults, RLVR, GRPO variants, and RL→distill production stacks. Complements verifiability/RLVR and distillation vault notes.

## Related

- [[grpo-trl-training-agents-class3-sergiopaniego]]
- [[distillation-post-training-frontier-2026]]
- [[training-agents-class-1-sft-by-agent]]
- [[verifiability-constraint-rlvr-unverifiable-tanayj]]
- [[continuous-batching-grpo-trl]]
- [[why-on-policy-distillation-works]]
- [[rlhf-from-first-principles]]
- [[harbor-rl-coding-environments]]
- [[policy-gradients-timeline-reinforce-to-grpo]]
- [[frontis-ma1-openmle-meta-evolution-neural-avb]]
