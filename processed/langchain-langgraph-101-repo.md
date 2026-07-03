---
tags:
  - langgraph
  - langchain
  - deep-agents
  - agents
  - multi-agent
  - tutorial
  - resource
  - mcp
  - langsmith
source: https://github.com/langchain-ai/langgraph-101
date: 2026-07-03
type: resource
author: langchain-ai
description: "Official LangChain hands-on repo—101/201 Jupyter tracks plus Studio-ready agents for LangGraph, middleware/HITL, multi-agent, and Deep Agents (skills, AGENTS.md, memory)."
summary: "Official LangChain hands-on repo—101/201 Jupyter tracks plus Studio-ready agents for LangGraph, middleware/HITL, multi-agent, and Deep Agents (skills, AGENTS.md, memory)."
raw: "[[raw/github_langchain-ai_langgraph-101]]"
---

# LangGraph 101 (LangChain repo)

**langchain-ai/langgraph-101** — MIT tutorial repo for **LangChain + LangGraph + Deep Agents**, positioned as a condensed live-workshop companion to [LangChain Academy](https://academy.langchain.com/).

## What you get

| Track | Content |
|-------|---------|
| **101** | First agent (tools, memory, streaming); middleware, guardrails, HITL |
| **201** | Email triage agent; supervisor multi-agent; parallel research; **Deep Agents** build (AGENTS.md, skills, backends, long-term memory, interrupts) |
| **`agents/`** | Runnable graphs for **`langgraph dev`** / Studio — weather, email, music store, researcher, deep_agent (LinkedIn/X post skills) |

Shared **`utils/models.py`** centralizes LLM provider (default OpenAI `o3-mini`; Azure/Bedrock/Vertex toggles). **`uv sync`** + `.env` for keys; **`langgraph.json`** registers graphs.

## Why it matters

Canonical **on-ramp** from LangChain for controlled agent graphs (vs ad-hoc tool loops) and for **Deep Agents** as a LangGraph harness—aligns with vault notes on subagents, fault tolerance, and prompt caching in the LangChain stack.

## Practical entry

```bash
git clone https://github.com/langchain-ai/langgraph-101.git
cd langgraph-101 && cp .env.example .env && uv sync && source .venv/bin/activate
langgraph dev
```

Work 101 notebooks → 201 → Studio on `agents/deep_agent/`.

## Related

- [[fault-tolerance-langgraph-retries-timeouts]]
- [[deep-agents-prompt-caching]]
- [[introducing-dynamic-subagents-deep-agents]]
- [[how-to-use-rlms-in-deep-agents]]
- [[dive-into-claude-code-vila-lab]]