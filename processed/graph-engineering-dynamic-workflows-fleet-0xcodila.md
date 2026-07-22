---
tags: ["agents", "multi-agent", "orchestration", "claude-code", "dynamic-workflows", "loop-engineering", "verification", "agent-harness", "harness-engineering", "parallelism", "cost-optimization", "worktrees"]
source: https://x.com/0xcodila/status/2079597821511020996
date: 2026-07-21
type: bookmark
description: "0xCodila graph engineering guide: real edges vs fake waits, Claude Code dynamic workflows fleets, fresh-context verifiers, isolation, Bun-scale costs, when not to graph."
author: 0xcodila
summary: "0xCodila graph engineering guide: real edges vs fake waits, Claude Code dynamic workflows fleets, fresh-context verifiers, isolation, Bun-scale costs, when not to graph."
raw: "[[raw/0xcodila_2079597821511020996]]"
---

# Graph engineering — fleets over linear agents (0xCodila)

Successor framing to **Loop Engineering**: a single try→check→adjust loop is the atom, but loops alone hit **Goodhart** (optimize the metric, miss the goal). The next shape is a **graph of loops** — nodes think, edges carry results; cycles watch and correct each other. Claude Code **dynamic workflows** are the shipping tool for drawing that shape instead of one linear agent.

Thesis: multi-step agents feel slow not only from model weakness but from drawing a **line** where the work was a **graph** — fake waits fill context and drop goals.

## Core moves

1. **See real edges** — Node = one job/agent/IO. Edge = true data dependency. For every "and then," ask if the next step *reads* prior output. No data → parallel. Linear A→B→C is already a graph — the saddest chain (C stalls → D never runs).

2. **Build a first fleet (CC v2.1.154+)** — Paid plan; Pro enables Dynamic workflows in `/config`. Prompt on a real repo → "Dynamic workflow requested" → approve JS orchestration → `/workflows` for scope/fan-out/verify/synthesize → one synthesized report (intermediates in script vars, not chat context). Save good runs (`s` → `~/.claude/workflows`). Coordination is cheap vs chat handoff; **agent work still burns tokens** — start scoped (e.g. max 20).

3. **Ceiling** — Up to ~1000 agents fan-out, ~16 concurrent waves. Jobs no single context can hold (full-codebase audit, migration, multi-angle search).

## What breaks

- **Self-agreeing graph** — Same-context "verifiers" are loops in costume. Verifier must be a **fresh node**, own context, **real signal** (tests pass), not "agent said done."
- **Workers collide** — Bun port ops failure: shared git/workspace overwrites. Structural fix: forbid unsafe shared commands, **isolated worktrees**, explicit merge + disagreement rules. Plan *where each agent works / how results merge / conflict* before fan-out.

## Six starter graphs

Security sweep + verifier; cited multi-angle research with mutual refutation; module port with test gates; size-routed adversarial review; scheduled re-runnable scans; open discovery until two quiet rounds.

## Ceiling case + honesty anchors

Simon Willison on Bun Zig→Rust: ~50 workflows, peak 64 parallel, ~535k Zig → 1M+ Rust in 11 days, **~$165k** usage, heavy human design/monitoring, reviewability debate. Scale is real; so are cost and supervision.

Anchors topology can't fake: tests that **did** pass; evidence verifiers; **frozen rules** agents cannot weaken.

## When *not* to graph

Small/isolated edits; need step-by-step human approval; still exploring problem shape; true sequential dependence (no two independent boxes). If Step 1 finds no parallel edges, stay on a loop.

## Shift

Prompter asks more of one agent; **architect** draws nodes/edges: fan out independence, gate confidence edges, freeze truth nodes.

## Why it matters

Operator companion to [[graph-engineering-14-step-roadmap-0xcodez]] and [[loops-vs-graphs-polygres-infinite-context-daleverett]] — emphasizes **fake edges**, fresh-context verification, worktree isolation, and explicit anti-graph cases. Directly relevant to Claude Code dynamic workflows and Hermes-style multi-agent width limits.

## Related

- [[graph-engineering-14-step-roadmap-0xcodez]]
- [[loops-vs-graphs-polygres-infinite-context-daleverett]]
- [[loop-engineering-14-step-roadmap]]
- [[loop-engineering-clearly-explained]]
- [[how-to-build-conductor-multi-agent-leanxbt]]
- [[Dynamic Workflows in Claude Code]]
- [[from-1-agent-to-swarm-orchestration-roadmap]]
- [[agent-workflows-silent-degradation-verification-vladic]]
- [[software-factories-light-and-dark-addy-osmani]]
