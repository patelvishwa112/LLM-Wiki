---
tags:
  - anthropic
  - claude-code
  - software-factory
  - agent-harness
  - harness-engineering
  - evals
  - verification
  - skills
  - enterprise
source: https://claude.com/blog/the-ai-native-sdlc-playbook
date: 2026-08-21
type: article
author: louis-claxton
description: "Anthropic Applied AI playbook — rebuild SDLC around agents: intent.md through maintain loop; humans at gates; skills/hooks/evals as the control plane."
summary: "Anthropic Applied AI playbook — rebuild SDLC around agents: intent.md through maintain loop; humans at gates; skills/hooks/evals as the control plane."
raw: "[[raw/claude_ai-native-sdlc-playbook]]"
published: 2026-08-21
---

# The AI-Native SDLC playbook

Louis Claxton, Anthropic Applied AI, Aug 21 2026. 40-minute enterprise guide. Full text: [[raw/claude_ai-native-sdlc-playbook]].

## Thesis

Agents collapsed the **build** stage. The SDLC still assumes code is the expensive, human-written bottleneck. So plan / review / test / deploy stay human-speed, line-by-line review cannot keep up, and governance queues explode.

AI-native SDLC = same control **objectives**, new **enforcement**. Linear handoffs become a loop. Each stage **commits an artifact** the next stage reads. Humans stay accountable at gates, not as typists.

## Artifact chain

intent.md → spec.md → plan.md → diff+tests → PR+review findings → incident/intent again.

.md early (product owner + agent both act on it). Code later. Git history is the audit trail.

## Six plays (compressed)

1. **Plan** — originator brainstorms with Claude; product owner reviews committed `intent.md`. No prerequisites. Time-to-intent: weeks → hours.
2. **Design** — one session turns intent into `spec.md` under brand/security/UX **skills**. Product owner reviews flagged policy conflicts; does not write the spec. Design mocks via Claude Design then export to Claude Code.
3. **Build** — start in **plan mode**; accept `plan.md` before any edit. Auto mode once CLAUDE.md + skills + hooks + tests exist. CLAUDE.md = one-page joiner brief (mistake twice → write it down). Skills = institutional policy (advisory). Hooks = deterministic (block protected paths, format, secrets). Parallel worktrees + subagents (verifier reports, does not fix).
4. **Test** — session verifies itself (make test / screenshot) before a human sees it. Hook: agent cannot edit tests while fixing. Continuous **evals in CI** on CLAUDE.md/skills/hooks changes (20–50 real tasks). Incidents become evals.
5. **Deploy** — Claude reviews PRs via REVIEW.md (bugs/security/compliance vs spec+plan). Human code owner still approves. `@claude` fixes comments. Hooks as **approval gates** (production deploy needs named auth). Managed settings for regulated orgs: deny secrets/egress, sandbox fail-closed, managed hooks/MCP only. Agent may act **up to** the production gate, never past it. Rollback is the most rehearsed path.
6. **Maintain** — deterministic monitor breaches a control band → invoke Claude (1σ log / 2σ diagnose / 3σ propose PR or runbook) → writes `intent.md` → loop. Claude Tag: first responder in Slack; channel is the audit trail.

## Shifts vs traditional

| Stage | Old | New |
| Plan | committee → stories | intent.md from source |
| Design | analysts then designers | one agent session + skills |
| Build | handwritten + docs after | generated + CLAUDE.md/skills |
| Test | QA at boundaries | evals through implementation |
| Deploy | humans read every line | layered agent review; hooks as gates |
| Maintain | humans watch prod | agents diagnose; write next intent |

## Why it matters

This is Anthropic’s official “how to run the factory” — complements dzhng (ledger/seams), Foody (evals as PRD), Liu (skills as folders). The load-bearing idea: **committed artifacts + gates**, not smarter chat.

## Skeptical read

Product pitch for Claude Code / Cowork / Design / Tag / Enterprise. “Hours not weeks” is an Applied-AI-team claim, not a customer study. Two sources of truth (Jira + markdown) will be the real mess. Eval suites of 20–50 tasks will overfit.

## Related

- [[ai-native-engineering-org]]
- [[software-factories-no-slop-dzhng]]
- [[era-of-evals-brendan-foody]]
- [[skills-what-are-they-good-for-samzliu]]
- [[eval-engineering-merge-gate-hanakoxbt]]
- [[writing-good-skills-measured-rulebook-aparna]]
