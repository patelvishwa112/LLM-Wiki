---
title: Training Search Agents with GRPO
type: bookmark
description: "Jasper Lu's open tutorial trains gpt-oss-20b with Dr. GRPO on an F4 reward over SEC filings, lifting eval F1 from 0.19 to 0.39, and finds a tool-format penalty unexpectedly raises recall."
tags: [rl, grpo, post-training, agent-harness, training, rag]
source: https://x.com/lu__jasper/status/2100601963813507268
date: 2026-09-17
author: Jasper Lu
summary: "Jasper Lu's open tutorial trains gpt-oss-20b with Dr. GRPO on an F4 reward over SEC filings, lifting eval F1 from 0.19 to 0.39, and finds a tool-format penalty unexpectedly raises recall."
raw: "[[raw/lu__jasper_2100601963813507268]]"
---

# Training Search Agents with GRPO

**Source:** Jasper Lu, 2026-09-17. An educational research write-up on training a retrieval agent with GRPO, published with browsable rollouts and open-source code at jasperlu.com/blog/training-search-agents-grpo.

The post trains a search subagent on the RL split of the Harness-1 dataset — 3,453 queries over 37,113 SEC filings chunked into 2,115,106 pieces — using gpt-oss-20b through the Tinker API and a deliberately thin lexical harness: `bm25_search`, `grep_corpus`, `read_document`, `curate`, `drop_curated`, `finish`. Two design choices carry the pedagogy. The agent accumulates a curated result set as it goes rather than submitting once at the end, so an episode that runs out of turns still returns something gradable; and the system prompt describes the tools without pushing recall or precision, leaving search behaviour to be discovered by training rather than dictated by prompt engineering. That framing is the post's sharpest claim: in this domain a well-designed reward shapes search behaviour more effectively than system-prompt changes or harness engineering.

The reward is where the reasoning shows. Pure recall is gamed by curating the whole corpus and pure precision by curating one chunk, so the objective is F-beta with beta = 4 — recall weighted sixteen times more than precision, on the argument that a missed document costs an end user more than a useless one — plus a flat -0.2 for an empty curated set so "never curated" is distinguishable from "curated only wrong documents". Training uses Dr. GRPO, which drops the division by the group standard deviation to avoid letting queries the policy already agrees on dominate the update, run synchronously with zero train/inference mismatch so no ratio clipping is needed. Before training, Lu checks RL-ability with a best-of-N gap: a task where best-of-N clearly beats best-of-1 has behaviour for RL to sharpen, and GRPO in particular produces no gradient when a group's rewards are identical.

Reported progress is 0.19 to a peak of 0.39 eval F1 on a 20B model that initially could not drive the harness properly. The most interesting result is incidental: adding a penalty for off-form tool-call headers drove malformed calls below 1% within a few steps, but also lengthened episodes (roughly 18 to 30 turns) and improved retrieval — held-out F1 0.36 vs 0.33 and recall 0.43 vs 0.32 against the same run without the penalty. Lu declines to explain this and offers two untested hypotheses, landing on the general lesson that a narrow reward change can reshape the whole policy.

## Why it matters

This is one of the few public RL-for-agents write-ups with the ablations, learning-rate sweeps and every rollout left visible, which makes it directly reusable rather than merely readable. Two practical takeaways for anyone post-training an agent: spend the first part of the budget measuring whether the task is RL-able at all (best-of-N versus best-of-1, and reward variance within a group) before paying for a training run, and treat the reward function as the highest-leverage surface — the format penalty, ostensibly a formatting fix, bought four points of held-out F1 and eleven of recall. It also suggests a third of a training budget can disappear into teaching harness mechanics, which is exactly the kind of cost that a harness-engineering investment is meant to remove.

## Key points

- Dataset: 3,453 queries over 37,113 SEC filings, 2,115,106 chunks; ablations at 256 train / 32 eval over 124,395 chunks, scaled runs at 1,024 train / 64 eval over 237,533 chunks.
- Model and stack: gpt-oss-20b, Dr. GRPO, Tinker API, a simplified Harness-1 harness with lexical tools only.
- Reward: F4 (beta = 4, recall weighted 16x), so recall 1.0 / precision 0.25 scores 0.85 instead of 0.40 under F1; empty curated set gets -0.2.
- Dr. GRPO drops the standard-deviation division, which vanilla GRPO uses and which over-weights queries the policy is already consistent on.
- Result: eval F1 0.19 to a peak of 0.39; held-out F1 0.36 and recall 0.43 with the format penalty vs 0.33 and 0.32 without.
- Off-form tool calls fall below 1% within a few steps, and trajectories lengthen from about 18 to 30 turns as a side effect.
- Pre-flight check: a best-of-N gap over best-of-1 is the cheapest proxy for whether RL has headroom on a task.
- Open directions: curriculum sampling by measured pass rate, SFT warmup for harness mechanics, richer reward shapes (turn penalties, tool diversity).

## Related

- [[continuous-batching-grpo-trl]]
- [[policy-gradients-timeline-reinforce-to-grpo]]
- [[raschka-rlvr-grpo-clipped-ratios-kl-format-rewards]]
- [[rl-agents-system-prompt-reward-function]]
- [[three-layers-harness-loop-graph-lunarresearcher]]
