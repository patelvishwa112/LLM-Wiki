---
tags:
- graph-engineering
- loop-engineering
- agents
- multi-agent
- orchestration
- agent-harness
- harness-engineering
- verification
- langgraph
- cost-optimization
source: https://x.com/akshay_pachaar/status/2081089131808243999
date: 2026-07-25
author: Akshay (@akshay_pachaar)
type: bookmark
description: "Graph engineering is coordination of loops (nodes/edges/state), not a loop replacement. Four hard parts: node worthiness, typed shared state, code-first routing, anti-groupthink reviewers. Most times graphs are overkill (~15x tokens)."
summary: "Graph engineering is coordination of loops (nodes/edges/state), not a loop replacement. Four hard parts: node worthiness, typed shared state, code-first routing, anti-groupthink reviewers. Most times graphs are overkill (~15x tokens)."
raw: "[[raw/akshay_pachaar_2081089131808243999]]"
---

# Graph engineering: substance over the meme

@akshay_pachaar on the Jul 2026 rename wave (Steinberger "loops → graphs?", Hamel "Loop Engineering Is Dead") — half joke, half real: multiple loops create a **coordination** problem, and graphs are the classic name for that.

## Graph = nodes + edges + state

- **Nodes** — agent, model call, deterministic fn, tool, human approval
- **Edges** — sequence / parallel / conditional
- **State** — shared object every node reads/writes

Starter diamond: researcher → writer → reviewer; fail edge loops to writer. **A single agent loop is a one-node graph with a self-edge.** Graphs connect and govern loops; they don't abolish them.

## Layer stack (each wraps the prior)

Prompt → context → harness → loop → **graph** (coordination across loops: what runs when, order, who checks whom). Skip a lower layer → graph fails more elaborately.

Practice isn't new: LangGraph (Jan 2024), AutoGen GraphFlow, Google ADK 2.0. Name is new ("welcome back, langchain").

## Four hard parts

1. **When a node deserves to exist** — specialty = different model/tools/role (e.g. read-only reviewer). Napkin test; if collapse loses nothing, it wasn't two nodes. Don't graph "summarize PDF" into five nodes.
2. **Shared state hygiene** — context rot becomes state rot. Typed schema, explicit write permissions, checkpoints for replay. Side-effect nodes must be idempotent (replay re-runs post-checkpoint).
3. **Trusted routing** — model-chosen routes = flexible + unstable. ADK 2.0 rule: deterministic code for checkable conditions; models only for real judgment.
4. **Anti-groupthink** — never grade own homework; multi-agent same-model same-context = organized nonsense. Reviewer on **different model**, **fresh context**, anchored to external evidence (tests ran, code compiled). Cognition/Devin: many readers, **one writer**.

## When overkill

Most of the time. Anthropic: ~4x tokens single agent vs chat; ~15x multi-agent. Multi-agent research +90.2% vs single Opus when work parallelizes; Building Effective Agents still says simplest first. LangGraph docs: plain tool loop → LangGraph overkill.

**Reach for a graph when:** genuine specialties, parallel fan-out/join, different models per step, failure isolation / auditable routing. Else stay in the loop.

## Start sequence

1. Master one loop (brakes, completion check, critic) — weak loops × N = distributed failure  
2. Paper first; challenge every node  
3. State schema + write access up front  
4. Reviewer = different model + fresh context + external evidence  
5. Budget caps per node  

## Why it matters

Clean bridge between vault's loop-engineering cluster and graph fleets roadmaps. Explicit: rename hype ≠ new CS; durable problem is **coordination after one loop stops being enough**.

## Related

- [[graph-engineering-14-step-roadmap-0xcodez]]
- [[graph-engineering-dynamic-workflows-fleet-0xcodila]]
- [[loops-vs-graphs-polygres-infinite-context-daleverett]]
- [[loop-engineering-clearly-explained]]
- [[wtf-is-a-loop]]
- [[four-loops-ai-engineering-taxonomy-aparna]]
- [[build-claude-code-harness-crewai-akshay]]
- [[how-to-build-conductor-multi-agent-leanxbt]]
- [[own-your-intelligence-harrison-chase]]
