---
tags:
- claude-code
- cost-optimization
- prompt-engineering
source: https://x.com/thegreatest_sv/status/2053128520138739985
raw: '[[raw/thegreatest_sv_2053128520138739985]]'
date: 2026-05-09
type: processed-note
related:
- '[[claude-code-hidden-settings]]'
- '[[deepseek-v4-claude-code-setup]]'
- '[[ai-writing-style-personalization]]'
description: 'Claude Code Cost Optimization: 20 Prompts to Cut Spend'
---

# Claude Code Cost Optimization: 20 Prompts to Cut Spend

## Summary
Twenty specific prompts and CLAUDE.md rules that dramatically reduce Claude Code token consumption, cutting a typical $200/month bill. The techniques range from output compression (caveman mode, diff-only) to reasoning constraints (thinking cap, output budgets) and session management (context compression, session handoffs).

## Key Takeaways
- **Startup audit**: "Respond in minimal words. Skip preamble. Code only." Saves ~$45/month
- **Caveman mode**: Permanent CLAUDE.md rule — minimal words, code only — yields 22-87% output reduction
- **Diff only**: "Show only changed lines with 3 lines context" — reduces 8000 tokens per edit to ~400
- **No preamble rule**: Never "Great question", "Certainly", "I hope this helps" — start with the answer directly
- **Thinking cap**: Use minimal reasoning. xhigh reasoning burns 50K tokens before answering
- **Output budget**: "Your response budget: 300 tokens. Hard cap."
- **File scope lock**: Only read files inside `/src/[folder]`
- **Plan before agent**: Describe plan in text before any task touching 3+ files
- **Context compression**: Summarize project in under 500 tokens
- **Session handoff**: Write 200-token summary, save to `.claude/SESSION_[date].md`

## Connections
- [[claude-code-hidden-settings]] — settings-level cost control (effort level, adaptive thinking)
- [[deepseek-v4-claude-code-setup]] — architectural cost optimization via parallel DeepSeek sessions
- [[ai-writing-style-personalization]] — the "no preamble" pattern overlaps with anti-AI writing style rules
