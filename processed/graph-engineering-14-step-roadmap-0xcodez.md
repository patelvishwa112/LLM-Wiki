---
tags: ["agents", "multi-agent", "orchestration", "claude-code", "dynamic-workflows", "loop-engineering", "verification", "agent-harness", "harness-engineering", "subagents", "parallelism", "cost-optimization"]
source: https://x.com/0xcodez/status/2079165300625330317
date: 2026-07-20
type: bookmark
author: 0xcodez
title: "Graph engineering: 14-step roadmap from linear agents to graph fleets"
description: "0xCodez 14-step graph engineering roadmap: turn linear multi-step agents into Claude Code dynamic-workflow graphs with nodes/edges, diamond topology, verifiers, model tiering, and self-routing fleets."
summary: "0xCodez 14-step graph engineering roadmap: turn linear multi-step agents into Claude Code dynamic-workflow graphs with nodes/edges, diamond topology, verifiers, model tiering, and self-routing fleets."
raw: "[[raw/0xcodez_2079165300625330317]]"
---

# Graph engineering: 14-step roadmap from linear agents to graph fleets

## Why it matters

Sequel-shaped to the author's [[loop-engineering-14-step-roadmap]]: loops are cycles; **graphs** are the shape of multi-step work (what can run in parallel, what must wait, what verifies before it propagates). Claude Code **dynamic workflows** make the orchestration layer plain JavaScript — zero model tokens for coordination — so fleets scale past a single context window.

## Core shift

- A **prompt** is a sentence; a **loop** is a cycle; a **harness** is the floor.
- The **shape of the work** (ordering, concurrency, barriers) is a **graph**: nodes think, edges carry results.
- Linear "and then" scripts are degenerate graphs. Most waits are fake edges (no data dependency).

## 14 steps (condensed)

1. **Nodes = jobs, edges = data flow** — Edge only if the next step *reads* prior output.
2. **Linear script = chain graph** — Cut non-data arrows; widen into parallelizable structure.
3. **Node contracts** — Bounded I/O + JSON schema on `agent()` so validation retries at the tool layer.
4. **Edges as data contracts** — Name by shape; reduce/filter/dedupe in free JS, not another LLM turn.
5. **`parallel()` fan-out** — Concurrent subagents; barrier + null-on-throw + `.filter(Boolean)`; parent context stays thin.
6. **Fan-in barriers only when needed** — Cross-set dedupe/rank/early-exit yes; pure flatten no (use pipeline).
7. **Diamond topology** — Fan out → reduce (code) → synthesize (agent). Default serious-graph shape.
8. **Runtime routing** — JS `if`/`switch` on validated outputs; judgment in nodes, reliability on edges.
9. **Verifiers on edges** — Adversarial skeptics, perspective-diverse lenses, judge panels (Bun-port style).
10. **Failure isolation** — Tolerate missing fan-in inputs; worktrees only when parallel writers collide.
11. **Converging cycles** — Loop-until-dry; **dedupe against everything seen**, not only confirmed hits.
12. **Model tiering** — Cheap models on repetitive fan-out nodes; premium on merge/judgment.
13. **Topology = cost/latency** — Prefer `pipeline()` streaming; `parallel()` barriers only for true sync points.
14. **Self-routing** — Let Claude write the workflow script; save good runs to `.claude/workflows/` (`/deep-research` skeleton: scope → parallel search → fetch → adversarial verify → synthesize).

## Six starter graphs

Security route sweep; cited `/deep-research`; file-by-file module port with test gates; size-routed adversarial diff review; scheduled ecosystem scan; unknown-size discovery until dry.

## Skeptical read

- Substack CTA (`movez.substack.com`) at top — still high-signal taxonomy for Claude Code workflow primitives.
- "Zero token coordination" assumes dynamic-workflow JS orchestration is available and trusted; operational complexity (worktrees, schemas, null-tolerant fan-in) is real engineering, not free.
- Claims about production Bun-port adversarial review are anecdotal without linked postmortem detail in-article.

## Key takeaways

- Stop adding steps; find **split** and **merge**.
- Most token burn on "middle transforms" should be **edges (code)**, not agents.
- Confidence comes from **structure on edges** (verifiers), not more identical workers.
- Closing line: *"A prompter asks a question. An architect draws a graph."*

## Related

- [[loop-engineering-14-step-roadmap]]
- [[fable-5-self-improving-system-14-steps]]
- [[claude-code-dynamic-workflows-intro]]
- [[dynamic-workflows-where-plan-lives]]
- [[from-1-agent-to-swarm-orchestration-roadmap]]
- [[how-to-build-conductor-multi-agent-leanxbt]]
- [[how-to-build-ai-agent-swarms]]
- [[fable-orchestrate-huge-project-40-subagents-ryancarson]]
- [[agent-workflows-silent-degradation-verification-vladic]]
- [[loop-engineering-technical-roadmap-h100envy]]
