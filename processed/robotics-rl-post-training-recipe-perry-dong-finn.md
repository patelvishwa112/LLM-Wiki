---
title: Towards Universal Post-Training for Robotics
type: bookmark
description: "Perry Dong & Chelsea Finn: robotics RL is still a craft not a recipe; EXPO-FT hits 30/30 in ~19 min of real-robot interaction, but reward, reset and init defaults are missing."
tags: [robotics, rl, post-training, vla, reward-models, training-data]
source: https://x.com/perryadong/status/2102805448936305107
date: 2026-09-23
author: Perry Dong
summary: "Perry Dong & Chelsea Finn: robotics RL is still a craft not a recipe; EXPO-FT hits 30/30 in ~19 min of real-robot interaction, but reward, reset and init defaults are missing."
raw: "[[raw/perryadong_2102805448936305107]]"
---

# Towards Universal Post-Training for Robotics

**Source:** Perry Dong (with Chelsea Finn), 2026-09-23. A blog post arguing robotics is at its GPT-2 moment and needs the post-training recipe LLMs already have.

The post starts from a deployment-reliability argument rather than a capability one. Pretrained VLAs and world-action models now execute genuinely complex tasks, but a policy that loads dishes right 95% of the time still breaks something every week in a real home. What turned GPT-2 from an interesting demo into something deployable was a shared post-training recipe — strong pretrained base, defined environments and reward, a known RL algorithm family anchored to a reference model, and documented pathologies like reward hacking — and any team could follow it. Robotics has the pretrained half and none of the recipe. RL for frontier robotics, in their phrasing, "is not yet a recipe. It's a craft," which is why it works for a handful of people and not for the field.

The technical core is an argument about why LLM RL does not transfer. The RL that scaled for Go and for language models is on-policy policy gradient with cheap samples and near-free verification — their AlphaGo example plays 288 games in parallel and scores 3,168. A robot picking up a glass emits ~500 control commands at 20ms intervals and learns only at step 500, so credit must be spread across a long, stochastic horizon while every real attempt costs wall-clock time on hardware. That pushes robotics toward value-based methods, and the classic ones (DDPG, TD3, SAC) assume unimodal Gaussian actions, which is wrong for diffusion policies where grasping by the handle or the base are both correct. Sending gradients through the full denoising chain is unstable; scoring candidates post-hoc is safe but teaches the policy nothing; RL-searching input noise is safe but can only recombine skills the base model already has.

Their answer, EXPO(-FT), learns a lightweight edit policy that makes small bounded nudges to the frontier model's proposed actions toward higher-value regions, picks the best candidate with a value function, then absorbs the accepted edits back into the base model so it proposes better actions next time. Human interventions during online learning are fed back in. Across six manipulation tasks — string-light routing, a pool shot, inserting a flower into a bottle, flipping an egg, ball balancing — it reaches 30/30 success with an average of ~19 minutes of online interaction, against 18.8 for SFT on π0.5, 20.5 for HG-DAgger, 19 for DSRL and 5.5 for HIL-SERL.

The authors are explicit that the algorithm is only half the gap. The protocol half is five defaults nobody has settled: reward specification (LLM RLVR has "check the answer, check the tests"; robotics has hand-built detectors or a human calling each trajectory), resets (learned reset policies, reversible task design, or skipping reset entirely), human-in-the-loop policy, hyperparameter tuning, and initialization. Remaining limits: a human still defines success and intervenes, longer horizons strain the value function, and 19 minutes of robot time is not 19 minutes of training since gradient updates dominate wall clock.

## Why it matters

This is the clearest statement so far of what "RLHF for robotics" would actually require, and it reframes the bottleneck as protocol engineering rather than algorithm research. For anyone building on frontier policies, the practical read is that a pretrained VLA plus 20 minutes of supervised online interaction can reach near-perfect reliability on a specific task — a service-shaped deployment motion, not a research project. For investors, it says the defensible asset in robotics is the reset/reward/human-feedback infrastructure that makes post-training repeatable, because the algorithm alone is becoming public.

## Key points

- EXPO-FT: 30/30 success across six manipulation tasks, ~19 minutes average online interaction; baselines average 18.8 (SFT on π0.5), 20.5 (HG-DAgger), 19 (DSRL) and 5.5 (HIL-SERL).
- A single "pick up a glass" episode is ~500 control steps with a 7-D action every 20ms and reward only at the end — the credit-assignment problem that rules out LLM-style on-policy RL.
- Gaussian-action assumptions break diffusion policies; three existing workarounds each fail on stability, on actually teaching the policy, or on exceeding pretrained skills.
- EXPO(-FT) confines RL volatility to a small edit policy with bounded nudges, then distills accepted edits into the billion-parameter base model.
- Five missing protocol defaults: reward specification, resets, human-in-the-loop, hyperparameter tuning, initialization — LLM RLVR's "check the answer, check the tests" has no robotics equivalent.
- Honest limitations: human defines success, shorter horizons only tested, gradient updates dominate wall clock.

## Related

- [[signal-in-robotics-data-varunnair]]
- [[beginners-guide-physical-ai-stack-muskan-kalra]]
- [[interlatent-modern-ai-robotics-first-principles]]
- [[rlhf-from-first-principles]]
- [[reward-hacking-and-tampering]]
