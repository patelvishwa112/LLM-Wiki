---
tags: ["agents", "multi-agent", "orchestration", "claude-code", "subagents", "worktrees", "verification", "agent-harness", "loop-engineering"]
source: https://x.com/0xmorlex/status/2070079645148451263
date: 2026-06-25
type: bookmark
author: 0xmorlex
summary: "Claude Code–focused roadmap from one reliable agent loop to a swarm: orchestrator plus isolated subagent workers, git worktrees for parallel edits, independent verifiers per lane, workflows for composition, shared claim-and-record state, cost routing by role, and structural guardrails instead of human supervision."
raw: "[[raw/0xmorlex_2070079645148451263]]"
---

# From 1 agent to a swarm: orchestration roadmap

**Author:** @0xMorlex (X Article)

## Core thesis

A swarm multiplies whatever you point at it — clear goals become throughput; vague goals become parallel failure. The skill is **orchestration** (lanes, shared stop condition, collision avoidance, independent QC), not headcount. Default to one agent in a tight loop; swarm only for embarrassingly parallel work or perspectives that pollute a single context.

## Three tiers (10 moves)

| Tier | Moves | Idea |
|------|-------|------|
| **Decide** | 1–3 | Restrain; one orchestrator + many narrow workers; subagents with minimal tools |
| **Run** | 4–7 | Worktree isolation; verifier per lane; workflows; single `/goal` owned by orchestrator |
| **Scale** | 8–10 | Shared state (claim/record); model routing by role; deny hooks + logging |

## Why it matters

- Operational counterpart to vault notes on loops, dynamic workflows, and Kimi-scale swarms — emphasizes **Claude Code primitives** (/agents, worktrees, workflows, /goal, permissions, hooks).
- Names the highest-leverage role: **independent verifier** (fresh context, adversarial to worker output).
- Explicit failure catalog matches production agent-ops (self-grading, no orchestrator, merge collisions, one expensive model everywhere).

## Key quote

> The leverage was never in the headcount of agents. It was in how well you orchestrated them.

## Related

- [[loop-engineering-14-step-roadmap]]
- [[9-step-loop-claude-code-senior-engineer]]
- [[dynamic-workflows-where-plan-lives]]
- [[claude-subagents-vs-agent-teams]]
- [[how-to-build-ai-agent-swarms]]
- [[feedback-loops-claude-code-less-babysitting]]