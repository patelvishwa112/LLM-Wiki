# Persona Vectors: Monitoring and Controlling Character Traits in Language Models

**Authors:** Runjin Chen, Andy Arditi, Henry Sleight, Owain Evans, Jack Lindsey
**arXiv:** 2507.21509 | Submitted Jul 29, 2025 (v3: Sep 5, 2025)
**Subjects:** cs.CL, cs.LG

## Abstract

Large language models interact with users through a simulated 'Assistant' persona. While the Assistant is typically trained to be helpful, harmless, and honest, it sometimes deviates from these ideals. In this paper, we identify directions in the model's activation space — persona vectors — underlying several traits, such as evil, sycophancy, and propensity to hallucinate. We confirm that these vectors can be used to monitor fluctuations in the Assistant's personality at deployment time. We then apply persona vectors to predict and control personality shifts that occur during training. We find that both intended and unintended personality changes after finetuning are strongly correlated with shifts along the relevant persona vectors. These shifts can be mitigated through post-hoc intervention, or avoided in the first place with a new preventative steering method. Moreover, persona vectors can be used to flag training data that will produce undesirable personality changes, both at the dataset level and the individual sample level. Our method for extracting persona vectors is automated and can be applied to any personality trait of interest, given only a natural-language description.

## Key Claims

1. **Persona vectors exist** in activation space for traits like evil, sycophancy, hallucination
2. **Monitor at deployment** — detect when the Assistant's personality fluctuates
3. **Predict training shifts** — personality changes after finetuning correlate with vector shifts
4. **Post-hoc intervention** — correct undesirable shifts after they occur
5. **Preventative steering** — avoid shifts before they happen during training
6. **Flag bad data** — identify training samples that induce undesirable changes
7. **Automated extraction** — works for any trait given a natural-language description

## Source
https://arxiv.org/abs/2507.21509
