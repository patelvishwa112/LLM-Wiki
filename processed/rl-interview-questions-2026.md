---
tags:
  - rl
  - rlhf
  - training
  - interview-questions
  - ppo
  - grpo
  - infrastructure
  - llm
source: https://x.com/sheriyuo/status/2063295181131247674
date: 2026-06-06
author: Xiuyu Li (@sheriyuo)
type: bookmark
summary: "35 RL interview questions distilled from Zhihu experiences and recent discussions, spanning Algorithm (19) and Infrastructure (16). Covers Actor-Critic, PPO/GRPO variants, reward design, KL penalty, DPO, MoE train-inference mismatch, async RL frameworks, KV cache, parallelism strategies, and staleness. Modern RL hiring expects full-stack understanding."
related:
  - "[[rl-interview-answers-2026]]"
  - "[[rlhf-from-first-principles]]"
  - "[[microsoft-mai-thinking1-rank-noninvariance]]"
---

# RL Interview Questions 2026

**Source:** Xiuyu Li (@sheriyuo). 182K views, 3.6K bookmarks. Distilled from every RL-related interview experience on Zhihu.

## Algorithm (19 questions)

| # | Question |
|---|----------|
| 1 | Why use Actor-Critic instead of a pure Critic approach? |
| 2 | What is the relationship between KL divergence, cross entropy, and MLE? |
| 3 | How should rewards be designed in different RL scenarios? |
| 4 | How do importance sampling, rejection sampling, and other Monte Carlo methods fit into RL? |
| 5 | How is advantage computed in PPO and GRPO? Why subtract a baseline? Is std normalization necessary? |
| 6 | How do RL training and test-time scaling perform exploration differently? |
| 7 | How does PPO clipping work? Why take the minimum objective? How does CISPO differ? |
| 8 | Why does GRPO include a KL penalty? Why do DAPO and GSPO remove it? |
| 9 | What happens if loss is accidentally All Reduced multiple times during LLM training? |
| 10 | What is the reward function in DPO? Can reward hacking occur? How to mitigate? |
| 11 | What methods address train-inference mismatch in MoE models? |
| 12 | How to select group size, learning rate, PPO epochs, and generation length? |
| 13 | How do Dr.GRPO, DAPO, GSPO, CISPO, SAPO, DPPO, MaxRL, SimKO improve on GRPO? |
| 14 | How do TRPO, DPPO, and AReaL enforce trust-region constraints? |
| 15 | Can RL fundamentally expand the capability frontier of LLMs? |
| 16 | Based on ProRL, how to think about scaling RL training boundaries? |
| 17 | What improvements does OPD introduce over traditional RL and SFT? |
| 18 | At which stage of training does reasoning ability emerge in LLMs? |
| 19 | From DeepSeek R1 to V4, what RL-related improvements have been introduced? |

## Infrastructure (16 questions)

| # | Question |
|---|----------|
| 1 | How many model copies in memory during GRPO training? How much can optimizations save? |
| 2 | KV cache transfer optimization and multi-GPU communication strategies |
| 3 | INT8 vs FP8 tradeoffs — which for training, which for inference? |
| 4 | Long-tail problem in RL rollouts — how to address? |
| 5 | Continuous batching issues in RL training — vLLM vs SGLang differences |
| 6 | Measuring utilization in vLLM/SGLang — KV cache utilization evaluation |
| 7 | Backpropagation in large-scale multi-node RL training |
| 8 | Async RL frameworks and synchronization bottlenecks they solve |
| 9 | AReaL: are KV caches from previous policies preserved? |
| 10 | How does Expert Parallelism affect MoE throughput? |
| 11 | Compute-communication overlap in long-context training — Megatron vs FSDP |
| 12 | Deterministic execution and batch invariance — does atomic add solve it? |
| 13 | AReaL vs slime on the RL rollout bottleneck |
| 14 | Staleness in fully async RL training — typical values? |
| 15 | Data flow through slime — Megatron integration and loss computation |
| 16 | VeRL, TRL, Unsloth, AReaL, or slime — which to choose and why? |

## Key Notes

- No strict LLM RL / Agentic RL separation — answers differ by setting
- Modern RL hiring expects full-stack: algo researchers get infra questions and vice versa
- Answers available in [[rl-interview-answers-2026]]
