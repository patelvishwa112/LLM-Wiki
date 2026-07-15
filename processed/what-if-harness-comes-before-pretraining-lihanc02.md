---
tags:
  - harness-engineering
  - agent-harness
  - agents
  - pretraining
  - post-training
  - data-flywheel
  - sft
  - rl
  - continual-learning
  - context-management
  - distillation
  - training
source: https://x.com/lihanc02/status/2077087985879888361
date: 2026-07-14
type: bookmark
description: "Hanchen Li — harness and pretraining hold hands both ways: flywheel data shaped by harness; harness as symbolic override of pretrain reflexes."
author: lihanc02
summary: "Hanchen Li — harness and pretraining hold hands both ways: flywheel data shaped by harness; harness as symbolic override of pretrain reflexes."
raw: "[[raw/lihanc02_2077087985879888361]]"
---

# What If the Harness Comes Before Pretraining?

@lihanc02 (Hanchen Li) — speculative essay arguing harness and pretraining are coupled at both ends of the pipeline, not “train first, harness as afterthought.”

**Harness** (author’s ICLR-reflections sense): layer that sets **format** of inputs to the checkpoint — context layout, tools, subagent structure — vs **environment**, which sets content.

## Thesis (two directions)

1. **Harness → Pretrain:** harness shapes which trajectories the **data flywheel** collects → what the next pretrain/midtrain/SFT run eats  
2. **Pretrain → Harness:** pretraining is a nonperfect statistical approx of intelligence; harness must correct baked-in instincts  

## Harness → Pretrain (flywheel)

- Tesla FSD analogy: deployment produces interventions → better model → wider deployment  
- Coding agents (Claude Code, Cursor): sessions = trajectories; filter successful ones → SFT on top of agent + harness  
- Completing the loop: harness is not only where the model acts — it is where **future training data is generated**

### RL vs flywheel

| | Role |
|--|------|
| **Flywheel (user trajectories)** | Scales with real use; simpler than fragile RL infra; needs users first |
| **RL** | Bootstraps / disciplines when cold-start is too weak or new capabilities land before public harness adoption |

Author: design harness (before or at least carefully relative to RL), ship, then let user data scale.

### Harness lock-in dilemma

Once you commit to harness A, all collected trajectories inherit its context-management methods. SFT on that data makes the model better at A → harder to switch to B → next data even more A-specific. Transfer across harnesses is understudied; early design can strand or free **billions** of dollars of trajectory value. Research directions: measure cross-harness transfer; design for reusable data.

## Pretrain → Harness (reflexes)

### Context-trust bias

Next-token training teaches “what’s in context is correct; continue it.” Subtle example: ask for CUDA kernel → model writes Triton → stays in Python forever because half-Python files in the corpus are almost never mid-file language switches. Not stubbornness — pretrain prior. Small SFT may not kill a dominant prior; RL can suppress wrong continuations but rare correct demos make the signal slow.

### Scuba-diver analogy

Evolutionary “pretrain” reflex underwater = hold breath and bolt up (deadly). Divers get an explicit symbolic rule: never hold breath, ascend slowly. Rule does not erase the reflex — it **overrides at the moment it fires**.

**Harness = symbolic layer on pretrain reflexes.**

Examples of overrides humans already do and harnesses can encode:

- Context cleaning / forget and restart  
- Spawn clean-context subagents  
- Rule: after N failed attempts, restart instead of patching (models sample forward with failed attempts still biasing tokens)

### Two homes for strategy

1. **Encode in harness** (author prefers for today): compact, subagents, restart policies; optionally a smaller **action model** chooses rules dynamically  
2. **Distill into weights**: train on human-corrected trajectories (e.g. switch Triton → CUDA mid-session). Aligns with classic LLM scaling (Meta AAI mentioned) but rare events + >1T params make the flywheel slow  

Flywheel **connects** them: harness fix first generates the trajectories distillation needs.

## Conclusion

Harness is both **corrective layer** and **data generator**. If the flywheel spins hard enough, agent systems could become a superset of human problem-solving. Personal views; not employer.

## Why it matters

Frames harness engineering as **training-data strategy**, not only product UX — lock-in, transfer, and “where does human judgment live” (rules vs weights). Directly bridges vault threads on harness discipline, production traces / continual learning, and distillation/post-training.

## Related

- [[learn-harness-engineering]]
- [[harness-engineering-2026-discipline]]
- [[harness-is-the-product-context-aware-agents]]
- [[improving-agents-data-mining-traces]]
- [[continual-learning-replit-agent-vibench]]
- [[distillation-post-training-frontier-2026]]
- [[the-great-flattening-tokenmaxx-vorflux-myprasanna]]
- [[the-agentic-engineer-workflow-aashatwt]]
