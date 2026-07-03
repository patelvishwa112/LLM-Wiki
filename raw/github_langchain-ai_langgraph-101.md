---source_url: https://github.com/langchain-ai/langgraph-101
ingested: 2026-07-03
author: langchain-ai
title: "LangGraph 101"
note: README captured via mcp_firecrawl_firecrawl_scrape on GitHub repo page (2026-07-03).
sha256: a6f4ca1ce4b643b953f422fb8e043941541079f1ca723d892e6365dfba9b1b53
---

# LangGraph 101

**Repository:** https://github.com/langchain-ai/langgraph-101  
**Description:** Learn about the fundamentals of LangGraph through a series of notebooks  
**License:** MIT  
**Stats (scrape):** ~499 stars, ~119 forks (2026-07-03)

Welcome to LangGraph 101!

## Introduction

This repository contains hands-on tutorials for learning LangChain, LangGraph, and Deep Agents, organized into two learning tracks:

- **101**: Fundamentals of building agents with LangChain and LangGraph
- **201**: Advanced patterns including multi-agent systems, deep agents, and production workflows

Condensed version of LangChain Academy, intended to be run in a session with a LangChain engineer. Deeper self-paced path: [LangChain Academy](https://academy.langchain.com/courses/intro-to-langgraph).

Framework relationship doc: [LangChain vs LangGraph vs Deep Agents](https://docs.langchain.com/oss/python/concepts/products).

## What's Inside

### 101 - Fundamentals (`notebooks/101/`)

- **101_langchain_langgraph.ipynb**: First agent with models, tools, memory, streaming
- **102_middleware.ipynb**: Middleware, human-in-the-loop, guardrails

### 201 - Production Patterns (`notebooks/201/`)

- **email_agent.ipynb**: Stateful email triage/response agent
- **multi_agent.ipynb**: Supervisors + specialized sub-agents
- **research_agent.ipynb**: Deep research with parallel sub-researchers
- **deepagents.ipynb**: Research agent from scratch with Deep Agents (AGENTS.md, skills, backends, long-term memory, HITL)

### Agents (`agents/`) — LangGraph Studio via `langgraph dev`

- `agents/101/` — weather agent from 101 notebook
- `agents/email_agent/` — email triage
- `agents/music_store/` — multi-agent music store
- `agents/researcher/` — deep research + parallel sub-researchers
- `agents/deep_agent/` — DeepAgents with AGENTS.md, skills (LinkedIn/Twitter post), memory, HITL

Primitives emphasized: `create_agent()`, `create_deep_agent()`, middleware, interrupt patterns.

## Project Structure (summary)

```
langgraph-101/
├── notebooks/101|201/
├── agents/ (101, email_agent, music_store, researcher, deep_agent + skills/)
├── utils/models.py, utils.py
├── mcp/ (e.g. email_tools.py)
├── langgraph.json
└── pyproject.toml (uv sync)
```

## Context (from README)

LangGraph adds **precision and control** to agent workflows (tool ordering, state-conditioned prompts). Deep Agents is a **harness on LangGraph** for planning, filesystem access, delegation, built-in tools, context management, and skills.

## Setup (summary)

```bash
git clone https://github.com/langchain-ai/langgraph-101.git
cd langgraph-101 && cp .env.example .env
pip install uv && uv sync && source .venv/bin/activate
langgraph dev  # Studio + local API (~2024)
```

Default model via `utils/models.py`: OpenAI `o3-mini`; switch blocks for Azure, Bedrock, Vertex AI.

## Recommended path

1. 101 notebooks → 201 notebooks (email → multi_agent → deepagents)
2. Run agents in Studio (`agents/deep_agent/` demo: research + LinkedIn post)

## Resources (links from README)

- LangChain / LangGraph / Deep Agents docs
- LangSmith for debugging/monitoring