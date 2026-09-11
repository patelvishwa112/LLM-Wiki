---
tags: ["models", "transformers", "reasoning", "interpretability", "gpt-6"]
source: https://x.com/rasbt/status/2097677953450561596
date: 2026-09-09
type: bookmark
description: "Raschka: looped transformers reuse block weights for extra depth; Astra's shorter CoT is capability not hidden neuralese. Article on Ahead of AI."
author: rasbt
summary: "Raschka: looped transformers reuse block weights for extra depth; Astra's shorter CoT is capability not hidden neuralese. Article on Ahead of AI."
raw: "[[raw/rasbt_2097677953450561596]]"
---

# GPT-6 Astra, Looped Transformers, and Hidden Reasoning

Sebastian Raschka (@rasbt), Ahead of AI, 2026-09-09. Tweet is a pointer. Full article: https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and — also [[raw/sebastianraschka_gpt-6-astra-looped-transformers-and]].

## Astra impressions (author)

Calls GPT-6 Astra the best model he has used as of writing. Covers benchmarks, computer-use, and that Astra is still a reasoning model (visible CoT not abolished).

## Looped transformers

Reuse the same block weights across extra passes (Nanbeige 4.2: 22 unique blocks × 2 passes ≈ 44 applications). Increases computational depth without a second parameter stack. 2 loops was their efficiency sweet spot. Related: Universal Transformers (flexible loop counts), Mixture-of-Recursions (router, early exit per token). Cost: extra FLOPs/latency vs just making the model bigger; KV-cache implications.

Whether Astra *uses* looping: plausible rumor (The Information); Raschka treats it as a small architectural tweak, not the main source of gains (scale, data, recipe). Pachocki: frontier compute-graph depth "within a factor of two of GPT-4."

## Hidden reasoning

Looping does more work in hidden states before the next token. Stronger models also emit fewer explicit reasoning tokens — already seen across generations (e.g. Luna vs Sol). Not unique to looping; at fixed accuracy Astra uses fewer tokens than GPT-5.6 Sol, which can mean fewer mistakes/backtracks, not unmonitorable neuralese. Journalist narrative overstated.

## Related

- [[looped-ttt-test-time-training-looped-transformers-alvinzh]]
- [[wtf-is-a-loop]]
- [[rlm-recursive-llm-query-system]]
