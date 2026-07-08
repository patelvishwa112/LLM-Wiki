---
tags:
  - fable-5
  - agents
  - agent-harness
  - claude-code
  - loops
  - continual-learning
  - skills
  - verification
  - dynamic-workflows
  - harness-engineering
source: https://x.com/0xcodez/status/2065089060104720776
date: 2026-06-11
type: bookmark
author: 0xcodez
description: "14-step roadmap for a compounding Fable 5 harness: four-layer stack, /goal vs Outcomes, verifiers, STATE.md, Skills, Routines, and model routing."
summary: "14-step roadmap for a compounding Fable 5 harness: four-layer stack, /goal vs Outcomes, verifiers, STATE.md, Skills, Routines, and model routing."
raw: "[[raw/0xcodez_2065089060104720776]]"
---

# Build self-improving agent system with Fable 5 (14 steps)

@0xCodez maps **Mythos-class Fable 5** (June 2026 launch) to a **system that compounds**—not weight-updating “self-learning,” but environment feedback: memory, Skills, eval loops, and independent graders.

## Four-layer compound stack

1. **Primitives** — Fable 5, sub-agents, tools, worktrees  
2. **Orchestration** — `/goal` (local Claude Code) vs **Outcomes** (CMA, file rubrics, long runs); Dynamic Workflows; **Routines** (scheduled/API/GitHub triggers, laptop-off)  
3. **Memory** — STATE.md (verified facts, rules, open failures, last-session pointer); Skills as cross-project procedural memory  
4. **Self-improvement** — vision verify, rule distillation, eval suites feeding back into Skills  

Outputs flow up through grading and write back to layer 3; the model stays stateless.

## Highest-leverage steps (condensed)

| Step | Idea |
|------|------|
| 6 | **Independent verifier sub-agent** beats self-critique (Anthropic / Parameter Golf evidence) |
| 7 | Dynamic Workflows: fan-out-synthesize, adversarial verify, loop-until-done |
| 8 | Git **worktrees** for parallel makers/verifiers and multi-experiment runs |
| 10–11 | Continual Learning Bench **5-stage memory**: fail → investigate → verify → distill → consult; **STATE.md** read at start, write at end |
| 12 | Lessons go into **Skills** (known failure modes, anti-patterns), not chat-only |
| 13 | Maker → screenshot → **vision verifier** vs goal/tokens |
| 14 | Mythos **safety classifiers** (cyber/bio/chem/distillation) → explicit **Opus 4.8** fallback |

## Model routing (cost-aware)

Fable 5 orchestrator → Opus 4.8 hard/blocked tasks → Sonnet 4.6 workers → Haiku 4.5 graders.

## Anti-patterns called out

5-minute chat sessions on Mythos pricing; self-critique; no STATE.md; static Skills; long runs on laptop instead of CMA/Routines; ignoring classifier blocks.

## Related

- [[designing-loops-with-fable-5]]
- [[fable-orchestrate-huge-project-40-subagents-ryancarson]]
- [[learn-harness-engineering]]
- [[dynamic-workflows-where-plan-lives]]