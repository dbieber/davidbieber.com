+++
title = "Brains Don't Do Solomonoff Induction"
date = 2021-01-06T00:00:00
uid = "IaqebZa62"
tags = ["thought-experiments"]
keywords = ["information"]
+++

[Dan Abolafia](http://zhat.io/) asked me some thought provoking questions about Solomonoff Induction and intelligence. This snippet comes from my answers.

> Question: Do you think a person has a hypothesis space and prior that are fixed at the moment of birth and never change over the course of the person's life?

tl;dr Nope.

There are different levels at which you can define hypothesis space. Consider two statements.

> Statement [1]: People learn and change their prior over hypotheses based on their observations and experiences over time.

In statement [1] (which I hope is unobjectionably true), "hypotheses" refers to hypotheses that will be formed during a person's life.

A person's belief about their hypotheses can change in response to new information. This can be done in a Bayesian way, using as a prior at any particular moment their beliefs from before gaining that new information. When they gain new information, they apply Bayesian inference to compute the posterior. The posterior becomes the new prior for the next time new information is obtained.

You can also "refactor" statement [1] to instead read:

> Statement [2]: The 'computation that a person embodies' is fixed at birth."

[1] and [2] are completely consistent with one another.

(Let me know if the term 'computation that a person embodies' needs clarifying.)

From the perspective of [2], a person has a single prior over "hypotheses".

(Or more precisely: a person has a single "hypothesis", which came from a single prior. But the person didn't 'have' that prior; instead, the process by which they were created did.)

Here a "hypothesis" is a much larger thing than in [1]. It's the complete manner in which the person will determine how to respond to inputs over the course of their life. (That is, it's the 'computation that the person embodies'.)

It's an interesting question to ask whether these hypotheses come from something that approximates Solomonoff induction.

Note that this wouldn't be the "brain approximating Solomonoff induction" original question -- rather, it would be more like "evolution approximating Solomonoff induction".

[Aside: And to answer this question: I don't think single reward minimization is the most natural way to model what these complex physical processes are doing; there are lots of competing forces at play. So even though you could in principle distill them to a single reward function, I don't think that's the most useful way of modeling things of this complexity and scale. Update: now that I have a better understanding of Solomonoff induction, I see how this doesn't answer the question.]

> If the answer to the main question is No, there needs to be an extra-Bayesian method for choosing priors and hypothesis spaces.

I agree with this.

Let's return to perspective [1]. At any given time, a person might have some beliefs about the world. Then they acquire new information. They update their beliefs. This in principle can be done in a Bayesian way all throughout ones life.

In practice, there need to be other processes at work, because people develop new concepts, choose to think about some things more than others, forget stuff, etc.

But with infinite memory and infinitely fast compute, an agent could in principle start with all possible concepts, and just keep doing Bayesian updates throughout their life, and I think such an agent would do quite well for themselves.

Note: for a hypothetical agent like this, the answer to the original question would be Yes. But agents like this don't exist.

> Agree or disagree: The brain samples hypotheses from a universal unchanging prior.

This I disagree with. I hope perspective [1] clarifies why.

Any action that the brain takes, such as sampling a hypothesis, is happening during an individual's life. Of course it's going to take into account all the experiences of the individual.

You could of course mean "hypothesis" in the sense of [2], where the complete life experiences of the individual are inputs to the hypothesis. But then why wait until there's a brain at all to sample the hypothesis? Now we're talking about a hypothesis (the 'computation that the person embodies') that has been in existence at least since the person's birth.

> Do you think [1] and [2] are equivalent?

I think they are two ways of describing the same situation. So, in that sense, yes.

I could see why people might disagree with this though. People can make good arguments that you're not just a fixed embodied computation. I think these arguments are wrong, but people can still make them. These hypothetical people would regard [1] as correct and [2] as incorrect, whereas I think both [1] and [2] are correct.

> Bayesian inference doesn't provide a way to create or destroy hypotheses. It merely provides a way for updating one's beliefs about existing hypotheses. How do you reconcile this with [1] and [2]?

This is right. Hypotheses can't be "formed" from Bayesian inference. As I was describing perspective [1], I was envisioning hypotheses being formed in some (likely extra-Bayesian, but it wasn't important) way and merely being updated via Bayesian inference.

[Aside: How are these hypotheses formed though?

Well, if you already have a prior for the state of the universe, then you might (1) make a determination about what variables are relevant to the situation, and (2) marginalize out all other variables. No need to do this though if memory and compute aren't limited.]

Earlier I wrote:

> Let's return to perspective [1]. At any given time, a person might have some beliefs about the world. Then they acquire new information. They update their beliefs. This in principle can be done in a Bayesian way all throughout ones life.

How does this work, you ask?

It relies on the agent starting with a prior over all possible hypotheses. This avoids the issue of needing to create hypotheses along the way, which Bayesian inference doesn't provide a mechanism for.

I tried to describe this by the following text:

> With infinite memory and infinitely fast compute, an agent could in principle start with all possible concepts, and just keep doing Bayesian updates throughout their life, and I think such an agent would do quite well for themselves.

If I understand correctly, this __is__ (more or less) Solomonoff induction. (I didn't realize this at the start of the conversation.)

We've started with a universal prior and applied bayesian inference to update it as we made observations.

Of course, this isn't what people do. So, my answer to the overall initial question is just a simple "Nope."

Cheers!
