---
title: "Gero-4B: Training a Calibrated Decision Model with Staged RL"
type: bookmark
description: "vixhal on turning Qwen3-4B into a calibrated decision model with a shared branch scorer, content-free stage-2 data, and a proper-scoring-rule RL reward."
tags: [rl, training, post-training, calibration, decision-making, lora, evals]
source: https://x.com/TheVixhal/status/2106439792800198966
date: 2026-10-03
author: "vixhaℓ"
summary: "vixhal on turning Qwen3-4B into a calibrated decision model with a shared branch scorer, content-free stage-2 data, and a proper-scoring-rule RL reward."
raw: "[[raw/TheVixhal_2106439792800198966]]"
---

# Gero-4B: Training a Calibrated Decision Model with Staged RL

**Source:** vixhal (@TheVixhal), 2026-10-03. A long build log on training Gero-4B, a Qwen3-4B model fine-tuned on a MacBook to output calibrated probabilities over a fixed set of options.

The target is a "decision model" rather than a chat model: given a ticket it returns a probability distribution over teams, severity levels, or yes/no, so downstream code consumes numbers instead of parsing text. Accuracy is the easy half; the hard half is calibration — a 0.9 should be right nine times out of ten, which is what lets you auto-handle everything above 0.95 and route the rest to a human. Chat models fail exactly here, claiming 95% about things they get wrong half the time.

The build is split into three single-job stages. Stage 1 fixes a prompt format where the context is a prefix and each option becomes its own branch, with the option list deliberately kept out of the prefix. Stage 2 converts the LLM into a scorer: the LM head is deleted, a single `Linear(2560, 1)` reads one score from the last token of each branch, and a softmax runs across branches. Prefix keys/values are cached once and handed to every branch, so cost is flat in the number of options, and because branches are separate rows under a causal mask, option order cannot leak — shuffling options changed scores by 0.0. This replaced a first attempt at a 256-slot classification head that broke past six options because slots 6-255 never left their random initialisation.

Stage 2 data is content-free by construction — invented crates, shelves, and codes like `QX-417A` — so the model can only learn the format, not the content: 50/50 facts and negation, rotating yes/no wording, distractors drawn from the same state, options sampled log-uniformly up to 256. A data checker that refuses to train on leaky datasets is called the biggest lesson of the project, and training uses soft targets plus two separate optimizers because multiplying the new scorer's gradients by 20 is a no-op under Adam.

Stage 3 is RL under a proper scoring rule. A naive "reward the confidence of the answer you picked" objective drives the correct answer's probability from 0.418 to 0.001 by learning to pick near-certainly-wrong options; the replacement splits the reward into a full-distribution log-score term and a decision-calibration term over the top answer, sampling G=8 outcomes from the data rather than the model. The KL anchor was set to weight 0 because it pulls the optimum away from the truth, and the export to a plain Hugging Face `Qwen3ForSequenceClassification` matched the training checkpoint on 98.8% of 1,866 held-out items.

## Why it matters

Calibration is the property that makes model output safe to gate automation on, and almost nobody ships it because the naive reward for it is exploitable. The reusable parts are the invariants rather than the model: shuffle-invariance by construction, zero-gradient-at-truth as a test for any loss term you add, and a structure probe during RL to detect one stage quietly overwriting another. The whole run fit on a 24 GB laptop, which puts calibrated decision heads within reach of small teams that just want to route tickets.

## Key points

- Gero-4B is Qwen3-4B with LoRA on the last 8 layers only, trained in Apple MLX on an M5 Pro with 24 GB.
- First design, a 256-output classification head over numbered options, collapsed beyond 6 options: rows 6-255 were still at random init because the data rarely had more options.
- Shared scorer + one branch per option gives order invariance (max score delta 0.0 on shuffle), unbounded option counts, and charges the prefix cost once.
- Correlated negation tokens taught "flip the answer on 'not'"; real entailment accuracy dropped 0.775 to 0.617 until negation words were decorrelated across states and questions.
- Multiplying gradients by 20 to get a higher scorer learning rate cancels out under Adam's per-parameter rescaling; the fix is two optimizers.
- Naive calibration reward pushed the correct answer from 0.418 to 0.001 — a perfectly "calibrated", useless policy.
- KL anchor weight set to 0; the test any added loss term must pass is zero gradient at the point where model probabilities equal the truth.
- Brier's gradient at 0.999 confidence is about 250x smaller than the log score's, so log scores are used in the RL reward; gradients are clipped because overconfident cases produce spikes.
- Murphy decomposition separates reliability (calibration) from resolution (separating easy from hard); a constant 70% predictor scores perfect reliability and zero resolution.
- Metric bug: scoring ambiguous items as 0/1 gave the honest model a reliability error of 0.1019 and the overconfident model 0.0001, rewarding exactly the behaviour being removed.
- Stage 3 guard: a fresh content-free structure probe must not move more than 0.01, and the script crashes if structure-only data leaks into the RL set.
- Final data mix was ~40% certain items, with ambiguous soft-label items up-weighted; checkpoints every 150 steps after losing a run's only checkpoint.

## Related

- [[how-to-fine-tune-llms-2026-grpo-ruler-art-akshay]]
- [[peft-beyond-lora]]
- [[policy-gradients-timeline-reinforce-to-grpo]]
- [[rl-agents-system-prompt-reward-function]]
- [[verifiability-constraint-rlvr-unverifiable-tanayj]]
