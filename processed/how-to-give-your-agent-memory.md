---
tags: ["agents", "agent-memory", "langsmith", "langchain", "observability", "procedural-memory", "agent-harness", "evals"]
source: https://x.com/jakebroekhuizen/status/2069828911501021337
date: 2026-06-24
type: bookmark
author: jakebroekhuizen
summary: "LangChain's Jake Broekhuizen on closing the agent memory loop with traces, analysis, and versioned context via LangSmith Observability, Engine, and Context Hub."
raw: "[[raw/jakebroekhuizen_2069828911501021337]]"
---

# How To Give Your Agent Memory

Jake Broekhuizen (LangChain Labs) frames **memory** as what lets agents stop forcing users to repeat the same corrections: a background process spots mistakes or new learnings, generalizes them, and writes durable context the harness loads on later runs.

## Key takeaways

- **Trace ≠ memory.** Logs and transcripts are evidence; memory exists only when a lesson becomes retrievable context that changes future behavior.
- **Two scopes:** working memory (current thread, tools, temp state) vs long-term memory (facts, preferences, skills, policies) with a read/write cycle after each run.
- **Cognitive taxonomy:** semantic (knows), episodic (experienced), procedural (how to behave). Many production wins are **procedural** — formatting, tool order, routing, tone — not more facts in the prompt.
- **Three-step loop:** (1) capture instrumented traces, (2) analyze for feedback, eval failures, and recurring patterns with careful diagnosis, (3) update only the context that should persist.
- **LangSmith stack:** Observability (traces) → Engine (automated improvement signal from traces) → Context Hub (versioned instructions, tools, skills). Updated context must be loaded on the next run to close the loop.
- **Design discipline:** most traces stay history; guard against stale prompt/skill caches; pair important memory changes with evals to catch regressions.

## Why it matters

This is an operational blueprint for **active learning** in agents — not stuffing more tokens into the system prompt, but institutionalizing how harnesses evolve from production trajectories. It complements harness-comparison surveys (what memory exists today) with a concrete closed loop for teams on LangSmith.

**Video walkthrough:** https://www.youtube.com/watch?v=y6WUw2_Hhrs

## Related

- [[agent-memory-landscape-2026]] — How major harnesses implement (and gap) memory today
- [[memory-is-retained-consequence]] — Memory as consequence that should survive, not stored knowledge
- [[langchain-fireworks-trace-judge-100x-cheaper]] — Same author ecosystem; trace data for judges and improvement
- [[2-ways-self-evolving-agents-model-harness]] — Model vs harness paths to agents that improve over time
- [[how-to-build-agent-that-never-forgets]] — Alternate architecture patterns for persistent agent memory