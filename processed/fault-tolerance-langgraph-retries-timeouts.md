---
tags:
- agents
- langgraph
- fault-tolerance
- retries
- error-handling
- saga
- production
source: https://x.com/sydneyrunkle/status/2062588423295111208
date: 2026-06-04
type: bookmark
author: Sydney Runkle & @quanzhenglong (LangChain)
raw: '[[raw/sydneyrunkle_2062588423295111208]]'
description: 'Fault Tolerance in LangGraph: Retries, Timeouts, and Error Handlers'
---

# Fault Tolerance in LangGraph: Retries, Timeouts, and Error Handlers

## Key Takeaways

- **Three primitives, one API.** RetryPolicy (backoff/jitter for transient errors), TimeoutPolicy (run_timeout + idle_timeout with progress-based refresh), error_handler (runs after retries exhausted, with NodeError context). All attach via `add_node()` — config lives next to the logic it protects.
- **Retries are smart about what they catch.** Default retry_on is conservative: ConnectionError, 5xx, generic transients. Does NOT retry ValueError/TypeError/RuntimeError — those are bugs. Can be a tuple of types or a callable predicate.
- **Error handlers fire only after retry exhaustion.** This is the property that makes them useful. If you want to run on every exception, use try/except inside the node. Handler gets `NodeError` with `.node` and `.error` attributes. Transition is atomic — committed to checkpoint so crashes mid-handler resume correctly.
- **SAGA pattern for side-effect workflows.** The real power: flight booking example with reserve → pay → issue → compensate. Each step has retries + error_handler that routes to a compensate node. The compensate node inspects `state["completed"]` and undoes only completed steps in reverse order. Per-step retries, atomic transition to compensation, persistent state tracking.
- **The gap between demo and production is fault tolerance.** A 1% transient failure rate is minor in a demo but compounds quickly in a production agent with dozens of steps and real-world consequences. Writing the error handling boilerplate is often longer than the business logic — LangGraph builds it into the runtime.

## Summary

Sydney Runkle and Quanzhen Long (LangChain) walk through LangGraph's three fault tolerance primitives and how they compose into production-grade agent reliability. RetryPolicy handles transient failures with exponential backoff and jitter. TimeoutPolicy caps node execution with both wall-clock and progress-based idle timeouts. Error handlers provide a clean escape hatch after retries are exhausted — with atomic checkpointing so the handler resumes correctly even if the host crashes.

The SAGA pattern example (flight booking) demonstrates the real power: a multi-step workflow where each step can fail, and a compensate node undoes only what needs undoing. The fault tolerance config lives right alongside the business logic via `add_node()` — no separate infrastructure layer.

## Related

- [[feedback-loops-claude-code-less-babysitting]]
- [[learn-harness-engineering]]
