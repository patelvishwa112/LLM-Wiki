---
tags: ["agents", "rl", "evals", "legal-ai", "rlm", "post-training"]
source: https://x.com/nikogrupen/status/2097369705791307952
date: 2026-09-08
type: bookmark
description: "Harvey (@nikogrupen): RLM harness for M&A diligence lifts mean rubric pass 23.3% to 62.4%; RL on Qwen3.5-122B root 29.9% to 63.0% on LAB Diligence."
author: nikogrupen
summary: "Harvey (@nikogrupen): RLM harness for M&A diligence lifts mean rubric pass 23.3% to 62.4%; RL on Qwen3.5-122B root 29.9% to 63.0% on LAB Diligence."
raw: "[[raw/nikogrupen_2097369705791307952]]"
---

# Post-training RLM Agents for End-to-End M&A Diligence

Niko (@nikogrupen), Harvey Applied Research, with Baseten. Companion: https://www.harvey.ai/blog/post-training-rlm-agents-for-m-and-a-diligence

## Setup

LAB Diligence: synthetic M&A datarooms up to 5,000 docs / ~80M tokens. **RLM harness:** whole dataroom in a Python REPL; root agent plans and delegates bounded slices to sub-agents; root writes a memo with citations, quantified risks, recommendations. LLM-judge rubric with hundreds of pass/fail criteria.

## Results (as reported)

- Standard tool-use loop: **23.3%** mean criteria pass (7 models).
- RLM harness: **62.4%** (+39.1 pp). Coverage of relevant content jumps from <1% toward near-100%.
- RL (GRPO) on Qwen3.5-122B-A10B as root, smaller Qwen sub-agents fixed: **29.9% → 63.0%** on 50 held-out rooms; document-review coverage **62% → 96%**.
- Self-distillation SFT on GLM-5.2: e.g. 46.1% → 60.1% on a 20-room hold-out. Scaled RL on GLM-5.3 as root in progress.

Behavior: better delegation scaling with room size; incremental memo writing interleaved with review (not one-shot at the end). Depth-2 recursion did not help in initial tests. Root is highest leverage despite minority of tokens. RL steps 48–74 minutes wall-clock, dominated by sub-agent waves.

## Takeaway

Model-harness co-optimization for long-horizon document work. Post-train *inside* the architecture you will serve. Modest on-policy data, no privileged legal labels.

## Related

- [[rlm-recursive-llm-query-system]]
- [[how-to-use-rlms-in-deep-agents]]
- [[prime-agent-rlm-continual-harness-primeintellect]]
- [[introducing-dynamic-subagents-deep-agents]]
