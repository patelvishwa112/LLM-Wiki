---
tags:
  - agentic-engineering
  - agents
  - agent-harness
  - harness-engineering
  - multi-agent
  - claude-code
  - skills
  - agent-memory
  - productivity
  - agent-ops
  - devin
source: https://x.com/aashatwt/status/2077428487779148061
date: 2026-07-15
type: bookmark
description: "Aasha notes on Kun's agentic engineer workflow — manager mindset, parallel Claude/Devin, memory over prompts, tmux/neovim environment."
author: aashatwt
summary: "Aasha notes on Kun's agentic engineer workflow — manager mindset, parallel Claude/Devin, memory over prompts, tmux/neovim environment."
raw: "[[raw/aashatwt_2077428487779148061]]"
---

# THE AGENTIC ENGINEER WORKFLOW

@aashatwt — notes and takeaways from Kun (ex principal eng at Microsoft, Meta, Atlassian; claimed 40–50 production PRs/day with AI agents). Thesis: **agentic engineering** is managing a team of agents, not coaxing one model to write snippets.

## Not agentic engineering

- Cursor autocomplete on a function
- "Claude, build a landing page"
- Full-day prompt thrash without systems

## Mindset shift

| Default | Agentic |
|---------|---------|
| How do I get AI to write this code? | How do I manage a team of agents so they build this for me? |

Engineering manager moves: clarify task, review work, keep quality high, fix **onboarding** when agents repeat mistakes — not blame the model.

**Build the system before you build the product.** Optimize environment around models more than model choice.

## Three capability pillars (from Kun)

1. **Parallel AI engineers** — multiple Claude Code sessions at different effort levels; git worktrees to avoid conflicts; Devin (or similar) for long-running ownership
2. **Workflow that scales** — `/compact` vs `/clear`, fight context drift, keep agents productive across long sessions
3. **Better code from AI** — "smell" command, clean-code/design patterns; MCP / bash / skills for external services

## Environment stack highlighted

- **tmux** — multi-session terminal
- **Neovim** — keyboard-first editing
- **Memory files** — how the author likes to work
- **Skills** — task-specific procedures

## Agents as new employees

Each new Claude session ≈ a new hire who can code but does not know the company, project, or style. Onboard with:

- Global memory files
- Project memory files
- Skills
- Coding conventions
- Testing instructions

**Memory > prompting.** A good prompt solves one problem; good memory solves the next N. Mentioned helpers: context.dev, supermemory, markdown memory in-repo.

## Plan first

Discuss options, UI, edge cases before implementation. Strong plan → boring implementation (desired).

## Parallel autonomous workers

Devin framed as background autonomous SWE (read codebase, implement, bug hunt, open PRs, iterate on feedback) while the human does planning, users, review. Assign responsibilities across agents rather than one chat doing everything. Pointer to @imjaredz multi-Devin video.

## Tooling / repos listed

tmux, vercel-labs skills CLI, OpenSuperWhisper, lavish, no-mistakes, gnhf, treehouse, firstmate (Kun-adjacent), plus skills packs (frontend-slides, emilkowalski, mattpocock, davidondrej).

## Why it matters

Compresses the "100x agentic engineer" idea into an operational checklist: manager role, environment + memory layer, worktrees/parallelism, and plan-before-code. Pairs with preference/harness notes and multi-agent orchestration bookmarks in the vault.

## Related

- [[hundred-x-agentic-engineer-preferences-systematicls]]
- [[every-agentic-engineering-hack-june-2026]]
- [[fable-manager-sol-worker-nateherk]]
- [[from-1-agent-to-swarm-orchestration-roadmap]]
- [[learn-harness-engineering]]
- [[how-to-build-agent-that-never-forgets]]
- [[the-great-flattening-tokenmaxx-vorflux-myprasanna]]
