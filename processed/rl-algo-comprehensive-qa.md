---
tags:
- rl
- grpo
- ppo
- dpo
- moe
- deepseek
- training
- advantage
- kl-divergence
- importance-sampling
- reward-design
- opd
- dapo
- gspo
- cispo
source: https://www.k-a.in/rl-algo.html
date: 2026-06-08
type: bookmark
author: k-a.in
title: RL ALGO — Comprehensive Q&A
summary: Comprehensive RL Q&A covering GRPO/PPO/DPO variants, advantage computation,
  KL penalties, MoE routing, hyperparameter selection, and DeepSeek R1→V3.2→V4 evolution.
  Based on Xiuyu Li's interview questions.
raw: '[[raw/kain_rl-algo]]'
related:
- '[[rlhf-from-first-principles]]'
- '[[rl-interview-questions-2026]]'
- '[[rl-interview-answers-2026]]'
- '[[here-is-the-full-timeline-of-policy-gradients-from]]'
description: Comprehensive RL Q&A covering GRPO/PPO/DPO variants, advantage computation,
  KL penalties, MoE routing, hyperparameter selection, and DeepSeek R1→V3.2→V4 evolution.
  Based on Xiuyu Li's interview questions.
---

# RL ALGO — Comprehensive Q&A

## Key Takeaways

1. **GRPO advantage is pure group-normalized reward.** A_i = (r_i − mean(r_j)) / std(r_j). No critic, no reward model. The baseline is the group mean. This is why GRPO works for LLMs where value functions are hard to learn.

2. **Std normalization has a degenerate case.** When all group samples have the same reward (all correct or all wrong), std ≈ 0 and advantage becomes meaningless. Dr.GRPO and DAPO fix this by skipping/filtering zero-variance groups.

3. **KL penalty is redundant in RLVR.** When rewards are verifiable (unit tests, symbolic checks), the verifier self-insures against reward hacking. KL becomes drag — stops the policy from moving far enough to learn. DAPO/GSPO drop it.

4. **PPO clipping: the min ensures conservative updates.** When A_t > 0, clip prevents overconfidence. When A_t < 0, clip prevents escaping punishment. Without clipping: pure IS-weighted gradient → catastrophic steps → policy collapse.

5. **DeepSeek RL arc:** PPO → GRPO with verifiable rewards (R1) → unified mixed-RL (V3.2) → specialist GRPO + OPD merge into one model (V4). Each step removes more infrastructure while getting more stable.

6. **MoE RL is harder.** Routing makes gradients spiky, load balancing fights policy gradient, expert parallelism spreads rollouts, reference model for KL doubles memory. DeepSeek's Off-Policy Sequence Masking freezes routing paths from sampling and reuses them in training.

## GRPO Variant Quick Reference

| Variant | Key Change |
|---------|-----------|
| Dr.GRPO | Remove std norm, skip zero-variance groups |
| DAPO | Drop KL, clip-higher, dynamic sampling |
| GSPO | Sequence-level IS constraint |
| CISPO | Clip IS ratio in gradient, not objective |
| SAPO | Soft gating, continuous trust region |
| DPPO | Direct divergence estimate (TV/KL) |
| MaxRL | Sampling-based → max-likelihood |
| SimKO | Asymmetric top-K boost/penalty |

## Training Hyperparameters

| Param | Recommendation |
|-------|---------------|
| Group size G | 8-16 |
| LR | 1e-6 to 5e-6 (7B models) |
| PPO epochs | 1-4 (R1 used 1) |
| Gen length | Adaptive (EOS within max) |

## Connection to Other Notes

This pairs with [[rl-interview-questions-2026]] (questions) and [[rl-interview-answers-2026]] (answers from Vivek). Together they form a complete RL interview prep reference. The DeepSeek arc complements the policy gradient timeline in [[here-is-the-full-timeline-of-policy-gradients-from]].
