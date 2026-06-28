---
tags:
- agents
- observability
- agent-harness
- opik
- debugging
- testing
- evals
- regression-testing
- self-repair
- production
source: https://x.com/akshay_pachaar/status/2064051835636498924
date: 2026-06-08
type: bookmark
author: akshay_pachaar
title: Your Agent Harness Should Repair Itself
summary: 'Opik closes the agent debugging loop: Trace → Ollie diagnoses → proposes
  fix → verify → regression test. Four-layer stack (Tracing, Ollie, Test Suites, Sandbox)
  that automates everything after the trace. 19.3K stars.'
raw: '[[raw/akshay_pachaar_2064051835636498924]]'
related:
- '[[wtf-is-a-loop]]'
- '[[agent-harness-engineering-agentforge]]'
- '[[harness-is-the-product-context-aware-agents]]'
description: 'Opik closes the agent debugging loop: Trace → Ollie diagnoses → proposes
  fix → verify → regression test. Four-layer stack (Tracing, Ollie, Test Suites, Sandbox)
  that automates everything after the trace. 19.3K stars.'
---

# Agent Harness Self-Repair (Opik)

## Key Takeaways

1. **Observability ends at the trace — the real work begins after.** Most platforms answer "what happened" but leave "why," "how to fix," and "won't break again" as manual work. This is the wrong abstraction for production agents.

2. **Opik closes the loop automatically.** Four-layer stack: Tracing (@opik.track) → Ollie (coding agent diagnoses + proposes fix) → Test Suites (plain-English assertions, auto-growing from real failures) → Agent Sandbox (end-to-end testing without git).

3. **The flywheel:** Bad trace → root cause → diff → approve → rerun → regression locked. Every cycle hardens the harness.

4. **Ollie is the differentiator.** A coding agent embedded in the observability tool. Reads span trees, source files, proposes exact-line fixes, reruns against original failing trace, locks regression tests. Your approval is the one manual step.

5. **Test suites grow from production failures.** Not synthetic scenarios. Every debugged failure becomes a regression case. Plain-English assertions ("The response must include specific deal details") instead of numerical metrics.

## Connection to Agent Harness Patterns

This is the verification/feedback layer that makes loops trustworthy ([[wtf-is-a-loop]]). The same pattern as roborev and Claude's self-verification: the loop is only as good as its ability to check its own work. Opik productizes this for any agent framework.
