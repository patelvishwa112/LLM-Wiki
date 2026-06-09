---
tags: [ai-agents, coding-agents, harness, claude-code, codex, nimbalyst, agent-architecture, llm-engineering]
source: https://x.com/wirthkarl/status/2059270673730580732
raw: "[[raw/wirthkarl_2059270673730580732]]"
author: Karl Wirth (@wirthkarl)
date: 2026-05-26
scraped: 2026-05-26
---

# Building the Harness Around Our Coding Agents: Eight Failure Modes, Eight Pillars

Karl Wirth (CEO of Nimbalyst, ex-Evergage) on the system his team built around Claude Code and Codex.

## Core Insight

> Teams building with AI usually end up building two products: the thing they ship, and the system around their agents that makes them useful.

## The 8 Pillars

| # | Pillar | Goal | Failure Mode It Answers |
|---|--------|------|------------------------|
| 1 | Context | Know the project | Agent doesn't know your codebase/rules/conventions |
| 2 | Provenance | Trace the why | Agent can't traverse links between artifacts |
| 3 | Capability | Act and observe | Agent trapped in text channel, can't run commands |
| 4 | Workflow | Reuse the arcs | Agent reinvents how to do every task |
| 5 | Restraint | Stay in bounds | Agent does dangerous things faster than expected |
| 6 | Verification | Prove the fix | Agent hallucinates "fixed" without proof |
| 7 | Visual Interface | Show the work | Decisions vanish into chat text walls |
| 8 | Coordination | Track every agent | Human loses track of parallel agents |

## Key Takeaways

1. **Harness = the durable layer around a model** — instructions, tools, permissions, context, verification
2. **Claude Code and Codex are harnesses at the model level** — your team owns the layer above
3. **Nothing in a good harness is novel** — it's other people's parts assembled around your project
4. **Context compounds** — rules, skills, memory, path-scoped instructions make every session better
5. **Capability and restraint must grow together** — every new tool needs matched scope
6. **Verification is non-negotiable** — failing-test-first, E2E specs, agent must prove fix works
7. **Portability matters** — the harness should work with Claude Code today, Codex today, whatever ships tomorrow
8. **Treat the harness as a product** — allocate dedicated effort to improving it

## Reference
- Nimbalyst: https://nimbalyst.com/
- THE_HARNESS.md: https://github.com/nimbalyst/nimbalyst/blob/main/docs/THE_HARNESS.md
