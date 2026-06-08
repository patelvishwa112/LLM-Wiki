---
title: "My Learnings From Training an LLM From Scratch — 5 Lessons From ~300 Experiments"
tags: ["training", "llm", "from-scratch", "architecture", "rl", "scaling-laws", "infrastructure", "gpu", "experiments", "documentation", "mtp", "hrm", "tiny-models", "sft", "research-methodology"]
source: https://x.com/harshbhatt7585/status/2063593933314113587
date: 2026-06-07
published: 2026-06-07
authors: ["Harsh Bhatt (@harshbhatt7585)"]
type: bookmark
raw: "[[raw/harshbhatt7585_2063593933314113587]]"
related: ["[[ai-engineering-roadmap-2026-from-scratch]]", "[[rlhf-from-first-principles]]", "[[how-gpu-executes-code-first-principles]]"]
summary: "Harsh Bhatt trained a ~160M model combining MTP, HRM, and causal LM across ~300 experiments. Five hard-won lessons: simplify ideas to core mechanics, small models are narrow-task specialists, RL only works above a knowledge threshold, infrastructure is a first-class factor, and document everything with leaderboards."
---

# My Learnings From Training an LLM From Scratch — 5 Lessons From ~300 Experiments

Harsh Bhatt trained a ~160M parameter model combining MTP (multi-token-prediction), HRM (Hierarchical Reasoning Model), and causal LM (GPT-style). It outperformed nanoGPT on CORE accuracy. He ran ~300 experiments across many architectures (text-diffusion, HRM, MoE). Many failed. Five lessons:

## The Four Building Blocks

Every training run: Architecture, Data, Optimizer, Learning algorithm (gradient descent).

## Lesson 1: Simplify to Core Mechanics, Don't Replicate Full Pipelines

When taking inspiration from a paper (e.g., HRM), extract the core idea — the "cycle loop" that gives latent reasoning — and test that minimal version. Don't replicate the full pipeline. Understanding why something works and extracting just the mechanism gave extra CORE score without major architecture changes or parameter increases.

## Lesson 2: Small Models Are Narrow-Task Specialists

~160M models can become good at narrow tasks (e.g., GSM8K math after SFT) but fail at multi-task. The latent space isn't big enough to compress diverse knowledge. Scaling laws: more parameters → bigger latent space → more knowledge capacity. Architecture also matters — better architectures compress knowledge more efficiently.

## Lesson 3: RL Is a Cherry on Top, Not a Foundation

RL only works when the model already has above-average knowledge of the domain. SFT on math wasn't enough — the model collected some rewards but couldn't solve most problems. Pre-training or heavy SFT must first give the model internal reasoning capacity. Then RL makes it expert.

Intuition: RL rewards are sparse (0 for wrong, 1 for correct). Without existing reasoning ability, the model resorts to trial-and-error across the entire token space — unreliable and wasteful. You need a foundation of knowledge first.

## Lesson 4: Infrastructure Is a First-Class Factor

GPU utilization matters. During RL experiments, sequential rollout collection used only 38% of the GPU. Fix: batch all 256 generations to predict next tokens simultaneously → fast synthetic data generation. Non-optimal infra code cost significant GPU minutes. Systems engineering knowledge is essential for LLM research — cold starts, gradient sync in distributed training, waiting time all add up.

## Lesson 5: Document Everything, Be Logical Not Emotional

Without documentation and leaderboards, experiments become emotional: "let's try increasing this, maybe it gets better." Created a leaderboard, ranked experiments, took benchmark-driven decisions. Curiosity without process wastes time.

**Code:** https://github.com/harshbhatt7585/deep-learning-papers-implementation/blob/main/tinyGroot
