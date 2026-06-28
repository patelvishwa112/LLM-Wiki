---
tags:
- hermes
- kanban
- agents
- multi-agent
- orchestration
- skills
- profiles
source: https://x.com/akshay_pachaar/status/2062526843564233040
date: 2026-06-04
type: bookmark
author: Akshay (@akshay_pachaar)
raw: '[[raw/akshaypachaar_2062526843564233040]]'
description: 'Hermes Kanban: Mission Control for Your Agents'
---

# Hermes Kanban: Mission Control for Your Agents

## Key Takeaways

- **Shared context via task summaries is the core insight.** Agents hand off structured summaries (files changed, what was built, what the next agent needs). No cold starts. The board survives crashes and reboots — every task preserves full run history.
- **Six-column board with agents behind columns.** Triage → Todo → Ready → In Progress → Blocked → Done. An orchestrator (PM agent) decomposes goals, checks existing profiles, creates dependency-linked task chains. Three patterns: Pipeline (parent-based chains), Human in the loop (kanban_block/unblock with retry context), Triage specifier (rough idea → full spec via kanban specify).
- **Phone-controlled via Telegram gateway.** Create and steer tasks from your phone. The PM agent runs 24/7, reachable on Telegram. Dashboard at localhost:9119 with live WebSocket updates, profile lanes, nudge dispatcher.
- **4 profiles in ~20 minutes.** Profile creation (`hermes profile create --clone`), SOUL.md per profile, skills installation from 687-skill Hub, `hermes kanban init`, gateway setup. Demo: working Google Docs clone built entirely by the agent team.
- **Three failure modes:** Database overload (cap concurrency with --max 4), scratch workspace deletion (use worktree for coding), local model saturation (--max 2 for Ollama/GPU).

## Summary

Akshay provides a complete walkthrough of Hermes Kanban — the multi-agent coordination system that turns independent agents into a coordinated team. The key breakthrough is structured task summaries: when an agent finishes, it writes what it built, what files changed, and what the next agent needs to know. The next agent reads that before starting — no cold starts, no context loss. A 4-agent software team (PM, backend, frontend, tester) can be set up in ~20 minutes, controlled from a phone via Telegram, and monitored via a live WebSocket dashboard.

## Related

- [[openclaw-hermes-supervisor-setup]]
- [[how-to-build-ai-agent-swarms]]
