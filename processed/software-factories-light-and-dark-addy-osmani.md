---
tags: ["software-factory", "harness-engineering", "loop-engineering", "agents", "agent-harness", "verification", "human-in-the-loop", "addy-osmani", "architecture", "comprehension-debt"]
source: https://x.com/addyosmani/status/2079442194449232227
date: 2026-07-21
type: bookmark
description: "Addy Osmani on loop→harness→factory, dark vs lit factories, comprehension debt, and back pressure as the real constraint."
author: addyosmani
summary: "Addy Osmani on loop→harness→factory, dark vs lit factories, comprehension debt, and back pressure as the real constraint."
raw: "[[raw/addyosmani_2079442194449232227]]"
---

# Software Factories, Light and Dark

Long-form X Article by **Addy Osmani**, building on Dex Horthy’s AIEWF talk *Harness Engineering is not Enough: Why Software Factories Fail*. Canonical framing for factory-scale agent coding.

## Stack: loop → harness → factory

| Layer | Meaning |
|-------|---------|
| **Loop** | One agent on repeat: gather context → act → check → until done. Design the *system* that prompts, not turn-by-turn chat. |
| **Harness** | Walls around the loop: sandbox, tools, memory, done-gates. Raw model without harness spins forever. |
| **Factory** | Many harnessed loops + work queue + review gate → production. Not a bigger agent — an **org chart made of loops**. |

Paradigm shift: unit of work moves from the code diff up to loop, harness, and flow between them.

## Factory wiring diagram

Closed loop: intent + prod signals → queue → harness builds → automated checks → **review gate** → deploy → monitoring → signals again.

Almost every box scales cheaply (generation, tests, scanners). The stubborn expensive box is the review gate — **judgment**.

## Dark vs lit

- **Dark factory (lights-out):** code ships that no human read; machines only verify. Feels like broken sound barrier at first; buries cost.
- **Lit factory:** same pipeline; lights stay on where a wrong call is expensive. Judgment moves **upstream** (product, design, architecture) — not only tacked on as end-stage PR review.

Manufacturing analogy: FANUC/Xiaomi dark factories; in software the “floor” is the **diff**.

## Comprehension debt

Widening gap between how much code exists and how much any human still understands. Dark factories take debt on as fast as generation allows while tests stay green. Dex’s field report: ~4 months fully automated factory with no human reading code → quiet, late failure, not a dramatic blow-up. Conflicting metrics: maximize token utilization vs minimize human understanding of the system.

Greenfield/weekend toys tolerate this longer; decade-old brownfield + production constraints do not.

## Back pressure (core rule)

> Hand a loop only as much autonomy as you can **cheaply and reliably verify** — not one inch more.

Verification, not generation, is the real constraint. Speeding generation without widening the verification neck just deepens the pile of bad PRs. Model improvements alone won’t close the gap: architectural excellence is hard to put in a fast reward signal.

## What earns the dark switch

Dark only if checks are cheap, high-frequency, hard to fake: green/red oracles, types, property tests, rubric-bound review agents; oracles that answer immediately and don’t drift. Short loops (Dex: ~3–10 steps hold; past ~20 context wander) earn automation; sprawling loops hide mistakes.

Keep lights on for: subtle bugs tests miss, large blast radius, year-shaping decisions (auth, billing, public APIs).

All-dark → rebuild in months. All-lit → review bottleneck. Skill is **per-loop light-switch placement**.

## Architecture as external safety net

Types, short call stacks, clear boundaries, test seams, DI — ordinary practices become a hard-to-fake net *outside* the model. Agents (Claude Code, Codex) are fluent in harness/tools, not long-term maintainability. Example dark-safe loop: nightly GH Actions one lint/anti-pattern fix → small PR.

## Loops vs graphs / state machines

Pure tool-call loops felt free until brownfield; discipline is putting the flowchart back around the loop. Graph = directed workflow graph (not knowledge graph): agent is clever *inside* nodes, can’t leave sanctioned edges. Matches Dex: “mostly deterministic code, with LLM steps sprinkled in.” LangGraph, LlamaIndex Workflows, hybrid grow-the-graph outer loops, actor model / state machines.

## Where humans go

Humans never left — they moved to the **outer loop**: right problem, sound diagnosis/implementation, approve, own consequences. Boundary = evidence (diffs, tests, logs, short explanation). Role: design the line and guard the gate, not write every change on the floor.

Closing line: robots fine in the dark; humans need light — danger is not knowing where the switch is.

## Why it matters

Best single writeup linking loop/harness vocabulary already in the vault to factory-scale ops, verification economics, and the dark/lit autonomy dial. Direct counterweight to “just scale generation” and pure lights-out token farming.

## Related

- [[software-factory-linear-claude-cloud-routines]]
- [[four-loops-ai-engineering-taxonomy-aparna]]
- [[addy-osmani-agent-autonomy-ladder-six-levels]]
- [[addy-osmani-agent-skills-open-source]]
- [[learn-harness-engineering]]
- [[loop-engineering]]
- [[loop-engineering-clearly-explained]]
- [[wtf-is-a-loop]]
- [[loops-vs-graphs-polygres-infinite-context-daleverett]]
- [[graph-engineering-14-step-roadmap-0xcodez]]
- [[human-in-the-loop-agent-loops]]
- [[how-to-create-loops-claude-code-sairahul1]]
