---
title: Your First RL Run with Jev as the Reward Model
type: bookmark
description: "Sophia Yang trains a rank-8 LoRA on Qwen3.8-27B against Jev's probabilities as reward on Fireworks: mean reward 0.583 to 0.759 in 24 updates for $0.06 of judge calls."
tags: [rl, grpo, reward-models, llm-judges, lora, post-training]
source: https://x.com/sophiamyang/status/2102861619889918023
date: 2026-09-23
author: Sophia Yang
summary: "Sophia Yang trains a rank-8 LoRA on Qwen3.8-27B against Jev's probabilities as reward on Fireworks: mean reward 0.583 to 0.759 in 24 updates for $0.06 of judge calls."
raw: "[[raw/sophiamyang_2102861619889918023]]"
---

# Your First RL Run with Jev as the Reward Model

**Source:** Sophia Yang, 2026-09-23. A tutorial write-up of a toy RL run that trains a model to write less "AI slop," using TypeSafe's Jev as the reward model on Fireworks.

The setup is deliberately minimal: base model Qwen3.8 27B, frozen, with a rank-8 LoRA adapter as the only trainable parameters; 96 AI-generated prompts spanning posts, summaries, edits, replies and creative writing; 8 rollouts per prompt, scored by Jev, with above-average drafts reinforced and below-average ones discouraged; four prompt groups per update, so 96 prompts complete in 24 updates. Twenty-four held-out prompts are scored by the same judge for the before/after comparison. Jev is a TypeSafe model that turns unstructured state into typed probabilistic decisions — cheap and fast enough to use as a per-rollout grader.

The reward function is the interesting design choice: three binary-ish judgments (does it read naturally rather than like generic slop; is it useful writing for the request; does it add material claims unsupported by the context), combined as `reward = ((style + quality) / 2) * source_support`. The multiplication makes unsupported claims punitive rather than a mild penalty — a draft that invents facts loses most of its reward regardless of style. Mechanically it's GRPO-style group-relative advantage without PPO clipping: advantage normalized by group standard deviation (floored at 0.1, clipped to ±3), groups with no reward spread skipped, unclipped importance-sampling loss, one-over-length weighting, and a KL penalty (β = 0.05) anchoring to the untrained model.

Results after 24 updates: mean reward 0.583 → 0.759, style 0.681 → 0.767, source support 0.695 → 0.868, quality flat (0.947 → 0.932, already at ceiling), and word count 243 → 147. So essentially the whole improvement is "stop adding unsupported claims," and the side effect is a 40% shorter output. Yang is candid about the confound: length normalization and Jev's own preference for terseness both push that direction, citing Dr. GRPO's finding that dividing by length favors short outputs. She also flags that one judge scored both training and evaluation, so a second judge or human ratings would be needed to believe the numbers, and that the KL term prevents drift but does not prevent gaming Jev.

Cost is the headline number for anyone who assumed reward models are the expensive part: 896 Jev calls cost $0.061 with a median latency of 186 ms, while the Fireworks training run itself is an estimated $3–5 for 864 drafts over ~72 minutes. The tutorial ships as a repo with offline mock runs, a smoke test that gates training (32 fixed Jev checks, three of six prompts needing reward spread ≥ 0.10), a blind-review flow, and checkpoint promotion to a deployable LoRA.

## Why it matters

This demonstrates the cost structure that makes judge-as-reward RL routine: a grader fast and cheap enough that reward modeling stops being the bottleneck and the GPU bill dominates. The 0.583 → 0.759 with quality flat is also a clean illustration of what judge-optimization actually buys — it bought claim-grounding and brevity, not better writing, which is the failure mode anyone building with LLM judges should expect. Treat it as a calibration datapoint, not an anti-slop model: the author explicitly says a universal version needs more than RL on one judge.

## Key points

- Qwen3.8 27B + rank-8 LoRA, 96 prompts, 8 rollouts each, 4 prompts per update → 24 updates; 24 held-out eval prompts.
- `reward = ((style + quality) / 2) * source_support` — multiplicative gating on unsupported claims.
- Reward 0.583 → 0.759; style 0.681 → 0.767; source support 0.695 → 0.868; quality 0.947 → 0.932; words 243 → 147.
- 896 Jev calls = $0.061 at 186 ms median latency; full 72-minute training run ≈ $3–5 Fireworks + $0.06 Jev.
- Loss is unclipped importance sampling with group-relative advantages, KL β = 0.05, not PPO-clipped GRPO; groups with no reward spread are skipped.
- Author's caveats: same judge for train and eval, length-normalization bias toward short outputs, KL stops drift but not reward gaming, Jev and Astra sometimes disagree.

## Related

- [[how-to-fine-tune-llms-2026-grpo-ruler-art-akshay]]
- [[grpo-trl-training-agents-class3-sergiopaniego]]
- [[generative-verifiers-genrm-deepmind]]
- [[reward-hacking-and-tampering]]
- [[rl-environments-guide-llm]]
