---
tags:
  - anthropic
  - ant-cli
  - claude-code
  - managed-agents
  - mcp
  - cli
  - agents
  - dev-tools
  - infrastructure
source: https://x.com/hey_madni/status/2063606029146034375
raw: "[[raw/hey_madni_2063606029146034375]]"
date: 2026-06-07
author: Madni Aghadi (@hey_madni)
type: bookmark
summary: "Comprehensive guide to Anthropic's ant CLI — a typed API client for the Claude platform. Covers installation, output formats, the four Managed Agents primitives (Agent, Environment, Session, Events), the full deploy workflow, Dreaming/Outcomes/multi-agent orchestration, self-hosted sandboxes with worker polling, MCP tunnels, Claude Code integration via /claude-api skill, agents-as-code CI/CD, and production shell pipelines. Four major releases in 55 days drove 80x Q1 growth."
related:
  - "[[claude-managed-agents]]"
  - "[[managed-agents-sandbox-mcp]]"
  - "[[managed-agents-dreaming-orchestration]]"
  - "[[claude-code-slash-command-library]]"
---

# Anthropic's ant CLI — Full Guide

**Source:** Madni Aghadi (@hey_madni). ant is a typed API client for the Claude platform — not a curl wrapper. One Go binary, MIT licensed.

## Mental Model

```
Claude Code = local orchestrator
Managed Agents = cloud workers
ant = layer connecting both
```

## Quick Reference

| Task | Command |
|------|---------|
| Install | `brew install anthropics/tap/ant` |
| List models | `ant models list` |
| Send message | `ant messages create --model claude-opus-4-8 --max-tokens 1024 --message '...'` |
| List agents | `ant beta:agents list` |
| Create agent | `ant beta:agents create --name "..." --model '...'` |
| Start session | `ant beta:sessions create --agent '...' --environment-id '...'` |
| Send task | `ant beta:sessions:events send --session-id '...' --event '...'` |
| Poll worker | `ant beta:worker poll` |
| Claude Code onboard | `/claude-api managed-agents-onboard` |

## Output Control

- `--format yaml|jsonl|explore` — explore is an interactive TUI
- `--transform "{id,name}"` — GJSON path reshaping
- `--raw-output` — bare string for piping to next command
- `--debug` — full HTTP request/response to stderr
- `@file://path` — inline file content, auto-detects binary for base64

## Managed Agents Stack

| Primitive | Role |
|-----------|------|
| **Agent** | Config: model, system prompt, tools, MCP servers |
| **Environment** | Cloud container with networking, sandboxing, packages |
| **Session** | Running instance, durable via append-only event log |
| **Events** | SSE stream: messages, tool results, status updates |

## Key Features (May–June 2026)

- **Dreaming (research):** Background memory curation between sessions. Harvey: 6x task completion.
- **Outcomes (beta):** Self-grading evaluator loop with rubrics, up to 20 iterations. Wisedocs: 50% review time reduction.
- **Multi-agent (beta):** Lead agent → parallel specialist sub-agents. Netflix: hundreds of simultaneous builds.
- **Self-hosted sandboxes (beta):** Tool execution in your infrastructure. `ant beta:worker poll` for always-on worker.
- **MCP tunnels (research):** Encrypted connection from cloud agents to internal private services.

## Billing

- Sessions: $0.08/hr, billed to millisecond, idle free
- Credit pools: Pro $20/mo, Max 5x $100/mo, Max 20x $200/mo
- CLI: free, MIT licensed

## The Big Picture

Anthropic spent two years being a model company. ant is the clearest signal that the actual product is now the platform. Model companies sell intelligence access. Platform companies sell the infrastructure to deploy intelligence at scale. 80x Q1 2026 growth, four major releases in 55 days.
