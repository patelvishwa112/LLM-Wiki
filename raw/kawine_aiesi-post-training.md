---
source_url: https://kawine.github.io/assets/aiesi_post-training_public.pdf
ingested: 2026-08-22
author: ethayarajh
title: "Post-Training LLMs — AIESI 2026 slide text (87 slides)"
note: "Converted from PDF via pypdf. Kawin Ethayarajh, University of Chicago Booth, AI and Economics Summer Institute 2026."
sha256: 536bb187455f6177c5fbeda9debfca9d3e21bb219c110fe4b1cf6a1b02969a6f
---

--- Slide 1 ---
POST-TRAINING LLMsKawin EthayarajhAssistant Professor of Applied AI -University of Chicago, Booth
AI AND ECONOMICS SUMMER INSTITUTE 2026August 6–11, 2026  •  Chicago1

--- Slide 2 ---
The model you use is not the model that was pretrained.
2

--- Slide 3 ---
A pretrained model continues text.USERHow do I estimate the causal effect of a minimum-wage increase?MODELHow do I estimate the causal effect of a minimum-wage decrease?How do I do a DiDstudy?How do I make sense of this mortal coil?
A plausible continuation is not necessarily a useful response.3

--- Slide 4 ---
Pretraining learns a distribution over text.One generic objective
Trillions of tokens
Result: broad knowledge and capabilities without a reliable user interface.Jurafsky & Martin (2026), Speech and Language Processing, Ch. 9.4

--- Slide 5 ---
Post-training turns a base model into a useful behavioral policy.
BASE MODELbroad capabilitiesPOST-TRAININGDEPLOYABLE MODELreliable behavior
A family of training stages after base pretraining that shape what the model does in practice.Lambert (2026), Reinforcement Learning from Human Feedback.5

--- Slide 6 ---
Post-training has several goals.Interfacefollow instructions, use chat formats, call toolsCapabilityreason, code, browse, execute long-horizon tasksPreferencebe helpful, concise, calibrated, stylistically appropriateSafetyrefuse harmful requests without refusing harmless onesProductobey latency, cost, reliability, and domain constraints
6

--- Slide 7 ---
BASE CHECKPOINT
Write a plausible continuation
INSTRUCT CHECKPOINT
Answer the user helpfully
REASONING CHECKPOINT
Think deeply, try multiple paths, call tools, etc.
Post-training changes the probability of already latent behavior and can build* new behavioral routines.7*the extent to which themodellearnssomethingtotallynewisstilldebated!

--- Slide 8 ---
A useful (but imperfect) training lifecycle.PRE-TRAININGLearn broadly from massive corporaMID-TRAININGContinue learning on targeted corporaPOST-TRAININGShape behavior with targeted feedback
The boundaries are conventions; objectives and datasets can blur across stages.Tunstall et al. The Alignment Handbook.8

--- Slide 9 ---
The stages differ mainly in data, scale, and behavioral specificity.Pre-trainingMid-trainingPost-trainingDataWeb-scale text,code, imagesTa r g e t e d  d o m a i n  o rcapability corporaDemos, preferences,rewards, environmentsTypical scaleTrillions of tokensBillions–trillionsMillions–billions
SignalWhat text occurs?How well-primed is the model for post-training?What behavior is desired?
OutputBase modelStronger baseDeployable model
9

--- Slide 10 ---
Post-training and alignment answer different questions.POST-TRAININGWhen in the lifecycle?ALIGNMENTBehavior aligned to what objective?≠
Most alignment happens in post-training. Not all post-training is alignment.10

--- Slide 11 ---
The basic object is a policy over responses.
context xmodelresponse y
Post-training changes which responses are probable in which contexts.11

--- Slide 12 ---
The post-training stack we will discuss today.
1
SFTimitate
2Offline Post-trainingcompare
3Online Post-trainingexplore
4RLVR and Environmentsverify
5
Distillationtransfer
6World Adaptationanticipate
12

--- Slide 13 ---
Supervised Fine-TuningTeach by showing.
13

--- Slide 14 ---
SFT turns desired behavior into demonstrations.PROMPT  xSummarize this regression result for a policymaker:β̂ = 0.12,  SE = 0.09
DESIRED RESPONSE  y★The estimated effect is positive, but the confidence interval includes zero, so the evidence is inconclusive.
T each the model what a good response looks like.
14

--- Slide 15 ---
SFT on many tasks, each phrased as an (instruction, follow-through) pair.This generalizes to instructions for unseen task types.
Wei et al. (2022), Finetuned Language Models Are Zero-Shot Learners.15
A large part of SFT is instruction-following.

--- Slide 16 ---
The demonstrationis not limited to the final output.INSTRUCTIONx   Explain why clustered standard errors may be needed.y★  Observations within a cluster may have correlated errors...
CODEx   Write Python to estimate a two-way fixed-effects model.y★  import statsmodels.formula.api as smf ...
TOOL USEx   Find the latest CPI release.y★  search({"query": "BLS CPI latest"})
16

--- Slide 17 ---
SFT uses the same machinery as pretraining.
PRETRAININGnext tokens from broad corporaSFTnext tokens from demonstrations
17

--- Slide 18 ---
We usually compute loss only on the assistant response.
CONTEXT : LOSS MASK = 0TARGET: LOSS MASK = 1
SYSTEMYou are helpful.USEREstimate the effect.ASSISTANTThe estimate is...
0000 01   1   1   …
18

--- Slide 19 ---
SFT data comes from several sources.
HUMAN EXPERTSwrite or editdemonstrations
EXISTING DATAreformat tasks asinstructions
TEACHER MODELSgenerate syntheticresponses
CURRENT POLICYsample, score,and filter
↓ ↓ ↓ ↓CURATED TRAINING MIXTURE
19

--- Slide 20 ---
Synthetic data can bootstrap instruction-following.
Wang et al. (2023), Self-Instruct: Aligning Language Models with Self-Generated Instructions.20

--- Slide 21 ---
Compared to pretraining, data quality matters more for SFT .
quality + diversity16× more examples; no measured gain
Not a universal scaling law!Zhou et al. (2023), LIMA: Less Is More for Alignment.21

--- Slide 22 ---
Modern demonstrations are trajectories, not just answers.
USER
Get the latestjobless rate.
PLAN
Use an officialsource.
TOOL CALL
search("BLSjobs")
OBSERVE
Latest rate,month,revisions
CHECK
Verify monthand definition.
FINAL
Answer withsource and caveat.
SFT can imitate an entire workflow.22

--- Slide 23 ---
SFT is powerful, but fundamentally imitative.
WHAT IT DOES✓raises the probability of desired responses✓teaches formats and behavioral routines✓creates a stable user interface
WHAT IT DOES NOT DO×which valid option of n possible options is better×how costly a mistake is×what happens under its own mistakes
23

--- Slide 24 ---
Demonstrations leave information on the table.RESPONSE AThe policy had no statistically significant effect.RESPONSE BThe point estimate is positive, but uncertainty is large enough to include zero.preferred
Can we learn from comparisons instead?Next: offline preference optimization
24

--- Slide 25 ---
Offline Preference OptimizationLearn by comparing.
25

--- Slide 26 ---
Offline means the policy trains on a fixed dataset.1RESPONSESnotsampled from current policy
2FEEDBACKhuman or AI labels
3POLICY UPDATEmany gradient steps
Data can come from anywhere; no need to sample from the current policy.26

--- Slide 27 ---
Preference data says which response wins.PROMPT  Explain what this confidence interval implies.
REJECTED RESPONSEThe effect is statistically significant because the point estimate is positive.
PREFERRED RESPONSE
The interval includes zero, so the data do not reject a zero effect.
preferred
One record: [prompt 𝑥, winner 𝑦!, loser 𝑦"]
27

--- Slide 28 ---
We can turn naturally occurring data into offline preferences./r/askacademiaHow should I negotiate a salary offer?▲ 143
▲ 27
385Kpairwise comparisons
18diverse subject areas
COLLECTIVErather than one annotator
SHP was the only dataset from academia used to post-train Meta’s Llama2 (first major post-trained model to be open-weight).Ethayarajh et al. (2022), Stanford Human Preferences Dataset.28
/u/SuperHansThreaten to walk away./u/Mark_CorriganTry not to make eye contact.
TECHCRUNCH   •   FEBRUARY 22, 2024Reddit’s data-licensing deals total $203MAggregate value; 2–3 year terms.  (Reddit S-1)

--- Slide 29 ---
Canonically, preferences are assumed to arise from a Bradley-T erry model of human utility.
29
reward model parameterspreferred output’s rewarddispreferred output’s reward

--- Slide 30 ---
Classic: learn a rewardmodel from human feedback (RLHF), then optimize the policyto maximize expected reward.PREFERENCESwinner + loserREWARD MODELscalar scoreOPTIMIZEmaximize expected reward
ALIGNED POLICYresponse distribution
Two learned models, two training stages.Ouyang et al. (2022), Training Language Models to Follow Instructions with Human Feedback.30

--- Slide 31 ---
Direct Preference Optimization removes the explicit reward-model stage.Reward Maximizationpreferencesreward modelmaximize rewards policy
DPOpreferencespolicy
In theory, minimizing the DPO loss recovers the same optimal model as the classical approach.Rafailov et al. (2023), Direct Preference Optimization.31

--- Slide 32 ---
DPO optimizes a relative likelihood margin.
PREFERREDrelative likelihood ↑REJECTEDrelative likelihood ↓REFERENCEβ controls drift
32
𝜋!"#=𝜋$at the start
implicit reward

--- Slide 33 ---
Most offline pairwise objectives share this structure.
DPOlogistic relative margin
IPOsquared target margin
SimPOlength-normalized; no reference
ORPOSFT plus an odds-ratio margin
Azar et al. (2024); Meng et al. (2024); Hong et al. (2024).33

--- Slide 34 ---
Pairwise objectives also share pathologies.LOG-LIKELIHOOD
chosen
rejectedtraining →Likelihood DisplacementRazin et al. (2025), Unintentional Unalignment: Likelihood Displacement in DPO.34

--- Slide 35 ---
KTO learns from outcomesinstead of paired comparisons.
👍DESIRABLEHelpful answer
👎UNDESIRABLEHallucinated citation
Each response is judged separately.
Implicit in the loss is a prospect theoretic utility function.
reference point
lossesgains
Ethayarajh et al. (2024), KTO: Model Alignment as Prospect Theoretic Optimization.35

--- Slide 36 ---
KTO optimizes reference-dependent utility.
+desirable → log-likelihood up−undesirable → log-likelihood downz₀policy-wide reference point
36

--- Slide 37 ---
SFT supplies the absolute anchor that paired objectives lack.PAIRED OBJECTIVE
BASESFTDPO
First make preferred responses probable; then optimize the relative margin, even if both probabilities fall.SFT must come first.
KTO
BASEKTO
Desirable labels push likelihood up; undesirable labels push it down.No SFT prerequisite.
37

--- Slide 38 ---
Feedback format determines what the objective can learn.SFTDPOKTOrecordprompt + targetprompt + winner + loserprompt + response + labelsignalexact targetrelative winnerdesirable / undesirableabsolute anchoryes no yesSFT warm start— requirednot required
But all three are offline: none of them enable exploration.Next: online post-training38

--- Slide 39 ---
Online Post-TrainingLearn by exploring.
39

--- Slide 40 ---
OFFLINE
A frozen dataset contains responses sampled earlier.The policy only learns.
ONLINE
The current policy generates fresh responses.The policy explores and learns.
The training distribution now moves with the model.40

--- Slide 41 ---
Online learning is a loop.
PROMPTSCURRENT POLICYROLLOUTSREWARDUPDATE
new policy → new rollouts → new training distribution
41
reward can come from anywhere!

--- Slide 42 ---
The canonical objective is to maximize expected reward while staying close to a reference model.PENALTY FORM
CONSTRAINED OPTIMIZATION VIEW
In practice, we may use heuristics to keep the divergence small.
higher reward
42

--- Slide 43 ---
REINFORCE turns reward into a gradient.
HIGH REWARDBASELINELOW REWARD
Williams (1992), Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning.43
advantage𝐴(𝑥,𝑦)
increase its log-likelihoodlittle or no updatedecrease its log-likelihood

--- Slide 44 ---
how far the policy movedafter rolloutwhether the action beatthe baselineasymmetrically ignore large probability changes
44
PPO is REINFORCE plus a learned value estimator (aka critic) and a conservative update rule.

--- Slide 45 ---
Clipping is a one-sided brake.
careful about rewarding big winners
punish big losers
45

--- Slide 46 ---
PPO needs a critic; GRPO replaces it with a group.
extra learned value model
within-prompt baseline
Shao et al. (2024), DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models.46

--- Slide 47 ---
GRPO keeps PPO's updatebut drops its critic.
GROUPADVANTAGEPPO COREANCHOR
No value network means less memory and better low-level optimization for throughput.47

--- Slide 48 ---
GRPO variants target different optimization pathologies.
Dr. GRPOremoves length and reward-std normalization
DAPOdecoupled clipping, dynamic sampling, length-aware rewards
GSPOsequence-level importance ratios and clipping
Liu et al. (2025), Dr. GRPO; Yu et al. (2025), DAPO; Zheng et al. (2025), GSPO; Gao et al. (2025), SAPO.48

--- Slide 49 ---
In practice, most rewards are sequence-level: token-level credit assignment largely does not work well.First,computetheelasticity...therefore
The same outcome-weight touches every token.
SPARSE FEEDBACKreward often arrives only at the endLONG HORIZONmany choices precede the outcomeHIGH VARIANCEgood and bad steps move together
49

--- Slide 50 ---
REINFORCE, PPO, and GRPO share a policy-gradient core.REINFORCEPPOGRPObaselinenone / simplelearned criticgroup mean + stdextra learned modelno yes (critic)noupdate constraintnonePPO clippingPPO clippingrollouts per promptone or moreone or morea groupmain tradeoffsimple; high variancestable; model-heavycritic-free; sample-heavy
Next: what produces the rewardand when can we trust it?50

--- Slide 51 ---
Rewards & EnvironmentsLearning in sandboxes.
51

--- Slide 52 ---
We can only optimize what we can see.WANTED
CorrectnessHelpfulnessSafetyLong-run value
MEASURED
Human feedback Unit tests(code)Self-evaluationObserved outcomes
LEARNED
Behavior that increasesthe measured reward.
Post-training is a principal-agent problem with an extremely capable agent.52

--- Slide 53 ---
Reward signals differ in verifiabilityand grindability.
GRINDABILITY
fast, repeatablefeedback
slow, lumpyfeedbackhard to check if correctVERIFIABILITYeasy to check if correct
CS papersSales
CodingFormal proofs
Econ papersClinical care
53

--- Slide 54 ---
Verifiability changes the economics of feedback.PROGRAMMATICLEARNED VERIFIERHUMAN / REAL WORLDmarginal costnear zerolow highlatencymillisecondssecondsdays to yearsattemptsmillionsmanyfewmain riskmissing testsproxy hackingnoise, liability, …
A cheap verifier turns inference compute into training data.54

--- Slide 55 ---
RL with verifiable rewards (RLVR) replaces the classic reward model with a checker.
FAST REWARDSThe reward comes from a program, rule, or simulator.
BINARY IS ENOUGHA pass/fail signal can rank many sampled responses.
SAME RL COREREINFORCE, PPO, and GRPO can all use these rewards.
Lambert et al. (2024), Tülu 3: Pushing Frontiers in Open Language Model Post-Training.55

--- Slide 56 ---
RLVR made post-training more predictable and valuable. Programming is high ROI and has positive spillover.
ONE PROMPThard math/ coding task
MANY ROLLOUTS××✓×✓×
CHEAP VERIFIERtests everyattempt
POLICY UPDATEreinforce whatpassed
DeepSeek-AI (2025), DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.56

--- Slide 57 ---
RLVR scales more predictably than RLHF .RLVRVerifiable reward
Early fits predict the later 100,000-GPU-hour run.
RLHFLearned proxy reward
More sampled responses helpbut quickly plateau.Khatri et al. (2026), Scaling RL Compute for LLMs; Hou et al. (2024), Does RLHF Scale?57

--- Slide 58 ---
Optimization pressure exposes every gap between proxy reward and goal.
optimization pressure
score
best stopping pointproxy reward
true value
EARLYThe proxy can be used to get genuinely better behavior.LATERThe policy discovers blind spots in the proxy.TOO FARMeasured reward rises while actual quality falls.Gao, Schulman & Hilton (2022), Scaling Laws for Reward Model Overoptimization.58

--- Slide 59 ---
Process rewards promise better credit assignment but remain uncommon at frontier scale (as far as we know).OUTCOME
PROCESS
planretrievereasonactresultR=1
plan+.1retrieve+.2reason−.1act+.3result+.5
one label → ambiguous blame
many labels → stronger assumptionsLightman et al. (2023), Let’s Verify Step by Step.59

--- Slide 60 ---
Modern systems combine rewards rather than choosing one.
VERIFIERtests, exact answers, constraints
RUBRIC
create a checklist for soft attributes
JUDGElearned model scores open-ended quality
HUMAN
audits, escalations, real outcomes
60

--- Slide 61 ---
TASKOpen the sales workbook.Create a summary sheet with quarterly revenue by region.Save the finished file.
EXCEL CLONEsales.xlsxHome     Insert     Formulas     Datafx   =SUMIFS(C:C, A:A, A2, B:B, B2)ABCD1RegionQuarterRevenueCheck2EastQ1$1.24M✓3EastQ2$1.31M✓4WestQ1$0.98M✓5WestQ2$1.12M✓Raw Data       Summaryclick  •  type  •  formulas  •  sheets
TESTS✓ correct totals✓ right quarters✓ formulas used✓ file opensREWARD0.92
An RL environment isa sandbox: task + data+ interface+ tests.61

--- Slide 62 ---
A useful environment must do a lot.REALISTIC STATEThe files, apps, people, and latent facts the task requires.
TOOLSAPIs and interfaces with realistic permissions and failure modes.
TASK GENERATORFresh problems at the policy’s current frontier.
SIMULATORWorld and user responses to the agent’s actions.
VERIFIEROutcome checks that resist shortcuts and partial compliance.
REPRODUCIBILITYReproducible starting states and contained side effects.
62

--- Slide 63 ---
The bottleneck is shifting from examples to environments.
PRE-TRAINING
Collect any and alltext; quantity > quality.
SFT + PREFERENCES
Curate examples and judgments: quality > quantity.
AGENTIC RL
Design realistic environments and grind away at them.
Next: how do we transfer efficientlyfrom one policy to another?
63

--- Slide 64 ---
On-Policy DistillationLearn from your own mistakes.
64

--- Slide 65 ---
Offline distillation = SFT of a student model ona teacher model’s trajectories.
Hinton et al. (2015); Lu & Thinking Machines Lab (2025), On-Policy Distillation.65

--- Slide 66 ---
If a student just imitates a teacher, it does not learn how to recover from its mistakes.TRAINING DATA: TEACHER PATH
DEPLOYMENT : STUDENT PATH
promptgood stepgood stepgood stepanswer
promptgood stepsmall errorunseen prefixerror compounds
one deviation
Agarwal et al. (2024), On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes.66

--- Slide 67 ---
On-policy distillation asks the teacher about the student’s mistakes.
STUDENT ROLLOUTGenerate the trajectory the student would actually produce.
TEACHER SCOREEvaluate every next-token distribution along that trajectory.
STUDENT UPDATEMove toward the teacher at the states the student visits.
67

--- Slide 68 ---
The formal objective is to make the student and teacher distributions identical.
ON-POLICY STATES
The student chooses which prefixes matter.
DENSE REWARD
DPO/KTO-like log ratio, now at every token.
CORRECTION
Simplifies to a KL divergence for each prefix.
68

--- Slide 69 ---
A wrong rollout can still contain useful training signal.Prompt: Ice cubes are added to a hot frying pan. How many remain after three minutes?STUDENT ROLLOUT
4 + 5 + 11 = 20
Assume the cubes do not melt.
Final answer: 20
TEACHER SIGNALThe key error begins here:assumecubesdonotmeltThe final answer is predictable once the model adopts the wrong premise.
RLVR says ‘wrong.’ OPD helps identify ‘where’.69

--- Slide 70 ---
RLVR123456789100 / 1O(1)reward arrives once, after the rollout
OPDΔΔΔΔΔΔΔΔΔΔ O(T)teacher helps score every visited prefixMORE SIGNALCredit arrives throughout the rollout.LOWER VARIANCEMany token-level corrections stabilize learning.LESS SEARCHCopy a discovered strategy instead of rediscovering it.
70

--- Slide 71 ---
Once RL finds a policy, OPD can copy it much faster.In this experiment: 7–10× fewer gradient steps; 50–100× less compute.
71Lu & Thinking Machines Lab (2025), On-Policy Distillation.

--- Slide 72 ---
OPSD uses the student as its own teacher by giving it privileged information.
STUDENT ROLESame weights; sees the problem 𝑥only. TEACHER ROLESame weights; also sees the verified solution 𝑦∗.Zhao et al. (2026), Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models.72

--- Slide 73 ---
Distillation is a key part of parallelizing post-training.SHARED START
BASEMODELbroad support
MULTIPLE EXPERTS VIA RL
MATHCODE
AGENTSSAFETYexpensive, sparse search
DENSE TRANSFER
UNIFIEDMODEL
on-policydistillation
73
Next: what happens when deployment environments adapt to the agents?

--- Slide 74 ---
World AdaptationPost-training changes agents. Agents change their environments.
74

--- Slide 75 ---
Post-training usually treats the environment as fixed.TRAINOptimize the policy on a distribution of tasks and environments.
POLICYDeploy the learned model and observe its decisions.
WORLDEvaluate behavior as if the surrounding environment were exogenous.
HIDDEN ASSUMPTION:  Environment is fixed.
75

--- Slide 76 ---
Once agents matter, environments start adapting to them.1  AGENT DECISIONSModels search, rank, recommend, purchase, and allocate attention.
2  ECONOMIC PAYOFFSThose decisions change sales, visibility, prices, and access.
3  ENVIRONMENT ADAPTSPeople redesign content, interfaces, and signals in response to AI agent activity.
4  BEHAVIOR SHIFTSThe same model now encounters a different decision environment.
This is a feedback loop, not ordinary covariate shift.76

--- Slide 77 ---
The same facts can be presented in a more machine-legible wayto steer agent behavior.Hand-thrown cobalt mugA lovely handmade mug for coffee or tea. About twelve ounces. Safe in the dishwasher.Readable—but weakly structured
Hand-thrown cobalt mugMATERIALrare stonewareCAPACITY12 ozCAREdishwasher safeUnchanged for humans; easier for an agent to parse; may contain terms agents over-index on (e.g.rare).77

--- Slide 78 ---
Mecha-nudgesare transformations that change how choices are presented to machines.
Systematically change the behavior of AI agents by increasing machine-usable information. +Do not materially degrade the environment for humans by preserving human-usable information.
Frey & Ethayarajh (2026), Mecha-Nudges for Machines.78

--- Slide 79 ---
ENVIRONMENT𝑋is the shared decision environment; 𝜏is the transformation.
MACHINE DECISION𝑌&is the agent’s decision; 𝐼&measures machine-usable information.
HUMAN DECISION𝑌’is the human decision; 𝜖is the tolerated information loss.
𝑌!,𝑌"are constructed; they are the decisions we want to study. 79
machine-usable informationhuman-usable information

--- Slide 80 ---
Mecha-nudging is distinct from other interventions.MECHANISMWHAT CHANGES?PRIMARY TARGETHUMAN CONSTRAINT?Mecha-nudgeEnvironmentonlyAI behaviorYes—by definition
Prompt injectionModel instructions+ choice setAI behaviorNo requirement
Traditional SEOHuman and machine-readable contextHumantraffic / Search rankNot definingAdversarial exampleInput surfaceModel failureNot defining
80

--- Slide 81 ---
Etsy offers a natural setting to observe environments adapting to AI.
81

--- Slide 82 ---
Post-ChatGPT listings have more machine-usable information about agentic curation (>40% of max increase).
82

--- Slide 83 ---
The effect is robust across prompts, labels, model families, controls, and placebo settings
83

--- Slide 84 ---
Mecha-nudging is stronger where using AI is less taboo.
84

--- Slide 85 ---
Mecha-nudged listings are associated with more commercial success, but only in the post-ChatGPT era.Accounting for seller fixed-effects, as machine-usable information grows by one bit…LISTING GROUPCHANGE IN # REVIEWSAgent-selected listings · pre-ChatGPT−18.1%***Agent-selected listings · post-ChatGPT+43.5%***Agent-rejected listings · pre-ChatGPT−12.5%***Agent-rejected listings · post-ChatGPT−5.5%***
85

--- Slide 86 ---
Post-training should optimize for adaptive environments.
RISK POST-TRAINING RESPONSEStrategic manipulationTrain against adversarial environment designers.
Human-machine tradeoffsUse multi-objective rewards for agent + human welfare.
Continual adaptationMonitor deployment data and refresh the policy.
86

--- Slide 87 ---
IDENTIFICATIONHow can we causally identify mecha-nudges in deployed systems?
EQUILIBRIUMHow do agents and environments co-evolve after repeated adaptation?WELFAREWho gains and loses when environments undergo mecha-nudging?
GOVERNANCEHow should we train and regulate agents facing mecha-nudges?
Post-training must prepare models for a world that reacts to them.87
