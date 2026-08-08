---
tags: ["skills", "agents", "agent-harness", "progressive-disclosure", "context-engineering", "coding-tools", "posthog", "productivity", "evals"]
source: https://x.com/posthog/status/2084345938089316582
date: 2026-08-03
type: bookmark
description: "PostHog (Ian Vanagas) on writing agent skills that work — 226 internal skills, progressive disclosure, anti-rot principles, and when not to skill-ify."
author: posthog
summary: "PostHog (Ian Vanagas) on writing agent skills that work — 226 internal skills, progressive disclosure, anti-rot principles, and when not to skill-ify."
raw: "[[raw/posthog_2084345938089316582]]"
---

# What nobody tells you about writing agent skills (PostHog)

Ian Vanagas / PostHog *build mode* essay. Internal scale: **226 skills** in skill store; **187 SKILL.md** across **28 products**.

## Problem

Agents have **amnesia** — rediscover codebase, tools, and gotchas every session; burn tokens repeating known failures. Skills = institutional memory: write once, stop re-explaining.

## Five lessons

### 1. Master progressive disclosure

- Skills are **routers**, not dumps
- Name + description answer **when** to load, not a full table of contents
- Nested structure (schemas, examples, indexes) enables further disclosure
- Too many skills / bloated descriptions hurt routing (PostHog + Databricks observed)

### 2. Skills aren’t just code / brittle scripts

- Prefer precise **goals, constraints, non-discoverable context**
- Stay ambiguous on exact path — leave room for model reasoning
- Over-prescribed command lists become brittle workflows

### 3. Skills rot — design against it

- Split durable structure from volatile content
- Point at single source of truth (docs) instead of copying
- Prefer regenerate-from-base over endless patches
- PostHog “context mill” pipeline: docs + examples → versioned skills for MCP/wizard/etc.

### 4. Asking questions > making demands

Before writing: ask the agent what it can do, what it needs, how last run failed. Highest-leverage hour for skill design.

### 5. Not everything deserves a skill

Create when work is repeated, agents fail by default, needs private context, or can run with goals/eval/schedule. Heuristic: done 3× and will do 3× more.

## Why it matters

Most practical large-org write-up on operationalizing skills — pairs with Aparna’s measured skills rulebook and Anthropic Claude Code skills lessons. Progressive disclosure + rot control are the hard parts, not SKILL.md syntax.

## Related

- [[writing-good-skills-measured-rulebook-aparna]]
- [[anthropic-claude-code-skills-lessons]]
- [[how-to-create-right-skill-ai-agent]]
- [[dark-arts-of-skill-engineering-pbakaus]]
- [[self-improvement-loop-for-skills-zach-lloyd]]
- [[context-engineering-field-guide-phosphenq]]
- [[context-engineering-delete-audit-free-ai-guides]]
- [[managed-deep-agents-harrison-chase]]
- [[15-claude-skills-that-stuck-vaibhav-sisinty]]
