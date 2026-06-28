---
tags:
- agents
- memory
- anthropic
- enterprise
- agent-ops
source: https://claude.com/blog/claude-managed-agents-memory
raw: '[[raw/anthropic-managed-agents-memory]]'
date: 2026-06-07
author: Anthropic
type: bookmark
summary: Built-in memory for Claude Managed Agents lets agents learn across sessions
  using a filesystem-based memory layer — portable, observable, and optimized for
  long-running multi-session work with scoped permissions and audit logs.
related:
- '[[managed-agents-dreaming-orchestration]]'
- '[[claude-managed-agents]]'
- '[[ai-agents]]'
description: Built-in memory for Claude Managed Agents lets agents learn across sessions
  using a filesystem-based memory layer — portable, observable, and optimized for
  long-running multi-session work with scoped permissions and audit logs.
---

# Managed Agents: Built-in Memory

A filesystem-based memory layer that lets Managed Agents learn from every session, share knowledge, and improve over time.

## Key Points

| Feature | Description |
|---------|-------------|
| Filesystem-based | Memory mounts onto a filesystem; agents use the same bash and code execution tools |
| Cross-session learning | Agents retain and build on knowledge across sessions |
| Scoped permissions | Stores can be shared across agents with different access levels (org-wide read-only, per-user read-write) |
| Concurrent access | Multiple agents can work against the same store without overwriting |
| Audit trail | All changes tracked with agent/session attribution, rollback support, redaction capability |
| Exportable | Memories are files that can be managed via API |

## Model Capability

Latest models are more discerning about what to remember — saving comprehensive, well-organized memories and selecting only task-relevant context.

## Customer Results

- **Netflix** — Agents carry context across sessions, including multi-turn insights and mid-conversation human corrections
- **Rakuten** — Task-based agents cut first-pass errors by 97%, 27% lower cost, 34% lower latency
- **Wisedocs** — Document verification pipeline, cross-session memory spots recurring issues, 30% faster verification
- **Ando** — Workplace messaging platform capturing organizational interaction patterns without custom memory infrastructure
