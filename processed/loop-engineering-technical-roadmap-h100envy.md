---
tags:
- loop-engineering
- agent-harness
- agents
- reward-hacking
- observability
- context-engineering
- claude-code
- production
- agent-ops
source: https://x.com/h100envy/status/2068987470960623783
date: 2026-06-22
type: bookmark
author: h100envy
summary: 'Step-by-step technical roadmap for autonomous agent loops: external deterministic
  checks, stateless iterations, narrow context budgets, anti-reward-hacking gates,
  disk state, isolation, and JSONL observability.'
raw: '[[raw/h100envy_2068987470960623783]]'
description: 'Step-by-step technical roadmap for autonomous agent loops: external
  deterministic checks, stateless iterations, narrow context budgets, anti-reward-hacking
  gates, disk state, isolation, and JSONL observability.'
---

# Loop Engineering: Technical Roadmap for Autonomous Loops

**Source:** [X Article by @h100envy](https://x.com/h100envy/status/2068987470960623783)

## Summary

@h100envy argues that agent skill ceilings are set by **loops that converge** (find work → act → verify → repeat), not by one-shot prompts. The article is a strict ordered playbook: only automate tasks with a **machine oracle** (tests/lint/build) that is deterministic and idempotent; baseline a manual green run with token/call metrics; run a **stateless** while-loop (fresh agent context each iteration, state on git/disk) to fight context rot; assemble **narrow per-iteration context** (failure slice + stack-trace/diff files + hard token budget); block **reward hacking** (test-diff gate + optional cross-model reviewer); persist **STATUS.md + `.loop_state.json`**; isolate via **worktree + container** (`--network none`); add **brakes + JSONL logs** (heartbeat, repeat detector, budget cap); and estimate cost as linear in iterations only if context stays bounded.

## Why It Matters

This vault already tracks loop/harness content (`[[wtf-is-a-loop]]`, `[[loop-engineering-14-step-roadmap]]`); this piece is unusually **implementation-heavy** (bash snippets for loop shell, `build_context.sh`, reward-hack gate, docker sandbox, JSONL schema). It names failure modes (runaway, silent death, random walk, understanding debt) and ties each to log signatures—directly applicable to Hermes `/goal`, cron jobs, and Claude Code overnight runs.

## Key Steps (compressed)

| Step | Idea |
|------|------|
| 0 | External exit-code oracle; no self-grading; de-flake checks first |
| 1 | One measured manual green path before automation |
| 2 | Stateless `while` + `MAX_ITER`; progress on disk not in chat |
| 2.5 | `.loop_context.md` from failure + trace + last diff; token ceiling |
| 3 | Test immutability gate; adversarial reviewer on another model |
| 4 | Human STATUS + machine JSON state protocol |
| 5 | Worktree + container blast radius; no network |
| 6 | JSONL observability + heartbeat + stuck/repeat detection |
| 7 | Cost model: avoid quadratic context growth |

## Related

- [[wtf-is-a-loop]]
- [[loop-engineering-14-step-roadmap]]
- [[feedback-loops-claude-code-less-babysitting]]
- [[your-agent-harness-should-repair-itself]]
- [[loop-driven-development]]
- [[harness-engineering-2026-discipline]]