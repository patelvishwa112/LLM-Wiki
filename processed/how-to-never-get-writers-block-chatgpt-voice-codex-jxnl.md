---
type: bookmark
description: "Jason (@jxnlco) replaces human ghostwriting with ChatGPT live voice + Codex: talk-walk transcripts, only-use-my-words essay skill, then FFmpeg/Remotion video essay edits — open skills in jxnl/dots."
tags: ["writing", "skills", "codex", "chatgpt", "voice", "content-strategy", "creator-economy", "productivity", "ghostwriting", "video", "ffmpeg", "remotion"]
source: https://x.com/jxnlco/status/2076846537230160251
date: 2026-07-14
author: jxnlco
summary: "Jason (@jxnlco) replaces human ghostwriting with ChatGPT live voice + Codex: talk-walk transcripts, only-use-my-words essay skill, then FFmpeg/Remotion video essay edits — open skills in jxnl/dots."
raw: "[[raw/jxnlco_2076846537230160251]]"
---

# How to never get writer's block with ChatGPT Voice and Codex

Practical content pipeline from **Jason** (@jxnlco): RSI and typing friction pushed him from a human ghostwriter (talk → notes → draft) to an AI recreation of the same loop — voice capture, constrained drafting, optional video essay polish.

## Pipeline

### 1. Talk (ChatGPT live voice as ghostwriter)
Walk-and-talk with a voice prompt that stays mostly silent, interrupts only for clarity, and saves broad questions for the end. Goal: get ideas out; end of walk = transcript in chat.

### 2. Write (transcript → essay in Codex)
Codex opens the chat (Chrome control), pulls the transcript, drafts with:
- short one-word section titles
- **only words/phrases/ideas/examples from the speaker, in order**
- strip filler, repetition, false starts
- no new ideas or generic AI language

Enrichment: past Slack/X/blog samples as tone context; extra skills for titles, thumbnails, follow-ups. Core anti-slop rule: **“Only use my words.”** This X post itself was written that way.

Open skill: [transcript-to-blog](https://github.com/jxnl/dots/tree/master/agents/skills/transcript-to-blog) — writing contract (audience/message/pain/proof/action), short pre-draft interview, `[evidence needed]` instead of invented facts, writing-check reference.

### 3. Record and edit (blog → video essay)
Read finished post aloud into iMovie (or similar). Hand Codex recording + post + overlay images:
- word-level timestamps
- cut false starts, long pauses, filler via **FFmpeg**
- image overlays at useful moments
- **Remotion** word-level subtitles
- keep order, pacing, meaning — no rewrite/reorder/distracting effects

Open skill: [recording-to-video-essay](https://github.com/jxnl/dots/tree/master/agents/skills/recording-to-video-essay) — edit-plan review before render, phrase-anchored overlays, preview then final.

## Why it matters

Separates **idea generation** (speech, low friction) from **shaping** (agent skills with hard voice constraints) and **distribution** (video polish as tooling, not rewrite). The reusable design pattern is constraint-first skills that refuse to invent content — transferable beyond blogging to any “externalize judgment without generic LLM voice” workflow.

## Skeptical / limits

Author notes residual slop remains. Voice mode + browser/agent stack is product-specific; the skill repos matter more than the vendor path. RSI origin story is personal context, not a claim about universal productivity gains.

## Related

- [[premium-ghostwriter-five-skills-nicolas-cole]]
- [[david-ogilvy-writing-coach-claude-skill]]
- [[human-nature-meta-skill-dan-koe]]
- [[how-to-create-right-skill-ai-agent]]
- [[writing-good-skills-measured-rulebook-aparna]]
- [[anthropic-claude-code-skills-lessons]]
- [[claude-code-slash-command-library]]
