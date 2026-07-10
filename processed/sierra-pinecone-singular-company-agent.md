---
type: bookmark
description: "Sierra's Neil Rahilly on Pinecone — one persistent company-wide agent (Claude Code/Codex), MCP Gateway for context, artifacts as UI, and measuring outcomes not token activity."
tags:
  - agents
  - agent-harness
  - enterprise
  - sierra
  - pinecone
  - claude-code
  - codex
  - mcp
  - agent-ops
  - productivity
  - outcomes
  - artifacts
source: https://x.com/neilrahilly/status/2075290325757608148
date: 2026-07-09
author: Neil Rahilly (@neilrahilly)
summary: "Sierra collapsed role-specific internal agents into Pinecone — one Slack thread across systems, proactive persistence, MCP-scoped context; 70% of PRs and 75k+ sessions since March."
raw: "[[raw/neilrahilly_2075290325757608148]]"
---

# Sierra Pinecone — singular company-wide agent

Neil Rahilly (Sierra) describes how a six-person **AI acceleration team** scaled internal agent use after engineers saw ~5× throughput with parallel agents, git worktrees, **Claude Code**, and **Codex** — and the design choices behind **Pinecone**, Sierra's company agent.

## 1. Agent, singular

Role-specific agents (support, analyst, engineer, sales) failed: employees had to remember which bot to use, while high-value work spans departments. Sierra merged them into **Pinecone** — one Slack handle, one URL, one thread. It routes across systems so staff don't act as human routers. Parallels Sierra's customer agents (full-service, not IVR menus). One agent means every harness improvement lifts the whole company.

## 2. Proactive, not reactive

Work spans days or weeks. Pinecone **persists context** and can act on triggers (webhooks, Linear, reviews) — prep notes, draft debriefs, summarized reviews with risks. Direction: agents prompting humans when judgment is needed, not only the reverse.

## 3. Context is the bottleneck

Frontier models are "smart enough"; differentiation is **company context** (Slack, GitHub, ClickHouse, Salesforce, PagerDuty, etc.). Early analyst agent hacked with Claude Code + Opus 4.6 + MCP cut afternoon investigations to minutes.

Unrestricted access is a security risk — **MCP Gateway** inherits per-employee permissions, enforces policy per tool call, isolates customer data, audits. Built on Claude Code and Codex with **model routing** above the providers. Durable edge: context, workflows, routing — plus experiments in Pinecone "dreaming" (daily reflection to improve its own skills).

## 4. Agent as UI, systems of record as backend

Work produces **artifacts** (PRs, decks, contracts, reviews). Pinecone returns updated artifacts, not chat advice. GitHub/Linear/Salesforce stay canonical; the agent is the cross-system layer. Bet: SaaS tools become backends; agent is primary interface.

## 5. Outcomes, not activity

Since March: **75,000+ sessions**, **600+ users**, **70% of PRs** opened via Pinecone, plus silent automations. Sessions and tool calls prove adoption but not value — Sierra wants downstream outcomes (faster deals, first-pass fixes, reclaimed evenings). Measurement gap is explicit next work.

**Framing:** 1968 "10× engineer" study → hunt unicorns for 50 years; now equip everyone with an agent so judgment, taste, and relationships get more time.

## Related

- [[glean-coding-harness-programmatic-tool-calling]]
- [[ambient-pm-agents-evidence-first-prd]]
- [[how-to-become-applied-ai-engineer-eyad-khrais]]
- [[claude-code-dynamic-workflows-intro]]
- [[agent-workflows-silent-degradation-verification-vladic]]