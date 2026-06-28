---
tags:
- agents
- multi-agent
- architecture
- prompt-engineering
- rl
source: https://x.com/neural_avb/status/2054906931664585027
raw: '[[raw/neural_avb_2054906931664585027]]'
date: 2026-05-14
type: processed-note
related:
- '[[iii-agent-harness-workers]]'
- '[[coding-agent-harness-eight-pillars]]'
description: 'RLM: Recursive LLM Querying System Prompt'
---

# RLM: Recursive LLM Querying System Prompt

## Summary
The full system prompt for the RLM (Recursive Language Model) repo — an architecture where a parent LLM with ~1M character context splits queries across sub-LLMs in 100K-char chunks using an interactive REPL environment. The system prompt defines how the agent accesses context, invokes recursive sub-agents via `llm_query`, and returns results via `FINAL`.

## Key Takeaways
- **Context paradigm**: ~1M chars total context, split into five 100K-char chunks for sub-LLM queries
- **REPL environment**: Agent interacts with a `context` variable and a `llm_query` async function that recursively calls sub-LLMs
- **Return values are Python objects**: `llm_query` returns native Python objects (dicts, lists, strings), not raw text — no need for `eval()` or `json.loads()`
- **FINAL function**: A global function for returning results as strings or native Python data types
- **Leaf agent separation**: A separate prompt for leaf agents that don't have access to `llm_query` (preventing infinite recursion)
- **Intent propagation**: When invoking recursive sub-agents, the parent must pass through the user's original intent and desired level of detail

## Connections
- [[iii-agent-harness-workers]] — similar worker delegation pattern for distributed agent tasks
- [[coding-agent-harness-eight-pillars]] — the architectural pillars this recursive design draws from
