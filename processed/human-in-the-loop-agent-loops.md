---
tags: [agents, loop-engineering, claude-code, agent-harness, evals, verification, mcp, productivity, cursor, cloud-agents, multi-agent]
source: https://x.com/ericzakariasson/status/2070493377267646797
date: 2026-06-26
type: bookmark
author: ericzakariasson
summary: "Eric Zakariasson (Cursor): long agent tasks need a scorable definition of done (eval score, tests, Playwright QA, p95, validation counts), a /loop with explicit stop conditions, /notify via MCP (Slack) for human-in-the-loop decisions, cloud runners for multi-hour work, and ~3–5 parallel loops with a cap when pings stack up."
raw: "[[raw/ericzakariasson_2070493377267646797]]"
---

# Human in the /loop

Practical pattern for **async agent coding**: you are not watching the terminal—you show up when the loop scores, stalls, or needs a decision.

## Definition of done (must be machine-checkable)

| Work type | Target |
|-----------|--------|
| Model / eval | Metric improves (autoresearch-style keep/revert) |
| UI | Playwright + screenshot QA |
| Backend / refactor | Test suite green and stays green |
| Perf | p95 or benchmark under threshold |
| Data cleanup | Zero failing rows / all items pass check |

Start prompts more explicit than you think; loosen once you see what the model infers.

## Loop + stop rules

Change → measure → keep or revert → repeat. Stop when: target hit, no improvement after N tries, out of ideas, or blocked (ask human).

## Notify, don’t babysit

MCP + `/notify` to Slack (or any channel)—status and “need a decision”; your reply becomes the next loop input. Not full agent access to Slack.

## Ops model

- **Cloud** agents for hours-long loops; local client orchestrates.
- **Concurrency**: ~3–5 long loops plus short tasks; stop starting new work when multiple loops wait on you.

## Prompt skeleton

`/loop until <check> hits <target>` (frozen metric) + `/notify` on start, surprises, done, stuck.

## Why it matters

Compresses loop-engineering theory into a **verification-first** workflow: the harness is the scorer + notification channel, not chat attention. Pairs with Hermes-style background work and terminal notify_on_complete patterns.

## Related

- [[wtf-is-a-loop]]
- [[loop-engineering-clearly-explained]]
- [[from-1-agent-to-swarm-orchestration-roadmap]]
- [[feedback-loops-claude-code-less-babysitting]]
- [[9-step-loop-claude-code-senior-engineer]]