---
title: "Text Classification from Bag-of-Words to Jev"
type: bookmark
description: "Raschka's history of text classification, then hands-on Jev results: 96.47% on 25k IMDb reviews for $0.65, a DIY single-head Jev clone, and RLCD/calibration economics."
tags: [models, training, fine-tuning, cost-optimization, inference, harness-engineering]
source: https://x.com/rasbt/status/2104923912920281279
date: 2026-09-29
author: Sebastian Raschka
summary: "Raschka's history of text classification, then hands-on Jev results: 96.47% on 25k IMDb reviews for $0.65, a DIY single-head Jev clone, and RLCD/calibration economics."
raw: "[[raw/rasbt_2104923912920281279]]"
---

# Text Classification from Bag-of-Words to Jev

**Source:** Sebastian Raschka (Ahead of AI), 2026-09-29. The tweet is a one-line pointer to a long illustrated article tracing text classification from naive Bayes to TypeSafe AI's Jev, with his own benchmark runs.

Raschka frames Jev as the endpoint of a 60-year lineage rather than a new capability. The lineage runs from bag-of-words vectors feeding naive Bayes/logistic regression/XGBoost, through word embeddings plus RNNs and text CNNs, to pretrained transformers fine-tuned with a classification head. His reference point is the IMDb sentiment benchmark: 89.9% for bag-of-words + logistic regression, 85.66% for an LSTM trained from scratch, 90.07% for a text CNN, 95.4% for ULMFiT, and roughly 95% for a lightly tuned ModernBERT. The lesson he draws is that the classifier itself was never the interesting part — representation and pretraining were.

Jev (TypeSafe AI, proprietary) keeps the classifier humble and moves the value into generality and interface: three API shapes — Choice for multi-class with per-class probabilities and a confidence field, Noul for a single yes-probability usable as binary or multi-label, and Score for ordinal rubric levels. On 25,000 held-out IMDb reviews, Choice hit 96.47% accuracy (24,117 correct) in 22m24s for $0.6492, Noul 96.20% for $0.6345 — comparable to a fine-tuned ModernBERT that took 23 minutes to train and 7 minutes to evaluate, but needing no training data at all. He flags that IMDb may have been in training data and that repeat runs drift slightly from GPU kernel non-determinism.

The mechanism is demystified as a single-output-node head: for each candidate label, feed text + instructions + that label's description into a BERT- or GPT-style model, score each with a shared linear head, and softmax across candidates. Because the head is shared, the number of classes is a runtime parameter, not an architecture decision. Architecture, data, and training are unpublished; he guesses a small ModernBERT-like backbone, 100% synthetic curated data, and RLCD ("Reinforcement Learning for Calibrated Decisions") — closest published analogue being RLCR's `R = c − (q − c)²` reward, which cut expected calibration error from 0.37 to 0.03 on HotpotQA.

## Why it matters

The practical claim is that the default "cheap LLM for one-offs, fine-tune for repeats" rule of thumb collapses: a classifier-class model is now good enough and cheap enough to sit inside an agent loop as a routine primitive — pre-screening for prompt injection, choosing reasoning effort, routing to a skill, judging outputs, selecting files. For anyone building harnesses on top of expensive frontier models, $0.65 per 25k decisions implies you can afford per-turn classification on every request instead of sampling.

## Key points

- Jev Choice: 96.47% on 25k IMDb test reviews, 22m24s, $0.6492 total; Noul: 96.20%, $0.6345. ModernBERT fine-tune ≈ same accuracy, 23 min train + 7 min eval.
- Reference ladder on IMDb: 89.9% bag-of-words + logreg, 85.66% LSTM from scratch, 90.07% text CNN, 95.4% ULMFiT, ~95% ModernBERT.
- Jev-like API is one shared linear scoring head over per-candidate representations, softmaxed — so class count and label descriptions change without retraining architecture.
- Confidence is a separate field from the winning class probability; Noul returned 0.98 where Choice returned 1.0 on identical text.
- Calibration: RLCR's Brier-style penalty took ECE 0.37 → 0.03 on HotpotQA (accuracy 62.1% vs 63.0%) and 0.46 → 0.21 averaged over six datasets (accuracy 53.9% → 56.2%); adding Brier to cross-entropy for ModernBERT helped only marginally.
- Harness use cases he lists: prompt-injection pre-screening, reasoning-effort selection, skill selection from a library, eval judging/self-refinement, relevant-file retrieval.
- Clones tested: Contrastive Language Models 82.90% IMDb and fails a Tetris test; Laya 92.33% and also fails; an arXiv survey counted 2,170 Jev-related projects. OpenAI announced a Jev-like Decision API at DevDay 2026.

## Related

- [[controlling-reasoning-effort-in-llms]]
- [[gpt6-astra-looped-transformers-rasbt]]
- [[economy-of-tokens-vipulved-modular-ai]]
- [[harness-engineering-2026-discipline]]
