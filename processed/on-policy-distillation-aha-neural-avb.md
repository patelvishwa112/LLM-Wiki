---
tags: ["training", "distillation", "rl", "post-training"]
source: https://x.com/neural_avb/status/2096121273285828673
date: 2026-09-05
type: bookmark
description: "AVB: On-Policy Distillation = student's path + dense teacher token logprobs (SFT dense + RL on-policy); warm up off-policy before OPD."
author: neural_avb
summary: "AVB: On-Policy Distillation = student's path + dense teacher token logprobs (SFT dense + RL on-policy); warm up off-policy before OPD."
raw: "[[raw/neural_avb_2096121273285828673]]"
---

# The "Aha" Moment with On-Policy Distillation

AVB (@neural_avb). Companion video 2026-08-27. Raw may be truncated vs X Article (~26k).

## Map

| | Path | Feedback |
|---|---|---|
| SFT | teacher's | dense token |
| RLVR | student's | sparse outcome |
| OPD | student's | dense teacher logprobs |

Student generates; teacher scores logprobs on **that** trajectory; reverse-KL / sampled-token variant pushes student toward teacher along the student's own states. Repeat as the student distribution moves.

Chess: watch GM games (off-policy) vs play and get per-move notes (on-policy). Off-policy never teaches recovery from states the teacher never visited.

Caveat (Omar Khattab): if the student cannot reach a state, OPD never supervises it. Warm up with off-policy (SFT) for new formats/behaviors, then OPD/RL.

Also covers reverse vs forward KL vs JSD, full-vocab vs sampled vs top-k (see video / remainder of article).

## Related

- [[why-rl-environments-work-now-paniego]]
- [[finetune-free-trl-colab-cli-paniego]]
