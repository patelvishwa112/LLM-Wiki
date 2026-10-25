---
title: "The RL Algorithm Progression: VPG to REINFORCE to PPO to GRPO"
type: bookmark
description: "Cameron Wolfe traces LLM RL as one policy-gradient lineage — VPG, REINFORCE, actor-critic/PPO, GRPO — with DAPO/GSPO/CISPO as detail changes on the same core."
tags: [rl, training, post-training, grpo, rlhf, models]
source: https://x.com/cwolferesearch/status/2103195163740832169
date: 2026-09-24
author: Cameron R. Wolfe, Ph.D.
summary: "Cameron Wolfe traces LLM RL as one policy-gradient lineage — VPG, REINFORCE, actor-critic/PPO, GRPO — with DAPO/GSPO/CISPO as detail changes on the same core."
raw: "[[raw/cwolferesearch_2103195163740832169]]"
---

# The RL Algorithm Progression: VPG to REINFORCE to PPO to GRPO

**Source:** Cameron R. Wolfe, Ph.D., 2026-09-24. A long-form X post condensing his LLM RL writeup into a five-step genealogy of policy-gradient algorithms.

Wolfe argues that the zoo of RL algorithms used for LLM post-training is a single coherent idea refined five times: VPG → REINFORCE → PPO (actor-critic) → GRPO → GRPO variants. Vanilla policy gradient sets the template — a gradient of log-probability multiplied by a learning signal, pushing up actions that produce high reward and down actions that produce low reward. The variant is simply a sampled Monte Carlo estimate of an expectation that cannot be computed exactly, which makes it tractable but high-variance; subtracting a baseline removes some of that variance without biasing the gradient.

The next step swaps the crude baseline for a learned value function, giving the actor-critic split: a policy trained alongside a critic that predicts expected return, and an advantage computed as the gap between realised return and that expectation. PPO is the best-known instance, pairing advantage estimates with a clipped importance-ratio objective so the policy cannot be moved too far from the sampling policy in a single update — allowing multiple epochs over the same rollouts without destructive updates.

GRPO removes the critic entirely. Instead of a value model, it samples several completions per prompt and derives each completion's advantage from its reward relative to the rest of its group, keeping PPO-style clipping while eliminating the critic's memory, compute, and engineering overhead. Wolfe notes that later methods — DAPO, Dr. GRPO, GSPO, TIS, CISPO — do not replace this framework but adjust loss aggregation, reward normalization, sampling, clipping, importance ratios, and off-policy handling. His stated payoff: mastering VPG, advantage estimation, importance sampling, and constrained updates makes most new RL-for-LLM papers readable, and in a reply he places RLOO as a REINFORCE variant that corrects the bias in its baseline rather than as a GRPO ancestor.

## Why it matters

RL recipe choices for post-training are usually presented as competing algorithms with separate papers and ablations; this note reframes them as knobs on one objective, which is the right mental model when you have to debug a training run. If a GRPO run is misbehaving, knowing that clipping, group-relative advantage normalization and importance sampling are the load-bearing pieces tells you where to look, and knowing a critic is optional tells you what you are actually paying for by adding one.

## Key points

- Lineage: VPG → REINFORCE → PPO (actor-critic) → GRPO → GRPO variants (DAPO, Dr. GRPO, GSPO, TIS, CISPO).
- The universal policy-gradient form: gradient of log-probability of an action times a learning signal (return or advantage).
- REINFORCE is a Monte Carlo estimate of the VPG expectation — computable in practice, but high variance; a baseline reduces variance.
- Actor-critic replaces the baseline with a learned value function; advantage = return minus expected return from that state.
- PPO adds a clipped surrogate objective on the importance ratio, permitting multiple policy updates per batch of rollouts.
- GRPO drops the critic and estimates advantage from a completion's reward relative to other completions of the same prompt, keeping PPO-style clipping.
- Recent variants modify loss aggregation, reward normalization, sampling, clipping, importance ratios, and off-policy data handling, not the underlying framework.
- Wolfe on RLOO: a REINFORCE variant that corrects a bias introduced by REINFORCE's baseline — not a GRPO predecessor.

## Related

- [[policy-gradients-timeline-reinforce-to-grpo]]
- [[rlhf-from-first-principles]]
- [[grpo-trl-training-agents-class3-sergiopaniego]]
- [[how-to-fine-tune-llms-2026-grpo-ruler-art-akshay]]
- [[verifiability-constraint-rlvr-unverifiable-tanayj]]
