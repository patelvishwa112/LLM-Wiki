---
tags: ["agent-harness", "hermes", "architecture", "agents", "analysis"]
source: "https://x.com/aparnadhinak/status/2060406977357070522"
raw: "[[raw/aparnadhinak_2060406977357070522]]"
author: "Aparna Dhinakaran (@aparnadhinak)"
date: 2026-05-29
type: analysis
related: ["iii-agent-harness-workers", "coding-agent-harness-eight-pillars"]
---

# Hermes Agent Harness Deep Dive by Aparna Dhinakaran (May 2026)

---

## Summary

Aparna Dhinakaran analyzes Hermes (by @NousResearch) using their nine-part agent harness framework from "What is an Agent Harness." Hermes implements all nine components — the interesting part is *how* it implements them, plus the extra systems sitting outside the frame.

## Key Takeaways

### The 9 Components — How Hermes Implements Them

1. **Outer iteration loop** — Strong provider abstraction: same runtime drives chat-completions, Anthropic Messages, Codex Responses, Codex app-server, and Bedrock. Tool-call formats and provider quirks normalized by transport adapters.

2. **Context management and compression** — Full compression path with session lineage. Compressed turns summarized by auxiliary model. Head/tail protected by token budget. Old tool outputs pruned before summarization. Most uniquely: compression creates child sessions with parent-child lineage tracked in SQLite, not just a rewritten transcript.

3. **Skills and tools management** — Tool registration and tool exposure are separate concerns. Tools register centrally; toolsets decide what the model sees per run (scoped by platform, scenario, and delegation). Broad installed library while keeping per-run surface small.

4. **Subagent management** — Solid delegation: child runs get own task ID, terminal context, structured summary. Dangerous commands default deny in delegated contexts. Gap: no durable child-run plane that survives parent completion.

5. **Built-in pre-packaged skills** — Skills system with persistence, reuse, and discoverability.

6. **Session persistence and recovery** — SQLite with FTS5 search and WAL journaling. Sessions track source tags, parent-child lineage, and gateway routing metadata. Exposes `session_search` tool for model-driven recall.

7. **System prompt assembly** — Three tiers: **stable** (identity, tool guidance, skills index), **context** (project files from cwd — AGENTS.md, CLAUDE.md, .cursorrules), **volatile** (memory snapshots, user profile, external providers, model metadata). Prompt rebuild tied to compression invalidation points.

8. **Lifecycle hooks** — Two surfaces: plugin lifecycle hooks (in-process, can block/rewrite) and filesystem gateway hooks (shell/Python scripts on startup, step, command triggers). Both enable policy enforcement independent of model cooperation.

9. **Permission and safety layer** — Built into delegation, tool exposure, and prompt injection scanning on context files.

### Beyond the Framework — Three Standout Subsystems

- **Messaging gateway** — Telegram, Discord, Slack, WhatsApp, and others routed through shared session model. Compared to OpenClaw's UX approach.
- **Profile system** — Isolated agent roots. Two profiles = two different agents from state/footprint perspective.
- **Cron as first-class** — Jobs are durable, permission-gated, delivered through gateway paths, isolated per profile. Forces unattended operation into main architecture.

### Where It Should Go Next

Move from strong delegation to first-class orchestration: durable child-run control with run IDs, explicit lifecycle management, external steering, and cleanup surviving parent completion. Hermes already has the substrate (session infrastructure + gateway routing).

### Verdict

> "Hermes is probably one of the best open model harnesses in the ecosystem. The pace of shipping is insane, and most of the hard substrate work is already in place."

## Connection to Wiki

- Builds on Aparna's earlier "What is an Agent Harness" framework
- Relates to [[iii-agent-harness-workers]] (Mike Piccolo's analysis)
- Contrasts with [[claude-code]] architecture
- Directly relevant to understanding the agent we're running on
