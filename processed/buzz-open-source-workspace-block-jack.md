---
tags: ["agents", "agent-harness", "enterprise", "open-source", "nostr", "block", "goose", "claude-code", "codex", "multi-agent", "agent-ops", "cryptographic-identity", "context-management", "decentralization"]
source: https://x.com/jack/status/2080056638820450400
date: 2026-07-23
type: bookmark
description: "Jack Dorsey/Block open-sources Buzz — self-hosted Nostr workspace where people and agents share cryptographic identity, one event log, and harnesses for Goose/Codex/Claude Code."
author: jack
summary: "Jack Dorsey/Block open-sources Buzz — self-hosted Nostr workspace where people and agents share cryptographic identity, one event log, and harnesses for Goose/Codex/Claude Code."
raw: "[[raw/jack_2080056638820450400]]"
---

# Buzz — open-source workspace for people + agents (Block / Jack)

**@jack** announces **Buzz** (Apache 2.0): an open-source workspace from **Block** that puts people, agents, conversations, and code behind **one cryptographic identity system**, aimed at reducing dependency on Slack + GitHub.

## Key takeaways

- **Problem = context seams.** Work is scattered across chat, code host, CI, and agent tools. Every seam drops information; agents suffer most because they cannot help with what they cannot see.
- **Block context.** Block is “rebuilding itself to be an intelligence.” **Goose** (agent substrate, open-sourced early 2025) already runs company-wide; tool seams became the limit. Buzz is the product-shaped answer.
- **Unified signed event log.** Everything (messages, patches, reviews, workflow steps, approvals) is a **signed event on a self-hosted relay**. One record, one search, full audit trail.
- **Agents as equal members.** Agents get keys/channels like humans: search history, open repos, send patches, review code, run workflows, edit canvases — actions **signed and attributable**.
- **Principles:** self-sovereign (own relay/domain/keys); open (Nostr, model-agnostic, harnesses for Goose/Codex/Claude Code, no lock-in); **one context** (feature branch = channel; discussion + patches + CI + merge in one permanent thread).
- **Shipped now vs next.** Today: channels, threads, DMs, canvases, media, search, audit log, workflows, desktop app. In progress/planned: full git hosting, mobile/push, approval gates, relay federation, private agent scoping, hosted option, token efficiency, workflow/agent ecosystem, agents that can **transact**.
- **Framing: “truly social AI.”** Not companion chat or agent-only swarms humans watch — people *and* agents as equal network members doing real work.

Links: https://buzz.xyz · https://github.com/block/buzz

## Why it matters

Enterprise agent notes in the vault (Sierra singular agent, Glean harness, software factories) keep hitting the same wall: **tool fragmentation kills agent context**. Buzz is a first-party, open-protocol bet (Nostr + crypto identity + audit) that the right unit of collaboration is a **shared signed workspace**, not glue between Slack and GitHub. Worth tracking for harness design, agent identity/accountability, and open multi-agent ops.

## Skeptical read

Early product; full git hosting and approval gates incomplete. Self-hosted relay + federation path is ambitious — adoption will hinge on ops cost vs Slack/GitHub gravity and whether “agents that can transact” stays vision or ships with real rails. Jack’s Nostr/Bitcoin lineage colors the architecture; useful if the open event model wins, less so if teams just want hosted SaaS with good agent hooks.

## Related

- [[sierra-pinecone-singular-company-agent]]
- [[glean-coding-harness-programmatic-tool-calling]]
- [[software-factory-linear-claude-cloud-routines]]
- [[how-to-build-custom-agent-harness-langchain]]
- [[harness-is-the-product-context-aware-agents]]
- [[agent-harness-engineering-agentforge]]
- [[from-1-agent-to-swarm-orchestration-roadmap]]
- [[post-agent-companies]]
