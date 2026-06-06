---
source_url: https://x.com/adithya_s_k/status/2054961319179420035
title: "RL Coding Environments 101: Why Harbor Exists"
author: "@adithya_s_k (Adithya S K)"
published: 2026-05-14
ingested: 2026-06-01
sha256: 18c1fe24773865b6f0822c675ddd7e698fef6d06d635a165e4086c9f39ef1cfe
platform: X (Article)
tags: ["rl", "agents", "evals", "coding-tools", "training", "environment"]
stats: "31.6K views, 510 bookmarks, 329 likes, 29 reposts"
---

# RL Coding Environments 101: Why Harbor Exists

By Adithya S K | May 14, 2026 | 31.6K views, 510 bookmarks

## Content

Coding as an RL task is having a moment. And if you've actually tried to do RL on a coding task, you already know the model is the easy part. It's everything around the model that eats your week.

> disclaimer: I have used Claude Code with Claude Opus to help me put this together but I've been working with Harbor pretty extensively across a bunch of projects.

You need a real environment. Right toolchain, right system libs, deps pinned, GPU drivers if you need them, a way to reset state between rollouts. You need to pick a coding harness. Claude Code? Aider? OpenHands? Your own scaffold? You need initialization points. What commit, what starting prompt, what files does the agent see first? And you need a reward you can actually trust. Run the tests, score the diff, ask a judge, all of the above.

Every one of those decisions is its own rabbit hole, reinvented from scratch every time someone publishes a new coding benchmark or RL recipe. This blog is about why that's not sustainable, and why the answer is starting to look like a framework called **Harbor**.

## RL on code is winning because the reward is mostly verifiable

Everyone moved to the same idea: stop pretending pretraining is enough, train against signals that compile and run. pytest doesn't lie.

A non-exhaustive tour:
- **Meta's SWE-RL**: Trained Llama3-SWE-RL-70B with rule-based reward (diff similarity against ground-truth PR patches) on millions of merged PRs. Hit 41% on SWE-bench Verified. (https://github.com/facebookresearch/swe-rl)
- **OpenAI's Codex (codex-1)**: Version of o3 trained with RL on real-world coding tasks across many environments. o3 jumped from 48.9% to 71.7% on SWE-bench Verified.
- **DeepSeek-R1** (Nature, 2025): Showed you can get reasoning from pure RL with verifiable rewards, no SFT warm-up. Used GRPO and compiler feedback on LeetCode problems as signal.
- **Moonshot's Kimi K2**: Introduced "Gym-like extensible framework" for scaling RL across diverse coding scenarios. 65.8% on SWE-bench Verified with just a bash/editor harness.
- **Qwen3-Coder-Next**: Explicit that large-scale synthesis of verifiable coding tasks paired with executable environments is the central training advance.
- **Prime Intellect's INTELLECT-3**: 100B+ MoE trained with large-scale RL across thousands of community-contributed environments.
- **Anthropic's Claude 4.x**: Reportedly scaling RL environment spend 3 to 5x into 2026.

The thesis is now consensus: coding is uniquely well suited to RL because the reward is verifiable. You can run the code and check. No reward model, no human-labeled preferences, no drift.

## The new bottleneck isn't the model. It's the environment.

The moment you commit to RL with verifiable rewards, your training run is only as good as the environments you can spin up. And environments are hard.

> "The current ecosystem for environments is fragmented. Implementations are often tightly coupled with a specific training stack, making them difficult to adapt, reuse, or share..." — Prime Intellect, Environments Hub announcement

Wing Venture's analysis: "verification, not models, is the true bottleneck to automation."

MiniMax's Forge framework runs RL training across 100,000+ distinct agent scaffolds and environments with daily throughput in the millions of samples. That's an infrastructure problem.

Every coding environment needs three things:
1. A frozen state or snapshot (specific commit, codebase, pinned deps)
2. A way to run it (Docker image with right toolchain)
3. A way to score the agent's output (tests, diff, judge model, custom verifier)

Every benchmark team rebuilds this from scratch. SWE-bench has its harness. R2E has its own. Magicoder has its own. Agents can't move between benchmarks, datasets can't compose.

## Enter Harbor

Harbor (https://github.com/harbor-framework/harbor) is a coding-environment framework from the team behind Terminal-Bench. Announced alongside Terminal-Bench 2.0 by @Mike_A_Merrill and @alexgshaw.

A Harbor task is a directory with four files:

```
hello-world/
├── instruction.md          # What the agent should do, in English
├── task.toml               # Typed config: timeouts, resources, metadata
├── environment/
│   └── Dockerfile          # (or docker-compose.yaml)
├── solution/
│   └── solve.sh            # Optional oracle solution
└── tests/
    └── test.sh             # Verifier: writes reward to /logs/verifier/
```

Each file answers exactly one question:
- environment/Dockerfile → how do I run this?
- instruction.md → what should the agent do?
- tests/test.sh → how do I know it succeeded?
- task.toml → who built this, for what, with what limits? (typed schema: CPU/memory/GPU, internet allowlist, MCP servers, container healthchecks, verifier API keys)

A trivial verifier is just a bash script that writes a number. For multi-metric rewards you write reward.json (e.g. {"correctness": 0.75, "structure": 1.0}). The reward is just numbers in a known location. That uniformity is the entire trick.

## Bring your own agent harness

Harbor ships with **26 built-in agent adapters**: Claude Code, Codex CLI, OpenHands, Gemini CLI, Aider, Goose, Cursor CLI, Cline CLI, Copilot CLI, OpenCode, Qwen Coder, Kimi CLI, Mini-SWE-Agent, SWE-Agent, Trae Agent (ByteDance), Rovodev (Atlassian), NeMo Agent (NVIDIA), plus Harbor's own Terminus-2 reference agent and an oracle adapter.

The contract for a custom harness: subclass BaseAgent, implement setup() and run(), run with --agent-import-path your.module:YourAgent. Any task works with any agent. Train with one harness, eval with another, ship a third. This is the USB-C of agent harnesses.

## Rewards beyond pass/fail

The reward contract (numbers in /logs/verifier/reward.{txt,json}) is thin on purpose:
- **Test-execution rewards**: run pytest/cargo/jest, write 1.0 or 0.0
- **Diff-similarity**: partial credit for partial fixes (the SWE-RL recipe)
- **LLM-as-a-judge**: verifier shells out to a judge model, gets back 0-1 score. API keys flow through task.toml
- **Step-level rewards**: Multi-step tasks emit per-step verifier_results, aggregated by MEAN or FINAL
- **Reward Kit**: `harbor-rewardkit` with 20+ built-in primitives (file_exists, command_succeeds, ...) plus TOML-defined LLM judges and agent-as-judge rubrics

## The uniform output spec: ATIF

Every agent's output looks the same. **ATIF** (Agent Trajectory Interchange Format, RFC-0001, currently v1.7). Whether you ran Claude Code, OpenHands, Codex, or your own scaffold, Harbor's adapters convert the trace to uniform JSON: per-step records with source, model_name, message, reasoning_content, tool_calls, observation, and metrics (token counts, cached tokens, cost in USD).

The version history reads as Harbor figuring out what RL pipelines need:
- v1.3: completion_token_ids "to enable RL training without retokenization drift"
- v1.4: prompt_token_ids
- v1.5: tool_definitions for SFT pipelines

Harbor has dedicated docs for SFT and RL workflows, and ships a SkyRL integration. Same task spec → same execution sandbox → same reward signal → same trace format → trainable. No reshaping, no glue code.

## Getting started

```bash
uv tool install harbor
export ANTHROPIC_API_KEY=<YOUR-KEY>
harbor run --dataset terminal-bench@2.0 --agent claude-code --model anthropic/claude-opus-4-1 --n-concurrent 4

# Single task with oracle
uv run harbor run --agent oracle --path ./tasks/hello-world
# Mean: 1.000 ✓
```

10+ sandbox backends behind one flag: Local Docker, Daytona, Modal, E2B, Runloop, Apple Container, GKE, Tensorlake, Islo, Singularity.

50+ benchmark adapters: SWE-Bench family, Aider Polyglot, LiveCodeBench, GAIA, BFCL, MedAgentBench, ML-Dev-Bench, and more.

Inspect with `harbor view`, a local web UI that renders trajectories, per-criterion reward breakdowns, and collected artifacts.

## Why this matters now

The next year of frontier coding-model work is going to be dominated by who can stand up the most environments, the fastest, with the highest verification fidelity. The bottleneck is shared infrastructure. Harbor is the simplest version of that shared infrastructure that doesn't lose. Four files, any agent, 10+ sandboxes, uniform trainable traces.
