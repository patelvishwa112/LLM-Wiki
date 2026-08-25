---
tags:
  - evals
  - rl
  - rlvr
  - training
  - agents
  - mercor
source: https://x.com/brendanfoody/status/1939764763485171948
date: 2025-06-30
type: bookmark
author: brendanfoody
description: "Brendan Foody — RL will saturate any eval, so the bottleneck is building environments that map real work; evals are the new PRD."
summary: "Brendan Foody — RL will saturate any eval, so the bottleneck is building environments that map real work; evals are the new PRD."
raw: "[[raw/brendanfoody_1939764763485171948]]"
published: 2025-06-30
---

# Welcome to The Era of Evals

Brendan Foody (Mercor), Jun 30 2025.

## Claim

RL is getting good enough to saturate whatever you measure. The barrier to agents in the real economy is not more model scale — it is **evals for everything**. Lab/academic evals do not match what enterprises actually buy.

**Evals are the new PRD.** Building environments that map real workspaces and deliverables turns recurring knowledge-work cost into a one-time fixed cost. More data-efficient than pretrain / SFT / RLHF.

## Verifiable rewards

Environments reward outcomes and intermediate steps. Many attempts + test-time compute. Autograders mark good trajectories; RL upweights the thoughts that got there. Hill-climb the eval.

Spectrum:

- **Objective** — games, math, code, some biology. Clear state/action/outcome. Where RL already won (AlphaProof, AlphaFold, R1, codegen).
- **Subjective** — memos, legal briefs, therapy. Multiple valid expert opinions. Rubric rewards (lineage: Constitutional AI / RLAIF).
- **Computer-use** — middle. Goals fuzzy; once defined, actions/outcomes are programmatic. Containerized envs scale thousands of parallel rollouts.

## Environments create experience

Eventually models learn from real-world outcomes (test scores, closed sales, built bridges). Intermediate rewards stay necessary. Humans stay inside the env as teachers of style and taste.

Never escape data. The frontier is **human-created environments** as durable experiential signal.

## Path (and pitch)

Highest-leverage human work: write evals and RL environments. Mercor: autograders → simulated workspaces, multi-turn, multimodal.

Once agent steps are reliable, what remains is RL on humankind’s stated goals.

## Why it matters

Pairs with Ethayarajh’s stack (RLVR + world adaptation) and Anthropic SDLC (continuous evals in CI). The Foody claim is upstream: if you cannot grade it, you cannot train or govern it.

## Skeptical read

Mercor is selling the thing he says is the bottleneck. “Saturate any eval” assumes the grader cannot be gamed — reward hacking is the whole unstated problem. Rubrics for subjective work are still politics.

## Related

- [[aiesi-post-training-world-adaptation]]
- [[eval-engineering-merge-gate-hanakoxbt]]
- [[generative-verifiers-genrm-deepmind]]
- [[ai-native-sdlc-playbook]]
- [[controlling-reasoning-effort-in-llms]]
