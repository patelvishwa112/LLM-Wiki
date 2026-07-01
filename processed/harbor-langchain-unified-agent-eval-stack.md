---
tags:
- langchain
- langgraph
- harbor
- agents
- evals
- langsmith
- sandbox
- deep-agents
- observability
- agent-harness
source: https://x.com/langchain/status/2071972238128005278
date: 2026-06-30
type: bookmark
author: langchain
summary: "LangChain announces Harbor integrations for Deep Agents/LangGraph, LangSmith Sandboxes, and LangSmith Experiments—an isolated, parallel agent eval stack with script-based verifiers and trace-backed debugging."
description: "LangChain announces Harbor integrations for Deep Agents/LangGraph, LangSmith Sandboxes, and LangSmith Experiments—an isolated, parallel agent eval stack with script-based verifiers and trace-backed debugging."
raw: "[[raw/langchain_2071972238128005278]]"
---

# Harbor x LangChain: A Unified Stack for Evaluating Agents

Official **LangChain** X Article on wiring **Harbor** (stateful agent eval harness) to **Deep Agents / LangGraph**, **LangSmith Sandboxes**, and **LangSmith** datasets/experiments/traces.

## Problem

Computer-use harnesses (Claude Code, Pi, Deep Agents) need **per-task isolated environments**; LLM-only evals miss filesystem/state artifacts.

## Harbor task model

Each task = **Environment** (Docker/Compose) + **Instruction** (markdown) + **Evaluation script** (`test.sh`) — judge **artifacts**, not final chat text.

## Three integrations

1. **`--agent langgraph`** — `langgraph.json` registry → `make_graph()` factory; use **`LocalShellBackend`** so Deep Agents touch real sandbox FS/shell.
2. **`-e langsmith`** (also Daytona/Docker/Modal/E2B) — fresh cloud sandbox per trial; scale **`n_attempts × tasks`** in parallel.
3. **`--plugin langsmith`** — sync dataset, create experiment, log verifier reward + attach agent traces when available.

## Stack roles

| Layer | Job |
|-------|-----|
| Harbor | Orchestrate trials + verifiers |
| Deep Agents | Agent under test |
| LangSmith Sandbox | Isolated execution |
| LangSmith | Datasets, experiments, traces, scores |

Quick start: `pip install harbor[langsmith]` + `harbor run --agent langgraph --dataset … -e langsmith --plugin langsmith --model …`

## Why it matters

Concrete reference architecture for **production agent evals**—pairs with vault Harbor RL notes and LangSmith observability/memory ingests.

## Related

- [[harbor-rl-coding-environments]]
- [[harbor-by-terminal-bench-multi-language-agent-evaluation-fr]]
- [[agent-evals-practical-guide]]
- [[deep-agents-prompt-caching]]
- [[introducing-dynamic-subagents-deep-agents]]
- [[how-to-give-your-agent-memory]]
- [[fault-tolerance-langgraph-retries-timeouts]]