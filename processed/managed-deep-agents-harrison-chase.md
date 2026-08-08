---
tags: ["agents", "agent-harness", "harness-engineering", "langchain", "langsmith", "deep-agents", "managed-agents", "mcp", "skills", "enterprise", "production", "sandboxes", "evals"]
source: https://x.com/hwchase17/status/2085780032031760694
date: 2026-08-07
type: bookmark
description: "Harrison Chase launches Managed Deep Agents — Deep Agents harness plus LangSmith production infra (deployments, sandboxes, Context Hub, Harbor evals, memory, auth)."
author: hwchase17
summary: "Harrison Chase launches Managed Deep Agents — Deep Agents harness plus LangSmith production infra (deployments, sandboxes, Context Hub, Harbor evals, memory, auth)."
raw: "[[raw/hwchase17_2085780032031760694]]"
---

# Managed Deep Agents (Harrison Chase)

LangChain launches **Managed Deep Agents**: the Deep Agents harness run on managed infrastructure, aimed at developers who need production agents rather than local demos.

## Journey (as framed)

1. Early frameworks/apps (2022–23): LangChain, ChatGPT, AutoGPT
2. Mature control frameworks (2024–mid-2025): LangGraph, ADK, Vercel AI SDK — complex AI apps, not yet tool-loop agents
3. Tool-loop agents (mid-2025+): Manus, Deep Research, Claude Code; harnesses (Claude Code, Pi, Deep Agents)

## Two learnings that drove “managed”

- **Infrastructure primitives:** durable execution, sandboxes, “brain vs hands”
- **Control standards:** AGENTS.md, MCP, skills (progressive disclosure)

## Three parts of building agents

1. Business logic (context, tools, instructions) — always yours
2. The harness
3. Production infrastructure for the harness

Managed services bundle 2+3 so builders focus on 1.

## Prior experiments

- **Fleet** — very managed, file-based, non-dev audience; standards as files
- **Claude Managed Agents** — API-first, “dreaming”
- **Vercel Eve** — file-based + easy deploy

## Managed Deep Agents stack (LangSmith)

| Concern | Piece |
|---------|--------|
| Runtime | LangSmith Deployments |
| UX / streaming | Agent Server + Channels |
| Sandboxes | LangSmith Sandboxes |
| Context | Context Hub |
| Evaluation | Harbor |
| Memory | Opinionated on Deep Agents |
| Auth | Built-in AuthN |

Agents as files (like Fleet/Eve) but with **custom middleware and tools as code**.

## Why it matters

Closes the gap between “works in my terminal” and “runs reliably in production.” Same author as own-your-intelligence (model + harness + context compound loop) — this is the productized harness/infra half.

## Skeptical read

Launch narrative; production claims need independent load/cost experience. AuthN for agents acting on user systems still needs org-owned permission models (called out in replies).

## Related

- [[own-your-intelligence-harrison-chase]]
- [[how-to-build-custom-agent-harness-langchain]]
- [[deep-agents-prompt-caching]]
- [[claude-managed-agents]]
- [[managed-agents-sandbox-mcp]]
- [[managed-agents-dreaming-orchestration]]
- [[harbor-langchain-unified-agent-eval-stack]]
- [[sierra-pinecone-singular-company-agent]]
- [[learn-harness-engineering]]
- [[writing-good-skills-measured-rulebook-aparna]]
