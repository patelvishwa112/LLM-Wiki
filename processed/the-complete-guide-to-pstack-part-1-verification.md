---
tags:
  - verification
  - agent-harness
  - harness-engineering
  - skills
  - claude-code
  - pstack
  - controls
  - parallelism
  - code-quality
  - agent-ops
  - grok-bot
source: https://x.com/poteto/status/2094457600259842065
date: 2026-08-31
author: lauren (@poteto)
type: bookmark
description: "pstack Pt. 1 — verification is the infrastructure skill: give the agent a CLI that drives and inspects your app, a feature map, and cloud parallelism; then it can close the loop without you. 2,462 PRs landed in August."
summary: "Verification is critical infrastructure, not just a skill: an agent-owned CLI (control-atlas) plus a searchable feature map lets agents verify their own work, which is what makes high-volume, high-quality PR output possible."
raw: "[[raw/poteto_2094457600259842065]]"
status: current
as_of: 2026-08-31
---

# The Complete Guide to pstack Pt. 1 — Verification Is All You Need

Lauren Tan (Grok Bot at xAI, previously Cursor / React Compiler / Meta / Netflix) describes pstack, her personal skills stack for "rigorous engineering work". Reported outcome: **2,462 PRs landed in production in August**, while she acts as the codebase's gardener — refactoring, adding lints and checks, and holding quality as the team grew.

Her reframe of PR count is the interesting bit: before agents, volume was a vanity metric. It only becomes a real signal when quality holds *and* the volume is what lets you keep refactoring foundations under a fast-growing codebase.

## The claim: verification is infrastructure

> "If an agent can't verify its own work, nothing else matters. You remain the bottleneck."

So treat the verification skill like critical infrastructure, not a prompt. A good one amplifies the whole team, including non-engineers, because anyone can validate that their change actually works.

## How to build one

1. Install pstack, run `/create-verification-skill`. It is a **meta-skill**: it teaches the agent to build a verification skill for your specific app, distilled from the ones used on Grok Bot and Cursor.
2. Pick a debuggable stack. Electron/web → Chrome DevTools Protocol; iOS → simulator. You want the agent to have the same interact/debug/perf tooling you would use by hand. Her strong opinion: it is worth choosing a stack (or building debug tooling) that gives agents an unfair advantage — an undebuggable stack makes agents unproductive.
3. **"Build the Lever"** — give agents *tools*, not markdown. For verification that means a small CLI, e.g. `control-atlas.mjs`:
   - health/state: `doctor`, `cleanup`, `watch --restart`
   - navigation: `new-session`, `select-project`, `home`, `scroll`
   - interaction: `send`, `click`, `click-xy`, `aria-click`, `type`, `press`, `eval`, `feature-flag`
   - inspection: `snapshot`, `screenshot`, `components`, `console`, `network-log`
   - perf: `trace`, `profile`, `record`, `perf-metrics`, `wait-settle`
   Fewer tokens than writing throwaway scripts, and reproducible/testable.
4. Make the dev experience agent-grade: seedable dev database, test users/auth, API calls against staging, one-command environment bring-up. You needed this anyway; now it is the agent's primary utility.
5. CLI design rules she calls out: composable, deep-module API; `--dry-run` on anything destructive; subcommands for progressive disclosure; descriptive errors that say what to do instead; rich `--help`; JSON output.

## Parallelism: cloud agents, not worktrees

Worktrees are her explicit anti-pattern — storage and resource heavy, and maybe ~10 parallel agents before the machine complains. Cloud agents (Cursor) get a real computer, can install deps, run the app, record video/screenshots; snapshotting the first build makes later runs fast. `/swarm` then fans out N cloud agents running the verification skill — useful to confirm a perf win with a real sample size, or fuzz for regressions.

## Feature Maps

As an app grows the agent cannot guess where features live. A **Feature Map** is a searchable set of markdown files (created under `references/features/` with a README index) describing each feature, what it does, and how a user reaches it — including the commands to drive it and known gotchas. Cheapest way to keep agents effective in a large UI.

## Daily usage pattern

- Prefix work with `/poteto-mode`; in Cursor `Opt+Enter` pins it as a Custom Mode so the reminder persists every turn.
- The load-bearing prompt shape: **"use /control-app to verify your changes and show me a video and screenshots as proof"**. Ask for evidence, not a claim of completion.
- In Grok Bot, spawn a cloud agent to do the work so the bot stays a coordinator with a clean context window.
- Wire the verification skill into routines/automations: every Slack/feedback report gets reproduced automatically; once the skill and Feature Map are good enough, optionally auto-fixed.
- Keep it sharp with `/maintain-verification-skill`; she suggests an on-call rotation for it.

## Verdict

The most convincing argument I have read for why "the agent must be able to run the thing" beats prompt cleverness. Two caveats: it is deeply tied to Grok Bot/Cursor cloud agents (`/swarm`, Custom Modes), and the 2,462 PR figure is self-reported with no quality metric attached beyond her own maintenance narrative. The transferable core is stack-agnostic: **build a CLI that lets the agent drive your app, plus a map of what it can drive.**

Part 2: [[the-complete-guide-to-pstack-part-2-supervising-planning]]

## Related

- [[agent-workflows-silent-degradation-verification-vladic]]
- [[feedback-loops-claude-code-less-babysitting]]
- [[why-harness-engineering-is-so-hard-winterarc]]
- [[learn-harness-engineering]]
- [[dark-arts-of-skill-engineering-pbakaus]]
- [[agent-harness-engineering-claude-14-step-roadmap]]
