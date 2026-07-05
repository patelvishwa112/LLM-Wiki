---source_url: https://github.com/shepherd-agents/shepherd
ingested: 2026-07-05
author: shepherd-agents
title: "Shepherd — programmable meta-agents via reversible traces"
note: README excerpt from Firecrawl scrape of GitHub landing page
sha256: 73854a0dfd15e633b230d000d631c425166bcb063faf953ee108c207633316bc
---

# shepherd-agents/shepherd

**Shepherd: Programmable Meta-Agents via Reversible Execution Traces** (alpha)

PyPI: `pip install shepherd-ai` — https://pypi.org/project/shepherd-ai/

Runtime substrate for agent work needing inspection, reversibility, and supervision. Records agent runs as durable execution traces with retained workspace outputs reviewed before select/release/discard.

## Core idea

Tasks can be sandboxed agents whose work returns as **reviewable proposals** — nothing touches your files until accepted. Agent runs become Git-like traces: meta-agents observe, fork, replay, revert.

Copy-on-write fork ~5× faster than docker commit; ~95% KV cache reuse on replay (per project claims).

## Quickstart pattern

- `shepherd init` / `shepherd doctor claude`
- Task = Python function with no body; signature + docstring are the contract
- `shepherd run changeset --latest` inspect retained outputs
- `shepherd run select` / `discard` commit or drop

Offline quickstart uses deterministic provider (no API key).

## Links

- Docs: https://docs.shepherd-agents.ai/
- Paper: https://arxiv.org/abs/2605.10913
- Experiments: https://github.com/shepherd-agents/shepherd-experiments
- License: MIT