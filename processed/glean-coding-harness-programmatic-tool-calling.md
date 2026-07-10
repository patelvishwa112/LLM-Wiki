---
type: bookmark
description: "Glean's enterprise agent harness uses 100% programmatic Python tool calls, sandbox file truncation, and search-driven progressive disclosure — 24% fewer tokens than hybrid tool-calling."
tags:
  - agent-harness
  - harness-engineering
  - glean
  - enterprise
  - programmatic-tool-calling
  - context-management
  - progressive-disclosure
  - cost-optimization
  - search
  - agent-ops
source: https://x.com/tonygentilcore/status/2075234683202531403
date: 2026-07-09
author: Tony Gentilcore (@tonygentilcore)
summary: "Glean moved to code-only tool orchestration in a sandbox, with truncated previews + on-disk full outputs and two core search tools for 1000+ enterprise skills — cutting tokens 24%."
raw: "[[raw/tonygentilcore_2075234683202531403]]"
---

# Glean coding harness — 100% programmatic tool calling

Tony Gentilcore (Glean, ex-Chrome/web performance) describes how Glean's **agent harness** scales long-running enterprise work through context management, trace learning, specialist routing — and a decisive shift to **100% programmatic tool calling** via Python in the agent sandbox.

## Core thesis

Standard ReAct-style loops serialize every tool I/O into the context window. Multi-system workflows pay token waste, latency, and reasoning overhead unrelated to task logic. Glean exposes only the **shell** to the model; search, write tools, and skills flow through a **tools SDK** executed as scripts.

A hybrid mode (standard calls for simple steps, code for complex) failed because choosing the mode each turn added overhead. Models handle one-line scripts as well as JSON tool calls, so standard tool-calling was removed entirely.

## Tool truncation + sandbox filesystem

Full tool outputs land on disk; the model sees a **truncated preview** plus metadata (how much data is on disk). It reads files only when needed — after seeing structure and sample rows, it often infers the rest without loading full payloads. That limits **context rot** on long jobs over large corpora.

## Search + progressive disclosure

Preloading 1000+ enterprise tools/skills would dilute attention and cost. The harness starts with two search tools: **enterprise context** and **tools/skills**. Discovery returns lightweight names/descriptions; full schemas and skill docs load only when relevant (**progressive disclosure**).

Search results are **appended at the end** of the conversation so prefix cache on earlier turns stays valid — faster and cheaper responses.

## Why it matters

Enterprise work is cross-SaaS orchestration with precise state — code is a better primitive than NL tool calls. The design is **model-agnostic** (frontier and strong open coding models). Reported outcome: **24% token reduction** vs the prior harness while supporting 1000+ tools.

A reply notes Claude Code/Cursor harnesses work for knowledge work but can be cost-inefficient — motivating domain-specific enterprise harnesses like Glean's.

## Related

- [[learn-harness-engineering]]
- [[how-to-build-custom-agent-harness-langchain]]
- [[improving-agents-data-mining-traces]]
- [[deep-agents-prompt-caching]]
- [[harness-is-the-product-280k]]