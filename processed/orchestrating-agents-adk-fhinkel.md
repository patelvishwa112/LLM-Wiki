---
tags: ["agents", "multi-agent", "orchestration", "adk", "google", "context-management", "subagents", "agent-harness"]
source: https://x.com/fhinkel/status/2076782085516493079
date: 2026-07-13
type: bookmark
description: "Franziska Hinkelmann on Google ADK multi-agent orchestration: specialist subagents + default isolation; share only sliced session state, not a global context pool."
author: fhinkel
summary: "Franziska Hinkelmann on Google ADK multi-agent orchestration: specialist subagents + default isolation; share only sliced session state, not a global context pool."
raw: "[[raw/fhinkel_2076782085516493079]]"
---

# Orchestrating Agents in ADK — @fhinkel

Follow-on to agent memory: memory fixes conversation continuity but does not fix the **generalist agent** failure mode — one context stuffed with every tool and instruction until routing gets fuzzy and unrelated context bleeds into decisions.

## Core move

Stop one mega-agent; build a **team**:

- **Parent orchestrator** — read request, pick specialist, hand off (delegation is the real job).
- **Subagents** — narrow instruction + small tool set (e.g. flight_agent vs hotel_agent).
- ADK auto-injects delegation tools named after each subagent.

## Context sharing rule

| Pattern | Tradeoff |
|---------|----------|
| Global state pool | Convenient; reintroduces context pollution |
| Strict isolation | Specialists stay sharp; must choose what to pass |

**Default to isolation.** Share only the state keys a subagent needs (`ctx.state["trip:destination"]`, dates, etc.) — not full conversation or raw tool dumps into the orchestrator window.

## Why it matters

Maps cleanly to context-engineering / token-budget discipline: multi-agent is a **boundary** design problem, not only an orchestration graph problem. Same pattern as Deep Agents dynamic subagents and swarm roadmaps, expressed in Google ADK APIs (session state, SequentialAgent, ParallelAgent).

## Related

- [[introducing-dynamic-subagents-deep-agents]]
- [[from-1-agent-to-swarm-orchestration-roadmap]]
- [[how-to-build-ai-agent-swarms]]
- [[openclaw-hermes-supervisor-setup]]
- [[dynamic-workflows-where-plan-lives]]
- [[how-to-give-your-agent-memory]]
