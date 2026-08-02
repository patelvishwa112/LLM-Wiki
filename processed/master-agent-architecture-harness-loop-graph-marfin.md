---
tags: ["agents", "agent-harness", "harness-engineering", "loop-engineering", "graph-engineering", "verification", "claude-code", "subagents", "production"]
source: https://x.com/marfinxx/status/2081687570488954915
date: 2026-08-01
type: bookmark
description: "Unifies harness, loop, and graph as nested production layers ending in adversarial red-team gate and state hashing."
author: marfinxx
summary: "Unifies harness, loop, and graph as nested production layers ending in adversarial red-team gate and state hashing."
raw: "[[raw/marfinxx_2081687570488954915]]"
---

# Master Agent Architecture: Harness + Loop + Graph

## Key Takeaways

- Failure modes of treating layers as rivals: endless retries without compile checks; 50-node graphs before one solid sub-agent; prompt thrash while ignoring the environment.
- Nested model: **Harness** (env, sandboxes, state, tool cache) ⊃ **Graph** (topology, fan-out, joins) ⊃ **Loop** (evidence checks, linters, retries) ⊃ model.
- **Harness:** CLAUDE.md + settings + hooks (pre_tool hash, post_tool audit) + memory (progress, tool_cache, git_checkpoint). State hashing stops re-reading unchanged files.
- **Loop:** evidence over confidence — unit tests, linters, schema validation, budget caps before “done.”
- **Graph:** parallel specialized sub-agents + sync gates; avoid unconstrained cycles.
- **5-stage pipeline:** sandbox init → parallel fan-out/scoping → local evidence-gated loops → hash/dedupe → **adversarial red-team gate** then commit/PR.
- Anti-patterns: loop on confidence; noisy full-repo context; unconstrained graphs; forcing deterministic work into the LLM.

## Why it matters

Cleanest single diagram that reconciles the vault’s harness / loop / graph clusters into one production stack with a skeptical final verifier.

## Related

- [[loop-graph-harness-pipeline-archiveexplorer]]
- [[learn-harness-engineering]]
- [[wtf-is-a-loop]]
- [[loop-engineering-clearly-explained]]
- [[graph-engineering-three-commitments-cyrilxbt]]
- [[aftermarket-harnesses-ttunguz]]
- [[own-your-intelligence-harrison-chase]]
