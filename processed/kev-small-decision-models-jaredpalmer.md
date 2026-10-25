---
title: "Kev: Small Decision Models You Can Train and Run Yourself"
type: bookmark
description: "Jared Palmer's Kev 1.0 — a family of 0.8B–27B Qwen-based decision models that answer batched yes/no, choice and score questions with calibrated probabilities, come within a point of hosted Jev on new sources, and fine-tune on your own labels for about $1."
tags: [small-models, decision-models, fine-tuning, local-llms, inference, calibration, apple-silicon]
source: https://x.com/jaredpalmer/status/2105803387220726185
date: 2026-10-01
author: Jared Palmer
summary: "Jared Palmer's Kev 1.0 — a family of 0.8B–27B Qwen-based decision models that answer batched yes/no, choice and score questions with calibrated probabilities, come within a point of hosted Jev on new sources, and fine-tune on your own labels for about $1."
raw: "[[raw/jaredpalmer_2105803387220726185]]"
---

# Kev: Small Decision Models You Can Train and Run Yourself

**Source:** Jared Palmer (@jaredpalmer), 2026-10-01. A one-line pointer post to the open-source `jaredpalmer/kev` repo — decision models built on Qwen3.5/3.8 that mimic TypeSafe's hosted Jev API.

Kev narrows the problem a language model is asked to solve. Instead of free-form generation, one request carries a `state` (the text being judged) and a set of typed questions about it: `noul` for a probability of yes, `choice` over 1–255 named options, `score` over ordered levels. Questions share the text but cannot see each other, and every checkpoint ships with a fitted temperature, so the probabilities are calibrated rather than raw softmax output. That is the whole point of the "decision model" framing: the output is a number a routing rule can threshold, not prose a downstream parser has to interpret. The API is deliberately TypeSafe-compatible, so an existing Jev client is pointed at a local server by changing a base URL.

The family spans 0.8B to 27B, released together as Kev 1.0 with fixed Hub revisions. The 0.8B/4B/9B are a small adapter on a frozen Qwen3.5 base; the 27B starts from Qwen3.8-27B's post-trained weights and fine-tunes all of them, so it ships as 51 GB of full weights. The accuracy story is that the decision head transfers well and the base model carries the knowledge: on the community Decision Index's held-out datasets Kev-27B scores 52.3 against hosted Jev's 54.0, and on new-source accuracy it is 0.851/0.889 (dev/test) versus Jev's 0.857 — within a point, on a comparison the author is careful to call uncontrolled, since Jev's training data is unknown. Knowledge questions track the base: Kev-27B matches Jev on MMLU (0.90) but trails badly on MMLU-Pro (0.675 vs 0.840).

The practical claim is that a short fine-tune beats prompt engineering when your questions differ from the released ones. `--init_from` reloads the released adapter and pointer head, so the model keeps what it knows: on an example support workload, 1,050 generated records and 15 minutes on an H100 took Kev-4B from 67.7% to 73.6% accuracy and from automating 34% to 48% of decisions at a 5% error budget; one epoch on 5,219 labelled consumer-finance complaints moved it from 0.804 to 0.904 on unseen complaints. The control case is the argument — starting from the base model instead dropped a user's eval score to 0.33 against 0.84 for the released model, and 400 records produced a gain inside the noise, so dataset size is the gating variable.

Operationally the repo is built for a single operator: local serving on CUDA, ROCm or MLX, a Modal deploy that scales to zero, and a coding-agent skill that runs interview → data → fine-tune → temperature fit → score → deploy → teardown. Notable honesty in a project README: it records eval suites it removed as unsound gates (WANLI pairs where the two annotators disagreed, a gold set derived from two frontier models whose split-half correlation across 20 checkpoints was −0.01).

## Why it matters

Most agent and product pipelines do not need generation at the decision step — they need a probability they can threshold, and they are paying frontier-model prices and latency for it. Kev is a concrete, runnable demonstration that a 4B model with a fitted temperature lands within a few points of a hosted commercial decision API, at 18 ms of model time per six-question request on an H100 and ~101 req/s in-process. The fine-tune numbers also give a realistic expectation for domain adaptation: single-digit accuracy points and a meaningful jump in automatable volume, from data you can generate in an afternoon.

## Key points

- One request answers multiple typed questions about one `state`: `noul` (P(yes)), `choice` (1–255 options with probabilities and confidence), `score` (mean level plus distribution); questions are isolated from each other.
- Calibrated by default — each checkpoint ships a fitted temperature; confidence formulas are TypeSafe's, not measured accuracy rates.
- Held-out Decision Index: Kev-0.8B 23.3, 4B 38.0, 9B 41.0, 27B 52.3, hosted Jev 54.0.
- New-source accuracy (dev/test): 0.648/0.697, 0.817/0.838, 0.820/0.852, 0.851/0.889 for 0.8B/4B/9B/27B; Jev 0.857. Brier at 27B 0.225/0.156 vs Jev 0.211.
- At a 5% error budget, 4B/9B/27B automate 0.52–0.69 of new-source decisions, 0.8B 0.14, Jev 0.70.
- Validated context: 8,192 tokens for 0.8B/4B/9B, 65,536 for 27B (accuracy on real contracts within 3 points of 8k).
- Fine-tune (`--init_from`) on 1,050 records: 67.7% → 73.6% accuracy, 34% → 48% automated at 5% error; 5,219 real complaints: 0.804 → 0.904 on unseen data; ~$1 per Kev-4B run on an H100.
- Starting from base instead of the released checkpoint scored 0.33 on Kev's eval set vs 0.84; with 400 records the gain was inside the noise.
- Speed: six questions, 18.1 ms model time on H100, 41.5 ms on L40S, 721 ms on an M5 (136 ms cached).

## Related

- [[mlx-engine-v185-kv-cache-agentic]]
- [[google-gemma-4-12b-local-fine-tuning]]
- [[0xsojalsec-llms-local]]
- [[who-will-set-price-intelligence]]
