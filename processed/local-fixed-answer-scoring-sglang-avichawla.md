---
title: "Build your own Jev: fixed-answer scoring with SGLang"
type: bookmark
description: "A working local reproduction of Jev-style decision inference: score the next-token logits for single-token labels via SGLang /v1/score, softmax over only the allowed answers, and skip autoregressive decoding."
tags: [inference, serving, structured-outputs, local-llms, cost-optimization, throughput, qwen]
source: https://x.com/_avichawla/status/2101563610644496464
date: 2026-09-20
author: "Avi Chawla"
summary: "A working local reproduction of Jev-style decision inference: score the next-token logits for single-token labels via SGLang /v1/score, softmax over only the allowed answers, and skip autoregressive decoding."
raw: "[[raw/_avichawla_2101563610644496464]]"
---
# Build your own Jev: fixed-answer scoring with SGLang

**Source:** Avi Chawla (@_avichawla), 2026-09-20. A long tutorial reproducing the inference path of Jev — a closed-source, fast "decision" model — on open Qwen and DeepSeek checkpoints using SGLang's `/v1/score` endpoint, with a latency benchmark against ordinary generation.

The argument is narrow and useful: many LLM calls do not need new text, because the application already knows the valid answers. A support ticket must go to billing, technical support, or account access; the model only has to pick one, and say how sure it is. Generation spends tokens writing a sentence or a JSON object the caller then parses. Scoring instead reads the model's next-token logits at the positions of three single-token labels (A, B, C), ignores the rest of the vocabulary, and applies softmax across just those three. The tutorial's worked example: logits 8.2 / 5.5 / 4.8 become roughly 0.91 / 0.06 / 0.03, and the application gets a distribution rather than a string.

The implementation is five steps and runs on one model server: launch `Qwen/Qwen2.5-0.5B-Instruct` with `sglang[all]==0.5.10.post1`, build a prompt that ends at "Label:", resolve each label's token ID through `/tokenize` and reject any label that is not exactly one token (for this checkpoint A/B/C map to IDs 32/33/34), then POST to `/v1/score` with `label_token_ids` and `apply_softmax: true`. The real run returned 0.678 / 0.311 / 0.011 for billing / technical support / account access, from logits 25.28 / 24.50 / 21.19 — enough to route under a 0.70 threshold, but not by much.

Two design points carry more weight than the code. First, structured output is not the same thing: a schema-constrained decoder still generates the brace, the field name and the value token by token, so it only constrains syntax, while scoring replaces decoding entirely when the candidate set is closed. Second, because scoring normalizes only over declared choices, a non-exhaustive list will confidently force an incident ticket into billing; the fix is an explicit OTHER or ESCALATE option in the label set. Chawla is explicit about the limits: this reproduces the inference path, not Jev's weights, RLCD training, or evaluation stack, and a 0.91 score is 91 percent of the probability mass over three choices, not 91 percent accuracy — calibration needs labeled examples.

## Why it matters

If a decision's answer space is finite, comparing one forward pass against an 8-32 token generation is a large, free latency and cost win, and the label-probability margin gives you a routing threshold that lives in application code where it can be tested. This is the cheapest available pattern for classifiers, routers, and gates inside agent harnesses — the same family of decisions that memory systems, guardrails, and tool selectors make hundreds of times per run — and it now has a copy-pasteable local implementation on hardware that fits on a laptop GPU.

## Key points

- `/v1/score` with `label_token_ids` + `apply_softmax: true` returns a distribution over declared answers in one forward pass, with no generated tokens.
- Labels must be validated as single tokens via `/tokenize` (Qwen2.5-0.5B maps A/B/C to 32/33/34); multi-token phrases would require sequence scoring and make length part of the comparison.
- Measured on Qwen2.5-0.5B-Instruct: 0.678 billing, 0.311 technical support, 0.011 account access, from logits 25.28 / 24.50 / 21.19 — a 0.70 policy threshold would have escalated this ticket.
- Restricted softmax renormalizes over the allowed set only, so add OTHER/ESCALATE whenever the choices may not be exhaustive.
- Benchmark harness: 100 fixed local cases across support routing, candidate screening and expense review; Jev-style and generation lanes released together from a two-thread `threading.Barrier` against one SGLang server, so both share continuous batching, GPU and scheduler.
- Models exercised: Qwen3-4B-Instruct-2507, Qwen2.5-0.5B and 1.5B, SmolLM2-1.7B, TinyLlama-1.1B, DeepSeek-R1-Distill-Qwen-1.5B; the generation lane is capped at 32 tokens and parses the first 100 characters for a choice name.
- Scope limit stated by the author: inference mechanism only — no Jev weights, no RLCD, no evaluation stack; probabilities need labeled data before they mean calibration.

## Related

- [[jev-agent-memory-context-engineering-dhravya]]
- [[rlm-structured-outputs]]
- [[inference-engines-2026]]
- [[efficiently-scaling-transformer-inference-checklist-wafer]]
- [[0xsojalsec-llms-local]]
