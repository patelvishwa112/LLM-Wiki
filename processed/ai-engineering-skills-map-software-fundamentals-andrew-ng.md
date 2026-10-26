---
tags:
  - ai-engineering
  - software-engineering
  - fundamentals
  - agents
  - coding-tools
  - career
  - hiring
  - architecture
  - data
  - evals
source: https://x.com/AndrewYNg/status/2093388974194872781
date: 2026-08-28
author: Andrew Ng (@AndrewYNg)
type: bookmark
description: "Andrew Ng's follow-up to the Skills Map: agentic coding kills syntax trivia but raises the value of five software fundamentals you must know to steer an agent's tradeoffs."
summary: "Agentic coding devalues memorized syntax and raises the value of software fundamentals — full stack, data, architecture, security/reliability, production operations — because you cannot steer tradeoffs you don't know exist."
raw: "[[raw/andrewyng_2093388974194872781]]"
status: current
as_of: 2026-08-28
---

# AI Engineering Skills Map: Software Engineering Fundamentals

Second publish of Andrew Ng's Skills Map work (first: [[ai-engineering-skills-map-andrew-ng]]), this time drilling into the **software-engineering fundamentals** pillar. His claim is narrow and useful: agentic coding did not make fundamentals optional, it moved their value from *writing* code to *steering* it.

## The core argument

A novice who vibe-codes can ship a simple app, but the coding agent then makes bad tradeoffs in **latency, availability, consistency, reliability, maintainability, simplicity and cost** — not because the agent is weak, but because the human did not know those tradeoffs existed and never steered toward one. Knowing fundamentals is what turns an agent from an autocomplete into a directed engineering tool.

Second argument: an AI application is still an application. The AI core is expressed through a broader software system, so you need enough full-stack literacy to shape that system.

## The five areas

1. **Building full-stack applications** — UI components, caching, page rendering, API choice/design, auth, state and session management, async processing, persistence, testing, security, accessibility. Agents let specialists (frontend, mobile) play a broader role, but only if they understand the stack.
2. **Managing data** — access patterns drive what to store and for how long; pick data model and storage type (relational, document, key-value, graph) knowing it fixes speed, scalability, availability, reliability, cost. Transactions, concurrency, freshness, privacy/governance/compliance, lifecycle. Data is the hardest layer to change later, so poor data architecture silently caps what the AI can know.
3. **Designing system architectures** — understand the intended load, latency and cost sensitivity first, then decide platform, frontend/backend boundary, decomposition, state placement, monolith vs microservices, and the stack (often by running experiments). The right architecture is a moving target across prototype → first production → scale.
4. **Security and reliability** — testing strategy (unit vs integration mix, frameworks, coverage), designing for failure (rate limits, graceful degradation, blast-radius reduction), and "shift left" security: scan code, dependencies and cloud config with AI tooling, which still requires security knowledge to interpret.
5. **Scaling and operating in production** — SDLC, deployment environments, release strategy, CI/CD, IaaS; observability, alerts, incident management; scaling servers, load balancing, sharding/indexing/replication; version control, code review, dependency maintenance, tech debt.

## Verdict

The honest read: this is a **hiring and self-assessment checklist** more than a curriculum. The one claim worth internalizing is causal — agent quality is bounded by the operator's ability to name tradeoffs. That is exactly what [[ai-engineering-roadmap-2026-from-scratch]] and [[how-to-become-applied-ai-engineer-eyad-khrais]] assume but rarely spell out. Memorizing syntax is dead; knowing why a system is slow, inconsistent or expensive is the moat.

## Related

- [[ai-engineering-skills-map-andrew-ng]]
- [[ai-engineering-roadmap-2026-from-scratch]]
- [[2026-ai-engineering-roadmap]]
- [[how-to-become-applied-ai-engineer-eyad-khrais]]
- [[harness-engineering-2026-discipline]]
