---
title: Xiaomi MiMo open-sources agentic RL environments and verl training code
type: bookmark
description: "MiMo's OSS release: five agentic RL environments (code, cyber, general, webdev, music) with verifiers, graders and launch scripts on a verl 0.9.0.dev fork, plus the 9B SFT checkpoint and 77.4B-token data."
tags: [rl-environments, rl, training, post-training, agent-harness, open-source, qwen]
source: https://x.com/eliebakouch/status/2103670720249164197
date: 2026-09-26
author: "elie"
summary: "MiMo's OSS release: five agentic RL environments (code, cyber, general, webdev, music) with verifiers, graders and launch scripts on a verl 0.9.0.dev fork, plus the 9B SFT checkpoint and 77.4B-token data."
raw: "[[raw/eliebakouch_2103670720249164197]]"
---
# Xiaomi MiMo open-sources agentic RL environments and verl training code

**Source:** elie (@eliebakouch), 2026-09-26. A two-line pointer post to Xiaomi's released RL environments and training code; all substance below comes from the linked repositories.

The post itself says only "xiaomi MiMo oss RL environments + training code" and links `github.com/XiaomiMiMo/verl`. That repo is a fork of verl (0.9.0.dev, branch `mimo-oss`, 736 stars, created 2026-09-21) whose README describes it as "Agentic RL training code for MiMo," with the recipe in Section 7 of the MiMo-V2.6 technical report. The fork adds reproduction code for five environments, each pairing a task family with an explicit verifier and a launch script — executable tests for software engineering, rule checks for vulnerability reproduction, rubric-based judging for knowledge work, visual grading for web development, rule checks for symbolic music composition. Training data ships as per-domain parquet configs under Apache-2.0, and container images are published separately, so the harness side is reproducible rather than described.

What makes the release concrete is that the verifier is the product. Each domain is a different answer to "how do you score a rollout without a human," and the mix spans the cheap end (executable tests, rule checks) and the expensive end (rubric judges, visual graders). The 9B model card in the same release quantifies what that buys as supervised fine-tuning data: 77.4B total tokens with 27.2B loss-bearing, split Code 23.2B, Cyber 11.0B, General 22.0B, Visual 21.2B.

The repo also documents the anti-hack posture, which is the part practitioners usually learn the hard way: as of 2026-10-19 the Code images ship with anti-hack preprocessing applied and `anti_hack_cleanup: true` must stay on in the provided configs. Agent harnesses live in submodules (`mimoagent`, a mini-swe-agent fork, and `uni-agent` for the model gateway and trajectory capture) with thin glue in `recipes/`, so the environment, the harness, and the trainer can be swapped independently.

## Why it matters

Open RL environments, not open weights, are the current bottleneck for anyone doing agentic post-training: the reward function is where the engineering lives. MiMo is publishing five verifier-equipped families with launch scripts and images, which means a small team can reproduce a frontier-style agentic RL loop instead of building sandboxes and graders from scratch. The anti-hack preprocessing is a direct signal that verifier gaming — not capability — is the failure mode to design around when you train against code execution.

## Key points

- Five domains with distinct verifiers: Code (executable tests), Cyber (vulnerability reproduction, rule checks), General (rubric judging), Visual (web development, visual grading), Music (symbolic composition, rule checks).
- Built on verl 0.9.0.dev; per-domain launch scripts (`scripts/code/train.sh`, `scripts/arvo/arvo.sh`, `scripts/general/general.sh`, `scripts/design/webdev.sh`, `scripts/design/music.sh`) read variables from adjacent `*.env.example` files.
- Starting checkpoint `MiMo-V2.6-Distill-Qwen-9B` is SFT of Qwen3.5-9B on 77.4B tokens (27.2B loss-bearing); SFT alone moves SWE Pro 32.0 → 44.6, MiMo Cyber mini 5.7 → 31.3, AutomationBench 5.0 → 30.3, JobBench 2.6 → 18.3.
- Data: `XiaomiMiMo/MiMo-V2.6-RL-oss`, Apache-2.0, one parquet config per domain (code, cyber, general, webdev, music).
- Anti-hack preprocessing is mandatory in the Code images as of 2026-10-19 (`anti_hack_cleanup: true`); graders and execution environments live in the `mimoagent` fork, not in the trainer.
- Code uses `uni-agent` for the model gateway and TransferQueue trajectory capture; Cyber, General and Visual drive `mimoagent` straight from a verl AgentLoop; Music uses neither.

## Related

- [[harbor-rl-coding-environments]]
- [[rl-environments-guide-llm]]
- [[why-rl-environments-work-now-paniego]]
- [[slime-open-source-rl-kernel-glm-dailydose]]
- [[how-we-build-agent-environments-vtrivedy]]
