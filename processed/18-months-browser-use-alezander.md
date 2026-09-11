---
tags: ["browser-agents", "evals", "agents", "agent-harness"]
source: https://x.com/Alezander9/status/2095329845811237064
date: 2026-09-03
type: bookmark
description: "Alexander Yue (Browser Use #2): eval-first; label your own traces; simple judge prompt beat agentic judges; code-exec over fixed actions; Slack-native evals."
author: Alezander9
summary: "Alexander Yue (Browser Use #2): eval-first; label your own traces; simple judge prompt beat agentic judges; code-exec over fixed actions; Slack-native evals."
raw: "[[raw/Alezander9_2095329845811237064]]"
---

# 18 Months Building and Evaluating Agents at Browser Use

Alexander Yue (@Alezander9), engineer #2 from Mar 2025. Path to a better agent is measurement. Built evals from scratch; observability first; later Laminar as trace SoT (owning millions of traces is a product you don't sell).

Public benchmarks ≠ user traffic. Clustered real tasks; real success far below benches. **Label your own data** (~20h, few hundred labels to validate a judge). One carefully written judge prompt beat every agentic judge. Then a judge that learns across runs + parallel rubric vs the live web.

First eval platform: heavy UI, became untrusted. Second: no UI, config-as-code, restricted writes, CI, **Slack-native** trigger/results. Never tolerate a lost run. Track variance because the live web moves. Unlimited eval budget (~$100+/full run) is the cheap part.

BU_Bench_V1: 100 hand-selected public tasks from usage analysis; became default browser-agent bench; now saturated (>10 models >90%). v2 from anonymized real tasks. Internal ranking matched Odysseys academic bench.

v3 API scored better, felt worse. Code-exec harness (browser-harness / JS / forked coding agent + CDP) beat fixed action menus. Deleted helpers for models that already speak the protocol; paid off when cheap frontier arrived. Cloud + persistent workspace (email, phone, card). Agent writes harness bugs to a file. Fun experiments (game mode, Slack fleet) produced roadmap-unplannable assets.

Regret: CI poor as RL sandbox (reward hacking). Thesis: agent improvement is entirely about evaluation.

## Related

- [[astra-computer-use-a11y-kylejeong]]
- [[llm-as-judge-architectures-runtime-joshrosen]]
- [[why-rl-environments-work-now-paniego]]
