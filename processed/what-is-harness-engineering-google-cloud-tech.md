---
tags:
  - harness-engineering
  - agent-harness
  - agents
  - coding-agents
  - sandbox
  - verification
  - loop-engineering
  - observability
  - google-adk
  - antigravity
  - codex
source: https://x.com/GoogleCloudTech/status/2091986652595950079
date: 2026-08-24
author: Google Cloud Tech (@GoogleCloudTech), by @shirmeir86
type: bookmark
description: "Google Cloud Tech on harness engineering: the deterministic shell around a model — sandboxed boundaries, automatic repair loops, a discoverable repo map — with runnable Antigravity + ADK code."
summary: "Harness engineering means designing the deterministic environment around the model — strict sandbox boundaries, repair loops that feed failures back, and a repo map instead of a giant manual — illustrated with Antigravity SDK + ADK 2.0 graph workflows."
raw: "[[raw/googlecloudtech_2091986652595950079]]"
status: current
as_of: 2026-08-24
---

# What Is Harness Engineering and Why Should I Care?

Google Cloud Tech's answer to "how do you ship a product with zero manually written lines of code?" The answer is not a better model — it is **the harness**: every deterministic component that wraps the LLM. A cited experiment: 3 engineers shipped an internal beta where application code, tests, CI, docs, observability and tooling were all written by Codex, because *they designed the harness instead of writing the app*.

## Definition

The racehorse framing: the harness is the track, the blinders, and the reins. Concretely (via Balaji Subramaniam) it is the **orchestration layer, execution sandboxing, state persistence, and verification tools**. Arthur Thompson's version: "all the deterministic components that wrap the LLM."

The job shift: from writing logic to designing the environment.

## Three practices

1. **Strict boundaries** — don't let the agent guess what it can touch. Confine it to a sandbox so it cannot wipe production data; enforce access rules in the runtime, not in the prompt.
2. **Repair loops** — agents will fail builds and tests. A good harness traps the error, feeds clean logs back, lets the agent fix itself, and has a **kill switch** so a breaking/fixing loop cannot spin forever.
3. **A map, not a manual** — structure the repo so the agent discovers context progressively; huge instruction files overwhelm it (the post cites the OpenAI team's finding).

## The code (the useful part)

Antigravity SDK + ADK, with containment expressed in config rather than prose:

```python
sandbox_dir = os.path.abspath("./sandbox"); save_dir = os.path.abspath("./trajectories")
sdk_config = LocalAgentConfig(
    system_instructions="You are a helpful local environment assistant.",
    workspaces=[sandbox_dir],        # hard containment
    policies=[policy.allow_all()],   # allowed *inside* the sandbox
    save_dir=save_dir,               # trajectory memory
)
root_agent = AntigravityAgent(name="antigravity_assistant", config=sdk_config)
```

Then tests become graph nodes, not a separate script — `execution_test_node` increments `iteration_count`, routes `END` on pass or after `iteration_count > 5` (the kill switch), and otherwise returns the traceback with `route="loop_back"`. The workflow is two edges:

```python
repair_loop = Workflow(name="repair_loop", edges=[
    ("START", root_agent, execution_test_node),
    (execution_test_node, {"loop_back": root_agent}),
])
```

That is the whole self-healing loop: agent → test → (pass | error back to agent, max 5 tries).

## Verdict

The most **concrete** harness recipe in the vault so far: containment, memory directory, routing graph and iteration cap in ~40 lines you can copy. It converges with the diagnosis in [[why-harness-engineering-is-so-hard-winterarc]] — constraints belong in code/schemas, not in longer prompts — and with [[harness-engineering-2026-discipline]]. Caveat: the "0 lines of manually written code" claim is second-hand and unverifiable from the post; treat it as a directional anecdote, not a benchmark.

## Related

- [[harness-engineering-2026-discipline]]
- [[why-harness-engineering-is-so-hard-winterarc]]
- [[learn-harness-engineering]]
- [[agent-harness-engineering-claude-14-step-roadmap]]
- [[coding-agent-harness-eight-pillars]]
- [[deepseek-harness-five-patterns-saboo]]
