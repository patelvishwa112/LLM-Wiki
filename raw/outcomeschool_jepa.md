<!-- sha256: 1702be67c4acf14e257d86d9df090d060dd18739557cd659ef581a39ca161537 -->

Amit Shekhar — June 6, 2026 — Outcome School
https://outcomeschool.com/blog/joint-embedding-predictive-architecture-jepa

Joint Embedding Predictive Architecture (JEPA)

How humans and animals learn by observing the world

Before jumping into JEPA, we must know how we, as humans, learn in the first place. A baby pushes a glass towards the edge of a table. The glass falls. The baby just learned something deep: objects fall when they go off an edge. Nobody taught this with words. Nobody handed the baby a textbook. The baby simply observed the world and figured out how the world works.

This is how humans and animals learn most things. We watch. We observe. And we build an understanding of the world inside our head. This inner sense lets us imagine what will happen next, before it even happens. And this simple human ability is the seed from which the whole idea of JEPA grows.

The question: can a machine also learn like this? Can a machine learn how the world works just by observing, the way a baby does?

Yann LeCun's vision of autonomous machine intelligence

Yann LeCun is one of the most respected researchers in AI. He served as Chief AI Scientist at Meta, where JEPA research was done, and is now building world models at Advanced Machine Intelligence (AMI) Labs. In June 2022, he wrote "A Path Towards Autonomous Machine Intelligence" — a vision for machines that learn a model of the world by observation, just like a baby, and could then imagine the result of actions and plan toward a goal. He calls this autonomous machine intelligence — a machine that learns on its own from observation and acts with common sense. JEPA is the core building block he proposed for this.

A simple everyday analogy

Looking at a photo of a street. The left half is visible (dog, grass, tree). The right half is covered by paper. Can we guess what's behind? Yes — "probably more grass, maybe more of the tree, and the dog's tail." But we do NOT guess exact pixels. We don't know the exact shade of every blade of grass or position of every leaf. We only guess the gist. The idea of what is hidden. "More grass, a tail, a bit of tree."

This is exactly how JEPA thinks. JEPA looks at one part of the data and predicts the gist of the hidden part, not every exact pixel.

What does JEPA mean

JEPA = Joint + Embedding + Predictive + Architecture

Joint: two things working together — the visible part (context) and the hidden part (target), handled side by side.
Embedding: a short list of numbers that captures the meaning of something. A compact summary, not raw pixels.
Predictive: guessing — the model predicts the summary of the hidden part from the summary of the visible part.
Architecture: the design, the blueprint of how pieces are connected.

In simple words: JEPA is a design where the model takes a summary of the visible part and predicts the summary of the hidden part.

What is an embedding or representation space

An embedding is a short list of numbers that captures the meaning of something. It's a compact summary. Raw photo: millions of pixels. Embedding: "this is a dog, it is brown, on grass, facing left." The space where all these summaries live is the embedding space or representation space. Similar things sit close together; different things are far apart. An embedding throws away messy, unimportant details and keeps the meaning.

The problem with predicting raw pixels

For a long time, AI models (generative models) learned by predicting raw input — e.g., cover half an image and redraw the missing half pixel by pixel. The catch: to redraw perfectly, the model must guess every tiny detail (exact grass texture, sky noise, leaf lighting). These details are unpredictable. The model wastes enormous effort guessing details nobody can guess. Like being asked to redraw a photograph from memory perfectly, including every random speck of dust.

The problem with contrastive methods

Contrastive learning: show two versions of same image → "pull them close." Show two different images → "push them apart." The "different" examples are negative examples. This works but usually needs many negative examples and hand-made data augmentation (cropping, flipping, color changes). The burden: extra negative examples and hand-made tricks.

The core idea of JEPA

JEPA takes a smarter path: predict in the embedding space, not in the pixel space. It does not redraw the hidden part — it only predicts the SUMMARY of the hidden part.

Generative model: visible part → redraw every hidden PIXEL (hard, wasteful)
JEPA: visible part → predict the SUMMARY only (clean, efficient)

When predicting only the summary, we're allowed to ignore messy, unpredictable details. We only guess the meaning — the part that can actually be guessed.

JEPA keeps the good parts of both older methods and drops their pain:
- From generative: learns the relationship between visible and hidden by predicting hidden from visible — but drops the pain of redrawing raw pixels.
- From contrastive: works in the clean world of summaries — but drops the pain of negative examples and hand-made augmentations.

The building blocks of JEPA

- Visible part = x (context); Hidden part = y (target)
- x-encoder: takes visible context x → summary s_x
- y-encoder: takes hidden target y → summary s_y
- Predictor: takes s_x + position → predicted summary s_y-hat

The position tells the predictor which hidden part to guess (like pointing at a specific covered window). The latent variable z carries missing clues — e.g., from the left half you can't know if it's raining on the right half. z handles uncertainty, letting the model say "the hidden part could be this, or it could be that."

The energy-based view: Energy = wrongness score. Low energy = predicted summary s_y-hat is close to real summary s_y. High energy = far apart. Training = making this gap small for real matching pairs.

How I-JEPA works (for images)

I-JEPA (Image JEPA), released by Meta AI in 2023, uses self-supervised learning — the model teaches itself by hiding part of data and predicting it.

Steps:
1. Take one image, cut into patches, processed by Vision Transformer (ViT)
2. Choose one larger visible context block (x) and several hidden target blocks (y). Target patches removed from context so model can't copy.
3. Context encoder → summary of visible block (x-encoder)
4. Target encoder runs over whole image, produces summaries for every patch, then picks out target block summaries (y-encoder). Important: encoder sees full image, selection happens after.
5. Predictor takes context summary + position → predicts target summaries. Never draws pixels, only predicts summaries.
6. Compare predicted summaries with real summaries from target encoder.

Avoiding collapse: If both encoders learn freely, they can cheat — output the same boring summary for everything, zero error, zero learning (representation collapse).

I-JEPA's solution — an uneven design:
- Context encoder: learns fast, updates every step
- Target encoder: does NOT learn directly. Follows context encoder slowly via Exponential Moving Average (EMA). Stop-gradient prevents learning signal from flowing into it.
- Target encoder acts as a fixed answer key. Student can't secretly change the answer key to make answers look correct.

This avoids collapse without any negative examples or hand-made data augmentation. I-JEPA trained on ImageNet using 16 GPUs in under 72 hours, far less than older methods.

V-JEPA and the world-model vision

V-JEPA (Video JEPA), released by Meta AI in February 2024, extends the idea to video. Hides regions of video, predicts summaries from visible regions, all in embedding space, never in pixels. V-JEPA 2 (June 2025) points toward world models — an internal sense of how the world behaves so a machine can imagine the result of an action before doing it.

A special version of V-JEPA 2 trained on robot video controlled a real robot arm to pick up and place objects in new labs, just by being given a goal image. The robot plans steps by imagining outcomes in the embedding space. This connects back to LeCun's 2022 vision.

When and why JEPA matters

1. Focuses on meaning, not messy detail — skips the impossible task of guessing unpredictable pixels
2. Efficient — predicting summaries is lighter than redrawing pixels, trains faster and cheaper
3. Clean — avoids negative examples and hand-made augmentations
4. Complementary to LLMs — LLMs learn from text but miss physical sense. JEPA learns intuitive understanding by watching the world.
5. Points toward bigger dream — machines that can imagine, plan, and act with common sense.

The one core idea: we look at part of a scene and predict the gist of the hidden part, not every exact pixel. That simple human intuition is the soul of JEPA.