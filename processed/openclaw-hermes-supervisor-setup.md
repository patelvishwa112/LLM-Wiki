---
tags:
- hermes
- agents
- multi-agent
- orchestration
- openclaw
- discord
- supervisor
source: https://x.com/gkisokay/status/2037902655016804496
date: 2026-03-28
type: bookmark
author: Graeme Keith (@gkisokay)
raw: '[[raw/gkisokay_2037902655016804496]]'
description: 'The Setup That Saved Me Hours Every Day: OpenClaw + Hermes Supervisor'
---

# The Setup That Saved Me Hours Every Day: OpenClaw + Hermes Supervisor

## Key Takeaways

- **Supervisor pattern: Hermes watches, OpenClaw works, you verify.** Two bots, two roles, one human. Hermes monitors output channels, ACKs clean outputs, escalates issues with specific reasons. No more reading error logs or debugging outputs manually.
- **Intent marker protocol prevents chaos.** Four markers: [STATUS_REQUEST], [REVIEW_REQUEST], [ESCALATION_NOTICE], [ACK]. Every message in the coordination channel requires exactly one marker + @mention. No marker → ignored. [ACK] is terminal — no reply allowed.
- **Hard termination guarantees.** Max 3 messages per exchange (STATUS_REQUEST → REVIEW_REQUEST → ACK). Three termination triggers: ACK received, no request intent, one message per turn. Designed explicitly to prevent the infinite ping-pong loops that kill naive multi-agent setups.
- **System prompt is the constraint that makes it work.** Hermes' supervisor prompt explicitly forbids content generation: "You do not generate content. You do not trade. You do not publish. You verify and route." Without this, Hermes drifts into "helpful assistant" mode.
- **Cognitive load reduction is the real win.** The background anxiety of constantly scanning for failures is the hidden cost. A supervisor agent frees working memory for creative work — new strategies, experiments, products.

## Summary

Graeme Keith describes a practical supervisor pattern using Hermes agent to oversee his OpenClaw instance on Discord. The setup eliminates the operational burden of monitoring cron jobs, verifying outputs, and debugging failures — transforming Hermes from a general assistant into a dedicated ops supervisor.

The implementation is a detailed 5-step guide: install Hermes, create a private #operator-ai Discord channel, wire both bots, give Hermes a supervisor identity via system prompt, and configure OpenClaw's SOUL.md with the protocol. The critical innovation is the structured intent marker protocol with hard termination guarantees — max 3 messages per exchange, [ACK] as terminal, one message per turn.

The article's deeper insight: the value isn't ops efficiency, it's cognitive. Having a supervisor agent eliminates the background mental load of always watching for failures, freeing you for creative work that compounds.
