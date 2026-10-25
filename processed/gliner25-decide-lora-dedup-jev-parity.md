---
title: "GLiNER2.5-Decide + LoRA: A Local Decision Model That Matches Jev"
type: bookmark
description: "Fine-tuning Fastino's 435M GLiNER2.5-Decide encoder with 3 epochs of LoRA takes QQP duplicate detection from 69.7% to 80.3% accuracy — past Jev's 79.3% — at ~7.6x lower serial latency, on-device."
tags: [small-models, decision-models, fine-tuning, lora, inference, calibration, local-llms]
source: https://x.com/imohitmayank/status/2104236841419649301
date: 2026-09-27
author: Mohit
summary: "Fine-tuning Fastino's 435M GLiNER2.5-Decide encoder with 3 epochs of LoRA takes QQP duplicate detection from 69.7% to 80.3% accuracy — past Jev's 79.3% — at ~7.6x lower serial latency, on-device."
raw: "[[raw/imohitmayank_2104236841419649301]]"
---

# GLiNER2.5-Decide + LoRA: A Local Decision Model That Matches Jev

**Source:** Mohit (@imohitmayank), 2026-09-27. A hands-on X article that benchmarks TypeSafe's hosted Jev against the open GLiNER2.5-Decide checkpoint, then closes the accuracy gap with LoRA fine-tuning.

Most classification-shaped questions sent to a chat model — are these two support tickets duplicates, is this urgent — end up paying for token-by-token generation and then re-parsing free text into a schema. Jev's pitch is to replace that with a typed answer plus a probability from a "System One" model. Mohit's complaint is narrower and practical: Jev is an API with closed weights, so every call carries network latency and no data can stay in-house. His experiment asks whether an open encoder, fine-tuned on your own labels, can hit the same accuracy on the same machine that serves the request.

The base model, Fastino's GLiNER2.5-Decide, is a DeBERTa-v3-large encoder of roughly 435M parameters (about 340M in the transformer stack, 95M in the embedding table) with one head per task — classification, NER, structured records, relations. Classification works by flattening the task into the prompt itself: a schema string like `( [P] label ( [L] duplicate [L] not_duplicate ) ) [SEP_TEXT] question 1 … question 2 …` is tokenized, and after the encoder the library gathers only the `[L]` marker rows into an `[n_labels, 1024]` tensor, scores each through a shared 1024→2048→1 MLP, and softmaxes for exclusive tasks. There is no generation and no decoder.

On a balanced 1,500-pair slice of GLUE QQP, zero-shot Decide reaches 69.7% accuracy against Jev's 79.3% — roughly ten points short, and re-running with a Jev-aligned schema (same instruction wording, label descriptions) did not move it, so the author rules out prompt engineering as the cause. Latency was the opposite story: ~68ms serial versus 520ms for the API. Three epochs of LoRA on a disjoint 1,500-row sample (r=8, alpha=16, encoder lr 1e-5, head lr 5e-4, batch 4) produced 80.3% accuracy and 0.811 F1 while still running locally.

The honest caveat is scope: one task, one dataset, 1,500 examples, and a training/eval split carved out of the same validation set — a proof of concept that fine-tuning closes the gap, not a production model or a leaderboard entry. The transferable lesson is the recipe: a 435M encoder plus a few thousand labeled pairs and a cheap adapter is often a better answer than prompting a hosted "small" model you cannot inspect.

## Why it matters

It quantifies the real trade-off in decision-model deployment: hosted System One APIs win on out-of-the-box accuracy, but a local encoder with a fine-tuned adapter can beat them by a point or two once you have labels, at a fraction of the per-call latency and with no data leaving the machine. For teams already generating labels in production — duplicate tickets, moderation flags, match/no-match on retrieved pairs — the marginal cost of closing the accuracy gap is a few hundred training rows and a LoRA run, not a new vendor contract.

## Key points

- Zero-shot GLiNER2.5-Decide on 1,500 balanced GLUE QQP pairs: 69.7% accuracy, 0.724 F1 on duplicates, 0.695 macro F1; Jev (`jev-latest`): 79.3% accuracy, 0.759 F1, 0.788 macro F1.
- Latency was already inverted before any training: ~68ms serial for Decide versus 520.1ms for the Jev API (7.6x), 18.0ms amortized at `batch_size=8` (~29x), and 55.6 ex/s versus 22.6 ex/s throughput with Jev at concurrency 12.
- After 3 epochs of LoRA (`r=8`, alpha 16, dropout 0.05, encoder lr 1e-5, task heads 5e-4, batch 4): 80.3% accuracy (+10.5 points) and 0.811 F1, still ~7-8x faster than the API in serial inference.
- Error mix improved on both sides of the duplicate class: false duplicates fell 298 → 182 and correct predictions rose 1,046 → 1,204 on the same eval slice.
- Architecture detail worth stealing: task specification lives in the input string as `[P]`/`[L]` markers, and only the label-row embeddings go through a shared MLP, so the same encoder serves classification, NER and relation heads.
- The 435M-parameter model is a DeBERTa-v3-large encoder — no autoregressive decoding, so no token-by-token latency and no schema drift.

## Related

- [[jev-system-one-decisions-akshay]]
- [[kev-small-decision-models-jaredpalmer]]
- [[gero-4b-calibrated-decision-model-rl]]
- [[text-classification-bag-of-words-to-jev-rasbt]]
- [[jev-as-judge-probability-uncertainty-signal]]
