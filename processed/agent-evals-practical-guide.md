---
tags: ["agents", "evals", "agent-ops", "testing", "production"]
source: https://x.com/Vtrivedy10/status/2057175860910964967
date: 2026-05-20
type: bookmark
related: [[coding-agent-harness-eight-pillars]], [[21-agent-building-mistakes]]
---

# Agent Evals — Practical Guide to Measuring Agents in Production

## Summary
A brain dump from production experience on how and why to use evals for agents before and after shipping to production. Eight practical principles distilled from real-world agent deployment.

## Key Takeaways

1. **Evals should simulate real user behavior**, not random benchmarks. They reflect priors on likely user behaviors.

2. **Best evals are discovered from real-world traces.** Ship an imperfect agent, capture failures, build evals from those traces to prevent regressions.

3. **Evals enable apples-to-apples comparison** across time and model changes. Answers "is my agent still good a month from now with a new model?"

4. **Evals ≈ Environments.** The eval environment must mirror production as closely as possible. The more eval drifts from prod, the larger the Sim2Real gap.

5. **Evals are regression tests.** Prompt changes that fix one thing can break another — evals catch this.

6. **Evals are training data.** Agent = fit(model, evals). Good evals → good agent.

7. **Some evals can fail today** if they're too hard for current models — they become targets for next-gen agents.

8. **The best eval is one that actually exists.** Start with small unit-test-style evals to build momentum. Unit tests are familiar to engineers.

## Connections
- [[coding-agent-harness-eight-pillars]] — Eight pillars of coding agent harness design, including testing
- [[21-agent-building-mistakes]] — Common mistakes include skipping evals
- Production trace → eval pipeline mirrors observability-driven development patterns
