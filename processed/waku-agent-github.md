---
tags:
  - agents
  - agent-harness
  - harness-engineering
  - agent-memory
  - evals
  - llm-judges
  - loop-engineering
  - mcp
  - hermes
  - openclaw
  - skills
  - observability
  - local-first
  - sqlite
source: https://github.com/ShenSeanChen/waku-agent
date: 2026-07-18
type: resource
description: "Waku: MIT local-first personal agent teaching harness, loop (~95 LOC), memory pillars + retrieval gate, and dual evals/release gate; dashboard + Telegram/voice; Hermes/OpenClaw-shaped blueprint."
author: ShenSeanChen
summary: "Waku: MIT local-first personal agent teaching harness, loop (~95 LOC), memory pillars + retrieval gate, and dual evals/release gate; dashboard + Telegram/voice; Hermes/OpenClaw-shaped blueprint."
raw: "[[raw/github_shenseanchen_waku-agent]]"
---

# waku-agent (GitHub)

[ShenSeanChen/waku-agent](https://github.com/ShenSeanChen/waku-agent) — local-first personal AI assistant meant to be **read in an afternoon**. Teaching repo for the four pillars of serious agents: **Harness · Loop · Memory · Eval/LLM-Ops**. ~277★ / 75 forks at ingest; MIT. Built for Sean's AI Stories; explicitly compared to Hermes/OpenClaw as a smaller readable blueprint.

## Architecture (from README)

- **Gateway:** CLI, browser dashboard (`localhost:7777`), Telegram, voice (wake "waku waku")
- **Loop:** plain Python tool-calling loop (~95 lines), max iterations hard stop
- **Memory:** SQLite + FTS5 semantic/episodic/procedural; retrieval gate (skip vs retrieve); consolidation; SOUL.md + skills; working-memory turn window
- **Ops:** always-on JSONL traces, usage ledger, deterministic evals vs LLM-as-judge, `make gate` release gate, optional Phoenix/Langfuse
- **MCP + multi-provider** adapters (Anthropic, OpenAI, Gemini, DeepSeek, MiniMax, Kimi, GLM, OpenRouter)
- **Experimental:** delegate coding tasks to **pi**; skeletons for terminal/browser/cron

## Why it matters

Clean reference implementation of the same conceptual stack as Hermes-class assistants without product opacity: memory gate discipline, loop engineering, dual eval suites, local SQLite ownership. Useful for comparing harness patterns, teaching, or forking a minimal agent.

## Related

- [[hermes-seven-skills-cobi-bean]]
- [[openclaw-hermes-supervisor-setup]]
- [[harness-is-the-product-context-aware-agents]]
- [[context-engineering-field-guide-phosphenq]]
- [[agent-as-a-judge-trajectory-evals-aparna]]
- [[do-automated-evals-work-parlance-labs]]
- [[how-to-build-agent-that-never-forgets]]
- [[wtf-is-a-loop]]
