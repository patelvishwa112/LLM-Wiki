---
title: Exp1 Initial Result — 0% Causal Efficacy with Pre-Trained SAE on Llama 1B
date: 2026-05-29
type: experiment
tags:
- interpretability
- sparse-autoencoders
- experiment
- steering
- encoding-deployment-gap
- exp1-gap-closure
status: in-progress
project: ~/Projects/llama-sae-interp/
model: Llama-3.2-1B-Instruct
hardware: Apple M1 Mac Mini, 8GB RAM
sae: sae-Llama-3.2-1B-131k (pre-trained, HuggingFace)
related:
- '[[beyond-ghost-sae-experiment-proposals]]'
- '[[ghost-in-residual-stream-experiment]]'
description: 'Exp1: SAE Gap Closure — Initial Result (Pre-Trained SAE)'
---

# Exp1: SAE Gap Closure — Initial Result (Pre-Trained SAE)

## Setup
- **Model:** Llama-3.2-1B-Instruct (MLX), not Qwen 0.5B (proposal target)
- **SAE:** Pre-trained sae-Llama-3.2-1B-131k from HuggingFace (131,072 latent features), not self-trained
- **Layer:** L10 (mid-network, MLP output)
- **Questions:** 50 encoding, 15 steering (simple factual: capitals, etc.)
- **Pipeline:** 3-phase to stay in 8GB: (1) model-only activation capture, (2) SAE-only feature extraction + steering direction pre-compute, (3) model-only generation with pre-computed vectors
- **Steering:** top-5 SAE features by activation magnitude, clamped at 3.0×, applied to residual stream after MLP

## Result
- **Baseline accuracy:** 11/15 (73.3%)
- **Steered accuracy:** 11/15 (73.3%)
- **Causal efficacy: 0%** — zero questions changed output
- **Every single token was identical between baseline and steered generation**

## Questions for Claude

1. Why zero effect? Is this expected with pre-trained SAEs? The proposal says train SAEs on the specific factual questions — is that the critical missing piece?

2. Are we targeting the right layer? L10 is mid-network for Llama 1B (16 layers total). The ghost experiment on Qwen 0.5B found peak encoding at L20-21 (of 24). Should we try a later layer like L12-13?

3. Is the steering methodology correct? We're:
   - Taking top-5 features by raw activation magnitude at the last token
   - Summing feature_value × decoder_vector for each
   - Normalizing and clamping at 3.0×
   - Adding to residual stream after MLP at the target layer
   - But we only steer at ONE token position (the last prompt token)

   Anthropic's steering work steers throughout generation, not just at one position. Is single-position steering fundamentally insufficient?

4. Could the issue be that our SAE features (131K, trained on general text) are capturing surface-level patterns rather than semantic factual knowledge? The proposal says 4×-8× expansion (~2048-4096 features). We have 64× expansion. Does the huge feature count mean features are too granular to steer?

5. The proposal frames the gap as "circuit competition, not representation failure." If SAE features encode facts but can't steer output, does that support the circuit competition hypothesis? How would we test for an active override circuit?

6. What's the minimum viable experiment to prove the pipeline works? Should we try:
   - A known-steerable feature (e.g., sentiment, language) before factual knowledge?
   - Anthropic's "Neutrality" feature approach — find a feature that broadly shifts behavior?
   - Steering at every token position instead of just the last one?
