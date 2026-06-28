---
tags:
- frontier-labs
- deepmind
- pre-training
- scaling-laws
- research-taste
- kernel-engineering
- distillation
- quantization
- inference-code-design
- career-advice
- llm-research
source: https://youtu.be/cDyi91onoJ8
date: 2026-06-15
type: lecture
author: Vlad Fineberg (Google DeepMind Pre-training Area Lead)
title: How to Get a Job at a Frontier Lab — Vlad Fineberg (DeepMind)
summary: 'Vlad Fineberg (DeepMind pre-training area lead) breaks down the skills frontier
  labs actually hire for: low-level kernel engineering for LLM runtime, research taste
  as a stochastic MDP skill, scaling laws intuition, distillation infrastructure,
  inference code design, and quantization. He explains why software engineers struggle
  with research uncertainty, the Prime Directive of literature review, pre-training
  war stories (Flash 2.0 pipeline prefill), MFU realities, and concrete exercises
  to demonstrate fit. Essential viewing for anyone targeting OpenAI, Anthropic, Google
  DeepMind, or similar.'
raw: '[[raw/youtube_cDyi91onoJ8_timestamped]]'
description: 'Vlad Fineberg (DeepMind pre-training area lead) breaks down the skills
  frontier labs actually hire for: low-level kernel engineering for LLM runtime, research
  taste as a stochastic MDP skill, scaling laws intuition, distillation infrastructure,
  inference code design, and quantization. He explains why software engineers struggle
  with research uncertainty, the Prime Directive of literature review, pre-training
  war stories (Flash 2.0 pipeline prefill), MFU realities, and concrete exercises
  to demonstrate fit. Essential viewing for anyone targeting OpenAI, Anthropic, Google
  DeepMind, or similar.'
---

## Overview & Why This Matters

This interview with Vlad Fineberg (Google DeepMind Pre-training Area Lead) is one of the most concrete, high-signal discussions available on what frontier labs actually need right now. Unlike generic "learn PyTorch" advice, Fineberg focuses on the specific, high-leverage skills that are in voracious demand: **kernel-level engineering for LLM runtime**, **research taste as a stochastic decision process**, and **infrastructure that enables new research methods at scale**.

The core message: the gap between a strong software engineer and a frontier-lab researcher is not just "more math." It is the ability to navigate uncertainty, build intuition for which research paths are likely to pay off, and do the unglamorous infrastructure work that makes new methods possible.

**What you will learn:**
- The exact skills (kernel dev, distillation infra, inference code design, quantization) that labs are hiring for aggressively.
- Why research is a stochastic MDP (not a deterministic DAG) and what "research taste" actually means in practice.
- How to demonstrate fit with concrete, verifiable exercises (scaling book + transformer implementation).
- Real war stories (Flash 2.0) that show how small serving innovations unlock new model capabilities.
- The honest day-to-day reality of pre-training at scale.

---

## Chapter 1: Skills in Highest Demand at Frontier Labs (0:37 – 2:44)

**Key insight:** The single sharpest skill in demand across all labs right now is **low-level engineering to accelerate LLM runtime** — kernel development, efficient KV caching, high-throughput low-latency implementations at massive scale.

Fineberg emphasizes that when you change model architecture or serving strategy, you must implement the change *efficiently*. The inner loop of research is creating software artifacts that function at large scales. This is classical backend/distributed systems engineering applied to the new constraints of trillion-token training and inference.

**What the reader can learn / do:**
- Specialize in writing high-performance kernels and inference code for transformers.
- Understand the full stack: from matmul optimization to KV cache management to multi-data-center storage for distillation statistics.
- This skill is "sharp" because it sits at the intersection of research ideas and production constraints.

---

## Chapter 2: Research vs Applied & the Fluid Spectrum (2:44 – 5:07)

**Key insight:** There is no clean line between "research" and "applied." Even teams integrating LLMs into Search must do hard research on factuality, grounding, and source quality. Everyone must be fluid across the spectrum.

DeepMind has classical pre-training/post-training research teams *and* teams focused on product integration. The pure research only matters to the extent it can be realized in actual training runs.

**What the reader can learn / do:**
- Do not silo yourself into "pure research" or "pure engineering." The highest-leverage people move fluidly between both.
- When working on product integration, treat it as research — the same rigor applies.

---

## Chapter 3: Software Engineer vs AI Researcher — The Stochastic MDP (5:07 – 13:34)

**Key insight:** Software engineering follows a deterministic DAG (you can plan the shortest path). Research is a **stochastic Markov Decision Process** — many nodes may or may not work, and you must build intuition ("research taste") for which paths are worth the time investment.

This is the core mindset shift that takes time and specialized training (often a PhD) to develop. The ability to estimate success probability *before* running the experiment is what separates researchers from engineers.

**What the reader can learn / do:**
- Read the foundational scaling papers (Kaplan, Chinchilla, PaLM) until you internalize the scaling-laws worldview.
- Practice estimating whether a research idea is likely to work before investing weeks.
- Build "research taste" by running many small experiments and reflecting on which ones paid off.

---

## Chapter 4: Literature Review & Prerequisites (13:34 – 20:00)

**Key insight:** Before you can push the frontier, you must know the sum total of humanity's bleeding edge in that area. The first skill many strong engineers lack is the ability to efficiently traverse the citation tree and identify high-value papers without reading everything.

You also need the mathematical and CS prerequisites to understand methodology deeply enough to improve upon it.

**What the reader can learn / do:**
- Build a systematic literature review habit focused on scaling laws and pre-training.
- Develop the skill of assessing whether a paper is worth a full read from its abstract + key figures.

---

## Chapter 5: Pre-training, Scaling Laws & the One-Shot Nature of the Problem (17:37 – 20:00)

**Key insight:** Every pre-training run is a one-shot experiment at a scale larger than anything you've done before. You cannot iterate like on ImageNet. You must have a *recipe* (training routine) + a *prediction rule* that accurately forecasts final test loss before you spend the flops.

This is why scaling laws work is foundational.

---

## Chapter 6: The Three Pillars of Pre-training Research (39:47 – 43:02)

Fineberg's team focuses on three verticals:
1. **Distillation** — transferring knowledge/statistics from teacher to student at massive scale (requires enormous infrastructure investment).
2. **Inference code design** — neural architectures optimized for the hardware they will run on (shapes, gating, attention patterns that maximize MFU).
3. **Quantization** — pushing beyond 4-bit while preserving quality, because 99% of AI hardware cost is power.

**Key insight on MFU (43:44 – 47:02):** Low single-digit to low-tens MFU is normal and not waste. Neural nets must do attention, activations, memory reads/writes — operations that run slower than pure matmuls. The goal of inference code design is to choose shapes that saturate *all* hardware units (flops, memory bandwidth, communication) while still delivering high model quality.

---

## Chapter 7: War Story — Flash 2.0 & Pipeline Prefill for MoE (50:31 – 58:59)

**Key insight:** The decision to use pipeline prefill (parallelizing layers across machines instead of experts) unlocked MoE at the Flash scale by solving the HBM and communication latency problem. This "small" serving innovation had dramatic quality implications and was the result of a transparent technical process on a small team.

The 40-day training run with almost no sleep shows the reality of shipping frontier models.

---

## Chapter 8: Career Advice & Concrete Exercises (59:01 – end)

**Key insight:** Chase real problems people face in the world, even if the work sounds menial. Be the kind of coworker people genuinely want to see succeed — this creates compounding collaboration and opens doors more reliably than Machiavellian tactics.

**Concrete signal:** Do the scaling book exercises (handwritten) + implement a real transformer, record yourself, and send it. Fineberg is explicitly inviting this as interview evidence and has already started reviewing submissions.

**Internal transfer advice:** Become the person in your current org who integrates LLMs effectively. This creates massive value and naturally makes you the partner the research teams want to work with.

---

## Actionable Takeaways for the Reader

1. **Develop the scarce skill:** Low-level kernel / inference code engineering for LLMs.
2. **Build research taste:** Treat research as a stochastic MDP. Practice estimating which ideas are worth the time.
3. **Do the public signal:** Complete the scaling book exercises + transformer implementation and share the video.
4. **Read the canon:** Kaplan → Chinchilla → PaLM scaling papers until the worldview is second nature.
5. **Be the collaborator people root for:** This is the highest-ROI professional habit.

This interview is essential for anyone targeting frontier labs in 2026–2027. The skills Fineberg describes are not "nice to have" — they are the current hiring bottlenecks.

**Related notes:** [[scaling-laws]], [[frontier-labs-hiring]], [[research-taste-mdp]], [[distillation-infrastructure]], [[inference-code-design]]
