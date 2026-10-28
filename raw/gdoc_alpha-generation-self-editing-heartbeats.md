---
source_url: https://docs.google.com/document/d/14qXSLPBZENOTmYJMJPQ7xFRtMzm00qCF9foTKqque70/mobilebasic
ingested: 2026-10-28
title: "Alpha generation p1 (self-editing heartbeats with seeds)"
author: unknown
sha256: b76a6719282639926e98e638a582b91e7491720b181ae2f131fcab18713d62fa
note: "Text extracted from public Google Doc; Google redirect links unwrapped and literal markdown escapes normalized. Body unchanged otherwise."
---

Note: this is part of a broader set of posts I will write on using models and applications in unorthodox ways. The current “shape of LLMs” and the cultural zeitgeist around AI use is focused on replacement of human labor, which I believe is missing the full picture. We have not seen many net new use cases, and I hope to change that. Please comment if you have thoughts, I hope to make this collaborative.

Alpha generation p1: self-editing heartbeats with seeds

Many of us use agents for information discovery. However, agents often find articles and resources that are “consensus” and quite surface level. A simple human google search, and a quick rabbit hole dive can get you to a much better suite of articles, whether it is a substack, a personal block, or a 2nd order academic article. Agents should be better at surfacing high quality information – and better yet – should be calibrated to what is important and what isn't.

In the last 3 months, I have been using a method that has drastically improved my agents abilities to find “rare tokens” – which I classify as pieces of content on the internet that are quite valuable to read, information dense, but also not seen by many. I hope to share that method here in the hope that it invites discussion about interesting ways to think about agent use (see Skill for quickstart)

The core beliefs of my strategy are

1. Seeding: Providing the model with an idea of “what good looks like”:

1. Tweets of importance (tweet that blew up with lots of individuals in the field of interest in the comments, ex [Nan Ransohoff x post for neo-philanthropy](https://x.com/nanransohoff/status/2056837134955470868?s=20))
2. Niche search engines & aggregators (ex [Secret Web](https://blog.clew.se/posts/secret-web/))
3. Sites to reverse engineer (ex gov’t aggregators, chinese province postings, etc)

2. Setup: Using a singular agent with a 1 minute, recurring, self-editing heartbeat on codex, a scratchpad, an edited dataroom, computer use (namely chrome), and the seeding in the first prompt.

1. Automations:

1. One of the most notable ways to use Codex as seen in the examples of Chief of Staff threads, daily reminders, and agentic cron jobs.
2. However, automations are useful beyond their original purpose because they can

1. They can wake up a thread every single minute
2. Automations are self-editable; the codex thread created by the automation can edit the automation.

2. Scratchpad:

1. Lives on the heartbeat directly, the agent is effectively editing its own messages after each 1 minute cycle and passing in context about the next iteration, deprioritizing or prioritizing certain leads, telling itself where to spend time, etc.

3. Agent Loop:

1. Scoping out an extension of the task on the automation scratchpad
2. Executed that task
3. Saving the results to a dataroom
4. Seeding new points to the scratchpad for the next iteration

3. This solves the bespoke action problem

1. Usually, model behavior on finding 5 examples of something differs from n=100 because at low n, models will take “bespoke actions” (i.e. the model will search each of the 5 individuals) while at high n, models will attempt to enrich all data at once.
2. Bespoke action yields greater quality. We can have every single iteration be extremely bespoke which generates higher quality results over time, even if it takes longer.

4. Entropy injection:

1. This approach lets the model cascade into randomness based on context injection from ideas found while researching, and update its own priors (i.e. the core scratchpad). If you sample from k runs, you will lead to a more diverse set of results in the data room than before!
2. You don’t know where the model will end up and that is the beauty.

Examples:

Note: for all of these domains, I had little to no background and the goal of this agent is to build a way to easily discover unknown unknowns and build context about a space really quickly. These results may seem trivial to people who understand the space, but getting ~25 high quality articles that can be assembled into a collage to quickly go 0 to 1 is the goal at hand.

Neo Philanthropy

After Nan Ransohoff’s[X post](https://x.com/nanransohoff/status/2056837134955470868) and Substack article,[The third wave of American philanthropy](https://nanransohoff.substack.com/p/the-third-wave-of-american-philanthropy), I got nerdsniped by new philanthropic institutions. I seeded a run with her tweet, alongside posts from[Cate Hall](https://x.com/catehall/status/2057149168741994945),[Peter Olivier](https://x.com/PeterOlivier/status/2057205352362299807), and[Dwarkesh](https://x.com/dwarkesh_sp/status/2056856368745726238). Over roughly 24 hours, I had the agent explore the people interacting with the posts and enrich their profiles via CUA. Then I let it loose on building a dataroom.

The search branched into science funding, FROs, talent, and grantmaking infrastructure. The dataroom ended up with 841 X accounts, 923 interactions, roughly 150 helpful articles, and a reading map of the core arguments. Fav resulting articles (found automatically) were

- [Early stage funding markets for science - an analysis (Nadia Asparouhova, Jan 2023)](https://nadia.xyz/reports/early-stage-science-funding-asparouhova-jan-2023.pdf)
- [A Scrappy Complement to FROs: Building More BBNs](https://www.freaktakes.com/p/a-scrappy-complement-to-fros-building)
- [The Third Wave of American Philanthropy in Africa](https://africajobsfund.substack.com/p/the-third-wave-of-american-philanthropy)
- [Metascience 101 - EP2: “Is Science Slowing Down?”](https://www.macroscience.org/p/macroscience-101-ep2-is-science-slowing)

Foreign project lists & Semiconductor dataroom

I found a[Hunan government posting](https://www.hunan.gov.cn/zqt/zcsd/202601/t20260126_33900948.html) linking to a list of industrial commercialization pilots that I wouldn’t have encountered through my usual English-language searches. I seeded a run with it and asked the model to find similarly concrete lists, one by one, across other countries and languages. It followed ministry attachments, regional government portals, research-funding programs, and commercialization databases, building a collection of 100 additional sources and 1,190 translated project ideas.

One of those ideas described full process-automation for semiconductor manufacturing, which I used as the seed for a deeper run. The model followed the vendor and customer into patents, filings, documentation, competitors, and factory implementation details. The resulting semiconductor dataroom contained 261 sources, 1,078 findings, a process map and a vendor landscape. Some interesting finds from both:

- [Chongqing’s enterprise R&D project list (February 2026)](https://kjj.cq.gov.cn/zwxx_176/tzgg/202602/t20260227_15464655.html), includes143 approved projects with named companies and concrete technical problems:

- Specialized measurement equipment for ultra-thin, transparent semiconductor wafers.
- Laser power-transmission equipment using adaptive optics.
- AI-assisted thoracic surgery combining multiple sensing methods.
- Forest firefighting systems connecting space, aerial, and ground capabilities.

- [Yantai, Shandong’s technology-innovation project list (published March 2026, covering the 2025 cohort)](https://www.yantai.gov.cn/col/col11795/art/2026/art_5c05dffb34054bf84cade4583831432b.html): a municipal list spanning specialized machinery, advanced materials, and biotechnology:

- Automated fuel-loading and unloading equipment for Guohe-series nuclear reactors.
- Laser-manufactured, corrosion-resistant MAX-phase impellers for liquid-metal pumps.
- AI-designed microbial communities for fruit and vegetable fermentation.
- EEG signal analysis paired with upper-limb rehabilitation robots.

- [Hunan’s major industrial project list (June 2026)](https://www.hunan.gov.cn/zqt/zcsd/202606/t20260612_33999713.html): follow up on new Hunan industrials projects.

- A development base for reusable stainless-steel liquid-propellant rockets.
- A small synthetic-aperture radar satellite constellation.
- SiC/IGBT power-semiconductor packaging and testing facilities.
- Synthetic biology manufacturing using straw and reeds to produce new materials.

- [Koyang’s wafer-fab scheduling patent (2025)](https://patents.google.com/patent/CN119398463B/en), using reinforcement learning to match wafer batches to machines, then Monte Carlo tree search to compare schedules. Factory patent.

Biotech craze of last few days

More recently, I saw a handful of X posts discussing biotech investment ideas, including posts from[Metavestor](https://x.com/metavestor/status/2107110857532735727),[ekernf01](https://x.com/ekernf01/status/2106750558019490148), and[approvedfm](https://x.com/approvedfm/status/2099643508944691222), and seeded a run with them. I asked the agent to follow the replies, profiles, and linked writing recursively, building a map of interesting people and their arguments. The search moved into specialist Substacks and competing takes on where value might accrue as AI changes biology. As it developed, I steered it toward reading people’s arguments and disagreements, using those readings to seed the next iteration.

The dataroom ended up with 1,450 saved artifacts, 47 note packages, and an overview with 16 editorial picks and six key disagreements. I then had the agent turn that material into a beginner walkthrough, with 12 chapters and a glossary, so I could build context for myself!

Funnily the model converged to Octant Bio. What started as a broad search through biotech investment posts ended up spending a lot of time on Sri Kosuri’s[Mens et Manus](https://srikosuri.substack.com/p/mens-et-manus),[Frontier Drugs](https://srikosuri.substack.com/p/frontier-drugs), and the connected[OpenADMET benchmark](https://openadmet.ghost.io/dont-look-back-in-error-what-we-learned-predicting-pxr-induction-part-i/).

---

name: heartbeat-scratchpad-loop

description: Build or run a long-lived task as a self-modifying thread heartbeat where the automation prompt acts as compact working memory. Use when the user wants an automation, monitor, recurring check-in, polling loop, watch task, or long-running search/research/process that should wake up over time, do one focused step, rewrite its own state, and continue later.

---

# Heartbeat Scratchpad Loop

Use this skill when the user wants a lightweight long-running task that persists through thread heartbeats and updates itself over time.

The core pattern is:

- the thread is the execution surface

- the available tools are the action surface

- the automation prompt is the scratchpad

Prefer this over a static reminder when the task needs memory, iteration, ranking, reprioritization, or recurring validation.

## When To Use

Use this skill for requests like:

- "set up a loop to keep checking this"

- "poll yourself every few minutes and keep going"

- "monitor this topic/contact/project over time"

- "create a long-running search task"

- "use automations as a scratchpad"

- "wake this thread later and continue"

Do not use this pattern for:

- one-shot reminders with no state

- tasks that should obviously be a detached cron job against a workspace instead of a thread

- tasks with no clear objective or no meaningful action surface

## Workflow

1\. Decide the execution shape.

- Prefer a `heartbeat` automation when the task should continue in the current thread.

- Prefer `cron` only when the work should run detached against a workspace.

- If an existing automation already owns the task, update it instead of creating a duplicate.

2\. Reduce the task to objective `X` plus tool/data surface `Y`.

Define, in plain terms:

- objective

- data sources and tools

- ranking criteria

- what counts as progress

- notification threshold

- stop condition

- cadence

3\. Seed the first prompt compactly.

The first prompt should contain:

- `Current objective`

- `Sources to use`

- `Current state`

- `Ranked candidates / hypotheses / tasks`

- `Deprioritized items`

- `Next actions`

- `Guardrails`

- `Stop condition`

Read [references/prompt-template.md](references/prompt-template.md) when you need a scaffold.

4\. Run the control loop on each wakeup.

Each heartbeat should do one focused unit of work:

- inspect the current automation state

- inspect the external sources

- validate or rank 1-3 concrete items

- checkpoint durable work to git when the project is in a git repo and a meaningful unit of progress has landed

- rewrite the automation prompt with fresher compact state

- notify the user only if something crosses the notification threshold

Do not let the loop sprawl. Small focused steps beat broad rescans.

5\. Keep the scratchpad compact.

- Overwrite stale sections instead of appending endlessly.

- Promote only the highest-signal facts into the prompt.

- Keep lists ranked.

- Use absolute dates.

- Remove obsolete branches.

6\. Close the loop when done.

- Delete the automation when the objective is complete, stale, or no longer worth polling.

- If the task survives but the shape has changed, update the automation instead of letting stale instructions linger.

## Version Control

When the control loop is working inside a project repo:

- make small checkpoint commits as meaningful units of work land

- prefer one commit per durable step rather than one giant catch-up commit

- keep commit messages concrete and stateful

- if no git repo exists for a project that clearly needs ongoing checkpointing, initialize one at the project root unless the user has said not to

- mention the repo path and commit behavior when seeding or updating the loop prompt so the automation keeps treating commits as part of progress

## Scratchpad Rules

- The prompt is short-term memory, not a transcript.

- Prefer ranked bullets over narrative paragraphs.

- Store conclusions, not raw dumps.

- Track only the next few actions, not every possible branch.

- Keep one automation as the canonical owner for one subproblem.

Good scratchpad sections:

- `Current objective`

- `Signals / evidence`

- `Ranked leads`

- `Open questions`

- `Next actions`

- `Guardrails`

## Multi-Automation Pattern

For bigger tasks, split by role:

- `scout`: finds new candidates

- `validator`: checks whether candidates are real/relevant

- `monitor`: watches inbox/calendar/messages/news/source changes

- `coordinator`: maintains the merged shortlist and user-facing updates

Only split when the loops are genuinely separable. If not, keep one automation.

## Tooling

Use `automation_update` to create, update, view, or delete the automation.

## Response Style

When building one of these loops:

- say what the loop is for

- say what tool/data surfaces it will use

- make the automation prompt the scratchpad

- keep cadence and stop conditions explicit

- prefer concrete ranked state over vague ambitions
