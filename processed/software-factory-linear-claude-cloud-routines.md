---
type: bookmark
description: "Pierson Marks' afternoon-build software factory — Linear as hub, Claude Code Cloud Routines for pre-triage loops (PostHog/Vercel/Stripe), webhook-triggered SDLC via auto label and /do skill."
tags:
  - agents
  - software-factory
  - loop-engineering
  - claude-code
  - linear
  - mcp
  - agent-harness
  - human-in-the-loop
  - cronjob
  - product
  - observability
source: https://x.com/piersonmarks/status/2075361336381555096
date: 2026-07-09
author: Pierson Marks (@piersonmarks)
summary: "Split pre-triage (scheduled MCP loops into Linear) from implementation (Linear auto label → Hono webhook → Claude routine + /do skill); runs on Claude subscription without VPS babysitting."
raw: "[[raw/piersonmarks_2075361336381555096]]"
---

# Software factory on Linear + Claude Cloud Routines

Pierson Marks (Jellypod) documents a **software factory** built to stay simple, fit existing habits, and run on an existing **Claude** subscription — not a bespoke VPS stack.

## Architecture

**Linear** is the source of truth. Two phases with explicit seams:

1. **Pre-triage** — discover/create work (humans, agents, APIs) → issues in Linear.
2. **Implementation** — SDLC agent completes issues.

Pipeline: create work (loops + MCP) → store work (Linear) → complete work (agent).

Build pre-triage first; avoid one-shot over-engineering both sides.

## Pre-triage loops (Claude Code Cloud Routines)

Scheduled routines (not self-hosted always-on hardware):

- **System health** (daily 5am) — PostHog errors, Vercel diagnostics → Linear issues.
- **UX / feedback** (weekly Mon 9am) — Intercom/Fin, PostHog **session replays** (rage clicks, confusion).
- **Churn** (daily 6am) — Stripe cancelers + replays + Supabase usage → Slack report + prioritized Linear issues.

**Why Cloud Routines:** schedule/webhook triggers, parity with local Claude, **MCP via Desktop connectors** shared with cloud sessions, parallel runs without laptop RAM. Prompts are portable text.

Value exists even if implementation stays manual — start with one loop.

## Implementation (Linear → Claude)

Avoid being the manual kickoff bottleneck:

- Add **`auto`** label on a Linear issue.
- Webhook → internal **Hono** API (auth headers) → POST triggers **Claude routine**.
- Reusable **`/do` or `/implement` skill** — fetch issue, implement, browser verify (Playwright), PR, watch comments.
- Pre-triage issues usually **omit** `auto` (human adds label); agents can add `auto` when trusted.

Routine prompt waits for `<routine-fire-payload>` follow-up with issue id; comments on Linear as `[Claude]`, status In Progress.

Alternative: scheduled routine polls for `auto` issues not in progress.

## Why it matters

Observable factory on subscription billing: pre-triage feeds the tracker you already use; implementation scales via labels and webhooks. Session-replay-driven triage is a concrete ops pattern; **human-in-the-loop** stays one label away.

## Related

- [[four-loops-ai-engineering-taxonomy-aparna]]
- [[how-to-create-loops-claude-code-sairahul1]]
- [[human-in-the-loop-agent-loops]]
- [[sierra-pinecone-singular-company-agent]]
- [[spec-kit-github-sdd]]