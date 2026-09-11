---
tags: ["robotics", "training", "data", "annotation"]
source: https://x.com/_varunnair/status/2096119538589008251
date: 2026-09-05
type: bookmark
description: "Varun Nair: robotics ego-data scaling is really (s, annotated-a); annotation margin > collection; VPT-style inverse-dynamics teachers recover lost channels."
author: _varunnair
summary: "Varun Nair: robotics ego-data scaling is really (s, annotated-a); annotation margin > collection; VPT-style inverse-dynamics teachers recover lost channels."
raw: "[[raw/_varunnair_2096119538589008251]]"
---

# Where Is the Signal in Robotics Data

Varun Nair (@_varunnair). Ego-data hype (Dyna-2 1M hours ego, GEN-1.5 / Skild S1 in-context from human video) hides that **the action channel is annotated**, not recorded.

## Claim

Raw ego video is observational state (s). Where ground-truth action (a) is missing you annotate â (hand pose, grasp from thumb–index, IDM). Scaling curves are downstream of that pipeline. Skild: **$3 QC per $1 collection**. Dataset value is not fixed at capture — more signal can be extracted later.

## Three annotation buckets

1. **Recorded** near the robot action space (joints, proprio, gripper) — thin for ego.
2. **Human-judgment assigned** (hand pose, subtask boundaries) — current frontier of annotator models (MediaPipe → WiLoR/HaMeR, SAM 3, Gemini/Qwen action-to-text) with human-in-the-loop.
3. **Unrecoverable unless captured** (intent, contact forces, tactile, out-of-frame pose) — written off today.

## Move the boundary

VPT: IDM on ~2k labeled hours → pseudo-label 70k Minecraft hours. A labeled hour is worth more training the **annotator** than the policy. Cross-modal distillation: golden paired corpus (tactile+ego) trains a teacher that predicts the privileged channel from the surviving one, then run over owned ego hours.

Limitation: output is an in-distribution proxy, not the force. Judgment relocates to the golden set. Economics: outsourcing cannot invent contact force from video.

Vendor-adjacent to annotation businesses. Extract the **(s, â) vs (s, a)** and **annotator-over-policy** points.

## Related

- [[why-rl-environments-work-now-paniego]]
