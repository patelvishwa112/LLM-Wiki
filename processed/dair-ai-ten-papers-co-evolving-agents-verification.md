---
tags: ["papers", "agents", "evals", "mcp", "agent-memory", "skills", "verification", "self-improvement", "ml-research"]
source: https://x.com/dair_ai/status/2073814128888549810
date: 2026-07-05
type: bookmark
author: dair_ai
description: "DAIR.AI roundup of ten papers on co-evolving agents and evaluators, MCP server patterns, verification horizons, skill composition, metamemory, and scalable paper review."
summary: "DAIR.AI roundup of ten papers on co-evolving agents and evaluators, MCP server patterns, verification horizons, skill composition, metamemory, and scalable paper review."
raw: "[[raw/dair_ai_2073814128888549810]]"
---

# DAIR.AI — ten papers (agents, verification, MCP)

July 2026 **@dair_ai** thread: shared theme is **nothing stays frozen** — evaluators, verifiers, memory policies, and review pipelines must co-evolve with the systems they score.

## 1. Red Queen Gödel Machine
**Problem:** Static evaluators → reward saturation. **Idea:** Update utility/evaluator at epoch boundaries so agent and judge co-evolve (curriculum-like pressure).

## 2. MCP Server Patterns
Five named patterns from real MCP deployments (voice platform + registry): Resource Gateway, Tool Orchestrator, Stateful Session Server, Proxy Aggregator, Domain-Specific Adapter; plus anti-patterns and production concerns (auth, versioning, observability).

## 3. Verification Horizon (Qwen)
Coding-agent RL: stronger policies hack any **fixed** verifier. Study four verifier types (tests, rubrics, human, agent-as-judge) and three quality axes (scalability, faithfulness, robustness).

## 4. Paper Assistant Tool (Google)
Agentic **deep review** of full manuscripts (not skim). Progression: author aid → reviewer assistant → independent AI reviewer; toward agent-vetted preprint flows at conference submission scale.

## 5. Generative Skill Composition (SkillComposer)
Select **and order** skills in one autoregressive plan vs embedding retrieval. SkillsBench: beats top-3 retrieval, approaches gold-skill ceiling with fewer prompt tokens.

## 6. AutoMem (Stanford)
**Metamemory:** memory ops in the action space; scaffold + specialist meta-learning. Large long-horizon gains without changing task policy.

## 7. RLMF (Google + Yale)
Train calibration from **self-judgment quality** in preference optimization; SOTA faithful calibration.

## 8. ASPIRE
Robotics: continual code-as-policy, trace + skill library + evolutionary search.

## 9. HORIZON
EDA/hardware: markdown harness → eval pack; hands-free git worktree evolution on RTL benchmarks.

## 10. Reasoning quality emerges early (UCLA)
Early prefix / first-100-token loss predicts trace quality → cheap reasoning-data curation.

## Why it matters here

Aligns with the vault harness/eval cluster: **verifier and evaluator engineering** as first-class, not bolt-on. MCP patterns are actionable for MCP server design.

## Related

- [[macro-evals-for-agentic-systems-openai-cookbook]]
- [[verifiability-constraint-rlvr-unverifiable-tanayj]]
- [[2-ways-self-evolving-agents-model-harness]]
- [[self-learning-agents-three-layers-user-signal]]
- [[agent-memory-four-layer-stack-matthew-gunnin]]
- [[learn-harness-engineering]]
- [[langchain-fireworks-trace-judge-100x-cheaper]]