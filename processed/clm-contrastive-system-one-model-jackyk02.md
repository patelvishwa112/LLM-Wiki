---
title: "CLM: A Contrastive System One Model"
type: bookmark
description: "Jacky Kwok's CLM-8B: a contrastive state→action decision model, 9× faster than Jev, SOTA on DeepSWE (81.6%) and Terminal-Bench 2.1 (87.6%)."
tags: [training, scaling-laws, inference, evals, coding-agents, cost-optimization, models]
source: https://x.com/jackyk02/status/2102905335925424285
date: 2026-09-23
author: Jacky Kwok
summary: "Jacky Kwok's CLM-8B: a contrastive state→action decision model, 9× faster than Jev, SOTA on DeepSWE (81.6%) and Terminal-Bench 2.1 (87.6%)."
raw: "[[raw/jackyk02_2102905335925424285]]"
---

# CLM: A Contrastive System One Model

**Source:** Jacky Kwok (@jackyk02), 2026-09-23. Launch post for Contrastive Language Model (CLM), an 8B "System One" model that picks actions instead of writing tokens.

CLM reframes the fast-decision model as a retrieval/classification problem rather than a generation problem: it is trained with a contrastive objective that binds environment *states* to *actions*, then emits a structured choice (plus a score) at inference. CLM-8B is pre-trained on internet-scale data and — per the authors — reaches up to **9× faster inference than Jev** while staying competitive on computer-use, gaming and tool-calling workloads. With light fine-tuning it claims new SOTA on agentic coding: **DeepSWE 81.6%** and **Terminal-Bench 2.1 87.6%**, benchmarks where the post argues Jev degrades badly as a verifier over long horizons.

The systems contribution is the serving split: states and actions are **disaggregated**, so state embeddings and action embeddings are cached and reused independently. That matters when the state changes continuously (a screen, a document, a live environment) while the candidate action set stays fixed — the expensive half of the pair is precomputed once and only the cheap half is recomputed per step. The authors also report **scaling laws for contrastive test loss**, falling as a power law in training compute, model size and dataset size, which is the claim that turns a single 8B checkpoint into a family with predictable returns.

Caveats: every number here is self-reported at announcement, the comparison target ("Jev") is a different architecture with different serving assumptions, and the linked artifacts (Notion blog, GitHub org, Hugging Face models) are the only path to verification. No independent reproduction exists in the post.

## Why it matters

It splits "agent intelligence" into two components with different physics: a slow reasoner and a fast, cacheable decision layer. If the stated latency and scaling results hold, per-step decision cost in agent loops drops by roughly an order of magnitude, which changes how long an agent can run and how many tool calls are affordable. It also reframes verifier/reranker roles — the post's claim that a decision model *fails* as a long-horizon verifier is a useful negative result for anyone bolting a cheap model onto a verification step.

## Key points

- CLM-8B: contrastive state→action objective, no autoregressive text generation for the decision itself.
- Claimed **up to 9× faster inference than Jev**, comparable on computer-use, gaming, tool-calling.
- Fine-tuned: **DeepSWE 81.6%**, **Terminal-Bench 2.1 87.6%** — presented as new SOTA.
- Jev "fails to serve as an effective verifier" on these long-horizon agentic coding tasks (authors' claim).
- Infra trick: disaggregate state and action embeddings so each side caches independently → latency win when state evolves but action set is fixed.
- Scaling laws: test contrastive loss decreases as a power law in compute, model size, and data.
- Released with blog, GitHub code, Discord, and HF models — no third-party eval reported.

## Related

- [[scaling-laws]]
- [[thoughts-about-scaling-law-jietang]]
- [[harbor-by-terminal-bench-multi-language-agent-evaluation-fr]]
- [[inference-optimizations-sub-second-llm-checklist]]
- [[sub-agents-inference-time-scaling]]
