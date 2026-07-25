---
tags: ["distillation", "training", "post-training", "rlhf", "sft", "reasoning", "ai-policy", "api-distillation", "behavior-cloning", "models"]
source: https://x.com/completeskeptic/status/2080494182775521745
blog_url: https://www.completeskeptic.com/p/is-it-even-possible-for-the-chinese
date: 2026-07-24
type: bookmark
description: "Ex-OpenAI RLHF co-author clarifies three distillation tiers and argues API-only behavior parroting can still transfer capability via style."
author: completeskeptic
summary: "Ex-OpenAI RLHF co-author clarifies three distillation tiers and argues API-only behavior parroting can still transfer capability via style."
raw: "[[raw/completeskeptic_2080494182775521745]]"
---

# Behavior parroting — can Chinese labs distill US reasoning models?

Diogo Almeida (@CompleteSkeptic), ex-OpenAI and co-author on the original RLHF paper, reacts to the Kimi K3 / Anthropic / White House “distillation” fight with a clean taxonomy. TL;DR: **yes, API-side transfer is plausible**, but not via classic Hinton-style logits — and the mechanism is unintuitive.

## Three tiers (strongest → weakest)

1. **Logit distillation** — Match teacher next-token probability distributions (Hinton et al.). What labs mean by internal distillation (e.g. Opus from a stronger teacher’s logits). **Not** available via modern frontier APIs (logits closed).
2. **Behavior cloning** — Imitate full output token sequences (SFT / imitation learning). What most people mean by cross-lab distillation from APIs. **Blocked in practice for reasoning models** because providers hide full CoT and only show summarized “chicken scratch” traces — deliberately, to blunt cloning.
3. **Behavior parroting** (author’s term; related to Chen et al. “Only Answer” training) — Imitate **final answers only**, after privileged hidden reasoning. Intuitive failure mode: pure hallucination of plausible answers without acquiring skill.

## Why parroting might still work

- **Instruction following is largely style** — Hewitt et al.: training on outputs without instructions closes much of the RLHF gap.
- **Reasoning is partly style too** — models trained on traces that lead to *wrong* answers still work surprisingly well (cited arXiv results).
- **Leakage between hidden reasoning and visible response** — labs separate reasoning vs non-reasoning models; token-level output bias may carry style across the boundary.
- **Pre-training is massive parroting** — internet text already omits human intermediate work and private context, yet scales.

## Industry claim

API distillation is **an approximation (parroting) of an approximation (cloning) of logit distillation**. Still “pretty compelling” that commercial APIs leak useful signal. Asks for **scaling laws on behavior parroting of reasoning models**.

Comment side-note (thread): some practitioners claim unredacted CoT can leak via channel/tool misuse on OpenAI-class models — softens the “hidden CoT is airtight” assumption.

## Why it matters

- Separates overloaded “distillation” in **policy, export-control, and lab PR** from the actual training objective.
- Connects hidden-CoT product choices to **IP / competitive moat**, not just UX.
- Bridges vault notes on on-policy/off-policy distillation and SFT recipes with a **cross-lab API threat model**.

## Skeptical read

- Style-transfer case leans on a few papers + analogy to pre-training; the critical “reasoning→response style transfer” step is admitted as a guess.
- Does not quantify how far parroting gets a frontier student vs full CoT cloning or internal logits.
- Framing is partly a response to White House / Moonshot headlines — useful taxonomy, not a forensic of Kimi K3.

## Related

- [[distillation-post-training-frontier-2026]]
- [[why-on-policy-distillation-works]]
- [[on-policy-distillation-must-read]]
- [[on-policy-distillation-resources-2026]]
- [[knowledge-distillation-theturingpost]]
- [[rlhf-from-first-principles]]
- [[verifiability-constraint-rlvr-unverifiable-tanayj]]
- [[what-if-harness-comes-before-pretraining-lihanc02]]
