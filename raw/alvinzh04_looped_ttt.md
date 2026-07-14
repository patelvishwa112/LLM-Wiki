---
source_url: https://alvinzh04.github.io/blog/looped-ttt.html
ingested: 2026-07-14
author: AlvinZH04
title: "Loop deeper, or adapt? Test-time training in looped transformers"
sha256: a39aea540c9bf6d5f83f5ade16770a7b15440d6035f4514f85dbc0495f36449e
code_url: https://github.com/AlvinZH04/Loop-TTT
---
note: Firecrawl credits exhausted; body via Playwright MCP evaluate (article/main/body) on https://alvinzh04.github.io/blog/looped-ttt.html. Code: https://github.com/AlvinZH04/Loop-TTT

ABSTRACT

Looped (recurrent-depth) transformers spend extra test-time compute by iterating the same recurrent core. This started as a simple curiosity: if a looped model reuses the same weights every iteration, would nudging those weights at test time do something unexpected? Working on the Ouro-1.4B base model, we find that accuracy climbs to the model's trained loop depth and then overthinks. Right at that depth, a minimal form of test-time training improves generative math accuracy by a clear margin: on four-shot GSM8K, a single batch-episodic, target-label-free update to 97 RMSNorm scale vectors, computed from strict-masked prompt entropy, lifts accuracy +8.2 points (0.766 → 0.848, n=500) and beats simply decoding with more recurrent steps. Entropy minimization is already an established adaptation objective (Tent, and recently for LLM reasoning), so the informative questions here are about the loop, not about whether sharpening confidence can help at all. Mapping that design space, a few patterns emerge. The entropy objective outperforms a prompt language-model-loss objective in this setting, a direction the wider literature does not settle. The update also has to be reset after every batch, because letting it accumulate collapses the model. And, uniquely for a loop, in the tested sweeps the reliable place to read the adaptation signal was the model's trained recurrence depth; adapting from shallow or overthinking states could sharply hurt, and whether it helps under deeper decoding is less consistent. On four-shot GSM8K, most of the measurable gain is a reusable calibration vector derived from the shared demonstrations, capturable with no test-time gradient. Both headline effects reappear on the tested MATH-500 subset, while the depth/overthinking pattern (but not the entropy-TTT gain) transfers to a subset of MMLU. The result is a narrow operating regime in which a small test-time update to a looped model is most useful when its signal is read at the model's trained recurrence depth.

CONTENTS
The curiosity
Setup: the model, the recipe, the datasets
Depth is reasoning, then overthinking
A window where adapting beats looping
The design space: where, when, how much, and where in the loop
Which signal: entropy over LM loss
What adaptation does to the answers (pass@K)
Is it the loop?
Does it travel? MATH-500, MMLU, and scale
From online adaptation to reusable calibration
References
1. The curiosity

Most ways of spending more compute at inference add tokens: longer chains of thought. A looped transformer spends it differently: it applies the same recurrent core r times before decoding, turning depth into a dial you can turn at test time. Ouro (Zhu et al., 2025) is a real pretrained base LM built this way, trained with a maximum recurrence of four steps and evaluated here at a fixed depth of r=4. It is not an RL-tuned reasoning model; any reasoning trace here is elicited through prompting rather than a Thinking checkpoint. GSM8K uses four-shot chain-of-thought prompting, and MATH-500 uses a zero-shot step-by-step instruction. ("Trained depth" is our shorthand for this fixed r=4 below.)

The shared-weights part is what caught my attention. In an ordinary network, adapting a layer changes the computation once. In a loop, the same parameters are reused on every iteration, so a single small change to them is felt r times over. That raised a question I couldn't answer from the literature: if you take one gradient step on a looped model's weights at test time, does the loop do something unexpected with it? This post is what fell out of chasing that question. It is an open, curiosity-driven exploration of one model family. It is not a comprehensive study; I distinguish established results from suggestive interpretations. Code and released artifacts: github.com/AlvinZH04/Loop-TTT.

The organizing question: when you have spare test-time compute, should you loop deeper, or adapt the weights?

2. Setup: the model, the recipe, the datasets

Model. Ouro-1.4B (and 2.6B for a scaling check), the base models, recurrence set by total_ut_steps. Our baselines closely reproduce the paper's reported range (Ouro-1.4B GSM8K 0.754 greedy / 0.768 sampled vs the paper's 0.789, and Ouro-2.6B 0.838 vs 0.816) under similar but nonidentical prompting and scoring, a useful implementation sanity check rather than an exact reproduction.

The recipe. Test-time training here is Tent-inspired (Wang et al., 2021) and deliberately minimal, applied batch-episodically: for each batch of B prompts, we minimize a target-label-free objective (by default the mean entropy over all valid prompt-token transitions in the batch) with respect to the RMSNorm scale vectors, decode all B answers with the resulting shared update, then restore the base scales. The objective is a token-weighted batch mean (Eq. (3)), so longer prompts receive proportionally more weight, and batch size is a hyperparameter of the method. Related LLM test-time methods differ in what they optimize: per-prompt optimization of a final-layer vector with prompt cross-entropy (SLOT, Y. Hu et al., 2025), target-domain input-perplexity adaptation with LoRA (TLM, J. Hu et al., 2025), and joint input-perplexity and output-prefix-entropy adaptation with a reverse-KL anchor (SyTTA, Xu et al., 2025); ours instead adjusts shared RMSNorm scales batch-episodically, and is deliberately minimal.

Formally. Write φ for the RMSNorm (Zhang & Sennrich, 2019) scale vectors. Ouro-1.4B has 24 physical decoder layers; each has four RMSNorm scale vectors (96 in-loop), plus one final readout RMSNorm (the 97th), and the 24-layer core with its 96 in-loop scale vectors is reused at every recurrent step. Let at∈{0,1} be the prompt's attention mask. The recurrence and readout, the strict-masked entropy objective, and the episodic update are:

h(j+1) = Fθ,φ(h(j), x),   j = 0,…,m−1,   pt(m) = softmax(Wout ht(m))
(1)
Mt = at at+1 ∈ {0,1}
(2)
Lent(x1:B; φ) = 
∑b,t Mb,t (−∑v pb,t(m)(v) log pb,t(m)(v))
∑b,t Mb,t
(3)
φ ← φ − α · Adam(∇φ Lent)   (repeat for s steps; s = 1 by default)
(4)
y = GreedyDecode(p(d)θ,φ(· | x)),   then φ ← φ0   (episodic, restored per batch)
(5)

Here θ are the frozen base weights (only φ is trained), Fθ,φ is one iteration of the shared recurrent core (the same 24-layer stack and parameters at every step j), h(j) the hidden state after j iterations, and Wout the readout. m is the adaptation depth (loops before the update) and d the decoding depth (loops at generation).

The mask Mt in Eq. (2) keeps a position only when both the source token and its next-token target are real, so padding, the left-pad boundary, and the readout position drop out. The entropy (3) and the LM-loss variant then score the identical token set. The gradient in (4) flows through all m recurrent applications of the shared φ; nothing else is trainable. We write Adam(·) (Kingma & Ba, 2015) for the moment-normalized update direction (the bias-corrected first-over-second-moment ratio), so the learning rate α alone sets the step size and is not double-counted. One property of that step matters later: because Adam starts from zero moments, the very first step is close to a fixed-size move along the sign of the gradient, Δφ1 ≈ −α·sign(∇φ Lent), with a coordinatewise magnitude that barely depends on how large the gradient is. That pins the step's magnitude, but not its direction. What makes the single (s = 1) update cacheable is a separate, empirical fact: the exemplar-only update direction is nearly constant across batches (cosine ≈ 0.99, §10; the full-prompt update is less constant, ≈ 0.91), which Adam alone does not imply. The default method uses m = d = 4; the depth-location experiments (§4, §5) vary m and d independently.

Algorithm 1  Batch-episodic test-time training (one batch)
Input: prompts x1:B; base scales φ0; adaptation depth m; decoding depth d; optimizer steps s; learning rate α
1  φ ← φ0
2  for j = 1 to s do
3    run the m-step recurrence Fθ,φ(·, x1:B) → logits z(m)  // shared φ; cache off
4    L ← strict-masked mean entropy of softmax(z(m))  // Eq. (3); no labels
5    φ ← φ − α·Adam(∇φ L)  // update only the 97 RMSNorm scale vectors
6  y1:B ← generate(x1:B; φ, depth = d)  // decode with adapted scales
7  φ ← φ0  // restore (episodic)
Output: answers y1:B

No parameters are added, no full fine-tune, no output-side objective. Instead, 198,656 existing RMSNorm-scale scalars (0.014% of the model) are made temporarily trainable during each adaptation episode, roughly 8× fewer than a LoRA adapter (Hu et al., 2022) at rank 8 on just the query/value projections (about 38× fewer than LoRA-r8 on every linear layer). Because a looped model reuses the same 24-layer core, the 96 in-loop scales are felt at every recurrent step (the 97th, final readout scale, once after recurrence), so a very small update goes a long way. The experiments vary five choices: the objective, the token source, the adaptation depth, the reset schedule, and the update size.

Datasets. GSM8K (grade-school math, our primary benchmark, where our baseline approximately reproduces the reported range; Cobbe et al., 2021), MATH-500 (the 500-problem evaluation subset of harder competition math; Hendrycks et al., 2021; Lightman et al., 2023), and a subset of MMLU (multiple-choice knowledge; Hendrycks et al., 2021). Generative math answers are scored with Math-Verify v0.9.0 (Kydlíček) for mathematical equivalence, with a lightweight regex scorer retained as a diagnostic cross-check; MMLU is scored from next-token A/B/C/D logits. The main greedy GSM8K and MATH runs retain full decoded generations for offline rescoring; aggregate sampling and diagnostic exceptions are noted with their results.

3. Depth is reasoning, then overthinking

The first thing to establish is that looping is doing something. It is: GSM8K accuracy climbs steeply with recurrence, peaks at the trained depth r=4, and then declines if you keep looping: the same inverse-U that longer chains of thought show (Zhou et al., 2026), here along the latent depth axis (an analogy in shape, not a claim that token-length and recurrent-depth overthinking share a mechanism). We use "overthinking" operationally to mean accuracy degradation when inference recurrence exceeds the model's trained depth.

Fig. 1. Reasoning, then overthinking. GSM8K accuracy vs. loop depth r (greedy and sampled decoding). Both climb to the trained depth r=4 (~0.75) and fall off past it: r=16 collapses. Performance deteriorates beyond the trained depth.

Two regimes fall out of this curve, and they turn out to demand opposite things. Below the peak the loop is still buying reasoning: going from r=1 to r=2 is worth about +40 points. Past the peak the loop is wasted, even harmful. So "spend more compute" is not one question but two, split at the trained depth.

4. A window where adapting beats looping

Right at the peak (where looping deeper stops helping) is where the test-time update earns its keep. At r=4, one entropy step improves GSM8K accuracy (0.766 → 0.848, n=500) and outperforms simply increasing the decode depth to r=8 (0.694). This is an accuracy comparison between the tested procedures, not a wall-clock-, memory-, or latency-matched deployment study; adaptation adds a forward and backward pass plus an optimizer step, whereas deeper looping only changes inference depth. But the window is narrow: below the peak, adapting is the wrong move (just loop, it's worth far more); well past the peak, the loop has degraded too far for the update to recover.

Robustness: this gain is not a truncation artifact. Only about 1% of chains hit the token budget in either arm, and the truncation-excluded (completed-only) gain is +7.8, essentially unchanged from the +8.2 overall.

REGIME	OBSERVATION	PREFERRED INTERVENTION
r = 1 (below trained depth)	yes: r1→r2 ≈ +40 pt	loop deeper
r = 4 (at trained depth)	no: r4→r8 = −6 pt (greedy)	adapt (+8)
r = 8 (overthinking decode)	adapting from the r=8 state hurts	prefer decoding at r=4; if deep decoding is required, adapt@4 is less harmful than adapt@8 in the tested sweeps

The r=8 case is subtle, so we report it carefully rather than headline it. At a fixed 1024-token budget, adapting at the trained depth then decoding at r=8 is a small, non-significant gain (+0.033, CI includes 0), with low truncation in both arms (0.7% of baseline chains and 1.3% of adapt@4 chains hit the budget), so it is robust rather than a budget artifact. The real signal is the contrast: matched-depth adaptation at r=8 collapses (−0.237) while trained-depth adaptation holds. Inspecting the cut-off cases is consistent with this: adapting at the trained depth tends to leave the reasoning coherent (one chain was mid-sentence at its \boxed{} answer when it ran out of room), whereas adapting at the wrong depth can degenerate into repetition, most visibly at r=16, where trained-depth decoding truncates 20% of chains (6% for baseline) even as it still scores above baseline. The through-line is a direction: reading the adaptation signal at the trained depth was the most reliable place to adapt in the tested sweeps, so read where the model is competent, not necessarily where it will decode. (Qualitatively, trained-depth-adapted failures tend to be coherent generations truncated before the answer rather than broken; a completion-level error analysis would be needed to establish that systematically.)

To see how the update interacts with depth as a whole, we swept the entire loop-depth axis (r = 1…16) on the same 300 problems. The thing to hold onto is that every run makes two separate depth choices: the depth we read the entropy signal at (the adapt depth) and the depth we decode the answer at (the decode depth). Our three conditions differ only in where that signal is read:

each point on the x-axis is one decode depth r:
  baseline        no adaptation, just decode at r
  matched-depth   adapt at r, then decode at r    (read the signal at the depth you will decode)
  trained-depth   adapt at 4, then decode at r    (read the signal at the model's trained depth, 4)

So as we walk rightward along the x-axis, matched-depth TTT adapts deeper and deeper (its adapt depth follows the decode depth), while trained-depth TTT always reads the signal at the competent r=4 state and only decodes deeper. Both adapt; they differ only in where they read. The figure asks which choice is better.

Fig. 2. Where you read the signal changes what adaptation does. Three curves vs. loop depth (n=300, 1024-token budget; bars are 95% bootstrap CIs, Δ vs. baseline annotated, * = CI excludes 0). The baseline (grey) traces the reasoning-then-overthinking inverse-U, peaking at 0.773 (r=4) and collapsing to 0.160 (r=16). Matched-depth TTT (blue) tracks it near the peak but collapses hard once the loop is overthinking (matched@8: −0.237, CI [−0.30,−0.18]): adapting through a deep overthinking loop is actively harmful. Trained-depth TTT (adapt@4 → decode@r, orange) is far milder: it holds at r=8 (+0.033, CI includes 0) instead of collapsing, and significantly helps at the deepest depth (+0.103 at r=16). At the peak both updates give the same +0.090 here, consistent with the separate n=500 run's significant ~+8.

The n=300 intervals at the full 1024-token budget sharpen the reading. What is solid is the contrast in the tail: matched-depth adaptation collapses (−0.237 at r=8), while reading at the trained depth is substantially less harmful, holding at r=8 (+0.033, not significant) and even recovering a little accuracy at r=16 (+0.103, significant). Although that r=16 improvement is statistically significant, absolute accuracy there stays poor (0.16 to 0.26), so adaptation does not undo the damage from extreme depth extrapolation. Trained-depth TTT is still not a universal free lunch: past the trained depth it stops helping reliably, and the significant wins sit at the trained depth itself and, marginally, the deepest one. The takeaway is about where, not whether: reading the adaptation signal at the model's competent trained depth is the reliable choice; the decode depth is the fragile one.

5. The design space: where, when, how much, and where in the loop

Once you have a working intervention, the interesting question is what it's sensitive to. Holding the window fixed (r=4), we varied one knob at a time. The recipe's own defaults turn out to be the winners, but a couple of the axes behave in ways I didn't expect.

Where (which tokens): the prompt wins

Few-shot prompting makes even a base model produce a long chain of thought, so you might read the adaptation signal from the generated tokens. On the loop it's the opposite: adapting on the prompt, before decoding (+7.0) beats adapting on the model's own generated prefix or re-adapting online (both +4.0). Once the loop commits to a chain, sharpening on that chain just reinforces it; the clean prompt carries the best signal and costs the least.

Concretely, the three choices differ only in which tokens the entropy signal is read from, for a GSM8K item like "Natalia sold clips to 48 friends in April…":

the entropy signal is computed on…
  prompt   the 4 solved examples + the question, before any answer is written   -> default,  +7.0
  prefix   the prompt PLUS the first ~64 answer tokens the model generates       ->           +4.0
  online   a 64-token chunk, then re-adapt, then the next chunk, and so on       ->           +4.0
Fig. 3. Where to read the signal. Adapting on the prompt before decoding beats adapting on the model's own generated prefix or online (GSM8K, r=4, s=1, entropy, n=300; a location ablation, not a matched-budget comparison). The simplest point is the best point.
When (how long the update lives): reset often, or collapse

The recipe resets the weights after every batch. What if you let them accumulate across the test stream? It collapses: episodic (reset per batch) gives +7.0, resetting every 24 examples +4.4, and never resetting falls to −15.6. The loop already compounds one nudge within an example; compounding across examples drives the shared scales into the same collapse a too-large learning rate causes. Reset frequency is monotonic, which is exactly why the recipe resets so aggressively.

Concretely, the three schedules differ only in when the scales are restored to their base values φ0 as the model works through the test stream:

as the model answers a stream of problems, the adapted scales are…
  episodic    restored to the base weights after every batch                -> default,  +7.0
  windowed    restored once every 24 examples (allowed to drift in between)  ->           +4.4
  continual   never restored: the nudge piles up over the whole stream       ->          -15.6  (collapse)
Fig. 4. When to reset. Reset frequency across the test stream: episodic (per batch) helps most; never resetting (continual) collapses (GSM8K, r=4, s=1, entropy, n=300). Our "continual" keeps the drifted weights but rebuilds the optimizer each batch (see limitations).
Where in the loop: read the signal at the trained depth

This is the axis a single-pass model doesn't have, and the one that surprised me most. You can read the entropy signal at any loop depth m (the shared scales are the same at every iteration) and then decode at a possibly different depth d. Sweeping both in this location sweep (Fig. 5, 512-token generation budget): among the tested adapt depths, the model's trained depth (m=4) produced the strongest update at both tested decode depths. Decoding at the trained depth (d=4) it gives the full +7.0, and it is substantially less harmful than shallow- or overthinking-depth adaptation when decoding deeper. Decoding at d=8 is a separate question: in the whole-depth rerun of Section 4 (1,024-token budget), adapting at depth four and decoding at eight improved accuracy by 3.3 points, but the confidence interval included zero, so we do not treat that deeper-decode gain as conclusive. Qualitatively, the trained-depth update tends to leave the few failing chains coherent and merely cut off before the answer rather than broken, though we did not run a completion-level analysis to confirm this. So trained-depth adaptation is less harmful than adapting through the overthinking depth, though its deeper-decode gain is modest. Reading the signal too shallow (m=1,2, before the model has "finished reasoning") misleads catastrophically (−46 at one point); reading it at the overthinking depth (m=8, which spends the most compute) collapses.

Fig. 5. Where in the loop to adapt. Accuracy vs. the depth at which the signal is read, for two decode depths. adapt@4 (the trained depth) is best at both, and is the least harmful under deeper decoding, though its deeper-decode gain is modest (§4); too-shallow or overthinking-depth adaptation hurts (GSM8K, s=1, entropy, n=300, batch size 8, 512-token budget; a location ablation, not a compute-matched comparison).

So the looped answer to "where do you adapt" is neither "at the decode depth" (adapt@8 / decode@8 collapses) nor "early and cheap" (shallow adaptation hurts). It is adapt where the model is competent (the trained depth): that is the best tested source of the update and is substantially less harmful than adapting at an overthinking depth, even though its benefit under deeper decoding varies across runs. How much is the tame axis: one step is best; more overfits.

6. Which signal: entropy over LM loss

There are two natural target-label-free objectives on a prompt: predict its next tokens (language-model loss) or sharpen its next-token distributions (entropy / Tent). With the masking aligned so both score the identical token set, entropy wins clearly: +8.2 vs +3.4 at r=4 (n=500). This fits the overthinking picture: one interpretation is that entropy minimization concentrates probability on fewer competing continuations. This echoes Agarwal et al. (2025), who find token-level entropy minimization can encourage commitment to fewer reasoning paths, though their methods optimize generated trajectories or decoding logits rather than prompt-only RMSNorm scales. The preferred objective is not universal: TLM (J. Hu et al., 2025) reports input perplexity outperforming Tent-style entropy under domain shift, so which signal wins depends on the model, task, and adaptation regime.

Fig. 6. Confidence beats prediction. Entropy (Tent) vs. LM-loss objective at r=4, aligned masking, with bootstrap CIs (GSM8K, n=500). Sharpening confidence is the stronger test-time signal for this looped base model.
7. What adaptation does to the answers (pass@K)

Sharpening the model has a predictable side effect: it concentrates most of the gain at low K. We report pass@K using the unbiased estimator of Chen et al. (2021). Sampling eight completions per problem, the gain is concentrated at low sampling budgets: +11.4 points at pass@1 (0.64 → 0.76) and +2.5 at pass@8. TTT remains at or above baseline across the tested curve. Determining whether this changes semantic answer diversity requires completion-level diversity analysis.

Fig. 7. Front-loading accuracy. pass@K for baseline vs. entropy-TTT (GSM8K, K=8 samples, T=1.0, top_p=0.95, n=200). The gain is largest at pass@1 and shrinks by pass@8. Whether this reflects reduced answer diversity we do not yet claim: that needs a diversity measure, noted in limitations.
8. Is it the loop?

The tempting story is "recurrence is why a tiny update works." The more precise interpretation is narrower. Running the same adaptation procedure on a performance-matched non-looped model (Qwen2.5-3B base; Yang et al., 2024) does essentially nothing at the identical one-step setting, versus a clear gain on the loop.

MODEL	ARCHITECTURE	BASELINE	S=1, ENTROPY	BEST TESTED RESULT
Ouro-1.4B, r=4	looped	0.773	0.843	+7.0 at s=1
Qwen2.5-3B base	non-looped	0.767	0.763	0.780, +1.3 at s=2

The two models start from near-identical GSM8K baselines (0.773 vs 0.767, n=300), but the identical one-step entropy update (s=1) lifts the loop by +7.0 while leaving Qwen essentially flat (−0.4); Qwen's best tested result is only +1.3, and it needs a second step (s=2). The procedures are not even the same size (Ouro adapts 97 RMSNorm scale vectors, Qwen adapts 73) and the architectures and training histories also differ (and Ouro at r=1 already shows a smaller gain than at r=4). So the careful claim is: recurrent reuse appears to amplify the update in Ouro; Qwen is a performance-matched external control, not a clean causal isolation of recurrence. The clean test (replaying one fixed update at increasing depth within Ouro) is on the list.

9. Does it travel? MATH-500, MMLU, and scale

We also explore MATH-500, a subset of MMLU, and the larger Ouro-2.6B to probe whether the depth and adaptation effects transfer across task difficulty, output format, and model scale.

MATH-500 (harder math). Settings: zero-shot instruct prompt, n=200, a 2,048-token generation budget, greedy decoding, r=4, s=1. The same episodic entropy update generalizes: entropy +3.0 (baseline 0.740 → 0.770), while the LM-loss objective −2.0 (→ 0.720) actually hurts. So both headlines (TTT helps, and entropy beats LM) reappear on the tested MATH-500 subset, at smaller magnitude (less headroom). A separate n=500, 4,096-token run measures the MATH baseline at 0.754 (a different run from the TTT result above). A note on the number: Appendix C.1 (Table 16) of the Ouro paper reports 82.4 under an in-house 5-shot CoT, strict-match protocol; its LLM-as-judge evaluation (Table 17) is used for the Thinking-model reasoning benchmarks such as AIME, not for MATH-500. Our approximately 0.75 baseline instead uses a zero-shot instruction prompt, greedy decoding, and Math-Verify answer equivalence, with regex scoring as a cross-check. The paper does not document the exact normalization used by its strict matcher, and the prompting, generation budget, harness, and scorer all differ, so these numbers are not directly comparable.

MMLU (multiple choice). MMLU changes the output format: each question wants a single answer letter (A/B/C/D), which we score directly from the next-token logits rather than from a generated chain. We ran two probes on a subset of MMLU subjects. The depth probe covers 11 subjects; the TTT probe covers 10 of them (one subject completed only the depth run). Two clean findings come out. First, the depth inverse-U reproduces: nine of the eleven subjects peak at r=4; the remaining two peak at r=8. All eleven decline by r=16. Second, the entropy update is neutral on the 10 TTT subjects: the mean accuracy change is about +0.1 points (an unweighted macro-average across subjects), ranging from −4 to +5 points across subjects, i.e. no consistent effect. The split is the point. The phenomenon (accuracy degrading past the trained depth) is format-general, but the entropy-TTT recipe does not transfer to this single-letter setting. Sharpening next-token distributions across the prompt does not reliably improve the final A/B/C/D decision margin; this may reflect a mismatch between the adaptation proxy and the evaluation decision rather than a lack of entropy in the output format itself. This is a hard-skewed subject subset, so we do not report an absolute MMLU number against the paper's full 57-subject protocol.

Scale (Ouro-2.6B). The patterns are not 1.4B-specific, though they soften at scale. Read this as a confirmation, not a headline: each result below comes from a single run at the stated size. The 2.6B baseline falls near the paper's reported GSM8K range under our protocol (0.838 vs 0.816, n=500). In a separate depth sweep (n=200), accuracy peaked at the trained depth and declined under further looping (baseline by depth r = 1,2,4,8,16: 0.38, 0.75, 0.82, 0.805, 0.25); the decline was gentler than in the 1.4B sweep, with r=16 at 0.25 rather than 0.16. A distinct adaptation study (n=300) tested two learning-rate regimes at the trained depth. The 1.4B rate caused a sharp collapse (GSM8K 0.833 → 0.40), consistent with the diagnostic that 2.6B's one-step output-distribution KL was about 4.4× larger than 1.4B's. A learning rate about four times smaller was stable and improved accuracy on the same evaluation set by +1.7 points at one step and +3.4 at two (0.833 → 0.850 → 0.867), well below 1.4B's ~+8, consistent with less headroom at this size. We treat the "~4×" learning-rate ratio as an empirical observation, not a derived scaling law.

The picture in one line. Looped depth buys reasoning up to the trained depth then overthinks (general); at that depth a minimal entropy-TTT update helps, best read on the prompt at the trained depth and reset every batch (GSM8K, and reappearing on MATH-500); recurrence appears to amplify it; and it is a single-shot, generative-reasoning effect, not a universal win.
10. From online adaptation to reusable calibration

At Ouro's trained recurrence depth, a one-step entropy update to its RMSNorm scales improves generative math performance. Most of the measurable gain is captured by a reusable calibration vector derived from the shared demonstrations, and reading that signal at the trained depth is more reliable than adapting from incomplete or overthought recurrent states. The rest of this section unpacks that claim.

The update is mostly reusable

The same few-shot exemplars sit in every prompt, so I ran the decomposition on the shared prefix (paired rerun, n=300). Adapting on just the shared exemplars recovers +7.0 of this rerun's full +7.3 (run-to-run variation from the +7.0 full gain reported elsewhere), and one update learned once and reused for every problem (a fixed cached vector) recovers +6.7; the exemplar-only update directions have cosine similarity 0.99 across batches (versus 0.91 for the full-prompt update and 0.38 for question-only). At n=300 we did not detect a difference between full and fixed-cached TTT: full minus fixed-cached was +0.67 points, 95% CI [−3.0, +4.0]. This supports the conclusion that most measurable gain is reusable, but it does not establish equivalence, which would need a predefined practical margin and a higher-powered test. Adapting on the question alone gives +4.3, but that is not significant. So we cannot detect a per-instance component here; most of this "test-time training" is really a cacheable prompt calibration.

Removing the test-time gradient

If the update is mostly a fixed direction, can we drop the test-time gradient entirely? A single precomputed vector does most of the work. In a separate run (Fig. 8), the exemplar-derived cache (a static vector fit once at n=300 with no test-time gradient) recovers +5.0 of the +7.3, and a vector fit offline on a handful of held-out training prompts (distill, an offline-fitted static RMSNorm-scale delta, not a trained student model or a knowledge-distillation objective) recovers a comparable amount; fitting the static vector too hard degrades it below baseline (distill5 at −2.3), the same over-adaptation direction seen everywhere else. This +5.0 comes from a different run and setting than the +6.7 fixed-cached figure in the paired decomposition above, so the two cache numbers are not interchangeable.

Fig. 8. Cache vs. distill. A static RMSNorm-scale vector fit with zero test-time gradient: the exemplar-derived cache recovers +5.0 of full TTT's +7.3, and distill1 (fit offline on held-out training prompts) recovers a comparable amount; over-fitting it degrades the gain, with distill5 falling below baseline (−2.3) (Ouro-1.4B, r=4, n=300).
What this changes

Taken together, these results indicate that much of what presents as per-example test-time training is better described as a reusable prompt calibration that can be precomputed and cached, together with an amortization target that could be distilled into a fixed RMSNorm-scale delta. Under either interpretation, the loop's trained depth is where the adaptation signal is most informative. The update is also inexpensive: the adapted scales are a fraction of even a rank-8 LoRA adapter. The 96 in-loop scale vectors are reused at every recurrent step and the final readout scale is applied once after recurrence, so a looped model can be adapted at test time on a small parameter budget. We report this low cost as an observation about feasibility; whether it yields a practically useful method is not established here, and would require the transfer and confirmatory tests noted below.

Future work

The immediate open questions are transfer tests: whether a calibration vector fit on one prompt family carries to another; whether it carries across tasks (GSM8K → MATH); and whether it carries across looped-model families and scales. The cleanest recurrence test, replaying one fixed update at increasing depth within Ouro, would also separate amplification from confound.

A larger direction follows from the overthinking curve itself. Our study takes the looped model as given and adapts it at test time; the collapse past the trained depth is a property of how the model was trained, not a law of recurrence. Prior and recent work suggests looped models can be made more stable as depth grows: Universal Transformers (Dehghani et al., 2019) combine recurrent weight sharing with adaptive per-position halting, letting different tokens receive different numbers of refinement steps, and the readout blind spot analysis (Sharma & Vu, 2026), in controlled looped language models, shows that normalized readouts can leave recurrent hidden-state scale weakly supervised, and that explicit scale control improves the measured variable-depth perplexity-compute frontier. Most directly, STARS (Yang et al., 2026) trains recurrent dynamics toward greater fixed-point stability; in its experiments this prevents degradation in a controlled addition task and slows the decline under depth extrapolation on mathematical-reasoning benchmarks. A model trained to stay reliable at greater depth would change what a test-time update can do: the same "read the signal at the competent depth, then decode" strategy could become useful at depths where the current model only overthinks. Testing this cheap calibration on such depth-stabilized looped models is the direction we consider most promising, and one we have not yet explored.

This is the first post in a planned series on adaptation in looped transformers, and it deliberately stays with base models. Applying the same test-time update to RL-tuned reasoning (Thinking) checkpoints, where the test-time compute is spent on long generated traces rather than on the prompt, is a distinct regime we plan to take up in a follow-up post.

Scope

We tuned the recipe's settings by watching GSM8K test accuracy. The model never sees the gold answers, so this is not label leakage; but choosing the settings that scored best on this test set is its own selection effect, which the confidence intervals do not capture, so the headline numbers are likely optimistic. The displayed intervals are also pointwise: they are not adjusted for multiple comparisons or for configuration selection across the depths, objectives, learning rates, reset schedules, and parameterizations explored in the broader sequence, so the reported effects are exploratory rather than confirmatory. The where/when/where-in-loop results are location ablations, not budget-enforced comparisons. The "continual" condition is continual-in-weights but rebuilds the optimizer each batch, and the amplification claim rests on a cross-family control. A confirmatory evaluation on a separately selected split would quantify how much of the measured gain transfers beyond the configurations explored here.

Acknowledgments. Thanks to Fable 5 for extensive help running the experiments, analyzing results, and drafting this writeup, and to GPT-5.6-Sol for reviewing the post and providing revision suggestions. This post documents an exploratory sequence of experiments on recurrent-depth adaptation. Future work will test the resulting calibration vectors across prompt families, tasks, and looped-model families.

Code and artifacts. The implementation, prompts, run manifests, aggregate results, figure inputs, and released generation logs are available at github.com/AlvinZH04/Loop-TTT.

Open to discussion. Comments, questions, and pushback are all welcome. I'm reachable at bzhang90@jh.edu and always happy to discuss this work.

Cited as: Zhang, Alvin (2026). "Loop deeper, or adapt? Test-time training in looped transformers." loop_steer notes. alvinzh04.github.io/blog/looped-ttt.html

@misc{zhang2026loopsteer,
  title        = {Loop deeper, or adapt? Test-time training in looped transformers},
  author       = {Zhang, Alvin},
  year         = {2026},
  howpublished = {\url{https://alvinzh04.github.io/blog/looped-ttt.html}},
  note         = {loop\_steer notes}
}
References
[1] Wang, D., Shelhamer, E., Liu, S., Olshausen, B., & Darrell, T. "Tent: Fully Test-Time Adaptation by Entropy Minimization." ICLR 2021.
[2] Zhu, R.-J., Wang, Z., Hua, K., et al. "Scaling Latent Reasoning via Looped Language Models." arXiv:2510.25741, 2025 (revised 2026).
[3] Chen, M., et al. "Evaluating Large Language Models Trained on Code" (the unbiased pass@k estimator). 2021.
[4] Agarwal, S., Zhang, Z., Yuan, L., Han, J., & Peng, H. "The Unreasonable Effectiveness of Entropy Minimization in LLM Reasoning." arXiv:2505.15134, 2025.
[5] Hu, Y., Zhang, X., Fang, X., Chen, Z., Wang, X., Zhang, H., & Qi, G. "SLOT: Sample-specific Language Model Optimization at Test-time." arXiv:2505.12392, 2025.
[6] Hu, J., Zhang, Z., Chen, G., Wen, X., Shuai, C., Luo, W., Xiao, B., Li, Y., & Tan, M. "Test-Time Learning for Large Language Models (TLM)." arXiv:2505.20633, 2025.
[7] Xu, Y., Yao, H., Guo, Z., Li, P., Liu, A., Hu, X., Guo, W., & Xiong, H. "You Only Need 4 Extra Tokens: Synergistic Test-time Adaptation for LLMs (SyTTA)." arXiv:2510.10223, 2025.
[8] Yang, A., et al. "Qwen2.5 Technical Report." arXiv:2412.15115, 2024.
[9] Kydlíček, H. "Math-Verify: Math Verification Library." Hugging Face, software (v0.9.0, used here).
[10] Cobbe, K., et al. "Training Verifiers to Solve Math Word Problems." arXiv:2110.14168, 2021.
[11] Hendrycks, D., et al. "Measuring Mathematical Problem Solving With the MATH Dataset." arXiv:2103.03874, 2021.
[12] Hendrycks, D., et al. "Measuring Massive Multitask Language Understanding." arXiv:2009.03300, 2021.
[13] Dehghani, M., Gouws, S., Vinyals, O., Uszkoreit, J., & Kaiser, Ł. "Universal Transformers." ICLR 2019, arXiv:1807.03819.
[14] Sharma, R., & Vu, T. "Dense Supervision Is Not Enough: The Readout Blind Spot in Looped Language Models." arXiv:2606.24898, 2026.
[15] Lightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker, B., Lee, T., Leike, J., Schulman, J., Sutskever, I., & Cobbe, K. "Let's Verify Step by Step." arXiv:2305.20050, 2023 (source of the MATH-500 evaluation subset).
[16] Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., & Chen, W. "LoRA: Low-Rank Adaptation of Large Language Models." ICLR 2022.
[17] Zhou, S., Ling, R., Chen, J., Wang, X., Fan, T., & Wang, H. "When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling." arXiv:2604.10739, 2026.
[18] Kingma, D. P., & Ba, J. "Adam: A Method for Stochastic Optimization." ICLR 2015, arXiv:1412.6980.
[19] Zhang, B., & Sennrich, R. "Root Mean Square Layer Normalization." NeurIPS 2019, arXiv:1910.07467.
[20] Yang, X.-W., Han, Z.-Y., Zhang, X.-H., Wei, W.-D., Shao, J.-J., Guo, L.-Z., & Li, Y.-F. "Stabilizing Recurrent Dynamics for Test-Time Scalable Latent Reasoning in Looped Language Models." arXiv:2605.26733, 2026.
