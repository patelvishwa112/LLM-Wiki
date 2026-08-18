---
tags: ["papers", "evals", "reward-models", "reasoning", "inference-scaling", "verification", "deepmind", "agents"]
source: https://x.com/marfinxx/status/2089684002466619772
date: 2026-08-18
type: bookmark
description: "marfinxx on DeepMind GenRM — verification as Yes/No next-token + CoT majority vote; GSM8K 73→93.4%, MATH easy-to-hard 28→44.6%."
author: marfinxx
summary: "marfinxx on DeepMind GenRM — verification as Yes/No next-token + CoT majority vote; GSM8K 73→93.4%, MATH easy-to-hard 28→44.6%."
raw: "[[raw/marfinxx_2089684002466619772]]"
---

# marfinxx on GenRM (DeepMind generative verifiers)

Hype-framed thread pointing at Zhang et al. **Generative Verifiers** (ICLR 2025 / arXiv:2408.15240). Pipeline he sketches:

candidates → CoT verification rationales → P(Yes) scoring → majority-vote ensemble → pick solution

## Points (aligned with paper)

1. **Verification as NTP** — drop scalar RM head; score = P(Yes/No)  
2. **GenRM-CoT** — step-by-step critique before correctness  
3. **Inference-time scaling** — multi-rationale average beats prompt-only judges  
4. **Easy-to-hard** — GSM-trained 9B-class verifier lifts MATH500 **28% → 44.6%**  
5. **GSM8K** — **73% → 93.4%** with fewer generator samples in reported setup  

Cross-links his “Test-Time Compute Engineering” article course.

## Use

Entry pointer; **canonical technical note:** [[generative-verifiers-genrm-deepmind]].

## Skeptical read

Thread is promotional/summary; numbers need paper tables. “Superhuman” is marketing — paper claims large BoN gains vs fixed generators.

## Related

- [[generative-verifiers-genrm-deepmind]]
- [[verifiability-constraint-rlvr-unverifiable-tanayj]]
- [[controlling-reasoning-effort-in-llms]]
- [[eval-engineering-merge-gate-hanakoxbt]]
- [[agent-as-a-judge-trajectory-evals-aparna]]
- [[how-frontier-models-train-on-outcomes-2026-sergio]]
