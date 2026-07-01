---
tags:
  - agents
  - rlm
  - recursive-language-models
  - deep-agents
  - langchain
  - subagents
  - context-rot
  - long-context
  - code-interpreter
source: https://x.com/sydneyrunkle/status/2072347918447558978
date: 2026-07-01
type: bookmark
author: sydneyrunkle
description: "Deep Agents adds RLM-style programmatic subagent orchestration (QuickJS REPL); OOLONG AgNews scores 0.79 vs 0.44 at 128k vs turn-by-turn agent."
raw: "[[raw/sydneyrunkle_2072347918447558978]]"
summary: "Deep Agents adds RLM-style programmatic subagent orchestration (QuickJS REPL); OOLONG AgNews scores 0.79 vs 0.44 at 128k vs turn-by-turn agent."
---

# How to Use RLMs in Deep Agents

Follow-up from LangChain on **recursive language model** ideas (MIT CSAIL paper) applied to **Deep Agents**: the orchestrator writes **code** that dispatches subagents instead of chaining tool calls turn-by-turn.

## Problem

**Context rot** plus fragile mental bookkeeping (running totals, multi-phase plans) fails on large corpora. Subagents help isolate context but don't guarantee coverage or complex control flow at scale.

## Mechanism

- **CodeInterpreterMiddleware** runs orchestration scripts (map/reduce, batch loops, `Promise.all` fan-out).
- Subagents remain full agents (tools, prompts)—closer to **recursive agents** than the paper's pure LM-in-REPL recursion.
- Mix orchestrator and worker models for cost/quality tradeoffs.

## Evidence (OOLONG / AgNews)

At **128k tokens**, REPL-orchestrated agent **0.79** vs plain **0.44**; plain agent often refuses the task. At 64k both are closer (0.67 vs 0.58). Authors frame this as an unoptimized smoke test.

## Practical trigger

Install `deepagents[quickjs]`, pass middleware to `create_deep_agent`, and use the word **workflow** in the user message to elicit scripted subagent dispatch.

## Why it matters

Bridges **dynamic workflows** (Claude Code pattern vocabulary) with **LangChain Deep Agents** and gives a concrete harness for long-context **aggregate-over-all-rows** tasks where deterministic iteration matters.

## Related

- [[introducing-dynamic-subagents-deep-agents]]
- [[rlm-structured-outputs]]
- [[claude-code-dynamic-workflows-intro]]
- [[harness-is-the-product-context-aware-agents]]
- [[deep-agents-prompt-caching]]