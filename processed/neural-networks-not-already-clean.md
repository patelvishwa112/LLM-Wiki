---
title: Neural networks are not already clean
type: bookmark
description: "Leo Gao's reply to Nick Cammarata: simple-looking neuron patterns aren't proof of understanding — simulation via downstream KL is the test that separates a real explanation from a vibe check."
tags: [interpretability, mechanistic-interpretability, superposition, circuits, alignment, sae]
source: https://x.com/nabla_theta/status/2111265545719083217
date: 2026-10-17
author: Leo Gao
summary: "Leo Gao's reply to Nick Cammarata: simple-looking neuron patterns aren't proof of understanding — simulation via downstream KL is the test that separates a real explanation from a vibe check."
raw: "[[raw/nabla_theta_2111265545719083217]]"
---

# Neural networks are not already clean

**Source:** Leo Gao, 2026-10-17. A short X pointer to his LessWrong essay rebutting the claim that neurons are "already clean" and interpretability is therefore near-solved.

Gao concedes the empirical correction that motivated Cammarata's post: the field was too quick to label neurons polysemantic, and a closer look often does reveal a simple pattern behind the activating examples. But he separates that observation from the conclusion drawn from it. A pattern that covers the examples you happened to look at is not an explanation — it can be a description of a biased sample, and the auto-interp paper's own revision protocol already ran into exactly that wall.

The argument turns on two ways a vibe check fails. First, correlation is not symmetric: a neuron may fire only on a narrow, hard-to-compactly-characterize subset of the concept you named ("dogs on bicycles — but only on sunny days"). Forcing it to fire on the full concept would degrade the model, which is evidence the label was too broad rather than proof of polysemanticity. Second, activation magnitudes may carry the payload; if you can't predict which activations should be strong, you're missing part of the mechanism. Gao reports that ablating small activations substantially degrades performance, which conflicts with Cammarata's ablation results — a divergence he flags as worth chasing down.

His proposed bar is simulation: write an explicit rubric, substitute predicted values for real neuron activations, and measure the damage. He argues Cammarata's objection — that simulation scores demand too much — is an artifact of the correlation-based scoring in the original auto-interp work, and that switching to downstream KL over a large dataset largely dissolves it. KL needs no activation binning, ignores details that don't affect behavior, and would have caught known-bad explanations (the car-and-dog reading of the V-shaped-object neuron) from the start. Explaining neurons is in any case only a step: circuits remain large, redundant, and low-variance-explained, with superposition plus multiple computations per neuron as the standing explanation for why.

## Why it matters

If you are building or investing on the premise that interpretability will supply a safety case for frontier models, this is a direct argument that the current evidence base is weaker than the headline results suggest. The methodological point generalizes past mech interp: "the examples look consistent with my explanation" is a cheap test that a plausible-looking rubric can pass while being wrong, and Gao's KL-based simulation is a concrete, cheap alternative. Anyone evaluating interpretability claims — including claims about SAE latents and transcoder features — should ask for the simulation number, not the gallery.

## Key points

- Simple patterns behind top activating examples do not establish that a neuron only fires on that pattern; X-matches-Y is not commutative, and neurons frequently fire on a narrow uncharacterizable subset of the named concept.
- Weak activations cannot be discarded: Gao's best guess is that ablating small neuron activations substantially degrades model performance, contradicting Cammarata's ablation results.
- Simulation test: rubric-scored predicted activations substituted into the model; heavy degradation means the explanation was wrong.
- Correlation-based simulation scores are the problem, not simulation itself — downstream KL over a large dataset avoids activation binning and does not penalize behaviorally irrelevant detail.
- Downstream KL is preferred over loss delta, because modeling other neurons better can offset bad modeling and spuriously improve loss.
- The KL test would have flagged the car-and-dog explanation of the V-shaped-object neuron as bad (missing many V shapes, firing on round dogs/cars).
- Circuits still do not close the gap: they are large, redundant, and explain little of the variance, which Gao attributes to computation on features in superposition.
- Concrete counterexamples noted: a Colorado neuron that also fires on the Tornado Python library (small relative activation), a first-layer "-ado" word neuron (L0/N4730), and a "COLORFUL" GPU-brand neuron covering CSS `color` but not sibling CSS properties.

## Related

- [[mechanistic-interpretability]]
- [[superposition]]
- [[sparse-autoencoders]]
- [[priests-of-agi-interpretability-crisis]]
