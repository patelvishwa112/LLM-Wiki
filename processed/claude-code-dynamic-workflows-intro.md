---
tags:
  - claude-code
  - anthropic
  - agents
  - multi-agent
  - orchestration
  - parallelism
  - agent-ops
source: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
raw: "[[raw/anthropic-dynamic-workflows-claude-code]]"
date: 2026-05-28
author: Anthropic
type: bookmark
summary: "Dynamic workflows in Claude Code: Claude autonomously writes orchestration scripts that fan out tens to hundreds of parallel subagents, checks its own work, and iterates until answers converge. Use cases: codebase-wide bug hunts, large migrations, security audits, adversarial verification. Bun was ported from Zig to Rust (750K lines, 99.8% test pass) in 11 days using dynamic workflows. Available in research preview on Max/Team/Enterprise plans."
related:
  - "[[kimi-k2.6-agent-swarm-300-parallel-agents]]"
  - "[[harness-engineering-2026-discipline]]"
---

# Dynamic Workflows in Claude Code

**Source:** Anthropic, May 2026. Research preview available in Claude Code CLI, Desktop, VS Code extension, and API.

## What It Is

Claude dynamically writes orchestration scripts that spawn tens to hundreds of parallel subagents in a single session. Subagents work from independent angles, adversarial agents try to refute findings, and the run iterates until answers converge. Progress is saved continuously — interrupted jobs resume where they left off.

## Use Cases

| Category | Description |
|----------|-------------|
| **Codebase-wide bug hunts** | Parallel search across a service/repo, independent verification on every finding |
| **Security audits** | Auth checks, input validation, unsafe patterns — parallel + verified |
| **Large migrations** | Framework swaps, API deprecations, language ports spanning thousands of files |
| **Adversarial verification** | Independent agents try to break the result before you see it. For high-stakes work. |
| **Profiler-guided optimization** | Parallel performance analysis and fix proposals |

## Bun Rewrite: Zig → Rust

- **Scope:** ~750,000 lines of Rust, 99.8% test suite pass rate
- **Time:** 11 days from first commit to merge
- **How:** One workflow mapped Rust lifetimes for every Zig struct field. Next wrote every `.rs` file as behavior-identical port of `.zig`. Hundreds of agents in parallel, two reviewers per file. Fix loop drove build + test suite until clean. Overnight workflow addressed unnecessary data copies and opened PRs for each.

## Mechanics

| Mechanism | Detail |
|-----------|--------|
| **Planning** | Claude breaks task into subtasks based on prompt |
| **Fan-out** | Subagents run in parallel |
| **Verification** | Results checked before folding in; adversarial agents refute |
| **Iteration** | Run continues until answers converge |
| **Persistence** | Progress saved as you go; interrupted jobs resume |
| **Coordination** | Happens outside the conversation — plan stays on track |

## Access

| Plan | Availability |
|------|-------------|
| Max / Team | On by default |
| Enterprise | Off by default (admin can enable) |
| API | Available on Claude API, Bedrock, Vertex AI, Microsoft Foundry |

## Usage Notes

- **Token consumption:** Can be substantially higher than a typical Claude Code session. Start with scoped tasks.
- **Activation:** Ask Claude to "create a workflow" or enable **ultracode** (effort menu → xhigh; lets Claude decide when to use workflows automatically).
- **Confirmation:** First time a workflow triggers, Claude Code shows what's about to run and asks for confirmation.

## Key Insight

> Work that would normally take quarters finishes in days. A single pass by a single agent isn't enough for the hardest problems — parallel subagents, independent verification, and adversarial checking converge on answers no single pass can reach.
