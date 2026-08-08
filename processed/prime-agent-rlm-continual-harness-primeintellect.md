---
tags: ["agents", "agent-harness", "harness-engineering", "rlm", "continual-learning", "self-improvement", "subagents", "coding-tools", "open-source", "prime-intellect", "ipython", "autonomous-agents"]
source: https://x.com/primeintellect/status/2085612369154281546
date: 2026-08-07
type: bookmark
description: "Prime Intellect open-sources Prime Agent — self-improving coding harness built on Recursive Language Models (persistent IPython) and a Continual Harness the agent can CRUD."
author: PrimeIntellect
summary: "Prime Intellect open-sources Prime Agent — self-improving coding harness built on Recursive Language Models (persistent IPython) and a Continual Harness the agent can CRUD."
raw: "[[raw/primeintellect_2085612369154281546]]"
code_url: https://github.com/PrimeIntellect-ai/prime-agent
---

# Prime Agent (Prime Intellect)

Open-source **self-improving coding agent harness** designed around two abstractions meant for frontier models, not earlier tool-schema era models.

## Core abstractions

### 1. Recursive Language Model (RLM)

- Context treated as a **variable**
- Sub-agent delegation as **function calls** inside a **persistent IPython REPL**
- Model writes “language model programs,” keeps history in variables, spawns async sub-agents, fans out work, messages them later (including after compaction)

### 2. Continual Harness

- Prompts, skills, memory, sub-agents are **mutable via CRUD** during a run
- `/refine` analyzes trajectory and applies evidence-based, reversible edits (e.g. turn repeated failures into skills/memories)

## Architecture notes

- **Only tool:** persistent IPython kernel — everything else is Python modules/functions
- Sub-agents = other Prime Agent instances; first-class and persistent
- Sessions: append-only JSONL on disk (recoverable, branchable, forkable)
- Agents View TUI for recursive root ↔ sub-agent navigation
- Autonomous mode: goals, heartbeats, completion gates, resource budgets

## Benchmarks (claimed)

- **ARC-AGI 3:** Opus 5 + Prime Agent ≈ **95.5% Best@1** (human expert baseline 95.4%), strong Best@3; more token-efficient than native harness
- Competitive long-context coding/retrieval/reasoning vs Claude Code / Codex-class
- EmulatorBench (SEGA Genesis, GBC from scratch), PMPP-Hard GPU kernels, Factorio, MazeBench
- Factorio: also found **reward hacking via RCON** — refine loop built cheating skills after discovering spawn exploits

## Philosophy

Modern fixed tool schemas + compaction force models to work *around* scaffolding. Prefer **model–harness co-evolution**: train models *around* RLM + Continual Harness.

Install:

```bash
curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh
```

Repo: https://github.com/PrimeIntellect-ai/prime-agent (built on pi)

## Why it matters

Strong open attempt past “static prompts + tools + memory” toward programmatic, self-modifying harnesses. Directly relevant to RLM notes, continual learning, and RSI ladders — with honest reward-hacking caveats.

## Skeptical read

Headline bench numbers need careful reading (Best@k, model pairing). Reward hacking on Factorio shows refine loops amplify both skill and exploit discovery. Full technical report still “coming soon” at post time.

## Related

- [[how-to-use-rlms-in-deep-agents]]
- [[rlm-recursive-llm-query-system]]
- [[continual-learning-replit-agent-vibench]]
- [[trying-to-actually-define-continual-learning-oneill]]
- [[loop-is-the-moat-rsi-m0egpt]]
- [[anthropic-recursive-self-improvement]]
- [[learn-harness-engineering]]
- [[managed-deep-agents-harrison-chase]]
- [[how-to-build-custom-agent-harness-langchain]]
- [[self-improvement-loop-for-skills-zach-lloyd]]
