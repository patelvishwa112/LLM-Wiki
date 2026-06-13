---
tags: ["anthropic", "ant-cli", "managed-agents", "cli", "agent-infrastructure", "mcp"]
source: https://x.com/hey_madni/status/2063606029146034375
date: 2026-06-07
type: bookmark
author: hey_madni
summary: "Full guide to Anthropic's `ant` CLI (MIT-licensed Go binary): typed client for Messages, Models, Files, Batch, Beta:Agents, Sessions, Environments, Skills. Supports Managed Agents primitives, Dreaming, Outcomes, multi-agent orchestration, self-hosted sandboxes, MCP tunnels, and Claude Code integration. Sessions billed at $0.08/hour + tokens."
raw: "[[raw/hey_madni_2063606029146034375]]"
---

# Anthropic `ant` CLI — Full Guide to Managed Agents

Madni's deep dive into the `ant` CLI, the operational layer for Anthropic's shift from model provider to agent infrastructure platform.

## Core Primitives
- **Agent**: Configuration (model, system prompt, tools, MCP servers)
- **Environment**: Cloud container with networking/sandboxing
- **Session**: Running instance inside an environment (durable, append-only event log)
- **Events**: SSE stream for user messages, tool results, status

## Key Features (April–June 2026 releases)
- Dreaming (research preview): scheduled memory curation between sessions
- Outcomes (public beta): self-grading evaluator loop with rubrics
- Multi-agent orchestration (public beta): lead agent delegates to specialist sub-agents
- Self-hosted sandboxes (public beta): tool execution in your own infrastructure
- MCP tunnels (research preview): encrypted gateway to internal services

## Why It Matters
`ant` + Claude Code + Managed Agents forms the full stack: local orchestration → cloud workers → CLI management.

Directly relevant to Hermes agent infrastructure, MCP, skills, and multi-agent patterns.