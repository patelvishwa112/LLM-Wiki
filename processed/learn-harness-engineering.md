---
tags:
- harness-engineering
- agents
- claude-code
- codex
- agent-engineering
- verification
- course
source: https://walkinglabs.github.io/learn-harness-engineering/en/
date: 2026-06-05
type: resource
author: Walking Labs
description: Learn Harness Engineering
---

# Learn Harness Engineering

**What it is:** A project-based course by Walking Labs on the engineering of AI coding agents — how to design environments, state management, verification, and control systems that make Codex and Claude Code reliable for real development work.

**Core references:** OpenAI's "Harness Engineering" paper, Anthropic's "Effective Harnesses for Long-Running Agents" and "Harness Design for Long-Running Application Development", and the awesome-harness-engineering list.

## Key Concepts

- **Constrain agent behavior** with explicit rules and boundaries
- **Maintain context** across long-running, multi-session tasks
- **Stop agents** from declaring victory too early
- **Verify work** using full-pipeline tests and self-reflection
- **Make runtime observable** and debuggable

## The Core Mechanism

A harness is a closed-loop working system for the model, not a way to "make the model smarter":

```
Clear Objective → AGENTS.md → Initialization (init.sh) → Run Tasks (AI Agent)
    → Runtime Feedback (CLI / Logs) → Encounter Issues → Auto-fix → Verify & QA (Test suite)
        → Passed → Code Completed → Cleanup & Handoff (claude-progress.md)
        → Failed → Auto-fix (loop back)
```

## Structure

- **Lectures** — Theory: why capable agents still fail, harness design principles
- **Projects** — Hands-on: build a reliable agentic environment from scratch
- **Resource Library** — Copy-ready templates: AGENTS.md, feature_list.json, claude-progress.md

## Related

- [[feedback-loops-claude-code-less-babysitting]]
- [[openclaw-hermes-supervisor-setup]]
