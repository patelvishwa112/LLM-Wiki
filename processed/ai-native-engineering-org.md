---
tags:
  - anthropic
  - claude-code
  - engineering-management
  - productivity
  - team-structure
  - code-review
  - ai-native
source: https://claude.com/blog/running-an-ai-native-engineering-org
date: 2026-06-03
author: Fiona Fung (Anthropic, Director of Engineering for Claude Code & Claude Cowork)
type: bookmark
summary: "How the Claude Code team restructured for AI-native engineering. Four broken norms: JIT planning replaces roadmaps, ask Claude instead of authors, humans review only domain expertise (Claude handles style/bugs/tests), roles blur (PMs code, engineers design). Three core principles: dogfood, flat team, kill obsolete processes. Three metrics: onboarding ramp, PR cycle time, Claude-assisted commits (100%)."
related:
  - "[[anthropic-claude-code-skills-lessons]]"
  - "[[harness-engineering-2026-discipline]]"
---

# Running an AI-Native Engineering Org

**Source:** Fiona Fung, Director of Engineering for Claude Code & Claude Cowork at Anthropic. Code w/ Claude SF 2026.

## The Bottleneck Shift

Writing code, tests, and refactoring are no longer the bottleneck. **Verification, code review, and security** took their place.

## Four Broken Norms

| Norm | Before | After |
|------|--------|-------|
| **Planning** | 6-month roadmaps, design docs | JIT: prototype → internal users → feedback. Discussions in PRs. |
| **Context** | Find the author, ask them | Ask Claude first. Then ask: can this be automated? |
| **Code Review** | Humans review everything | Claude: style, bugs, tests. Humans: legal, security, product taste. |
| **Team** | Fixed roles | Blur: PMs code, engineers design. Hire builders + systems experts. |

## Core Principles

1. **Dogfood relentlessly** — everyone uses Claude Code and Cowork
2. **Flat team** — managers start as ICs, ship real code
3. **Kill obsolete processes** — explicit permission to question and remove

## Metrics

- Onboarding: engineers ship code in week one
- PR cycle time: dropping, but watch where CI/buildunder strain
- Claude-assisted commits: 100%. "I don't think I've seen a non-Claude-assisted commit in four months."

## Key Insight

> Don't confuse throughput with success. Throughput is one metric. The real metric is measuring the thing you're trying to solve.

Start by picking your noisiest workflow and asking: is it still serving its purpose? If so, can it be automated?
