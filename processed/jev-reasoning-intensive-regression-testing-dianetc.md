---
title: "Jev on Reasoning-Intensive Regression: GPT-5-Level CCC at Lower NMSE"
type: bookmark
description: "Diane tests Jev zero-shot on math-error detection and pairwise RAG regression: CCC 0.65 vs GPT-5's 0.69, 37% lower NMSE, about 0.70 after calibration."
tags: [evals, llm-judges, benchmarks, inference, models]
source: https://x.com/dianetc_/status/2104648568459948469
date: 2026-09-28
author: Diane
summary: "Diane tests Jev zero-shot on math-error detection and pairwise RAG regression: CCC 0.65 vs GPT-5's 0.69, 37% lower NMSE, about 0.70 after calibration."
raw: "[[raw/dianetc__2104648568459948469]]"
---

# Jev on Reasoning-Intensive Regression: GPT-5-Level CCC at Lower NMSE

**Source:** Diane, 2026-09-28. A short pointer post to her blog write-up of testing Jev on reasoning-intensive regression problems.

Diane runs Jev — the classification model that answers typed questions with probabilities instead of text — against two reasoning-intensive regression (RiR) tasks from the RiR paper (arXiv:2508.21762): finding the first erroneous step in a math solution on a 0–10 scale, and judging the relative quality of two RAG answers on a −2 to +2 scale. Since Jev only returns label probabilities, both tasks need wrappers: character-interval Choice questions converted to a probability-weighted midpoint, or a five-level Score mapped onto the target scale. Everything is zero-shot, no task-specific training.

On math error detection Jev reaches CCC 0.65 against 0.69 for detailed GPT-5 prompting and 0.78 for MENTAT, but its NMSE is 0.49 versus GPT-5's 0.78 — a 37% improvement. Diane declines to read that as superiority: probability averaging shrinks uncertain predictions toward the middle, and squared error rewards shrinkage, so Jev's predictions span only ~63% of the targets' spread while carrying similar correlation (~0.7). A shift-and-rescale calibration fit on training data and selected on a dev set lifts CCC to about 0.70 on the same 750 test examples.

The pairwise RAG result is weaker: CCC 0.39 (Score) to 0.35 (Choice), bracketed by GPT-4.1 at 0.47 above and GPT-5 at 0.31 below. Its NMSE of 1.33–1.35 is the best zero-shot number yet still worse than predicting the mean, and reverse-engineering GPT-4.1's metrics shows that model has more real signal (correlation ≥0.55 vs 0.41) but spreads its guesses too wide.

She frames this as evidence of demand for a "foundation model for regression" — the numerical analogue of what Jev does for classification — while conceding prior art in TabPFN and time-series forecasters, and pointing to REAL (arXiv:2603.17145) on regression-aware LLM judging.

## Why it matters

The cost and latency profile of a classification model makes numeric judging viable at production scale, but the metric you pick decides whether it looks brilliant or broken: same predictions, opposite verdicts under CCC and NMSE. Anyone swapping an LLM grader for a probability model needs calibration fit on labeled data and a held-out check, not the default scale. It also marks the boundary of the form factor — classification transfers well, genuine multi-step quantitative reasoning still belongs to frontier models.

## Key points

- Setup: two RiR tasks, zero-shot, 750 test examples for math error detection; CCC and NMSE (1.0 = predict the mean).
- Math error: Jev CCC 0.65 / NMSE 0.49; GPT-5 detailed prompt 0.69 / 0.78; MENTAT-GPT-5 0.78 / 0.42.
- The 37% NMSE win is shrinkage, not skill: Jev's predictions cover only ~63% of target spread at similar ~0.7 correlation.
- Post-hoc shift-and-rescale calibration (fit on train, selected on dev) raises math-error CCC to ~0.70.
- Pairwise RAG: Jev CCC 0.39 (Score) / 0.35 (Choice), between GPT-5 (0.31) and GPT-4.1 (0.47); NMSE 1.33–1.35, worse than the mean.
- A finer Choice grid gave no gain over Score — the difference sat inside run-to-run noise.

## Related

- [[llm-as-judge-architectures-runtime-joshrosen]]
- [[generative-verifiers-genrm-deepmind]]
- [[langchain-fireworks-trace-judge-100x-cheaper]]
- [[do-automated-evals-work-parlance-labs]]
- [[agent-as-a-judge-trajectory-evals-aparna]]
