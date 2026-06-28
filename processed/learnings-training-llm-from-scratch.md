---
tags:
- llm-training
- from-scratch
- rlhf
- infra
- architecture
- data
- optimizer
source: https://x.com/harshbhatt7585/status/2063593933314113587
date: 2026-06-07
type: bookmark
author: harshbhatt7585
summary: 'Hands-on lessons from training a ~160M LLM (MTP + HRM + causal LM) that
  beat nanoGPT on CORE: architecture experimentation beats full replication, small
  models excel at narrow tasks, RL only helps if the base model already has decent
  knowledge, infra (batching, GPU utilization) is critical, and documentation + leaderboards
  beat emotional tinkering.'
raw: '[[raw/harshbhatt7585_2063593933314113587]]'
description: 'Hands-on lessons from training a ~160M LLM (MTP + HRM + causal LM) that
  beat nanoGPT on CORE: architecture experimentation beats full replication, small
  models excel at narrow tasks, RL only helps if the base model already has decent
  knowledge, infra (batching, GPU utilization) is critical, and documentation + leaderboards
  beat emotional tinkering.'
---

# My Learnings From Training LLM from Scratch

Harsh Bhatt shares real-world insights from training a ~160M model that outperformed nanoGPT.

## Key Learnings
1. **Simplify before scaling**: Extract the core idea from a paper (e.g., HRM's "cycle loop") and test it in isolation rather than replicating the full pipeline.
2. **Small models are narrow specialists**: ~160M models can master narrow tasks (e.g., GSM8K) but lack capacity for multi-task performance.
3. **RL requires a competent base**: RL only improves a model that already has above-average knowledge/reasoning in the domain. It can't create expertise from near-zero.
4. **Infra matters as much as algorithms**: Poor batching, low GPU utilization (e.g., 38% in RL rollouts), and gradient sync issues waste massive compute. Batching generations improved throughput dramatically.
5. **Document everything**: Emotional experimentation wastes time. Create leaderboards, rank experiments, and make decisions based on benchmarks.

Code: https://github.com/harshbhatt7585/deep-learning-papers-implementation/blob/main/tinyGroot

Relevant to the user's values-slm and training experiments.