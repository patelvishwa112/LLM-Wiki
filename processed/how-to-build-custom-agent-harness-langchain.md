---
tags:
  - agents
  - agent-harness
  - langchain
  - middleware
  - deep-agents
  - create-agent
  - human-in-the-loop
  - production
source: https://www.langchain.com/blog/how-to-build-a-custom-agent-harness
date: 2026-06-03
type: bookmark
author: Sydney Runkle
description: "LangChain guide—agent = model + harness; customize via create_agent middleware hooks (memory, subagents, retries, HITL, cost limits) for task-harness fit."
summary: "LangChain guide—agent = model + harness; customize via create_agent middleware hooks (memory, subagents, retries, HITL, cost limits) for task-harness fit."
raw: "[[raw/langchain_blog_how-to-build-custom-agent-harness]]"
---

# How to build a custom agent harness (LangChain)

**Sydney Runkle** (LangChain blog, June 2026) frames **agent = model + harness**—the harness delivers **right context at each loop step**, not just a static system prompt.

## Base vs prebuilt harnesses

- **`create_agent(model, tools, system_prompt)`** — minimal core loop (Pi-like configurability).
- **Deep Agents / Claude Agent SDK** — opinionated middleware stacks for fast production defaults.
- Custom agents needing **business logic, guardrails, bespoke prompting** → compose **middleware** on `create_agent`.

## Middleware levers

Hooks at model/tool boundaries and lifecycle: **deterministic policy**, **tool lifecycle**, **custom state**, **stream routing**. Prebuilt middleware covers common patterns; custom pieces compose and reuse org-wide.

## Capability → middleware map (high signal)

| Need | Examples |
|------|----------|
| Context overflow | Summarization, context editing |
| Memory / skills | Filesystem, Memory, Skills middleware |
| Environment actions | Shell, filesystem, code interpreter |
| Delegation | SubAgent (sync/async), TodoList |
| Reliability | Tool/model retry, model fallback |
| Policy / HITL | PII middleware, human-in-the-loop |
| Cost | Call limits, prompt caching |

## Task-harness fit

CS triage vs long-running coding agent need different stacks—LangChain cites **GTM agent**, **open-swe**, **LangSmith Fleet** as `create_agent` + tailored middleware.

## Why it matters

Canonical LangChain articulation of **harness engineering**—pairs with vault notes on Deep Agents, LangGraph fault tolerance, and Hermes-style harness customization.

## Related

- [[langchain-langgraph-101-repo]]
- [[introducing-dynamic-subagents-deep-agents]]
- [[deep-agents-prompt-caching]]
- [[fault-tolerance-langgraph-retries-timeouts]]
- [[learn-harness-engineering]]
- [[agent-harness-engineering-agentforge]]