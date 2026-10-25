---
title: "Raschka: RLVR Round 2 — GRPO Stability, KL and Format Rewards"
type: bookmark
description: "Sebastian Raschka's second RL episode for building a reasoning model from scratch: clipped policy ratios, KL loss, entropy tracking and format rewards in GRPO."
tags: [rl, grpo, rlvr, training, post-training, reasoning]
source: https://x.com/rasbt/status/2108908657786355788
date: 2026-10-10
author: Sebastian Raschka
summary: "Sebastian Raschka's second RL episode for building a reasoning model from scratch: clipped policy ratios, KL loss, entropy tracking and format rewards in GRPO."
raw: "[[raw/rasbt_2108908657786355788]]"
---

# Raschka: RLVR Round 2 — GRPO Stability, KL and Format Rewards

**Source:** Sebastian Raschka (@rasbt), 2026-10-10. A post announcing part seven of his "Build A Reasoning Model From Scratch" series, the second episode on reinforcement learning with verifiable rewards.

The post is a chapter-by-chapter index (~1h50m) of an end-to-end GRPO debugging session rather than a summary of results. It starts by reading basic GRPO training metrics, moves training out of notebooks into Python scripts for longer runs, then walks through plotting logs, diagnosing instability, and evaluating checkpoints on MATH-500. From there the episode is about the two standard stabilisers: tracking advantage statistics and entropy (what entropy means, computing it in PyTorch, interpreting the values, adding it to the GRPO loop), and then clipped policy ratios — implementing the clipped loss and comparing results.

The second half covers reward hacking and KL divergence: adding a KL loss term, its limitations in the simplified form, then format rewards built around think tags — adding the special tokens to the tokenizer, implementing a format reward, measuring its effect, and gating the format reward on correct answers so it can't be farmed. It closes with further GRPO improvements from the research literature and next steps toward distillation.

The only substantive claim in the thread is Raschka's answer to a reader asking whether the KL term stops entropy collapse on longer runs: in his setup it did not, and clipped policy ratios were what helped most. A YouTube version is linked from the reply thread.

## Why it matters

Entropy collapse and reward hacking are the two failure modes that quietly waste GPU weeks in any RLVR run, and this is a rare public walkthrough that instruments both rather than presenting a final recipe. The practical takeaway for anyone training reasoning models — or evaluating a vendor's RL claims — is that clipping, not the KL penalty, is doing the stabilising work, and that format rewards need to be conditioned on correctness before they teach anything except the format.

## Key points

- Series episode: "Build A Reasoning Model From Scratch 7: Reinforcement Learning 2", ~1h50m, with a YouTube version.
- Coverage order: GRPO metrics → longer Python-script runs → log plotting → instability diagnosis → MATH-500 checkpoint evaluation.
- Entropy is treated as the diagnostic signal: computed in PyTorch, tracked per step, and read alongside advantage statistics.
- Clipped policy ratios are presented as the main stability fix, with a full implementation walkthrough.
- A KL loss term is added and then critiqued for the limitations of its simplified form.
- Format rewards need think-tag special tokens added to the tokenizer, and should only pay out for correct answers.
- Thread claim: after adding KL, entropy still collapsed on longer runs; clipped policy ratios helped most in this case.
- Ends on further GRPO improvements from the literature and distillation as the next step.

## Related

- [[policy-gradients-timeline-reinforce-to-grpo]]
- [[continuous-batching-grpo-trl]]
- [[grpo-trl-training-agents-class3-sergiopaniego]]
- [[how-to-fine-tune-llms-2026-grpo-ruler-art-akshay]]
- [[controlling-reasoning-effort-in-llms]]
