<!-- sha256: e619b0e76023acab -->
# When AI Builds Itself — Recursive Self-Improvement

**Source:** https://www.anthropic.com/institute/recursive-self-improvement
**Authors:** Marina Favaro and Jack Clark (The Anthropic Institute)
**Date:** 2026-06-08

---

For most of AI's history, humans drove every step in its development cycle. But at Anthropic, we are delegating a growing share of AI development to AI systems themselves, which is speeding up our work.

Taken far enough, and given enough compute, that trend points to an AI system capable of fully autonomously designing and developing its own successor. This is called recursive self-improvement. We are not there yet, and recursive self-improvement is not inevitable. But it could come sooner than most institutions are prepared for.

## The 5-Stage Evolution

1. **2021-2023 — Building the first Claude:** People writing code and docs on laptops.
2. **2023-2025 — Chatbots:** People used early chatbots to help with parts of the process, generating short code snippets.
3. **2025-2026 — Coding agents:** Agents wrote and edited code on their own, sometimes entire files.
4. **TODAY — Autonomous agents:** Agents can now run code themselves and delegate hours of work to other agents.
5. **20XX? — Closing the loop:** Agents could become capable enough to build and train models themselves.

## External Evidence: Accelerating Benchmarks

- Task length doubling time accelerated from 7 months → 4 months
- Claude 3 Opus (Mar 2024): ~4 min tasks → Sonnet 3.7: ~1.5 hrs → Opus 4.6: ~12 hrs
- SWE-bench: low single digits → saturated in 2 years
- CORE-Bench: 20% in 2024 → saturated in 15 months
- Claude Mythos Preview: "at least" 16 hours — upper end of what METR can measure

## Internal Evidence from Anthropic

### Engineering
- **>80% of code merged into Anthropic's codebase authored by Claude** (as of May 2026), up from low single digits before Feb 2025
- **8x more code per engineer per day** in Q2 2026 vs 2024
- Two inflection points: 2025 (Claude runs code instead of suggesting) and 2026 (autonomous long-horizon work)
- April 2026: Claude shipped 800+ fixes reducing API errors by 1000x — estimated 4 human-years of work

### Code Quality
- Claude's success rate on most open-ended tasks: 76% in May 2026 (up 50pp in 6 months)
- Code quality: "somewhat worse than human in late 2025, roughly at parity today, expected strictly better within the year"
- Automated Claude reviewer: would have caught ~1/3 of bugs behind past claude.ai incidents

### Research
- Training speedup optimization: Opus 4 (May 2025): ~3x → Mythos Preview (Apr 2026): ~52x. Skilled human: 4x in 4-8 hours.
- Open-ended research: Claude agents recovered 97% of gap between weak supervisor and strong model ceiling (humans: 23%), $18K compute, 800 cumulative hours
- Research judgment: Opus 4.5 beat human next-step choice 51% → Mythos Preview: 64% (on deliberately hard moments, n=129)

## The Narrowing Human Role

The human role is narrowing: doing → reviewing → choosing which problems matter. The 'doing' now costs almost nothing in human time. Human comparative advantage: research taste and judgment.

## Three Possible Futures

### 1. The Trend Stalls
Exponential trajectories become S-curves. Bottleneck is supply chain (chips, energy, interconnects) or a missing architectural idea beyond Transformers. Even frozen at today's level: Project Glasswing found 10,000+ high/critical vulnerabilities.

### 2. Compounding Efficiency Gains (most likely)
AI development substantially automated but humans set directions. 100-person companies do work of 10,000-100,000. Human code review becomes bottleneck (Amdahl's law). Explosion of ideas/initiatives beyond capacity to pursue.

### 3. Full Recursive Self-Improvement
AI systems design and refine themselves. Pace determined entirely by compute availability. Humans shift to oversight, validation, verification of an expanding "virtual lab." Most uncertain case — alignment must be solved.

## On Slowing Down

Anthropic would support a verified multilateral slowdown/pause, but notes: training runs are easier to conceal than missile silos, inputs are general-purpose, incentive to defect is enormous. A credible pause needs: trigger conditions, lifting conditions, adjudication, and verification — the latter is harder for AI than for nuclear weapons.

Unilateral pause: achievable immediately but accomplishes much less — changes the front-runner but doesn't create deliberation.

## Key Quotes

"Claude-written code was somewhat worse than human-written code at Anthropic in late 2025, is roughly at parity today, and we expect it to be strictly better within the year."

"The shape of stuff today is roughly 'humans have ideas, and the models are able to implement, test and evaluate them an order of magnitude faster than before.'"

"Work (and life) ran on a gift economy of small favors between humans... [Claude is] faster, it creates zero debt, but each of these is a lost bid for human collaboration."

"The comparative advantage of humans as of right now is still in seeing the bigger picture and thinking beyond the confines of the immediate task."
