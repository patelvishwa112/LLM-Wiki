---
tags:
- agents
- context-engineering
- harness-engineering
- agent-memory
- orchestration
- project-ideas
- claude-code
created: 2026-05-30
source: Claude Code DeepSeek V4 Pro research session
type: research-synthesis
related:
- '[[Llama SAE Interpretability Project]]'
- '[[Bookmarks Index]]'
description: Agent Systems & Context Engineering — Project Ideas (2026)
---

# Agent Systems & Context Engineering — Project Ideas (2026)

**Generated:** May 30, 2026 via Claude Code on DeepSeek V4 Pro
**Context:** Exploring buildable projects outside interpretability — agents, context engineering, harness engineering

## Three Tectonic Shifts Enabling These Projects

1. **Agent orchestration primitives matured.** Google A2A, OpenAI Symphony, Claude Code plugins/sub-agents. Gas Town proved 20-30 parallel Claude Code instances work. The question is *what* you orchestrate, not *how*.

2. **Context Engineering supplanted prompt engineering.** Anthropic's official framing + (S)AGE findings: 3-line prompts + memory = 200-line expert prompts. Agent failures are context failures, not model failures. The context window is a constrained memory space needing systematic optimization.

3. **Memory systems crossed the usefulness threshold.** RecMem: recurrence-based consolidation cuts tokens 87% while beating SOTA. MemMachine: 93% on LongMemEval with ~80% fewer tokens. Delta-Mem: persistent working memory at 0.12% of model parameters.

---

## Four Project Proposals

### 1. Agent Git — Versioned, Branching Memory for Coding Agents

**Problem:** Claude Code memory (CLAUDE.md + memory/) is flat, append-only, session-scoped. Agents forget across sessions, can't experiment with different memory.

**Approach:** SQLite + SQLite-vec for hybrid structured/semantic storage. Git-like branching memory. RecMem-style recurrence consolidation. Claude Code hook on SessionEnd. Three memory tiers: Episodic (compressed summaries), Semantic (vector-stored patterns), Preference (stable facts).

**Why now:** RecMem (ACL 2026) proved recurrence consolidation works. Claude Code hooks intercept session lifecycle. SQLite-vec makes local vector search zero-infra.

**Novelty:** All existing memory systems target conversational agents, not coding agents. The branching model (git-like memory namespaces) is entirely new.

**Time:** 2-3 weeks | **Risk:** Medium | **Cost:** Low

### 2. Context Compiler — LLM-as-Compiler for Agent Prompt Construction

**Problem:** Every agent run starts with hand-tuned prompts. Layout, ordering, and token allocation significantly affect performance (structured layouts beat unstructured by 10-20%). No tool optimizes this systematically.

**Approach:** Task description + tool manifest + memory store → optimized context window with explicit sections, token budgets, retrieval plan, model-specific layout. FoT-style dynamic reasoning graphs for information placement. Model-specific calibration (Sonnet vs Opus attention patterns).

**Why now:** Context engineering paradigm is well-defined. Framework of Thoughts (Feb 2026) provides graph-based optimization. MCP standardizes tool definitions.

**Novelty:** Treats context window as constrained memory and applies compiler design — register allocation → token allocation, instruction scheduling → section ordering, dead code elimination → redundancy removal.

**Time:** 3-4 weeks | **Risk:** High | **Cost:** Medium

### 3. Agent Worktree — Lightweight Parallel Agent Orchestration

**Problem:** Gas Town runs 20-30 parallel Claude Code instances but is "100% vibe coded" with complex infrastructure. No simple way to "spin up 3 agents for 3 tickets in parallel, isolated, and merge."

**Approach:** git worktree for filesystem isolation. SQLite task queue with dependencies. Claude Code CLI as workers. S-Bus style read-set tracking for merge conflict prediction. Coordinator agent (Hermes or thin Python) for decomposition, monitoring, merging.

**Why now:** Claude Code plugin/hook system is mature. S-Bus (May 2026) proved read-set tracking prevents agent conflicts. Git worktree is battle-tested isolation.

**Novelty:** Git-native approach vs Gas Town's monolithic complexity or Symphony's Elixir+Linear requirement. Read-set tracking for merge conflict prediction is novel.

**Time:** 2-3 weeks | **Risk:** Medium | **Cost:** High ($25-50/hr)

### 4. Semantic Watchdog — Harness-Level Correctness Gating

**Problem:** 63% of developers rarely let agents run fully autonomous (Stack Overflow May 2026). Bottleneck is trust. Generation scales effortlessly; validation doesn't.

**Approach:** Claude Code PostToolUse hook after every file modification. Multi-signal verification: structural (lint/type check), behavioral (relevant tests), semantic (Haiku diff analysis). Confidence scoring 0-100. Three-tier gating: ≥85 auto-commit, 50-84 flag for review, <50 auto-reject with feedback.

**Why now:** Claude Code hooks intercept every tool call. Haiku is cheap enough for per-change analysis (~$0.01/diff). Harness engineering provides conceptual framework.

**Novelty:** Existing CI/CD runs after commit. This runs *before* commit, in the agent's inner loop, with LLM-based semantic analysis. Learning component adapts to repo-specific failure modes.

**Time:** 1-2 weeks | **Risk:** Low | **Cost:** Low

---

## Comparison & Recommended Order

| | Agent Git | Context Compiler | Agent Worktree | Semantic Watchdog |
|---|---|---|---|---|
| **Domain** | Memory + Harness | Context Engineering | Orchestration | Verification |
| **Time** | 2-3 weeks | 3-4 weeks | 2-3 weeks | 1-2 weeks |
| **Novelty** | High | High | Medium-High | Medium |
| **Risk** | Medium | High | Medium | Low |
| **Cost** | Low | Medium | High | Low |

**Recommended path:** Semantic Watchdog (week 1, quick win) → Agent Git (weeks 2-3, builds on hook infra) → Agent Worktree or Context Compiler.

The projects compose: Agent Git provides memory for Worktree's coordinator; Watchdog verifies Worktree's parallel output; Context Compiler optimizes prompts for all agents.
