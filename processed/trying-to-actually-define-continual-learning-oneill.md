---
tags:
  - continual-learning
  - agent-memory
  - agents
  - agent-harness
  - harness-engineering
  - training
  - rl
  - sft
  - context-management
  - kv-cache
  - plasticity
  - post-training
source: https://x.com/oneill_c/status/2077453217609453784
date: 2026-07-15
type: bookmark
description: "Charlie ONeill — define continual learning for specialized agents; amnesiac intern; KV vs weights; Still/latents; bake-in vs retrieve; weight-update failure modes."
author: oneill_c
summary: "Charlie ONeill — define continual learning for specialized agents; amnesiac intern; KV vs weights; Still/latents; bake-in vs retrieve; weight-update failure modes."
raw: "[[raw/oneill_c_2077453217609453784]]"
---

# Trying to actually define continual learning

@oneill_c (Charlie O'Neill) — problem specification essay for **continual learning**, focused on specialized agentic workers (one company/team/user), not big-lab “update the general model with six months of internet.”

## Amnesiac intern

Inside one context window the model can learn astonishingly well. Window ends → new intern arrives with only the **notes** the prior left. Notes improve; the intern does not. Continual learning = making one machine keep learning from experience over long horizons. Humans are an existence proof for this *narrow* version.

## Two native memories (and a gap)

| Store | Properties |
|-------|------------|
| **Context / KV cache** | Near-lossless; expensive (prefill, linear growth); hard to scale orders of magnitude past ~1M tokens |
| **Weights** | Highly compressed; cheap at inference; **hard to update** without breaking the model |
| **In between** | Almost empty today |

Three research pushes:

1. **Longer context** (linear attention, cheaper KV) — not yet OOMs beyond current lengths without tradeoffs  
2. **Stateful harnesses** — memory.md, skills, NL compaction, vector search over history — hacky, **best practical results so far**  
3. **Learned latent compression of context** (author’s excitement) — Still (inspired by Cartridges / fast KV compaction); granular neural/latent compaction vs token-space summaries  

## Retrieve vs bake in

If long contexts compress to small latent caches: load the right cache at inference, or update weights?

**Automaticity** (Justin Skycak / learning science): basics should be effortless so working memory free for higher decisions. Basketball dribbling; frontier agents often “spend 95% of tokens” searching, reconstructing history, re-deriving procedures.

### Why “harness-only continual learning” is suboptimal (author)

1. **Cost** — margin pressure if weight bake-in can cut tokens dramatically  
2. **Skill acquisition** — facts write to files easily; excellent tool use / SWE / negotiation rarely lives only in longer instruction files → RL for skills  
3. **Bitter Lesson** — hand-engineered harnesses feel less scaled than learning; even self-rewriting harnesses still leave an amnesiac substrate (Dwarkesh trumpet-student rotation analogy)

## Weight updates “cook” the model

**Knowledge vs skill:** one-off knowledge seems easy; **iterative** regime may make knowledge *harder* than skill. Skill has a recipe (env + RL reward; autoevals from production traces). Knowledge needs three tests under **thousands of updates**:

1. Don’t overwrite useful **base-model** info  
2. Don’t forget **prior update** info  
3. Don’t degrade **general capabilities** (instruction-following, reasoning, future learning / plasticity)

Vanilla SFT fails all three iteratively. Distillation / RL somewhat better; still not robust for true continual regime. RL may learn policies without cleanly internalizing facts. Promising variants (ECHO, pedagogical RL, on-policy self-distillation) not yet stable continual. Maybe misspecified objective: reward correctness **and** efficiency so models learn automaticity (stop re-searching) via optimization.

## Lean into ICL?

Working thesis: pretrain + RL heavily optimize **in-context learning**; subsequent weight edits **interfere** with that substrate (plasticity research: repeated FT → worse at learning later tasks).

Possible stack:

- Lossless context for immediate relevance  
- **Compressed latent episodic** memory (e.g. Still) for recent experience  
- Weights for consolidated automatic knowledge/skills  

Hard problem: **what** belongs at each level, **when** to promote/compress, **how much** loss is OK — human episodic vs semantic vs procedural analogy.

## Continual learning is not one problem

Scope must be specified: knowledge vs skill, narrow specialized agent vs general model. Field is blind-men-and-elephant (forgetting metrics, memory hierarchies, RL objectives). Surface area on the *product* of the system before agreeing on method.

## Why it matters

Clearest public framing of specialized-agent continual learning: dual native stores, harness vs bake-in incentives, three knowledge-update tests, and hierarchical memory as research target — bridges vault notes on harness memory files, Replit/ViBench loops, and pretrain↔harness flywheels.

## Related

- [[continual-learning-replit-agent-vibench]]
- [[improving-agents-data-mining-traces]]
- [[how-to-build-agent-that-never-forgets]]
- [[your-ais-memory-is-quietly-making-it-dumber]]
- [[managed-agents-built-in-memory]]
- [[what-if-harness-comes-before-pretraining-lihanc02]]
- [[longmemeval-evaluating-agent-memory-across-sessions]]
