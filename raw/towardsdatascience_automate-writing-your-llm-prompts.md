<!-- sha256: 5db7fe8aa27123be59579dfbe859cc2eb2c5daa296beadff581990abc0a009b7 -->

W Brett Kennedy — June 5, 2026 — Towards Data Science
https://towardsdatascience.com/automate-writing-your-llm-prompts/
20 min read — Large Language Models

Automate Writing Your LLM Prompts
Using DSPy to automatically create, evaluate, and optimize your prompts

Working with LLMs, we've probably all had the experience of getting responses that weren't quite what we wanted. Usually we'll try rewording the prompts a few times until we get something reasonable. We sometimes have to be more clear, more precise, give examples, describe why we need the response, present a persona, or otherwise provide enough context and information that the LLM is able to provide a suitable response.

This can be fine when we're working directly with the LLM. However, it's quite different when we're writing an LLM-based application — software that will execute on its own, and that doing so will interact with one or more LLMs. Here, the software will work with predefined prompts and will pass these to the LLMs. If it doesn't go well, we're not there to reword the prompts and try again. Which means, they have to be written in a way that's robust and reliable in the first place — we need prompts that we can be confident will work consistently well in production.

Creating such a prompt can be tricky. In this article, we'll go over why that is, and also how a Python tool called DSPy can support creating prompts that will be reliable. DSPy not only generates prompts automatically for you, it also evaluates them thoroughly, so you can be confident of how well they'll likely work in production.

Also references the book "Building LLM Applications with DSPy" co-authored with Serj Smorodinsky (Manning Publishing).

The trick of creating a prompt that can work reliably in production

Part of what makes it difficult to create a reliable prompt is that we can't fully predict the input we'll have for the prompt. For example, if creating a software application that processes documents — they may be found online, or submitted by users. The application may ask an LLM to summarize, translate, extract key information, or perform some other task. For a plausibility assessment task, a simple prompt might be:

prompt_text = f"Assess how plausible the following text is: {document_text}"

This prompt may work sufficiently well, but it also may not. The LLM may pick up on irrelevant details, have a different sense of 'plausible' than intended, or format responses poorly. We may need to tweak the prompt significantly. As prompts get longer and more complicated, they become harder to tweak — it gets less clear what effect adding, removing, re-ordering, or re-wording phrases will have.

For a non-trivial application, the specific input will be at least somewhat unpredictable. The only way to test reliability is with a large, diverse, and realistic set of inputs. And for each test case, we need to carefully examine the LLM's response. This is straightforward for classification tasks, but for long-form outputs (summaries, translations, critiques), evaluating responses is time-consuming and error-prone.

Prompt Engineering (and its limitations)

Normally, working with LLMs uses prompt engineering: write one prompt, test it (usually with just a few inputs and eye-balling outputs), write another, test similarly, and continue. This has limitations:

- Time-consuming to test each candidate prompt with more than a small number of inputs
- LLMs are stochastic — same prompt can return different responses each time
- If we have 20 documents and test each 3 times = 60 tests total, which we realistically won't do
- Longer outputs are time-consuming to read and almost impossible to evaluate consistently
- Can't be certain the chosen prompt is really the strongest

In summary: prompt engineering is both time-consuming AND unreliable.

Is there a better way?

With ML projects, testing is automated: run each element through the model, get predictions, execute a function for an overall score (MSE, F1, AUROC, etc.). With LLMs, we've been ignoring decades of best practices for software development.

DSPy is the state of the art tool that lets us work with LLMs in a way that's efficient, thorough, and repeatable. We specify test data and a method to evaluate response quality, then DSPy handles everything else.

For a plausibility assessment example, we gather documents as test set with ground truth values (numeric 0-10 scale). Provide a Python evaluation function such as:

def evaluate_answer(test_instance, model_prediction):
   return abs(test_instance.ground_truth - model_prediction)

DSPy automatically executes the prompt on a specified LLM for each test document, compares to ground truth, and gives an overall score averaged over all test instances. Try different prompts or LLMs by simply re-executing — take the one with the best score.

For longer responses, an LLM-as-a-judge approach is often used. Not perfect, but removes human biases and can be automated, making thorough testing feasible.

What DSPy does for you (3 major things)

1. Automatically generates a prompt — provide a short, high-level task overview like "document -> assessment_of_plausibility" or "journal_article -> summary, critique"

2. Automatically evaluates the prompt — provide test data and a Python evaluation function; DSPy fully and consistently evaluates each prompt and LLM

3. Automatically optimizes the prompt — the most powerful element

Optimizing your prompts

DSPy goes into a loop:

best_prompt = ""
loop
  generate a new candidate prompt
  evaluate this candidate prompt
  if this is the best prompt so far:
    best_prompt = current prompt

Uses meta-prompting: one LLM generates the prompt for another LLM. DSPy uses early stopping for weak prompts (no need to test on full test set if performing poorly). The more effective optimization processes learn as they go — as each candidate prompt is evaluated, DSPy can see where and WHY each prompt performs well or poorly, and use this to suggest increasingly better candidate prompts.

After running DSPy

You'll have a prompt for your task and an estimate of how well it will work in production, based on test data behavior. If not strong enough, allocate more optimization time or try another LLM — just specify the new LLM and re-execute code.

Sample code

import dspy

OPENAI_API_KEY = [indicate your API key]
lm = dspy.LM("openai/gpt-4o-mini", api_key=OPENAI_API_KEY)
dspy.settings.configure(lm=lm)

predictor = dspy.Predict("question, context -> answer, confidence")
prediction = predictor(question="What is the capital of France?", context="")
print(prediction.answer, prediction.confidence)

This simple example specifies the task at a high level: given a question and context, return the answer and confidence. With evaluation and optimization added, code gets slightly longer but DSPy keeps most complexity under the hood. DSPy supports dozens of different LLM providers.

Conclusions

DSPy can't guarantee an extremely effective prompt for every task with every LLM, but saves enormous labour and tends to do as well or better than a professional prompt engineer. In experiments, DSPy has come out ahead consistently against manual prompt engineering.

For any non-trivial LLM application, use DSPy. It's like having a prompt engineering assistant — you set up the code and let it do the work. Can run for 20-30+ minutes to find a strong prompt. Monitor LLM costs, but higher quality prompts are usually cheaper in the long run. Easy to constrain: specify a small number of candidate prompts and take the strongest.