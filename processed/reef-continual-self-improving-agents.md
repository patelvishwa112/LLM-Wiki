---
tags: ["continual-learning", "agents", "agent-harness", "self-improvement", "training", "rl", "open-source", "inference"]
source: https://x.com/ao_qu18465/status/2094867930081337730
date: 2026-09-01
type: bookmark
description: "Ao Qu open-sources Reef: inference-first infra so agents evolve model and harness from live experience (recipes, Git LFS releases, Cordis)."
author: ao_qu18465
summary: "Ao Qu open-sources Reef: inference-first infra so agents evolve model and harness from live experience (recipes, Git LFS releases, Cordis)."
raw: "[[raw/ao_qu18465_2094867930081337730]]"
---

# Reef — continual self-improving agents

Ao Qu (@ao_qu18465, 2026-09-01) open-sources **Reef** (Human Agent Society): treat **continual self-improvement** as the practical frame; **RSI** as a more fully recursive special case.

Thesis: train → eval → deploy → discard-inference is the wrong lifecycle. Two breaks:

1. **Inference is training data.** Trajectories, results, user feedback are the experience stream — not waste.
2. **The whole agent evolves**, not just weights: prompts, memory, skills, tools, orchestration. Model and harness co-constrain each other.

Reef is therefore **inference infra first**, with learning attached — not another offline trainer that happens to sample with an engine (vs Slime/veRL).

## Own three things

| Own | Mechanism |
|-----|-----------|
| **Experience** | OpenAI-compatible `/v1/chat/completions`; `x-reef-agent-record-id`; `/reef/report` feedback. Stateful stream: off-policy staleness, session merge, dedupe. |
| **Whole agent** | **Harness:** Cordis as training backend → trajectory analysis → harness edits → install (`/reef/harness/install?adapter=pi`). **Model:** async training (Slime-adapted) → checkpoint/LoRA → NCCL hot-swap, no restart. |
| **Updates** | Every artifact (weights, LoRA, harness tree, routing) is versioned (**Git LFS**). Per-scenario append-only release chain with **compare-and-swap** so a stale publisher can’t clobber a newer head. Rejected candidates leave serving unchanged. |

## Recipes

Plug-in learning recipes on the same bus. Axes: **signal**, **how experience is acquired** (proactive vs reactive), **what evolves** (model / harness / both). Config example: `reef.recipe: recipes.sao.recipe:SAORecipe`. Demos named: **OpenClaw-RL** (async preference learning while chatting) and **TTT-Discover** (iterative packing). Some recipes “coming soon.”

Repo: https://github.com/Human-Agent-Society/reef

## Skeptical read

- Announcement + architecture GIFs, not a reproduced eval table.
- Hot-swap / CAS release path is the load-bearing ops claim — verify in the repo.
- Cordis harness evolution is the distinctive piece; model-side is a known RL loop with a serving face.
- Discord/star CTA. Extract the three “own”s and recipe axes.

## Related

- [[prime-agent-rlm-continual-harness-primeintellect]]
- [[self-learning-agents-three-layers-user-signal]]
- [[trying-to-actually-define-continual-learning-oneill]]
- [[knowledge-flywheels-yisongyue]]
- [[improving-agents-data-mining-traces]]
- [[what-if-harness-comes-before-pretraining-lihanc02]]
