---
tags: ["prompt-engineering", "writing", "claude"]
source: https://x.com/rubenhassid/status/2050878032609530144
raw: "[[raw/rubenhassid_2050878032609530144]]"
date: 2026-04-29
type: processed-note
related:
  - "[[claude-code-cost-optimization-prompts]]"
---

# Anti-AI Writing Style: Making AI Sound Human

## Summary
A method to make AI writing sound human by saving a set of writing rules as a `.md` file (called "anti-ai-writing-style") and uploading it to Claude. The rules define voice, tone, context modes, and anti-patterns that suppress the default assistant persona, replacing it with direct, specific, and natural human writing.

## Key Takeaways
- **Rule priority stack** (when rules collide): Be accurate → Be clear → Be specific → Sound human → Use style only when improving the sentence
- **Default voice**: Direct, specific, natural. Short paragraphs. Varied rhythm. Contractions. Active voice. Concrete details. Plain uncertainty ("I think", "probably")
- **Anti-patterns to avoid**: "Certainly", "Of course", "Happy to help", "Great question", "I hope this helps", "Would you like me to"
- **Context modes**: Different writing styles for chat (direct, warm), with explicit "do not say" lists per mode
- **Format**: Save as `.md` file, upload to Claude as a permanent voice reference

## Connections
- [[claude-code-cost-optimization-prompts]] — the "No preamble" rule in cost optimization aligns with these anti-AI writing patterns
