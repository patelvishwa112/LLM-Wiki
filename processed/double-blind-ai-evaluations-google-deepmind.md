---
tags:
  - evals
  - model-evaluation
  - benchmark-contamination
  - safety-evals
  - frontier-ai
  - confidential-computing
  - security
  - governance
  - google
  - gemini
source: https://x.com/GoogleDeepMind/status/2092961763553677387
date: 2026-08-27
author: Google DeepMind (@GoogleDeepMind); blog by William Isaac, Sol Messing, Kristian Lum
type: bookmark
description: "DeepMind's pilot of the first double-blind eval of a proprietary frontier model: evaluator prompts and Gemini Flash Lite weights both stay sealed inside Google Cloud Confidential Space."
summary: "Double-blind evaluation puts the evaluator's confidential benchmarks and the provider's model weights inside a cryptographic enclave, so neither side sees the other's asset — the technical fix for benchmark contamination."
raw: "[[raw/googledeepmind_2092961763553677387]]"
status: current
as_of: 2026-08-27
---

# Piloting the World's First Double-Blind AI Evaluations

Google DeepMind ran a first-of-its-kind pilot: a **proprietary frontier model evaluated on confidential benchmarks without either party revealing its asset**. The evaluator cannot see the Gemini weights; Google cannot see the test prompts. Partner list: Singapore AI Safety Institute, OpenMined, AVERI, MLCommons. Model under test: Gemini Flash Lite.

## The problem it solves

Benchmark contamination. If a model can see the test questions ahead of time — directly, or indirectly through an evaluator's leaky process — a high score tells you nothing about capability, and safety evals become theatre. Historically the industry chose between two bad options:

- evaluators hand over their prompts (provider may see the test set), or
- the provider hands over model weights (IP and control risk).

Contractual zero-logging and NDAs paper over this; they are not technical guarantees.

## How it works

A 7-step secure workflow between an "AI Owner" and an "Evaluator" through a **GPU enclave** built on Google Cloud Confidential Computing / Confidential Space. Attestation is the mechanism: cryptographic evidence about what code ran, on what hardware, with what data access. Both parties can verify the enclave's claims without either revealing its secret to the other.

Implication: the result is auditable *as an evaluation run in a verified environment*, which is a stronger claim than "trust our internal evals" but still a claim about the environment, not about the benchmark's design quality.

## Verdict

This is the right direction — evaluation integrity as an infrastructure problem rather than a policy promise. It matters most exactly where the stakes are highest: **cybersecurity, government, and pre-deployment safety testing** by third parties who cannot hand over prompts or receive weights. Two honest caveats: it is a **pilot on one model**, and the trust anchor is Google's own cloud attestation stack, so the guarantee is "sealed box, verified by the platform" — not "no one anywhere can game the benchmark." Worth tracking whether other labs adopt the pattern or build a neutral enclave operator, since a single-vendor enclave is a weak neutrality story.

## Related

- [[evals-strategic-ip-garrettlord]]
- [[agent-evals-practical-guide]]
- [[do-automated-evals-work-parlance-labs]]
- [[eval-engineering-failure-first-yarchi]]
- [[agent-as-a-judge-trajectory-evals-aparna]]
