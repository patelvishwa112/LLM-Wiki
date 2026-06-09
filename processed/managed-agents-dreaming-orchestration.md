---
tags:
  - agents
  - anthropic
  - memory
  - orchestration
  - multi-agent
  - agent-ops
source: https://claude.com/blog/new-in-claude-managed-agents
raw: "[[raw/anthropic-managed-agents-dreaming]]"
date: 2026-06-07
author: Anthropic
type: bookmark
summary: "Three major Managed Agents updates: dreaming for cross-session self-improvement, outcomes for rubric-driven self-evaluation, and multiagent orchestration for parallelizing complex work across specialist subagents."
related:
  - "[[managed-agents-built-in-memory]]"
  - "[[claude-managed-agents]]"
  - "[[ai-agents]]"
---

# Managed Agents: Dreaming, Outcomes & Multiagent Orchestration

Agents that self-improve across sessions, verify their own work against rubrics, and decompose complex tasks across parallel specialist subagents.

## Key Points

| Feature | Status | Description |
|---------|--------|-------------|
| Dreaming | Research preview | Scheduled process reviews past sessions and memory stores, extracts patterns, curates memories for self-improvement |
| Outcomes | Public beta | Rubric-driven self-evaluation with a separate grader in its own context window; agent self-corrects until output meets criteria |
| Multiagent orchestration | Public beta | Lead agent decomposes work, delegates to specialist subagents with their own models/prompts/tools, parallel execution on shared filesystem |
| Webhooks | Public beta | Get notified when agents complete outcome-defined tasks |

## Dreaming: Self-Improving Agents

Dreaming surfaces patterns a single agent cannot see alone: recurring mistakes, converged workflows, shared team preferences. It restructures memory to stay high-signal. Memory captures learning during work; dreaming refines it between sessions.

## Outcomes: Rubric-Driven Quality

A separate grader evaluates agent output against user-defined success criteria in its own context window — not influenced by the agent's reasoning. When output falls short, the grader pinpoints what to fix and the agent retries.

Performance gains: +8.4% task success on docx, +10.1% on pptx in internal benchmarks. Works for both objective criteria (structural requirements) and subjective quality (brand voice, visual guidelines).

## Multiagent Orchestration

Lead agent spawns specialist subagents that work in parallel. Each specialist has its own model, prompt, and tools. Events are persistent — every agent remembers what it's done. Full traceability in Claude Console.

## Customer Use

- **Harvey** — Legal drafting agents with dreaming; ~6x improvement in completion rates
- **Netflix** — Analysis agent processes logs from hundreds of builds, parallel batch analysis
- **Spiral (Every)** — Writing agent: Haiku lead fields requests, Opus subagents draft in parallel, outcomes enforce editorial standards
- **Wisedocs** — Document quality checks with outcomes grading; reviews 50% faster
