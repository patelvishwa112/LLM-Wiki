---
tags:
  - loop-engineering
  - agents
  - agent-harness
  - observability
  - evals
  - software-factory
  - autoresearch
  - arize
source: https://x.com/aparnadhinak/status/2073492320159510869
date: 2026-07-04
type: bookmark
author: aparnadhinak
description: "Aparna Dhinakaran maps four loop architectures (execution, task/Ralph, product factory, system/autoresearch) plus an oversight loop, from AIEWF June 2026 hype."
summary: "Aparna Dhinakaran maps four loop architectures (execution, task/Ralph, product factory, system/autoresearch) plus an oversight loop, from AIEWF June 2026 hype."
raw: "[[raw/aparnadhinak_2073492320159510869]]"
---

# Four Loops in AI Engineering (Taxonomy)

**Source:** [X Article @aparnadhinak](https://x.com/aparnadhinak/status/2073492320159510869) (co-authored @seldo)

## Summary

After Steinberger, Boris Cherny, Osmani, swyx, and LangChain all elevated “loops” in June 2026—and AIEWF ended with a debate on hype vs practice—Dhinakaran separates **four architectures** behind one word:

1. **Execution loop** — act–observe tool cycle within a task; ends on environment feedback (often too early when the agent self-declares done).
2. **Task loop (Ralph)** — fresh context per iteration against one spec until tests pass; human writes spec and watches failure patterns (locomotive engineer).
3. **Product loop (software factory)** — continuous codebase/backlog lifecycle (triage → ship → monitor); exit signals from issues, logs, reviews; autonomy dial per lifecycle stage (Factory, Warp Oz, Anthropic Tag ~65% codegen cited).
4. **System loop (autoresearch)** — outer loop improves prompts, harnesses, models, evals (Karpathy autoresearch, Meta Brain2Qwerty v2 with human final checkpoint).

**Agentic MapReduce** is explicitly *not* a loop—fan-out pipeline without feedback. A fifth **oversight loop** sets goals, budget, cull (swyx’s “???? loop”); AIEWF camps disagree on how far autonomy ratchets (Litt/Bakaus vs factory advocates). **Autonomy is independent per layer.** Closing loops at scale needs trace sweep + failure clustering (author ties to Arize AX).

## Why it matters

Stops talking past each other when “loop” means Ralph vs factory vs inner ReAct. Pairs with vault loop-engineering notes as the **reference map** for harness design and where humans stay in the stack.

## Related

- [[wtf-is-a-loop]] — Steinberger vs Cherny origin thread
- [[loop-engineering-clearly-explained]] — practitioner loop engineering
- [[human-in-the-loop-agent-loops]] — human placement in agent loops
- [[anthropic-recursive-self-improvement]] — system-level self-improvement framing
- [[from-1-agent-to-swarm-orchestration-roadmap]] — orchestration above single loops