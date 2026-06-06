---
tags: ["agents", "sub-agents", "inference-time-scaling", "multi-agent", "papers"]
source: https://x.com/neural_avb/status/2056358393892540552
date: 2026-05-08
type: bookmark
related: [[iii-agent-harness-workers]], [[coding-agent-harness-eight-pillars]], [[hermes-agent-use-cases-multi-agent-setup]]
---

# Sub-Agents as Inference-Time Scaling Primitive

## Summary
Sub-agents are emerging as a powerful inference-time scaling primitive that expands working memory, enables divide-and-conquer strategies, and accelerates problem-solving through parallel execution. The open question: how do we train models to best leverage sub-agents?

## Key Takeaways

**Three benefits of sub-agents:**
1. **Expand working memory** — Offload context to sub-agents, bypassing single-context limitations
2. **Divide-and-conquer hard problems** — Decompose complex tasks into parallelizable sub-tasks
3. **Parallel execution** — Solve problems faster by running sub-agents concurrently

**Open research question:** How do we train a model to best take advantage of sub-agents and ensure we get these benefits reliably?

**Paper:** arxiv.org/abs/2605.06639 (with breakdown at paperbreakdown.com)

## Connections
- [[iii-agent-harness-workers]] — Worker-based agent architecture for parallel task execution
- [[coding-agent-harness-eight-pillars]] — Agent harness design includes orchestration patterns
- [[hermes-agent-use-cases-multi-agent-setup]] — Practical multi-agent deployment with Hermes
- Sub-agents as inference-time scaling parallels test-time compute scaling in LLMs
