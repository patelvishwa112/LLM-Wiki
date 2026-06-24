---
tags: ["agents", "agent-harness", "mcp", "claude-code", "fundamentals", "observability", "guardrails", "subagents"]
source: https://x.com/sairahul1/status/2069351848742629693
date: 2026-06-24
type: bookmark
author: sairahul1
title: "Twenty core ideas behind every AI agent"
summary: "Framework-agnostic map of twenty recurring agent concepts across six layers, from execution loops and state through config, MCP, subagents, guardrails, and tracing."
raw: "[[raw/sairahul1_2069351848742629693]]"
---

## Key takeaways

**Thesis:** Framework churn is noise; the same ~20 ideas recur (loop, state, patterns, config, MCP, memory, subagents, loops, sandbox, hooks, tracing, etc.).

**Building blocks:** Agent as goal-driven loop; think–act–observe; state = context + external files; planner/executor, router/specialist, map-reduce.

**Configuration:** `CLAUDE.md` / `AGENTS.md`, on-demand workflow files, prompt caching, fighting context rot.

**Capability:** MCP with deferred loading, live doc retrieval, persistent memory across sessions.

**Orchestration:** Subagents for parallel/focused work; file-backed agent loops for repetitive bounded jobs.

**Guardrails:** Sandbox, permissions, pre-tool hooks, injection awareness, pre-commit gates.

**Observability:** Trace trees plus outcome-linked metrics (not just token counts).

**Starter stack:** project config file, sandbox, pre-commit gate, one subagent workflow.

## Why it matters

Serves as a vocabulary and checklist for comparing LangChain/CrewAI/Claude Code/Hermes-style systems without relearning each stack from scratch.

## Related

- [[harness-engineering-2026-discipline]]
- [[agent-harness-engineering-agentforge]]
- [[mcp-core-architecture-explained]]
- [[building-your-first-ai-agent-clear-path]]
- [[loop-designer-ten-step-roadmap-de1lymoon]]