---
tags:
  - agents
  - agent-harness
  - harness-engineering
  - agent-architecture
  - claude-code
  - openai
  - anthropic
  - thoughtworks
  - context-management
  - feedback-loops
  - agent-ops
  - cost-optimization
source: https://x.com/sairahul1/status/2063544956158185927
raw: "[[raw/sairahul1_2063544956158185927]]"
date: 2026-06-07
author: Rahul (@sairahul1)
type: bookmark
summary: "Harness Engineering emerged as a discipline in 2026. The core formula: Agent = Model + Harness. Covers the 5 harness artifacts (AGENT.md, JSON feature lists, session routines, sprint contracts, task templates), the 3 camps (OpenAI environment-first, Anthropic doer-vs-judge, ThoughtWorks 2x2 framework), 5 universal principles, and the paradox of harness decay — build to delete. Same model + better harness = +13% performance. Full harness 22x cost but working software vs broken demo."
related:
  - "[[agent-harness-engineering-agentforge]]"
  - "[[harness-is-the-product-context-aware-agents]]"
  - "[[claude-code-changed-what-agents-look-like]]"
  - "[[agent-memory-landscape-2026]]"
---

# Harness Engineering — What Every AI Engineer Needs to Know in 2026

**Source:** Rahul (@sairahul1). 115K views, 491 bookmarks. A new engineering discipline materialized in 90 days.

## Core Definition

> **Agent = Model + Harness**

The harness is everything that isn't the model: constraints, feedback loops, documentation, tool permissions. The OS analogy: Model = CPU, Context window = RAM, Harness = OS, Agent = Application.

## The 5 Harness Artifacts

| Artifact | Function |
|----------|----------|
| **AGENT.md / CLAUDE.md** | Onboarding docs distributed throughout the codebase |
| **JSON Feature Lists** | Progress tracker — agents are less likely to overwrite JSON than Markdown |
| **Session Init Routines** | 7-step boot sequence run identically every session |
| **Sprint Contracts** | Generator + Evaluator agents negotiate before coding begins |
| **Structured Task Templates** | Grounded impact map with real file paths, symbol names, patterns |

## The Three Camps

### OpenAI: Environment-First
Design the environment so thoroughly agents produce reviewable output in the first place. Strict dependency flows, AGENT.md throughout, agents wired into CI/CD. Sora Android: 4 engineers, 28 days, #1 Play Store, 99.9% crash-free. Codex: 70% of internal PRs.

### Anthropic: Separate Doer from Judge
Three specialized agents — Planner, Generator, Evaluator. Self-evaluation fails because agents give themselves straight A's. Making a standalone evaluator skeptical is easier than making a generator critical of its own work.

### ThoughtWorks: The 2×2 Framework
Classify every harness control on two axes:
- **When:** Feedforward (guides, before action) vs Feedback (sensors, after action)
- **How:** Computational (deterministic, ms) vs Inferential (LLM-powered, seconds)

Neither feedforward nor feedback alone works.

## The 5 Universal Principles

1. **Context Beats Instructions** — Show the agent the current state vs telling it abstractly
2. **Planning and Execution Must Be Separated** — Combined in same pass = unreliable output
3. **Feedback Loops Are Non-Negotiable** — Without feedback, it's just a prompt with extra steps
4. **One Thing at a Time** — Forced incrementalism: read → pick ONE → implement → commit → repeat
5. **The Codebase IS the Documentation** — No separate KB. Repo is single source of truth

## The Paradox: Build to Delete

**Harness decay:** Every harness component encodes an assumption about what the model can't do. As models improve, those assumptions expire.

- Opus 4.5 → 4.6: sprint decomposition became dead weight (38% cost savings)
- Opus 4.7: evaluator role started shrinking as model self-verified

**Build to delete:** Design every harness component to be removable. Test by turning it off. If quality doesn't change → delete. Carrying dead components costs tokens on every run with zero extra quality.

## Cost Reality

| Setup | Cost | Time | Result |
|-------|------|------|--------|
| Solo agent (no harness) | $9 | 20 min | Working UI, broken core |
| Full harness | $200 → $124 | 6 hours | Working software, polished UI |

**Trend line:** Better model = simpler harness = cheaper run = faster output. The engineers winning design the best constraints — and throw them away the moment they stop earning their keep.
