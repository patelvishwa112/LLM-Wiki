---
tags:
  - agents
  - mcp
  - enterprise
  - anthropic
  - security
  - agent-ops
source: https://claude.com/blog/claude-managed-agents-updates
date: 2026-06-07
author: Anthropic
type: bookmark
summary: "Claude Managed Agents now support self-hosted sandboxes that keep execution within enterprise perimeters and MCP tunnels that connect agents to private internal services without exposing them to the public internet."
related:
  - "[[mcp-core-architecture-explained]]"
  - "[[claude-managed-agents]]"
---

# Managed Agents: Self-Hosted Sandboxes & MCP Tunnels

Two infrastructure updates that let Managed Agents operate entirely within enterprise security boundaries — sandboxes you control and private network connectivity via MCP tunnels.

## Key Points

| Feature | Description |
|---------|-------------|
| Self-hosted sandboxes | Agent tool execution runs on your infrastructure or a managed provider; files and repositories never leave your perimeter |
| MCP tunnels | Agents reach internal MCP servers (databases, APIs, ticketing systems) via a lightweight outbound-only gateway — no inbound firewall rules or public endpoints |
| Architecture separation | The agent loop (orchestration, context management, error recovery) stays on Anthropic infrastructure; tool execution moves to your environment |
| Enterprise controls | Network policies, audit logging, and security tooling already in place remain effective |

## Sandbox Provider Options

- **Cloudflare** — MicroVMs and lightweight isolates with zero-trust secrets injection, customizable egress proxies
- **Daytona** — Full composable computers, long-running and stateful, SSH-accessible, can be paused/restored
- **Modal** — Cloud platform for AI workloads, sub-second startup, scales to hundreds of thousands of concurrent sandboxes, CPU/GPU on demand
- **Vercel** — VM security with VPC peering, millisecond startup, credentials injected at network boundary

## Customer Use Cases

- **Amplitude** — Design Agent for on-brand production UI, using Cloudflare sandboxes for observability
- **Clay** — Sculptor GTM engineering agent on Daytona for autonomous workflow building
- **Rogo** — Financial analyst agent on Vercel Sandbox for proprietary data handling
- **Mason** — Enterprise tool orchestration with Modal sandboxes, working version in under a week

## Availability

Self-hosted sandboxes: public beta. MCP tunnels: research preview (request access).
