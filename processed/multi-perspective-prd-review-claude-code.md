---
tags: [pm, prd, claude-code, agents, multi-agent, stakeholders, review, delegation, dynamic-workflows, product-management]
source: https://x.com/nurijanian/status/2066439099712741827
date: 2026-06-15
type: bookmark
author: nurijanian
summary: "Nurijanian (prodmgmt.world): parallel Claude Code reviewer agents (eng, design, exec, legal, UX, customer, devil's advocate) surface PRD objections before circulation — maps to dynamic workflows fan-out; packages as multi-perspective-review in PM OS."
raw: "[[raw/nurijanian_2066439099712741827]]"
---

# Multi-Perspective PRD Review (Claude Code)

**Problem:** Each stakeholder reads your doc with a different concern filter; killer objections show up in the live review, not in async comments.

**Pattern:** Bring the room to the doc first — seven fixed lenses, parallel read, merge objections while the doc is still private.

## Reviewer roster

| Lens | Typical catch |
|------|----------------|
| Engineering | Undefined terms, unscoped infra assumptions |
| Design | Missing states (especially empty/default) |
| Executive | Feature vs bet; goal linkage |
| Legal/risk | Data/compliance in channels you didn't model |
| UX research | Granularity of user control |
| Customer | Wrong motivation (e.g. "more notifications") |
| Devil's advocate | Weakest quantitative claim |

## Harness hook

Anthropic **dynamic workflows** (Claude Code, May 2026) — one request fans to many agents. Repeatable workflow name in article: `multi-perspective-review`.

## Fits your vault

- Same fan-out idea as [[dynamic-workflows-where-plan-lives]] and swarm/governance notes — applied to **PM docs**, not code.
- Complements [[pm-as-context-compressor]] (you compress context for others) and [[make-requirements-great]] (requirement quality).

## Related

- [[pm-as-context-compressor]]
- [[make-requirements-great]]
- [[testing-business-ideas-product-operating-system]]
- [[dynamic-workflows-where-plan-lives]]
- [[from-1-agent-to-swarm-orchestration-roadmap]]