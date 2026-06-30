---
tags:
- agents
- multi-agent
- subagents
- orchestration
- langchain
- deep-agents
- workflows
- rlm
- code-interpreter
description: "LangChain Deep Agents dynamic subagents — agent-written JS orchestration via QuickJS task() for scale, coverage, and six workflow patterns (RLM-style)."
summary: "LangChain Deep Agents dynamic subagents — agent-written JS orchestration via QuickJS task() for scale, coverage, and six workflow patterns (RLM-style)."
source: https://x.com/sydneyrunkle/status/2071629451712983319
date: 2026-06-29
type: bookmark
author: sydneyrunkle
raw: "[[raw/sydneyrunkle_2071629451712983319]]"
---

# Introducing Dynamic Subagents in Deep Agents

Sydney Runkle (LangChain) announces **dynamic subagents**: the main agent writes a short **JavaScript orchestration script** (loops, branches, `Promise.all`) executed in a **QuickJS code interpreter**, dispatching subagents via `task()` instead of hundreds of sequential tool calls.

## Problem / solution

| Limitation | Turn-by-turn subagent tools | Dynamic subagents |
|------------|----------------------------|-------------------|
| Scale (e.g. 300 doc pages) | 300 model-driven tool calls | One loop in code |
| Coverage | Model may stop at 75/500 items | Loop structurally guarantees full fan-out |
| Multi-phase / conditional flows | Fragile tool-call chains | Code as orchestration |

Parallels **Claude Code dynamic workflows** and **RLMs** (code dispatches agents).

## Stack

- `pip install -U "deepagents[quickjs]"` + `CodeInterpreterMiddleware` on `create_deep_agent`
- Trigger keyword: **"workflow"** in user message
- **dcode** CLI — interpreter pre-wired; ACP in Zed
- `task({ description, subagentType, responseSchema? })` for typed results

## Six orchestration patterns (with traces in post)

Classify-and-act, fanout-and-synthesize, adversarial verification, generate-and-filter, tournament, loop-until-done — same vocabulary as Anthropic's dynamic workflows, implemented in Deep Agents.

## Related

- [[claude-code-dynamic-workflows-intro]]
- [[rlm-structured-outputs]]
- [[deep-agents-prompt-caching]]
- [[from-1-agent-to-swarm-orchestration-roadmap]]