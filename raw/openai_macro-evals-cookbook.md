# Macro Evals for Agentic Systems (OpenAI Cookbook)
URL: https://developers.openai.com/cookbook/examples/partners/macro_evals_for_agentic_systems/macro_evals_for_agentic_systems
Date: 2026-05-19

---

## Content

Official OpenAI cookbook on macro-evaluation for multi-agent systems.

When an agentic system fails, the problem is often larger than a single bad response. A handoff may happen too late, a specialist agent may miss the same signal across many runs, or a review process may trigger for the wrong class of cases.

Two-level evaluation approach:
- Lower-level evals: Grade individual agents, handoffs, tools, and completed runs (e.g., Promptfoo)
- Macro evals: Look across many lower-level findings to discover recurring behavior patterns

Key labels: case_type (business situation), run_outcome (how run ended), eval_finding (local symptom), behavior_pattern (population-level pattern)

The goal: move from thousands of agent events to a small number of patterns understandable by both technical and business stakeholders.

Uses a synthetic EV order workflow with specialist agents handling pricing, compliance, supply, factory routing, scheduling, and release decisions.
