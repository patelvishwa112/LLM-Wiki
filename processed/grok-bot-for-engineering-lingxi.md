---
tags: ["agents", "multi-agent", "agent-ops", "agent-harness", "cronjob", "cursor", "verification", "xai"]
source: https://x.com/lingxi/status/2094493172516966781
date: 2026-08-31
type: bookmark
description: "Lingxi (xAI): Grok Bot mini-org — five domain engineer bots plus Jenny ops, Notion 30-min cadence, nightly audits, P0 steering of Cursor cloud agents."
author: lingxi
summary: "Lingxi (xAI): Grok Bot mini-org — five domain engineer bots plus Jenny ops, Notion 30-min cadence, nightly audits, P0 steering of Cursor cloud agents."
raw: "[[raw/lingxi_2094493172516966781]]"
---

# Grok Bot for Engineering

Lingxi Li (@lingxi, xAI, 2026-08-31). Dogfooding **Grok Bot** as a persistent intern that **orchestrates Cursor cloud agents** (including private workers / Mac mini — framed as replacing a 24/7 OpenClaw box). Claim: one person used to juggle ~15 cloud agents; the fleet now runs **200+**. Product pitch at the end.

## Mini-org shape

Five **domain** engineer bots (sharp specs inside ownership; they can cross but context is limited):

| Bot | Owns |
|-----|------|
| Baltata | mobile shared layer + iOS |
| Shaoruru | Desktop + CI/CD |
| Hogan | infra + unowned user issues |
| Craig | Android |
| Quill | Grok Bot harness |

**Jenny** = only non-coding bot (ops). 5 a.m. 1:1s vs playbook; onboarding; postmortems → playbook patch → announce to the others. Daily meetings treated as a **context-limit workaround**.

## Loops

- Kick Cursor cloud agent with personal skills (`/lingxi-design`, `/react-native-best-practices`, `/lingxi-review`, `/lingxi-product`); watch transcript; queue/interrupt; multimodal **screenshot proof** (before/after).
- Shared **Notion** every **30 min**: Bugbot/security, failing CI, merge conflicts → follow up or **Ready for Review** → auto code-review → **auto-merge** if high confidence + low blast radius.
- **Nightly 3 a.m. audits**: cleanup, perf, security, i18n, client parity, 24h PR catch-up; plus “six hours, build whatever.”
- **P0**: poll transcript every **5 min** and steer (token-expensive).

## Tips he emphasizes

Complete feedback loop (devtools / CLI / Accessibility) or package the unblock into a **repo skill**. Treat as a talented intern. Offload anything you do more than once a day. Hands-off like self-driving: free to ship when safe. Ops bot on **thinking traces** so mistakes don’t repeat.

## Skeptical read

- 2,000+ PRs / 4-week foundation / 3-week iOS v0 are **team marketing**, not audited here.
- Auto-merge + “meet my bar” is the load-bearing claim; no eval numbers.
- Vendor post (x.ai Grok Bot templates linked in-thread). Extract the **domain split + ops bot + 30-min board + proof loop**, not the productivity hockey stick.

## Related

- [[graph-engineering-dynamic-workflows-fleet-0xcodila]]
- [[second-brain-obsidian-night-shift-300-agent-swarm]]
- [[openclaw-hermes-supervisor-setup]]
- [[claude-code-four-loop-types-datasciencedojo]]
- [[eval-engineering-merge-gate-hanakoxbt]]
- [[no-process-no-agent-mardehaym]]
