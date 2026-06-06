---
tags: ["evals", "agents", "memory", "benchmarks"]
source: https://x.com/0xVK__/status/2051403242530341265
date: 2026-05-03
type: bookmark
---

# LongMemEval: Evaluating Agent Memory Across Sessions

## Key Takeaways
- LongMemEval is the leading benchmark for evaluating agent memory across sessions
- Memory is core to continual learning — retaining facts, preferences, and implied context
- Memory application (using retained info for tasks) is NOT covered and is the harder problem
- quarqlabs is open-sourcing a verification framework for transparent, reproducible evals

## Summary
LongMemEval is probably the most well-known benchmark for evaluating an agentic system's memory across sessions.

Memory is a core part of "continual learning." It tests whether an agent can retain facts, user preferences, and even implied context across multiple chats or sessions.

The other part is applying those memories to perform the task, which is not covered by LongMemEval. If memory is solved properly, it becomes much easier to retrieve the right information and use it effectively to perform tasks aligned with the user's query.

@quarqlabs is seeing strong results on LongMemEval and running evals one last time before sharing results publicly. They are open-sourcing a verification framework to ensure full transparency and reproducibility.

Key insight: LongMemEval evaluates memory retention, but the harder problem is memory application — using retained context to actually improve task performance.

## Source
[https://x.com/0xVK__/status/2051403242530341265](https://x.com/0xVK__/status/2051403242530341265)
