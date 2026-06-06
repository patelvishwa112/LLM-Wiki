---
title: "Beyond the Ghost — SAE-Based Experiment Proposals for Understanding and Steering Model Behavior"
date: 2026-05-29
type: proposal
tags:
  - interpretability
  - sparse-autoencoders
  - experiment
  - steering
  - circuits
  - mechanistic-interpretability
  - encoding-deployment-gap
status: draft
related:
  - "[[ghost-in-residual-stream-experiment]]"
  - "[[sparse-autoencoders]]"
  - "[[persona-vectors]]"
  - "[[priests-of-agi-interpretability-crisis]]"
  - "[[anthropic-natural-language-autoencoders]]"
  - "[[goodfire-parameter-decomposition-interpretability]]"
  - "[[raw/anthropic_evaluating-feature-steering]]"
  - "[[raw/anthropic_tracing-thoughts]]"
---

# Beyond the Ghost: SAE Experiments for Understanding and Steering Model Behavior

The ghost experiment established that the encoding-deployment gap exists at 0.5B scale: linear probes find knowledge at 79.7% accuracy but can only steer it 4.3% of the time. Persona information peaks at mid-network (L14, 31%) then fades. Multi-step reasoning is invisible to linear classifiers.

The question now: **Can SAEs, which claim to disentangle superposition into monosemantic features, close this gap? And can we use SAE features to understand not just what the model knows but what it's trying to do?**

## What We Know From the Literature

### SAEs Work, But With Caveats
- Anthropic demonstrated interpretable features in Claude 3 Sonnet and traced circuits in 3.5 Haiku
- But the Priests of AGI critique documents a placebo trial: random baselines matched trained SAEs on interpretability and causal editing (Korznikov et al. 2026)
- Only 30% of features are shared across different SAE training seeds (Paulo & Belrose)
- Anthropic's own finding: **feature activation context ≠ resulting behavior** — a feature that fires on "gender bias discussions" doesn't necessarily control gender bias output

### Circuits, Not Isolated Features
- Anthropic's "Tracing the Thoughts" revealed that features form circuits with complex interactions
- Hallucination is a competition: default refusal circuit vs. "known entity" feature
- Jailbreaks exploit coherence pressure — grammar features override safety features mid-sentence
- Planning ahead: rhyme features activate BEFORE the line is written, then the model writes toward them

### The Steering Sweet Spot
- Anthropic found a steering sweet spot (factor ±5) where features influence output without degrading capabilities
- But off-target effects are common and hard to predict from activation contexts alone
- A "Neutrality" feature reduced bias across all 9 dimensions — suggesting some features have broad, beneficial effects

---

## Proposed Experiments

### Experiment 1: SAE Feature Intervention — Closing the Encoding-Deployment Gap

**Question:** Do SAE features close the encoding-deployment gap compared to linear probes?

**Why it matters:** If SAEs truly disentangle superposition, their features should be more causally deployable. The ghost experiment showed linear probes have a 0.37 correlation between encoding and causation. SAEs might get closer to 1.0.

**Approach:**
1. Train an SAE on the same Qwen2.5-0.5B-Instruct model, on the same 500 factual questions from the ghost experiment
2. Extract SAE features at each layer (using MLX — SAE training on 0.5B hidden states is feasible on M1 with batching)
3. For each SAE feature, compute:
   - **Encoding score:** how well does the feature's activation predict the correct answer token?
   - **Causal efficacy:** when we clamp or amplify the feature, does the model output change toward the correct answer?
4. Compare the gap across SAE features vs. linear probe directions vs. random directions
5. Key comparison: do the top-5 SAE features for a given answer outperform the linear probe direction?

**Feasibility on M1 8GB:**
- SAE training: feasible with a small dictionary (e.g., 4×-8× expansion, ~2048-4096 features, batch size 32)
- Use MLX's sparse operations
- Memory: model (~1GB 4-bit) + SAE params (~10-20MB) + activations = <4GB total
- Training time: ~2-4 hours for one layer's SAE

**Success looks like:** SAE features show causal efficacy >20% (vs. linear probe's 4.3%) at layers where encoding peaks. If SAE features also show a gap, something deeper than superposition is at work.

**Pitfall:** The Priests of AGI critique — random SAE baselines can match trained ones. Run a control: train with shuffled activations and compare.

---

### Experiment 2: The Default Refusal Circuit — Tracing Competing Behaviors

**Question:** Does Qwen2.5-0.5B have a "default refusal" circuit like Claude, and can we identify what competes with it?

**Why it matters:** The ghost experiment found the model defaults to "The." — an incomplete start. Anthropic found Claude defaults to refusal, inhibited by "known entity." If small models have similar default behaviors, the encoding-deployment gap might be explainable as a circuit-level competition: knowledge is computed but overridden by a default behavior.

**Approach:**
1. Design prompts where the model should NOT answer (impossible questions) vs. SHOULD answer (easy factual)
2. Train SAEs at layers where the ghost experiment found high encoding but low deployment (L20-23)
3. For each prompt type, identify SAE features that consistently activate
4. Test causal interventions:
   - **Ablate** the "default behavior" feature → does the model start answering impossible questions? (hallucination induction)
   - **Amplify** the "known entity" feature → does the model answer questions it previously balked at?
5. Trace the circuit: which features inhibit which other features?

**Feasibility on M1 8GB:**
- Same SAE training as Experiment 1
- Prompt set: 100 easy factual + 100 impossible questions
- Circuit tracing: manual analysis of feature co-activation patterns (no need for full attribution graphs)

**Success looks like:** Finding a specific SAE feature whose ablation causes the model to hallucinate answers to impossible questions — proving a default behavior circuit exists at this scale. This would explain the "The." default in the ghost experiment: the model's default is "start a sentence but don't commit to an answer."

---

### Experiment 3: Persona Steering with SAE Features

**Question:** Can SAE features steer persona more precisely than the linear persona vectors from the ghost experiment?

**Why it matters:** The ghost experiment found personas peak at L14 (31% probe accuracy) then fade. SAEs might extract cleaner persona features that survive to later layers, enabling stronger steering. Anthropic found a "neutrality" feature that broadly reduced bias — can we find analogous "helpfulness" / "unhelpfulness" features?

**Approach:**
1. Train an SAE at the persona-peak layer (L14) and later layers (L20-23)
2. For each SAE feature, score its activation difference between "helpful" and "unhelpful" persona prompts
3. Identify the top-K persona-differential features
4. Test steering:
   - Amplifying "helpful" features on an unhelpful-prompted model
   - Amplifying "unhelpful" features on a neutral model
5. Measure specificity: does steering a persona feature change persona behavior while preserving factual accuracy? (avoid the off-target problem Anthropic found)

**Feasibility on M1 8GB:**
- Persona prompts already exist from ghost experiment
- SAE training at 2 layers
- Steering: lightweight — just modify activations during forward pass
- Evaluation: persona compliance rate + factual accuracy

**Success looks like:** SAE persona features achieve >50% persona compliance (vs. linear probe's 31%) while preserving >70% factual accuracy. Finding a feature that cleanly separates "persona" compute from "factual" compute would be a major finding.

**Key Anthropic lesson:** Test off-target effects. A "helpfulness" feature might also increase sycophancy or verbosity. Run BBQ-style bias checks if possible.

---

### Experiment 4: Planning Ahead — Does the Model Compute Answers Before Deciding to Say Them?

**Question:** Does the ghost experiment's encoding-deployment gap reflect a planning-then-override pattern? Does the model compute the answer, plan to say it, then get overridden by a coherence/safety/default mechanism?

**Why it matters:** Anthropic found Claude plans rhyme words BEFORE writing the line. The ghost experiment found factual answers are encoded at L20-21 but output doesn't reflect them until L23-24 (and even then weakly). What happens between "knowing" and "saying"?

**Approach:**
1. Take a factual prompt where the ghost experiment found high encoding but low deployment (e.g., "What is the atomic number of Helium?")
2. Train SAEs at each layer from L18 to L24
3. Trace feature activation over the forward pass:
   - At what layer does the "2" feature activate? (encoding)
   - At what layer does a "commit to answer" feature activate? (deployment decision)
   - Is there a "suppress" or "hedge" feature that activates between encoding and output?
4. Intervention: ablate the hypothesized "suppress" feature at L21-22 → does the model output "2" instead of "The."?

**Feasibility on M1 8GB:**
- SAE training at 7 layers (L18-L24) — most ambitious, maybe 6-8 hours
- Alternatively: train at L20, L21, L22 (where gap peaks) only
- Single-prompt deep analysis (inspired by Anthropic's case study approach)

**Success looks like:** Finding a specific feature at L22-23 that, when ablated, causes the model to output correct answers instead of "The." — proving that deployment is actively suppressed rather than simply absent. This would reframe the encoding-deployment gap as an **active override** rather than a **passive disconnection**.

---

### Experiment 5: Reasoning in SAE Feature Space

**Question:** Multi-step reasoning was invisible to linear probes (10.3%, chance level). Can SAEs recover reasoning representations?

**Why it matters:** If SAEs find reasoning features that linear probes missed, that's evidence reasoning is stored non-linearly (superposed across many directions). If SAEs also fail, reasoning at 0.5B might genuinely not be stored in the residual stream at all — which would explain why small models get worse with chain-of-thought fine-tuning.

**Approach:**
1. Take the same 50 reasoning questions from the ghost experiment
2. Train SAEs at every 4th layer (L4, L8, L12, L16, L20, L24)
3. For each SAE feature, compute encoding score for the correct answer
4. Also try: decoding the INTERMEDIATE STEP (e.g., "3 apples - 2 = 1, 1 + 5 = 6") not just the final answer
5. If SAE features show intermediate computation, trace the reasoning trajectory across layers
6. Intervention: if an intermediate step feature is found, clamp it and see if the final answer improves

**Feasibility on M1 8GB:**
- SAE training at 6 layers — ~4-6 hours
- Intermediate step decoding requires ground-truth intermediate answers (need to generate these for each question)
- Use Claude Code to generate step-by-step solutions for the 50 questions

**Success looks like:** SAE features at L12-16 showing 25%+ encoding for intermediate reasoning steps (vs. linear probe's 10%). Even finding one layer where a reasoning intermediate is decodable would be significant — it would mean the model IS computing reasoning, just not in a linearly accessible format.

If SAEs also fail: strong evidence that 0.5B models genuinely cannot form reasoning representations, supporting the "small models get worse with CoT" finding.

---

## Cross-Cutting Themes

### The Encoding-Deployment Gap May Be a Circuit Competition, Not a Representation Failure

The ghost experiment framed the gap as "the model knows but doesn't use." The Anthropic circuit work suggests a richer picture: the model computes the answer, but other circuits (default behaviors, coherence pressure, safety mechanisms) compete for control of the output. The gap isn't a failure of representation — it's a **routing problem**. Features exist but aren't connected to the output pathway.

### SAEs vs. Probes for Steering

SAEs have theoretical advantages (disentanglement) but practical weaknesses (seed instability, off-target effects, placebo concerns). The key question isn't "are SAEs better than probes?" but "do SAEs reveal circuit structure that probes can't?" If SAEs show that features compete and inhibit each other, they're valuable even if steering remains imperfect.

### Feasibility Tier List

| Experiment | Layers | SAEs to Train | Est. Time (M1) | Risk |
|-----------|--------|---------------|----------------|------|
| #1: Gap closure | 1 (L21) | 1 | 2-4 hrs | Low |
| #2: Default refusal | 3 (L20-22) | 3 | 4-6 hrs | Medium |
| #3: Persona steering | 2 (L14, L21) | 2 | 3-5 hrs | Low |
| #4: Planning/override | 3-7 (L18-24) | 3+ | 4-8 hrs | High |
| #5: Reasoning SAE | 6 (every 4th) | 6 | 6-10 hrs | High |

### Recommended Starting Point

**Experiment #1 (gap closure) + Experiment #2 (default refusal) together.** They share SAE training at L20-22 and answer complementary questions: "does disentanglement help?" and "what competes with the answer?" If SAE features close the gap (Exp 1), great — we have a better steering tool. If they don't, but we find a default refusal circuit (Exp 2), we understand WHY — the gap is a circuit-level competition, not a representation problem.

### What This Line of Work Could Build Toward

If we can identify circuit-level competitions in a 0.5B model, we can:
1. Build an "override dashboard" — a map of which features compete for output control
2. Design conditional steering: "amplify the answer feature, but only when the default-refusal feature is below threshold"
3. Apply the same protocol to larger models where the gap may be even larger

The ghost experiment found the ghost. SAEs can help us understand what's haunting it.
