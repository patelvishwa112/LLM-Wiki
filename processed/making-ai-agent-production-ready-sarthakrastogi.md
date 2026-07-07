---
tags:
  - agents
  - agent-harness
  - production
  - langgraph
  - langchain
  - langsmith
  - rag
  - evals
  - observability
  - fastapi
  - prompt-injection
  - semantic-cache
source: https://sarthakai.substack.com/p/making-an-ai-agent-production-ready
date: 2026-07-07
type: bookmark
description: "Sarthak Rastogi tutorial — production Apple-style support bot with FastAPI, LangGraph, GPTCache, Presidio, Rival AI, PageIndex RAG, Ragas validation, LangSmith."
author: Sarthak Rastogi
summary: "Sarthak Rastogi tutorial — production Apple-style support bot with FastAPI, LangGraph, GPTCache, Presidio, Rival AI, PageIndex RAG, Ragas validation, LangSmith."
raw: "[[raw/sarthakai_making-an-ai-agent-production-ready]]"
---

# Making an AI Agent Production-Ready (tutorial)

Sarthak Rastogi (Apr 2026) walks through a **reference production stack** for a domain support bot (Apple devices/services) with full code at `github.com/sarthakrastogi/production-ai-app`. Patterns generalize beyond support.

## Architecture principle

**Prevent work before the graph; do work inside it.** Semantic cache lookup sits **outside** LangGraph so cache hits never pay compile/checkpointer cost. Middleware (auth, rate limits, input guard, structlog `request_id`) runs first. One graph invocation → one LangSmith trace.

## Pipeline layers

| Layer | Components |
|-------|------------|
| Middleware | JWT auth, slowapi per-user limits, max-length guard, JSON structlog |
| Cache | GPTCache server mode — semantic match (“iPhone won’t turn on” ≈ “not powering up”) |
| Safety | Parallel Presidio PII scrub + Rival AI Bhairava attack detector (microservice + pybreaker) |
| Query intelligence | Single structured LLM call — intent, sub-queries, complexity, `needs_decomp` |
| Memory | LangGraph `AsyncPostgresSaver` checkpointer; trim + summarize old turns |
| Retrieval | **PageIndex** tree navigation (vectorless) in MongoDB; empty-context fallback |
| Execution | Route Flash vs Pro; LangGraph `Send` for parallel sub-queries |
| Validation | Ragas **faithfulness** + custom **completeness** (multi-part questions) |
| Store | Write-back to GPTCache on success |

## Resilience posture

- **Tenacity** on transient HTTP/LLM failures  
- **Circuit breakers** on Rival and PageIndex — business fallbacks: allow-through when attack detector down (support bot tradeoff); retrieval down → parametric LLM with warning; LLM down → 503  

## Ops & evals

LangSmith traces per node; structlog for app events. Docker Compose: app, rival-service, gptcache, mongo, postgres. Suggests eval regression suites, streaming, A/B models, cross-session memory as next steps.

## Why it matters

Concrete **layered harness** for hallucination, cost, injection, partial answers, and 2am debuggability — complements abstract harness/loop notes with implementable FastAPI + LangGraph wiring.

## Related

- [[fault-tolerance-langgraph-retries-timeouts]]
- [[langchain-langgraph-101-repo]]
- [[how-to-build-custom-agent-harness-langchain]]
- [[continual-learning-replit-agent-vibench]]
- [[agent-harness-should-repair-itself]]
- [[agent-workflows-silent-degradation-verification-vladic]]