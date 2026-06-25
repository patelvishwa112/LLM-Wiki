---
tags: ["terse", "modal", "claude-code", "agent-security", "prompt-injection", "litellm", "sandbox", "automated-learning", "workflows", "defense-in-depth"]
source: https://x.com/oliviersm199/status/2069790892530016547
date: 2026-06-24
type: bookmark
author: oliviersm199
summary: "Terse CTO Olivier Morissette on weekly workflow review loops via Modal sandboxes and Claude Code, with six application-layer defenses against attacker-controlled code and logs."
raw: "[[raw/oliviersm199_2069790892530016547]]"
---

# Secure Automated Learning Loops (Terse, Modal, Claude Code)

Terse (AI workflow platform) emails **weekly improvement suggestions** for each deployed workflow by analyzing production logs + source, then lets users apply patches via **`terse apply`**. The hard part is running **Claude Code over tenant-controlled inputs** without prompt injection, exfiltration, or runaway API spend.

## Key takeaways

- **Loop:** deploy context + logs → Modal sandbox → Claude Code CLI → structured patches → human review → CLI apply — aligned with "systems that improve with each use."
- **Threat:** User workflow source and logs are **attacker-controlled**; naive agent+tools + raw API keys + open egress = exfiltration or bill shock.
- **Modal base:** gVisor isolation, ephemeral FS, resource/time limits — infrastructure trust boundary.
- **Six app layers:** (1) egress allowlist to LiteLLM proxy only, (2) prebaked image (no runtime downloads), (3) short-lived budget/rate-capped virtual keys revoked post-run, (4) env-only credentials, non-root exec, (5) Claude Code tool denylist (curl, WebFetch, …), (6) **prompt sanitization** with `<untrusted field="…">` wrappers, control-char strip, truncation, tag-breakout neutralization, and explicit "data not instructions" preamble.
- **Product point:** Secure loops make encoding production edge cases into workflows nearly frictionless.

## Why it matters

Concrete reference architecture for **production agent improvement loops** where inputs are hostile — pairs loop hype with security engineering (proxy-scoped keys, sandbox egress, tool policy, untrusted-content marking) beyond "run Claude on customer logs."

## Related

- [[zero-trust-ai-agents]] — Enterprise zero-trust framing for agent access
- [[managed-agents-sandbox-mcp]] — Anthropic managed agents + Modal-class sandboxes
- [[how-to-give-your-agent-memory]] — Trace → analyze → update durable context
- [[loop-engineering-clearly-explained]] — Loop engineering vocabulary for production agents
- [[agent-harness-engineering-agentforge]] — Harness safety and prompt-injection awareness