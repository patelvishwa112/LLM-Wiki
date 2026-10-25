---
title: "Unsloth Decision Models: Qwen3.5 0.8B to 74.3% on 4GB VRAM"
type: bookmark
description: "Unsloth shows how to turn a 0.8B Qwen3.5 into a decision model — 20.7% to 74.3% aggregate accuracy on 3 decision benchmarks with LoRA r=64 for one epoch on 4GB VRAM."
tags: [training, fine-tuning, lora, slm, gpu, inference]
source: https://x.com/UnslothAI/status/2107868866361930236
date: 2026-10-07
author: Unsloth AI
summary: "Unsloth shows how to turn a 0.8B Qwen3.5 into a decision model — 20.7% to 74.3% aggregate accuracy on 3 decision benchmarks with LoRA r=64 for one epoch on 4GB VRAM."
raw: "[[raw/UnslothAI_2107868866361930236]]"
---
# Unsloth Decision Models: Qwen3.5 0.8B to 74.3% on 4GB VRAM

**Source:** Unsloth AI, 2026-10-07. Product/recipe announcement for fine-tuning small LLMs into "decision models" (typed-decision output instead of free-form chat), with repo and notebooks.

Unsloth's claim is that a general chat model can be converted into a narrow decision model — the same class of model as TypeSafe's Jev — with a single short LoRA run rather than a from-scratch training project. The demonstration uses Qwen3.5 0.8B as the base, fine-tuned with what the post calls a "Clef" head (a task-specific output head added on top of the base LM) plus LoRA at rank 64 for one epoch. On three decision benchmarks the tuned model's aggregate accuracy rises from 20.7% to 74.3%, and downstream accuracy in the specific task reported moves from a 30–37% band to 78%.

The resource footprint is the notable part: the whole run is stated to fit in 4GB of VRAM, which puts decision-model customization on consumer laptops and free-tier notebooks rather than on rented A100s. Unsloth frames the recipe as model-agnostic, saying the same procedure applies to other bases such as Qwen3.8 and Gemma 4 — though only the 0.8B Qwen3.5 numbers are given, so the generalization is an assertion, not a measured result.

Two artifacts are linked: the open-source `unslothai/unsloth` repo and a docs page with a guide and runnable notebooks. The post is a pointer-with-numbers rather than a methodology writeup; there is no detail on the benchmark identities, the head architecture, data volume, or how much of the gain comes from the head versus the LoRA weights. The head-vs-adapter split is the obvious thing to test against the notebooks, since the 20.7% baseline implies the base model was being scored through an untrained head, which inflates the apparent lift relative to tuning a plain-LM decision prompt.

## Why it matters

Decision models are the cheapest useful form of "AI in the loop" — routing, triage, classify-and-score calls that need to be fast, calibrated, and batchable, not conversational. If a 0.8B model can be pushed from near-random to mid-70s accuracy in one LoRA epoch on 4GB, the economics of running a decision layer locally (or per-tenant) change materially, and the eval harness, not the GPU bill, becomes the binding constraint.

## Key points

- Qwen3.5 0.8B fine-tuned by Unsloth: aggregate accuracy across 3 decision benchmarks 20.7% → 74.3%.
- Downstream task accuracy reported as 30–37% before tuning, 78% after.
- Training config: LoRA r=64, one epoch, "Clef" head on top of the base model.
- Hardware: 4GB VRAM — laptop-class, no datacenter GPU.
- Author claims the recipe transfers to other bases (Qwen3.8, Gemma 4); only the 0.8B numbers are measured in the post.
- Artifacts: `github.com/unslothai/unsloth` and a docs page with guide + notebooks.

## Related

- [[jev-system-one-decisions-akshay]]
- [[gero-4b-calibrated-decision-model-rl]]
- [[multi-lora-training-osmosis]]
- [[google-gemma-4-12b-local-fine-tuning]]
- [[peft-beyond-lora]]
