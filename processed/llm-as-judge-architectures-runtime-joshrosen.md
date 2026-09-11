---
tags: ["evals", "agents", "agent-harness", "llm-as-judge"]
source: https://x.com/JoshARosen/status/2097324183428444499
date: 2026-09-08
type: bookmark
description: "Josh Rosen: LLM-as-judge is moving from offline eval into agent control flow; patterns for runtime judges and why noisy judges become app failures."
author: JoshARosen
summary: "Josh Rosen: LLM-as-judge is moving from offline eval into agent control flow; patterns for runtime judges and why noisy judges become app failures."
raw: "[[raw/JoshARosen_2097324183428444499]]"
---

# LLM-as-Judge Architectures: Putting Evals Into Your Agent Runtime

Josh Rosen (@JoshARosen). Offline LLM-as-judge (dataset → grade → regression) is moving **into the agent loop**: the judge participates in control flow, not just scorecards.

## Why

Deterministic software has schema/type/assert. Agent work often needs a human-like judgment: complete enough? useful? evidence-backed? safe to write into the company brain?

## Patterns

1. **Another model** — worker vs judge; judge need not be generally smarter. Specialized/cheap judges (Prometheus, Galileo) for high-volume runtime.
2. **Break the judgment apart** — completeness vs groundedness vs process. G-Eval step generation; DeepEval DAG of small judgments inside a deterministic graph.
3. **Compare instead of score** — pairwise better than 7-vs-8. Runtime: pick among plans, two-agent analysis, proposed action vs alternative.
4. **Judge the work not the answer** — trace-level (retrieval, tool choice, evidence) as checkpoints before synthesis/implementation/action.
5. **More than one judge** — panels/debate; disagreement as retry/escalate signal, not just a vote.
6. **Judge the judge** — position bias, style bias; once on the critical path, judge error = application failure (loops, blocked good work, approved bad work, latency).

Closer: huge design space; do not put a noisy offline judge on every important action without maturing the architecture.

## Related

- [[dair-ai-ten-papers-co-evolving-agents-verification]]
- [[post-training-rlm-agents-ma-diligence-harvey]]
