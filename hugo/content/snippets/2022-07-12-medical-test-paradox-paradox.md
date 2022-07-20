+++
title = "The Medical Test Paradox Paradox"
date = 2022-07-12T00:00:00
tags = ["math"]
math = true
+++

In this snippet we're going to introduce the Medical Test Paradox _Paradox_.

First, you may already be familiar with the [Medical Test Paradox](https://www.youtube.com/watch?v=lG4VkPoG3ko). It's a popular recreational math problem that teaches Bayes' theorem and the importance of base rates. It goes like this.

> Suppose 1 in 10000 people have a certain disease, and there is a medical test that is 99% accurate. This means that if you do have the disease, the test comes back positive with 99% probability, and if you do not have the disease, the test comes back negative with 99% probability. It is wrong 1% of the time.
>
> If your test result comes back positive, what's the probability that you have the disease?

<details>
  <summary>Spoiler: Expand this to see the solution.</summary>

The classic solution proceeds as follows.

Let $D=\text{yes}$ be the event where you have the disease.
Let $T=\text{positive}$ be the event where the test comes back positive.

Using this notation, we want to find $P(D=\text{yes} | T=\text{positive})$.
We proceed by Bayes' theorem.

$P(D=\text{yes} | T=\text{positive}) = \frac{P(T=\text{positive} | D = \text{yes})P(D = \text{yes})}{P(T = \text{positive})}$
$$= \frac{P(T=\text{positive} | D = \text{yes})P(D = \text{yes})}{P(T=\text{positive} | D = \text{yes})P(D = \text{yes}) + P(T=\text{positive} | D = \text{no})P(D = \text{no})}$$
$$= \frac{0.99 \cdot \frac{1}{10000}}{0.99 \cdot \frac{1}{10000} + 0.01 \cdot \frac{9999}{10000}}$$
$$= 0.009803 \approx \fbox{1%}$$
</details>

It's a "paradox" only because the answer is surprisingly low. If you haven't solved it or peeked at the solution yet, have a guess at the rough answer before you look at the true one.

Now, on to the Medical Test Paradox Paradox. The Medical Test Paradox Paradox asks: given that tests for _actual_ diseases are generally much _less_ than 99% accurate, and given that prevalences for _actual_ diseases are [frequently](https://www.medicalhomeportal.org/diagnoses-and-conditions/diagnosis-prevalence-list) _less_ than 1 in 10000, _how is it that doctors use tests to diagnose people with these diseases, frequently literally saving their lives, **all the time**?_

This is meant to be treated as a serious question, a puzzle if you will. So take a minute and think about it, and attempt to provide a serious answer.

Like the Medical Test Paradox, the Medical Test Paradox _Paradox_ is of course not a true paradox. There is a simple explanation that accounts for an apparently paradoxical discrepancy. First, why does it look like a paradox at all?

Take any real disease with prevalence roughly 1 in 10000 (e.g. [from this list]([frequently](https://www.medicalhomeportal.org/diagnoses-and-conditions/diagnosis-prevalence-list))). These are real diseases affecting real people. The best tests for that disease likely has less than 99% accuracy.
So even if you test positive for the disease, Bayes' theorem suggests the probability you have the disease remains less than 1%. How are people then getting diagnosed with the disease at all? It seems as if doctors would have no way to conclude with greater than 1% certainty that you have the disease, even if your test comes back positive. You don't want to give someone a treatment with side effects if there's only a one percent chance they're actually afflicted with the disease in question.

<details>
  <summary>Expand to see the rest of the snippet. We discuss resolutions to the paradox.</summary>

The Medical Test Paradox assumes that prior to taking the medical test, the probability that you have the disease is given by the disease's prevalence, i.e. 1 in 10000. This is true if the medical test is being administered to random members of the population.
However, usually there is a _reason_ for administering a medical test.
Common reasons you might take a medical test include (a) you are showing symptoms or (b) exposure to a pathogen.
In these scenarios, the prior probability that you have the disease is higher than the disease's prevalence.

Doctors aren't just administering random tests to random people.
They are administering tests as part of a differential where the test is likely to distinguish between a small number of reasonable alternative hypotheses that could explain your symptoms, generally each with a prior far exceeding 1 in 10000 (I'd estimate values between 1 in 10 and 1 in 3 are more common, but of course it varies according to the specifics of the situation).
The priors are higher than the candidate diseases' prevalence because your symptoms already indicate that you have _something_, even though they don't fully narrow down what it is you have.

This _reason for administering the test_ resolves the Medical Test Paradox Paradox.

<details>
  <summary>Does this change how we think about the original Medical Test Paradox?</summary>

I think it does. Now, when asked "If your test result comes back positive, what's the probability that you have the disease?", I no longer think the appropriate answer is 1%. Instead, the appropriate response is "Why did I take the test? Was I exposed? Do I have symptoms? Or was I participating in an experimental trial?" Only if there was no reason for taking the test is the answer 1% appropriate. If there was a good reason, the probability is likely much higher than 1%.
</details>
</details>
