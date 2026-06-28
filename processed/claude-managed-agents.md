---
tags:
- agents
- anthropic
- enterprise
- mcp
- claude
- agent-ops
source: https://claude.com/blog/claude-managed-agents
raw: '[[raw/anthropic-managed-agents]]'
date: 2026-06-07
author: Anthropic
type: bookmark
summary: Claude Managed Agents is a suite of composable APIs for building and deploying
  cloud-hosted agents at scale, handling sandboxing, state management, permissioning,
  and orchestration so teams can go from prototype to production in days rather than
  months.
related:
- '[[ai-agents]]'
- '[[harness-engineering-2026-discipline]]'
- '[[harness-is-the-product-context-aware-agents]]'
description: Claude Managed Agents is a suite of composable APIs for building and
  deploying cloud-hosted agents at scale, handling sandboxing, state management, permissioning,
  and orchestration so teams can go from prototype to production in days rather than
  months.
---

# Claude Managed Agents: Production Agents 10x Faster

A managed platform for building, deploying, and scaling Claude-powered agents with built-in infrastructure, orchestration, and governance.

## Key Points

| Feature | Description |
|---------|-------------|
| Production-grade infrastructure | Secure sandboxing, authentication, tool execution handled by the platform |
| Long-running sessions | Agents operate autonomously for hours with persistent progress and outputs |
| Multi-agent coordination | Lead agent spawns and directs specialist subagents for parallel work (research preview) |
| Trusted governance | Scoped permissions, identity management, execution tracing built in |
| Self-evaluation loop | Claude self-evaluates against success criteria and iterates until outcomes are met |

## Performance

In internal testing on structured file generation, Managed Agents improved task success by up to 10 points over standard prompting loops, with the largest gains on the hardest problems.

## Customer Deployments

- **Notion** — Delegated work agents inside workspace; coding, websites, presentations run in parallel
- **Rakuten** — Enterprise agents across product, sales, marketing, finance deployed within a week
- **Asana** — AI Teammates that work alongside humans in projects, taking on tasks and drafting deliverables
- **Sentry** — Seer debugging agent paired with Claude agent that writes patches and opens PRs
- **Vibecode** — Prompt-to-deployed-app infrastructure, 10x faster than prior setups
- **Atlassian** — Agents integrated into Jira workflows for developer task delegation
- **General Legal** — Dynamic tool creation on-the-fly, handling any user query without pre-built tools

## Pricing

Standard Claude Platform token rates plus $0.08 per session-hour for active runtime.
