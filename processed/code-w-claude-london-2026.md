---
tags:
  - claude-code
  - anthropic
  - agents
  - managed-agents
  - mcp
  - developer-platform
  - conference
source: https://claude.com/blog/code-w-claude-london-2026-rethinking-how-we-build
raw: "[[raw/anthropic-code-w-claude-london-2026]]"
date: 2026-06-07
author: Anthropic
type: bookmark
summary: "Recap of Code w/ Claude London 2026: two new Managed Agents capabilities announced — self-hosted sandboxes (public beta) for tool execution within enterprise perimeters, and MCP tunnels (research preview) for connecting agents to private MCP servers without public internet exposure. Teams including Amplitude, Clay, and Rogo are already building on these features."
related:
  - "[[claude-code]]"
  - "[[model-context-protocol]]"
  - "[[ai-agents]]"
---

# Code w/ Claude London 2026

**Source:** Anthropic, June 2026. Europe debut of Code w/ Claude conference with keynotes, breakout sessions, and workshops.

## Keynote Theme

Boris Cherny (Head of Claude Code) described how agents are collapsing the distance between "I have an idea" and "it runs" — the calculator feeling, except the calculator writes distributed systems. Customer talks from Spotify, Base44, and Legora demonstrated real-world adoption.

## Two Major Announcements

### Self-Hosted Sandboxes (Public Beta)

Tool execution moves to enterprise-controlled infrastructure (own infra or managed providers like Cloudflare, Daytona, Modal, Vercel). The agent orchestration loop stays on Anthropic infrastructure, but files and repositories never leave the enterprise perimeter. Network policies, audit logging, and security tooling apply directly.

### MCP Tunnels (Research Preview)

Agents reach private MCP servers without exposing them to the public internet. A lightweight gateway makes a single outbound connection — no inbound firewall rules, no public endpoints, end-to-end encrypted traffic. Supported in Managed Agents and the Messages API, managed from Claude Console by org admins.

## Sessions

| Topic | Focus |
|-------|-------|
| Beyond the basics with Claude Code | Advanced patterns and techniques |
| The thinking lever | Optimizing think budgets and effort levels across models |
| Spotify | Scaling DevEx to teams and agents |
| Base44 | Scaling from 1 person to 80 in hypergrowth |
| Legora | What legal agents inherit from coding agents |

## Next

Code w/ Claude heads to Tokyo (June 5–6), with Day 1 streamed live.
