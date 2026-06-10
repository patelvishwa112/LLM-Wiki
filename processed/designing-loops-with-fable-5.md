---
tags: ["anthropic", "fable-5", "claude", "agents", "agent-harness", "loops", "self-correction", "memory", "agent-memory", "prompt-engineering", "evaluation", "continual-learning"]
source: https://x.com/RLanceMartin/status/2064397389189071163
date: 2026-06-09
type: article
authors: ["Lance Martin"]
title: "Designing loops with Fable 5"
summary: "Lance Martin (Anthropic MTS) on two techniques for Mythos-class models like Claude Fable 5: (1) self-correction loops using /goal or Outcomes with verifier sub-agents that outperform self-critique, and (2) cross-session memory with a fail→investigate→verify→distill→consult progression. Fable 5 showed ~6x improvement over Opus 4.7 on Parameter Golf and up to 73% verification coverage on continual learning tasks."
raw: "[[RLanceMartin_2064397389189071163]]"
related: ["[[agent-first-vs-prompt-first-design]]", "[[prompt-engineering-guide-fable-5]]", "[[claude-code-dynamic-workflows-intro]]"]
---

# Designing loops with Fable 5

## Two Core Techniques

**Self-correction loops:** Design loops that let the model self-correct against environment feedback. Use /goal (Claude Code) or Outcomes (Claude Managed Agents) rather than directly prompting and steering. 

**Key insight:** A verifier sub-agent outperforms self-critique because grading happens in an independent context window. Outcomes in CMA spawns a grader sub-agent automatically.

**Memory:** An outer loop spanning sessions. Claude writes to memory during a session; memories are retrieved in future sessions. Effective memory follows a progression: fail → investigate → verify → distill → consult.

## Experimental Results

**Parameter Golf (ML engineering challenge):** Fable 5 improved the training pipeline ~6x more than Opus 4.7. Fable 5 made structural bets (architecture changes); Opus 4.7 got stuck adjusting scalars after a small initial win.

**Continual Learning Bench 1.0 (SQL question-answering with memory):**
- Sonnet 4.6: exits at step 1 (failure notes only), rarely consults memory
- Opus 4.7: exits at step 3 (schema reference with uncertainty), 7-33% verification coverage
- Fable 5: completes the progression, up to 73% verification coverage, distills general rules
