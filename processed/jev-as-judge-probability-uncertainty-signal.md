---
title: "Jev as a Judge: Probability as a Cheaper Uncertainty Signal"
type: bookmark
description: "Hutton (Arize Phoenix) runs 36,190 judgments: Jev matches LLM judges at 98.3% accuracy for 64 cents, and its probability flags its own errors at AUC 0.95 versus 0.62-0.84 for repeat-sampled LLMs."
tags: [evals, llm-judges, cost-optimization, benchmarks, inference, observability]
source: https://x.com/ehutt_/status/2104674562583748874
date: 2026-09-28
author: Elizabeth Hutton
summary: "Hutton (Arize Phoenix) runs 36,190 judgments: Jev matches LLM judges at 98.3% accuracy for 64 cents, and its probability flags its own errors at AUC 0.95 versus 0.62-0.84 for repeat-sampled LLMs."
raw: "[[raw/ehutt__2104674562583748874]]"
---

# Jev as a Judge: Probability as a Cheaper Uncertainty Signal

**Source:** Elizabeth Hutton, 2026-09-28. A long-form Arize post testing whether a probability-returning classifier (Jev) can replace LLM judges and surface eval errors without repeated sampling.

Hutton's framing: an LLM judge is already a classifier wearing an LLM costume — answers are coerced into a label set and scored with classifier metrics. The established way to extract signal from that judge is nondeterminism: run it ten-plus times at high temperature and read the wobble as a difficulty map. Jev returns a probability instead of text, so the question is whether one call carries the same information. She sweeps five LLMs (three small, two frontier) and two Jev configurations over ten Phoenix evaluators with human-labeled suites — correctness, PII, completeness, tool invocation, tool response handling, retrieval relevance, user friction, hallucination, refusal, conciseness — 517 examples, ten reps each, 36,190 judgments, for a total spend of $169.84 of which Jev cost 64 cents.

Accuracy is a genuine tie: Jev scores 98.3% both as a drop-in (whole prompt stuffed into `state`) and via its native three-field API, against 96.7–98.6% for small models and 98.0–99.4% for frontier ones; no pairwise difference survived multiple-comparison correction. Native's one visible gain is 7.1 points on completeness, the evaluator whose conversations average ~1,950 tokens — separating data from instructions helps when there is context to digest. Stability is where Jev separates: it changed its label on 0.97% of examples as a drop-in and 0.19% natively, versus 26% for GPT-5 nano on tool invocation and 12% for Haiku 4.5 on PII, while being 13 to 55 times faster (133 ms median) and 12–290x cheaper depending on the comparison class.

The real finding is self-knowledge. Median probability on correct answers was 1.00 versus 0.71 on wrong ones; all 3,561 runs at ≥99% confidence were correct, while below 70% confidence Jev was right only 73% of the time — an ROC AUC of 0.95 drop-in and 0.99 native for detecting its own mistakes. Agreement-across-ten-runs, the method available to LLM judges, only reached 0.62–0.84, because 27–75% of an LLM's errors never wavered at all. Jev's entropy also predicts where LLM judges are unstable: on the 306 near-certain examples they wavered 3% of the time, on the 24 near-coin-flips 71%, rank correlation 0.47, AUC 0.85, and a 0.5-bit cutoff routes 11% of examples to human review while catching about two thirds of the instability.

## Why it matters

This converts eval quality control from a sampling budget into a single scalar: instead of paying for ten judge calls to learn which examples are contested, you read a probability and triage. The 0.95 AUC on self-detection is the number that matters most — it means a cheap judge can tell you where it is unreliable, which is exactly what LLM judges cannot do when their errors are consistent. The catch is threshold discipline: on two-label tasks the default 0.5 cutoff was already near-optimal here, but Arize's earlier RAGTruth work showed tuning worth real points, so any switch needs a cutoff fit on human labels and checked on held-out data.

## Key points

- Scale: 5 LLMs + 2 Jev configs, 10 Phoenix evaluators, 517 human-labeled examples (23–136 each), 10 reps, 36,190 judgments, $169.84 total — Jev's share 64 cents.
- Accuracy 98.3% for Jev in both drop-in and native configurations; small models 96.7–98.6%, frontier 98.0–99.4%; no significant pairwise difference after correction.
- Native API (state / instructions / criteria split) gains 7.1 points on completeness, the longest-context evaluator (~1,950 tokens); no other per-task difference significant.
- Label flip rate: 0.97% drop-in, 0.19% native — lowest of any judge; worst cases were GPT-5 nano 26% on tool invocation and Haiku 4.5 12% on PII.
- Confidence tracks correctness: median 1.00 when right vs 0.71 when wrong; 3,561/3,561 runs at ≥99% confidence were correct; below 70% confidence only 73% right; ROC AUC 0.95 drop-in, 0.99 native.
- Repeat-sampling the LLMs only reached AUC 0.62–0.84 for spotting their own errors, since 27–75% of mistakes were perfectly stable across all ten runs.
- Jev's entropy predicts LLM judge instability: 3% waiver on 306 near-certain examples vs 71% on 24 coin-flips; rank correlation 0.47; AUC 0.85; a 0.5-bit cutoff flags 11% of examples, where LLMs wavered ~2/3 of the time.
- Cost and latency: 12–40x cheaper than small models, 140–290x cheaper than frontier, 133 ms median — 13–55x faster than any LLM tested.
- Limits: small suites (weak power for small deltas), all binary labels, PII suite contains only positives so false alarms are unmeasured, no graded or open-ended tasks, and Jev never explains a verdict.

## Related

- [[llm-as-judge-architectures-runtime-joshrosen]]
- [[langchain-fireworks-trace-judge-100x-cheaper]]
- [[do-automated-evals-work-parlance-labs]]
- [[kev-small-decision-models-jaredpalmer]]
- [[how-to-build-eval-set-you-can-maintain-lotte]]
