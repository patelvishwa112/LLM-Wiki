---
title: From 296 Agents to One Graph
type: bookmark
description: "Survey-grounded case that harness, loop, and graph are distinct layers; measured agent repos show nearly no committed loop state and 68 confirmed infinite-loop failures."
tags: [agents, loop-engineering, graph-engineering, agent-harness, orchestration, verification, langgraph]
source: https://x.com/N01ennn/status/2096962591125905888
date: 2026-09-07
author: NO1ennn
summary: "Survey-grounded case that harness, loop, and graph are distinct layers; measured agent repos show nearly no committed loop state and 68 confirmed infinite-loop failures."
raw: "[[raw/N01ennn_2096962591125905888]]"
---

# From 296 Agents to One Graph

**Source:** NO1ennn, 2026-09-07. Long-form X article tying three arXiv/repo-empirical studies together: loop engineering's short history, a scan of real agent loops in the wild, a failure taxonomy for infinite agentic loops, and where GPT-6 Astra fits.

The article's spine is a separation of three layers that get used interchangeably: the harness (context, tools, permissions, persistence, observability — what the model can touch and how execution is constrained), the loop (observe/act/verify with explicit triggers and evidence-based stopping rules), and the graph (topology of nodes and edges that decides which step runs next, under what condition, with what state). The mnemonic offered is that the harness makes the model operate, loops make execution iterative and resumable, and graphs make control flow inspectable. Conflating them yields specific expensive mistakes: drawing topology before behavior is understood, letting a model grade its own work, unbounded retries, and over-broad tool grants.

Its strongest contribution is replacing discourse with measurement. A scan of 36,710 engineered software repositories, with 256 inspected by hand, confirmed 217 autonomous agent loops — 0.59% of the corpus, 189 of them Claude Code. Their shape contradicts the literature: 180 trigger on repository events (mostly per-PR review), 21 on a schedule (mostly issue triage), 15 on both. Across all 36,645 scanned repos there were two state files (both false positives), zero verifier subagents, zero budget files, zero measured cost logs, and zero machine-checkable stop conditions. The author's explanation is structural rather than cultural: a per-PR review run has nothing to persist, and a triage run inherits state from the tracker, so the prescribed committed-state pattern assumes a loop shape most projects do not run. The grim illustration is an hourly Gemini triage workflow in AI-Hypercomputer/xpk that logged 6,290 successful runs and zero agent executions, because its issue-search gate never matched.

The failure side comes from IAL-Scan: 6,549 agent repositories (246,748 Python files, 33.41M lines) yielding 74 findings, 68 confirmed infinite agentic loops across 47 projects at 91.9% precision. Every confirmed case had a missing strong bound; 41.2% involved tool-controlled retry, 38.2% model-controlled termination, 33.8% a missing exit, 27.9% state-growth amplification — producing API cost exhaustion and model denial of service in 95.6% of cases. LangGraph (23) and AutoGen (22) account for 45 of the 68 because their feedback paths are expressed through APIs (`add_conditional_edges`) rather than visible `while True`. Every framework ships a limit — `max_iterations`, `max_turns`, `recursion_limit`, `max_iter` — so the bug is a bound that does not cover the actual feedback path, not an absent feature.

The constructive half formalizes this as `Agent = Loop(LLM + Harness)`, notes three limits of single-agent loops (serialized interdependent work, writer and verifier collapsed into one role, state-as-context losing provenance), and answers with graph engineering's three views: task organization, agent coordination, and runtime state management. LangGraph specifics carry the concrete lesson — Pregel super-steps, per-key reducers where a merging reducer silently defeats field clearing (use `Overwrite`), `Command(goto=...)` for routing, `Send` for map-reduce fan-out, and the difference between catching `GraphRecursionError` at the default 1000-super-step ceiling versus reading `RemainingSteps` proactively so the graph can reach a completion node and return a partial result.

## Why it matters

If you are building agents, the two scans are a calibration check: almost nobody is running the committed-state, verifier-subagent loop the literature prescribes, and nearly all silent loop failures come from a bound that sits outside the repeating path. The actionable test is mechanical — trace your own feedback cycles and confirm the retry cap, timeout, and context guard are on that cycle, not on an inner call.

For anyone costing agent fleets, the Astra economics matter: appending to `messages` each iteration walks toward a 272K-token pricing cliff where the whole request bills at 2x input and 1.5x output, and since `none` reasoning effort is unsupported, every node call reasons. Unbounded loops got more expensive per iteration, not less.

## Key points

- Three distinct layers: harness = capability/permission envelope; loop = iterative execution with evidence-based stop; graph = inspectable control flow. "Harness makes it operate, loops make it resumable, graphs make control flow inspectable."
- Corpus scan: 36,710 repos → 217 confirmed autonomous agent loops (0.59%); 189 of 217 are Claude Code; 180 event-triggered, 21 scheduled, 15 both.
- Across 36,645 repos: 0 verifier subagents, 0 budget files, 0 measured cost logs, 0 matching stop conditions, 2 state files (both false positives). Configuration is committed; runtime state is not.
- AI-Hypercomputer/xpk: 6,290 green hourly runs, zero agent executions — a successful run is weak evidence anything happened.
- IAL-Scan: 6,549 repos, 246,748 files, 33.41M lines → 68 confirmed infinite agentic loops in 47 projects, 91.9% precision; 100% missing a strong bound; 95.6% API cost exhaustion / model DoS.
- Failures hide in framework APIs: LangGraph 23 + AutoGen 22 = 45 of 68, because `add_conditional_edges` shows no `while True`. Existing limits (`recursion_limit` 1000, `max_turns`, `max_iter`) don't help when set outside the repeating path.
- LangGraph mechanics: per-key reducers mean an empty update merges instead of clearing (use `Overwrite` for retry counters); `RemainingSteps` lets a graph degrade to a fallback node and checkpoint partial state instead of raising at the ceiling.
- Astra integration: async tool calling maps onto parallel super-step branches; mid-turn steering is escalation without restarting the node; `configuration_update` changes reasoning effort per node while preserving the prompt cache; misalignment monitoring ships in the model tier.
- Astra cost: $10/$50 per 1M input/output, $1 cached, 1.05M context, but >272K input tokens bills the entire request at 2x input / 1.5x output; no `none` effort means every node call reasons.
- Zero-trust rules: progress only on evidence (test/deploy green), cap retries on the feedback path, verified output or logged refusal as the only terminal states, permissions per step not per session, the human owns the graph.

## Related

- [[three-layers-harness-loop-graph-lunarresearcher]]
- [[master-agent-architecture-harness-loop-graph-marfin]]
- [[loop-graph-harness-pipeline-archiveexplorer]]
- [[fault-tolerance-langgraph-retries-timeouts]]
- [[graph-engineering-three-commitments-cyrilxbt]]
