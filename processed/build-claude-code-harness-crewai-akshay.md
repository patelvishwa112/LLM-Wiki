---
tags: ["agent-harness", "harness-engineering", "claude-code", "crewai", "multi-agent", "sandbox", "memory", "planning", "subagents", "agents", "coding-tools"]
source: https://x.com/akshay_pachaar/status/2077455755066868098
date: 2026-07-15
type: bookmark
description: "Akshay Pachaar rebuilds Claude Code-style coding harness in CrewAI — loop, tools, planning/reasoning, hierarchical subagents, E2B sandbox, HITL, memory, checkpoints."
author: akshay_pachaar
summary: "Akshay Pachaar rebuilds Claude Code-style coding harness in CrewAI — loop, tools, planning/reasoning, hierarchical subagents, E2B sandbox, HITL, memory, checkpoints."
raw: "[[raw/akshay_pachaar_2077455755066868098]]"
---

# Let’s build Claude Code’s harness (step-by-step)

Akshay Pachaar argues coding agents fail less from weak models than from missing **harness** layers (planning, tools, memory, safety, subagents, compression). Reconstructs a Claude Code–like stack in **CrewAI** and demos fixing a BankAccount suite (3 failing → 5/5, implementation-only).

## Key takeaways

- **Brain vs hands:** Model chooses next action; harness runs tools, keeps the run on track. Claude Code wins on machinery, not only model quality.
- **Core loop:** `model → tool_use? → execute → append → repeat` until plain text. CrewAI `Crew.kickoff()` supplies the loop; you define Agent/Task.
- **Tools = hands + external memory:** FileRead/Write, DirectoryRead, custom `@tool` (e.g. pytest with truncated stdout). Write large results to files, keep paths in context (context engineering).
- **Planning vs reasoning:** `planning=True` on Crew (roadmap, like Claude Code todos); `reasoning=True` on Agent (reflect/draft/evaluate/refine up to `max_reasoning_attempts`). Fights **context rot**.
- **Subagents:** Hierarchical process + manager with `allow_delegation=True`; specialists (Explorer / Engineer / Test Runner) return summaries so manager context stays small.
- **Safety:** Permission + isolation — `human_input=True` (or webhooks); **E2B** exec/Python tools so shell can’t touch host.
- **Memory & checkpoints:** `memory=True` (LLM extracts/retrieves cross-run facts); `checkpoint=True` (JSON or SQLite resume). Shared crew memory by default.
- **Eval pattern:** Auto-checkable test suite as objective; Anthropic-style fail-to-pass. Demo: 3 fail / 2 pass → all pass without editing tests.
- **Still your job:** role/goal/backstory prompts; sandbox wiring; which tools per agent. Harness adds token cost; some scaffolding is temporary model-limit workarounds (e.g. Sonnet 4.5 context resets retired for Opus 4.5).

## Why it matters

Practical map from Claude Code concepts to configurable CrewAI flags — good companion to LangChain custom harness posts and the vault’s harness-engineering cluster.

## Related

- [[learn-harness-engineering]]
- [[how-to-build-custom-agent-harness-langchain]]
- [[claude-code-changed-what-agents-look-like]]
- [[loop-engineering-clearly-explained]]
- [[glean-coding-harness-programmatic-tool-calling]]
- [[harness-engineering-2026-discipline]]
- [[how-to-create-loops-claude-code-sairahul1]]
- [[agent-harness-should-repair-itself]]
