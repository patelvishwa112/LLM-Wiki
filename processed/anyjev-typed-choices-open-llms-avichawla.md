---
title: "AnyJev: Turning Open LLMs into Typed Decision Models"
type: bookmark
description: "AnyJev, a Nokia open-source Python library, extracts typed choices, yes/no judgments, scores and probabilities from causal LLMs via three escalating levels L0/L1/L2."
tags: [structured-outputs, calibration, inference, open-weights, models, evals]
source: https://x.com/_avichawla/status/2103393403207901217
date: 2026-09-25
author: Avi Chawla
summary: "AnyJev, a Nokia open-source Python library, extracts typed choices, yes/no judgments, scores and probabilities from causal LLMs via three escalating levels L0/L1/L2."
raw: "[[raw/_avichawla_2103393403207901217]]"
---

# AnyJev: Turning Open LLMs into Typed Decision Models

**Source:** Avi Chawla, 2026-09-25. An X post introducing AnyJev, a Python library from Nokia Applied Research for extracting typed decisions from causal LLMs.

AnyJev converts an open causal LLM into a Jev-style decision interface: instead of generating free text, you ask for a typed choice, a yes/no judgment, a score, or a probability. Chawla describes three levels that trade labelled data and calibration for nothing at all in the L0 case. L0 needs no labels and mitigates position bias by rotating answer options, but the resulting probabilities are uncalibrated. L1 consumes 100–500 labelled examples per question to temperature-scale those probabilities, improving confidence estimates while leaving the answer ranking unchanged. L2 uses 100–300 labels to fit a closed-form linear head on an intermediate hidden state, leaving model weights untouched and permitting inference to stop before the forward pass completes — the cheapest option at run time.

The binding constraint is model access: AnyJev needs logits or hidden states, so it only works with open-weight models, and L2 heads are specific to a single model and a single question, so they do not generalise across checkpoints. In the replies, a commenter presses the fair objection that constrained decoding for typed choices is not new — outlines and guidance already do grammar and logit masking — and asks what the delta actually is; the answer implied by the level structure is calibration of the probability, not the extraction of the token. The library author adds that L0 also removes the model's label prior (the pull toward "yes", or toward one particular option), while another commenter proposes logging option-rotation flip rate as a label-free uncertainty signal and reserving L1/L2 heads for questions that actually flip.

## Why it matters

Most teams batching classification or routing through a frontier API pay full generation cost for what is structurally a single-token decision, and they get an uncalibrated confidence they cannot threshold. AnyJev is a concrete recipe for recovering a real probability from an open model at a fraction of that cost, and the L0→L2 ladder gives an explicit budget curve: zero labels for debiased argmax, a few hundred labels for faithful confidence, and a few hundred more for a near-free truncated forward pass. The caveat matters just as much — per-model, per-question heads mean this is a training-and-maintenance commitment, not a drop-in library call.

## Key points

- Three levels: L0 (no labels, option rotation, uncalibrated), L1 (100–500 labels per question, temperature scaling, ranking preserved), L2 (100–300 labels, closed-form head on an intermediate hidden state).
- L2 leaves model weights untouched and can return before the full forward pass completes, cutting inference cost.
- Requires access to logits or hidden states, so it targets open causal LLMs; L2 heads are model- and question-specific.
- Author clarification: L0 also removes the model's label prior (bias toward "yes" or a particular option), not just position bias.
- Community critique: typed-choice extraction itself overlaps with grammar/logit-masking libraries like outlines and guidance; calibration of the extracted probability is the differentiator.
- Suggested extension from the thread: use option-rotation flip rate as a label-free uncertainty signal, and only spend labels on questions that flip.
- Author also published a companion hands-on guide for building a local Jev-style decision path with next-token scoring and SGLang.

## Related

- [[jev-system-one-decisions-akshay]]
- [[jev-as-judge-probability-uncertainty-signal]]
- [[kev-small-decision-models-jaredpalmer]]
- [[gero-4b-calibrated-decision-model-rl]]
- [[text-classification-bag-of-words-to-jev-rasbt]]
