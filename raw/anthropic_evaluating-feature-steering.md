# Evaluating Feature Steering: A Case Study in Mitigating Social Biases

**Source:** https://www.anthropic.com/research/evaluating-feature-steering
**Authors:** Esin Durmus, Alex Tamkin, Jack Clark, et al. (Anthropic)
**Published:** Oct 25, 2024

---

## Summary

Anthropic ran quantitative evaluations of SAE feature steering on Claude 3 Sonnet, focusing on 29 social-bias-related features across BBQ bias benchmarks and MMLU/PubMedQA capabilities.

## Key Findings

### The Steering Sweet Spot
- Steering factors between -5 and +5 influence outputs without degrading capabilities
- Beyond ±5, MMLU accuracy drops sharply — model becomes unusable
- Same sweet spot holds across all 29 features tested

### On-Target Effects Work
- Steering "Gender bias awareness" feature increases gender bias scores by 10%
- Steering "Pro-life and anti-abortion" feature increased anti-abortion selections by 50%
- Steering "Left-wing political ideologies" decreased anti-abortion selections by 47%

### Off-Target Effects Are Real
- "Gender bias awareness" feature also increased age bias by 13% (unrelated)
- "Pro-life" feature had larger impact on immigration responses than the immigration-specific feature
- Features don't operate in isolation — there are underlying correlations between concepts

### Promising: Neutrality Feature
- "Neutrality and Impartiality" and "Multiple Perspectives" features reduce bias across ALL 9 BBQ dimensions
- Without significant capability degradation

## Critical Lesson for Experiments
**There is a disconnect between feature activation context and resulting behavior.** Features were identified by what contexts they fire on, not what behaviors they produce. A feature that fires on "gender bias discussions" might not actually control gender bias output — it might control something correlated but different.

## Limitations
- Only 29 features out of millions tested
- Noisy accuracy estimation (10 samples per question)
- Steering applied to entire prompt, not just model response
- SAE size not varied (34M params)
- No comparison to activation steering or prompting

## Future Work Suggested
- Scale up SAE size → more specific features
- Study circuits, not individual features
- Try multiplicative/projective/conditional steering
- Steering only on response tokens (not input)
