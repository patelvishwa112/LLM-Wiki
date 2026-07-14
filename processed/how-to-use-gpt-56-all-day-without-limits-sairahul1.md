---
tags: ["codex", "gpt-5.6", "cost-optimization", "subagents", "agent-harness", "routing", "openai", "sol", "luna", "productivity"]
source: https://x.com/sairahul1/status/2076556282195329249
date: 2026-07-13
type: bookmark
description: "Rahul (@sairahul1) Codex Pro limit guide: avoid Ultra (parent-clone subagents); Sol Extra High + Sol Medium + Luna Extra High; max_depth=1; AGENTS.md no auto-spawn; explicit stop points."
author: sairahul1
summary: "Rahul (@sairahul1) Codex Pro limit guide: avoid Ultra (parent-clone subagents); Sol Extra High + Sol Medium + Luna Extra High; max_depth=1; AGENTS.md no auto-spawn; explicit stop points."
raw: "[[raw/sairahul1_2076556282195329249]]"
---

# How To Use GPT-5.6 All Day Without Hitting Limits — @sairahul1

Codex Pro ($200) 5-hour window often dies in ~90 min because **spawned subagents clone parent model + effort** — Sol Ultra on the parent becomes N× Ultra. No native child-model override on `spawn_agent`.

## Never: Ultra

Ultra multiplies into parallel sub-subagents. ~3.1 bench points over Extra High for ~3× cost; main coding Ultra results unpublished. Skip.

## Three-role routing

| Role | Model / effort | Job |
|------|----------------|-----|
| Orchestrator | **Sol Extra High** | Plan, architect, decide (~1 pt under Max, ~3× cheaper) |
| Executor | **Sol Medium** | Code, tests, implement (claims beat Fable 5 on long agent workflows ~¼ cost) |
| Scanner | **Luna Extra High** | Read-only search/explore (vs Terra: ~1.3× faster, ~2.5× cheaper) |

Alt continuous loop: Sol EH plan → Luna EH execute → Sol EH review. Reported 48h continuous with zero limit hits.

## Config levers

1. **AGENTS.md** — only spawn subagents when explicitly asked; no auto-spawn.
2. **Custom agents** under `~/.codex/agents/`: `fast_scan` (Luna EH, read-only), `routine_worker` (Sol Medium), `deep_worker` (Sol EH).
3. **`[agents]`** — `max_depth = 1` (no recursive spawn), `max_threads = 6`, routing policy for auto-delegation.
4. **Prompt stop points** — plan-only → confirm; implement → stop after PR; debug → diagnose before edits.
5. **Effort defaults** — High for most; Extra High for hard/security; Medium daily driver for implementation.

## Why it matters

Concrete harness-level cost control for OpenAI Codex: model/effort **routing + depth caps** beat “run Ultra everywhere.” Pairs with Fable-manager / Sol-worker role splits and Rahul’s loop/harness series.

## Related

- [[how-to-create-loops-claude-code-sairahul1]]
- [[harness-engineering-2026-discipline]]
- [[twenty-core-agent-concepts-sairahul1]]
- [[fable-manager-sol-worker-nateherk]]
- [[15-prompts-cut-coding-costs-88-percent]]
- [[how-to-build-conductor-multi-agent-leanxbt]]
