---
title: "Evals: easy mode to god mode"
type: bookmark
description: "Alex Lieberman's evals crash course from LangChain's Viv Trivedy: tasks plus verifiers, then sandboxed environments, then a trace-driven self-improving loop."
tags: [evals, agent-harness, observability, verification, langchain, sandbox]
source: https://x.com/businessbarista/status/2099565601312166157
date: 2026-09-14
author: Alex Lieberman
summary: "Alex Lieberman's evals crash course from LangChain's Viv Trivedy: tasks plus verifiers, then sandboxed environments, then a trace-driven self-improving loop."
raw: "[[raw/businessbarista_2099565601312166157]]"
---

# Evals: easy mode to god mode

**Source:** Alex Lieberman, 2026-09-14. A summary thread of a 38-minute evals masterclass taught by Viv Trivedy, who leads Labs at LangChain.

The post compresses evals into three escalating levels. **Easy mode** is the definition — did the agent do the job correctly — decomposed into exactly two building blocks: *tasks* (the checkable jobs you care about: log the meeting, draft the email, find Acme in the right Salesforce tables) and *verifiers* (anything that can render a right/wrong verdict: a script, another model, or a human with a checklist).

**Hard mode** is environments: a safe practice field where the agent works and you evaluate it. The first rule is blunt — never test on production, because agents optimize for whatever score you gave them and will cheat. The second is about access: non-engineers still have options, including Harbor (open-source primitives for tasks, verifiers, sandboxes), the LangSmith Engine UI for people who can judge quality without living in GitHub, or stealing a published Harbor-format eval and having Claude Code or Codex explain and adapt it.

**God mode** is the self-improving loop: run the agent in the real world, convert production behavior into evals and environments, change the agent so failures stop recurring, repeat. The mechanics are tracing first (traces are "receipts" of every tool call, API ping, and dead end), storing those logs at whatever scale you can afford, then pointing a second agent at the first agent's traces to surface patterns — "always searches the wrong tables", "multi-company asks collapse to one company" — and propose overnight fixes if the eval suite is solid.

## Why it matters

This is the cheapest available framing of the eval stack: most teams stop at tasks and a judge, which yields scores that cannot explain a failure. The trace-first ordering is the part that actually changes engineering practice — without tool calls, inputs, and environment captured, a "pass" is a vibe check, and the self-improving loop has no substrate to mine. It also lowers the entry cost for non-engineers by naming concrete off-the-shelf paths (Harbor, LangSmith Engine).

## Key points

- Two primitives: **tasks** (checkable jobs) + **verifiers** (script, model, or human checklist).
- Never evaluate on production — agents game the score you give them.
- Harbor provides open-source primitives for tasks, verifiers, and sandboxes; LangSmith Engine is a UI layer for non-engineers.
- Bootstrapping trick: take a published Harbor-format eval, have a coding agent explain it, then adapt it.
- Self-improving loop = production behavior → evals/environments → agent change → repeat.
- Turn on tracing before anything else: traces capture tool calls, external pings, and dead ends.
- A second agent reads the first agent's traces to find failure patterns and propose fixes overnight, conditional on a solid eval suite.

## Related

- [[harbor-langchain-unified-agent-eval-stack]]
- [[agent-as-a-judge-trajectory-evals-aparna]]
- [[improving-agents-data-mining-traces]]
- [[eval-engineering-merge-gate-hanakoxbt]]
- [[era-of-evals-brendan-foody]]
