---
tags:
  - training
  - post-training
  - rl
  - sft
  - distillation
  - rlvr
  - kto
  - agents
  - economics
source: https://kawine.github.io/assets/aiesi_post-training_public.pdf
date: 2026-08-21
type: article
author: ethayarajh
description: "Kawin Ethayarajh AIESI 2026 deck — post-training stack SFT through distillation, then world adaptation and mecha-nudges as the next problem for economists."
summary: "Kawin Ethayarajh AIESI 2026 deck — post-training stack SFT through distillation, then world adaptation and mecha-nudges as the next problem for economists."
raw: "[[raw/kawine_aiesi-post-training]]"
published: 2026-08-06
---

# Post-Training LLMs (AIESI 2026)

Kawin Ethayarajh (Chicago Booth) to young economists, Aug 6–11 2026. Tweet announcement: https://x.com/ethayarajh/status/2090894841265733744 — slides https://kawine.github.io/assets/aiesi_post-training_public.pdf. 87-slide text in [[raw/kawine_aiesi-post-training]]; tweet in [[raw/ethayarajh_2090894841265733744]].

## Core claim

The model you use is not the pretrained model. Pretraining learns a distribution over text. Post-training turns a base model into a deployable behavioral policy: interface, capability, preference, safety, product constraints.

Useful (imperfect) stack:

1. SFT — imitate (demos)
2. Offline — compare (DPO / KTO / SimPO)
3. Online — explore (PPO / GRPO / CISPO)
4. RLVR + environments — verify
5. Distillation — transfer (**we are here**)
6. World adaptation — anticipate (**the future**)

Post-training mostly changes the probability of latent behavior; whether it builds totally new routines is still debated.

## Methods (compressed)

- SFT: (instruction, desired response) pairs. Economist example: report a regression so a policymaker hears "CI includes zero."
- Offline prefs: paired chosen/rejected (DPO) vs unpaired outcomes (KTO — Ethayarajh 2024, prospect-theoretic utility vs a reference point). Shared pathology: likelihood displacement.
- Online: PPO critic vs GRPO group baseline (DeepSeekMath). Variants (Dr. GRPO, DAPO) target length/std pathologies.
- RL environment = sandbox: realistic state + tools + task generator + simulator + shortcut-resistant verifier + reproducibility.
- Distillation: once RL finds a policy, on-policy distillation (OPD) copies it cheaper (Lu / Thinking Machines: 7–10× fewer steps, 50–100× less compute in the cited experiment). OPSD: same weights as student+teacher with privileged solution. Use to merge expensive specialist RL (math/code/agents/safety) into one model.

## World adaptation

Current post-training treats the environment as fixed because static verifiable rewards scale. Once agents rank, buy, and allocate attention, people redesign content and interfaces. That is a **feedback loop**, not covariate shift.

**Mecha-nudges** (Frey & Ethayarajh 2026): change machine-usable information without materially degrading the human-usable environment. Distinct from prompt injection, SEO, and adversarial examples.

Etsy evidence in the deck: post-ChatGPT listings carry more machine-usable info; mecha-nudged listings associate with more reviews only after ChatGPT; effect stronger where using AI is less taboo.

Post-training response: train against adversarial environment designers; multi-objective agent+human welfare; monitor and refresh.

Open questions for economists: identification, equilibrium, welfare, governance.

## Why it matters

Pairs with distillation-2026 notes (we are on step 5) and RLVR/reasoning-effort notes. Adds the missing step: the world talks back.

## Skeptical read

Mecha-nudge empirics are observational (seller FE, still selection). "OpenAI–Hugging Face incident" is a pointer, not a case study in the tweet. Slide OCR/extract is messy on dense diagrams.

## Related

- [[controlling-reasoning-effort-in-llms]]
- [[distillation-post-training-frontier-2026]]
- [[rlhf-from-first-principles]]
- [[generative-verifiers-genrm-deepmind]]
