---
tags: ["agents", "agent-ops", "coding-agents", "cost", "mcp"]
source: https://x.com/UberEng/status/2093444169037762840
date: 2026-08-28
type: bookmark
description: "Uber Eng (@udaykiran): software factory at scale — 70%+ PRs agent-attributed, 3600 skills, 7x WAU; cost equation, MCP-via-CLI, code-mode, context graph."
author: UberEng
summary: "Uber Eng (@udaykiran): software factory at scale — 70%+ PRs agent-attributed, 3600 skills, 7x WAU; cost equation, MCP-via-CLI, code-mode, context graph."
raw: "[[raw/UberEng_2093444169037762840]]"
---

# Running a Software Factory Efficiently at Uber Scale

Uber Engineering / @udaykiran. AI Engineer 2026 talk written up. Self-reported internal metrics.

## Scale claims

>70% of PRs attributed to local or cloud agents. 3,600+ skills. 30k+ skill executions/day. Feb–Aug 2026: WAU 7x, weekly agentic requests 9.4x, spend relatively stable since April. Holding model fixed Feb–Jul: cost/1k requests −34% from peak; cost/session −52% from June peak.

Growing share of sessions started by **managed agents** (review, self-healing CI, E2E PRs, on-call, bugs) not humans.

## Four layers + cost equation

Sessions from specialized managed agents down to general interactive. Decompose spend into adoption/engagement (want to grow) × middle terms (turns, tokens, price — where they optimize).

Levers: Pareto model selection on real-work benchmarks (uReview F1 vs cost/PR); weaker default **subagent** model; compaction at 400k even on 1M windows; medium reasoning default; **1-hour prompt-cache TTL** for interactive (engineers idle >5 min), 5-min for subagents; MCP schemas **not** preloaded — CLI tool resolution + tool search; **code-mode** (loop in subprocess, summary back; >50% tokens on SQL, >90% on bulk); SaaS MCP behind same gateway + skills.

**AI Context Graph:** 24M nodes / 80M edges / 30 systems. Grounded vs ungrounded same prompt: 38s vs 20 min of searching the wrong place.

Visibility: live status-line cost, Slack 50/80/100% nudges, session dashboard of 16 anti-patterns.

Thesis: move SDLC to managed agents with dedicated evals + Pareto models rather than optimizing thousands of personal terminal sessions.

## Related

- [[llm-as-judge-architectures-runtime-joshrosen]]
- [[kv-prefix-prompt-semantic-caching-llms-avichawla]]
