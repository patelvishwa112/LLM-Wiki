---
tags:
  - rl
  - rlvr
  - post-training
  - reasoning
  - entropy
  - exploration
  - reward-design
  - papers
  - training
  - llm
source: https://x.com/iScienceLuvr/status/2092900877031895511
date: 2026-08-27
author: Tanishq Mathew Abraham (@iScienceLuvr); paper by Clay, Gollapudi, Harilal, Jang, Morrison, Oh, Jaques
type: bookmark
description: "Primer on RLVR: sparse RL cannot find what the model never samples, dense rewards raise that ceiling, spurious-reward effects are a prompt-set artifact — post-training reshuffles pretrained probability mass."
summary: "Controlled RLVR study showing RL post-training redistributes probability mass the base model already has — explanation depends on prior mass, reward granularity, prompt diversity and scale, measured through policy entropy."
raw: "[[raw/iscienceluvr_2092900877031895511]]"
status: current
as_of: 2026-08-27
---

# Demystifying RL Post-Training of Language Models

Tanishq Abraham's summary of arXiv:2608.24949 (Clay, Gollapudi, Harilal, Jang, Morrison, Oh, Jaques), a primer that decomposes RLVR step by step in a deliberately simplified environment instead of reporting another benchmark win.

## The framing that makes it useful

**Post-training is redistribution, not creation.** RL sharpens probability mass the pretrained model already assigns to the desired behavior. The measurement follows from that: track (a) the probability the model puts on the target behavior and (b) the entropy of its output distribution, across pretraining → SFT → RL. Entropy becomes the lens for "how certain is this model, and at which stage did that certainty appear."

This reframes the usual question from "does RL work?" to "does the base model already contain the behavior, and can the reward signal find it?"

## The three results

1. **Sparse RL cannot find what the model never samples.** Binary success/fail reward only teaches from trajectories the policy actually generates. Zero prior mass on the correct behavior means zero learning signal — classical exploration failure, restated for LLMs.
2. **Dense rewards break that ceiling.** Finer-grained reward (partial credit, process signals) expands the reachable region, because the model can climb from near-misses it would never have converted into successes under sparse reward.
3. **"Spurious rewards" are a story about the prompt set.** Whether a bogus/mismatched reward appears to help depends on the distribution of prompts used in post-training — i.e. the pathology lives in the data mixture, not in the reward function alone.

## Verdict

The most practically actionable line for anyone running post-training: **choose the base model by measuring prior mass on the target behavior before you touch RL**, then choose reward granularity to match how far that mass is from usable. If the behavior is absent, dense rewards and better prompts are cheaper than RL; if it is present but diffuse, RLVR with the right granularity is the sharpening tool. Complements the mechanics in [[rlhf-from-first-principles]] and [[continuous-batching-grpo-trl]], and explains why distillation often wins where RL stalls ([[why-on-policy-distillation-works]]).

Paper: https://arxiv.org/abs/2608.24949 · Code: https://github.com/sankarh-1/demystifying-rl-finetuning · Project: https://minjang10.github.io/demystifying-rl-finetuning-web/

## Related

- [[rlhf-from-first-principles]]
- [[why-on-policy-distillation-works]]
- [[continuous-batching-grpo-trl]]
- [[training-search-agents-grpo-jasper-lu]]
