+++
title = "Machine Learning Journal of Hypotheses"
date = 2021-11-05T00:00:00
tags = ["machine-learning", "taking-silly-ideas-seriously"]
icon = "star"
+++

This snippet is about an idea for a new venue for publishing research hypotheses before any experiments have been carried out.
We can think of the idea as a "Hypothesis Journal" or "Hypothesis Arxiv". Similar to how arxiv.org hosts pre-prints for scholarly articles, the Hypothesis Arxiv would be a venue for researchers to submit their research hypotheses for the research community to see and evaluate. As I'm interested in having this venue serve as a place for the community to not only submit, but also discuss and evaluate the hypotheses, "Hypothesis OpenReview" might be an even more fitting title.

To narrow the scope of discussion, let's confine ourselves to thinking about machine learning research for the time being. My hope is that such a venue would allow the machine learning community to more thoughtfully select the set of hypotheses it focuses on from year to year.

I'll aim to cover (1) why this is a good idea, (2) what it might look like, and (3) I'll try to preempt some concerns one might have. We'll also take a quick look at (4) similar ideas that have been tried in the past, and what we can learn from them.

### The "Machine Learning Hypotheses" Journal

The "Hypothesis Journal" idea is for a new venue that accepts scholarly submissions from researchers in the form of hypotheses, rather than complete research papers.
A hypothesis is generally a simpler and shorter artifact than a research paper.
Whereas a research paper includes a hypothesis together with experiments, their results, analysis, and conclusions, a hypothesis paper stops short of performing the proposed experiments.
It still contains the background and motivation, hypothesis, and proposed experiments, but does not perform those experiments, gather any new data, or form any conclusions about the veracity of the hypothesis.

Once hypothesis papers are submitted, they are assigned reviewers.
Reviewers evaluate hypothesis along various dimensions for their scientific merit, allowing those hypothesis that seem most promising (e.g. interesting, plausible and potentially surprising, ethical, and likely impactful) to rise to the top.

In addition to the standard review period, an important piece of the idea is opening up discussion to the machine learning community at large. The difference here is that the official reviewers are selected because they are trusted experts in the same field as the hypothesis paper, whereas the public discussion is open to anyone.

The hope is that through the expert reviews and the community discussions, strong hypotheses can be identified and rewarded, and all hypotheses can see sunlight that allows them both to improve and inspire.

Since hypothesis papers take less effort and less time to produce, a researcher might produce and submit several hypothesis papers to the "Hypothesis Journal" in a single cycle. I am also hopeful that each hypothesis can be assigned a greater number of reviewers than conference papers typically are.
This would allow the variance of the reviewer pool to diminish a little, and for each hypothesis to receive valuable signal from a variety of reviewers as to its merits.

To make the idea concrete, let's call the journal "Machine Learning Hypotheses". And let's further say it has an annual submission deadline, and a short review cycle followed by a conference.

### Motivation

The pace of machine learning research is accelerating. Certain types of machine learning research are becoming increasingly expensive to perform (e.g. training large scale language models), prohibitively so for some researchers. A result of this is that there are far more hypotheses to test than resources available to test them. So, choosing wisely what hypotheses we investigate is increasingly important.

The current publication model incentives publication of complete results.
Researchers come together at conferences to discuss findings. It's at this point that the most significant mixing of ideas occurs.
In a flow diagram, the scientific process looks like roughly like this, with the greatest discussion and mixing of ideas currently taking place at the point marked (♥), while I am proposing increasing our focus on the point marked (¿):

   [Observations (from scientific literature, experiments, etc.)]
<br/>➔ [Hypothesis (¿)]
<br/>➔ [Experiments]
<br/>➔ [Results]
<br/>Path 1: ➔ [Success] ➔ [Write up paper (♥)]
<br/>Path 2: ➔ [Failure (✝)] ➔ [Go to start. Revise Hypothesis]

(♥): It is primarily at (♥), when a hypothesis has been confirmed, that the research community comes together en masse to discuss the findings. This takes place through publications, conferences, and journals.

(✝): I have seen proposed on several occasions that there be more opportunities for publishing negative results, and I support these proposals. That amounts to greater discussion taking place at (✝), e.g. through the introduction of "Negative Result Journals". This is not what I am proposing though; I am proposing increasing our community focus on (¿), when hypotheses are formed but not yet tested.

(¿): My proposal is that we have a forum for publishing and evaluating hypotheses, even before experiments have been run and data has been collected, thereby increasing the amount of discussion of ideas that takes place at the spot marked (¿) in the ongoing cycle of the scientific method.

The main benefit of increasing publication and discussion at the hypothesis stage of the scientific process is the potential to **more selectively and thoughtfully shape the collective portfolio of hypotheses that the research community as a whole pursues**. It does this through a few mechanisms. I would summarize them as (1) **quantity**: increasing the range and number of ideas generated, (2) **quality** and (3) **coordination**: improving the quality and diversity of research pursued through discussion, and (4) **speed**: tightening the feedback loop between when an idea is generated and when downstream ideas based on it are generated.

##### (1) Quantity

It is much easier to submit a hypothesis than to submit a full research paper. Therefore a "hypothesis arxiv" or "hypothesis journal", if adequately popular and prestigious, could substantially increase the number of ideas proposed and discussed widely compared with the number seen in publications today.

Compared with writing up a hypothesis, actually performing experiments, collecting data, performing analysis, and drawing conclusions is a considerable amount of work. Some individual researchers might be able to submit a few times, up to perhaps a full order of magnitude, more high quality hypotheses than complete research projects. These might include ideas the researcher would never have time to pursue fully on their own, but which the community could benefit from greatly.

By attaching credit and prestige to submitting hypothesis, we make it possible to split the role of researcher into two sub-roles. One sub-rule is the idea generator/"hypothesizer", and the other is the "experimentalist"[^1] that evaluates the hypothesis. This would enable some researchers to specialize into one of these two categories (while many researchers could continue operating both roles concurrently). Today, a successful research career requires mastering both of these skill sets. A prestigious "hypothesis journal" could reduce this pressure, perhaps allowing for people to make careers out of just one skill set of the other, more than is possible today.

Importantly, researchers would be able to submit hypotheses about experiments that they may be unable to carry out on their own. Take the case of training large language models as an example. This is a prohibitively expensive task for many research organizations. Even if you cannot train a large language model yourself, you can still learn about them and produce informed hypotheses about them.
So, the best ideas about large language models could come from someone not in a position to run the experiments themselves.
The "hypothesis arxiv" idea would allow these researchers to still play a vital role in the research process.
This idea could significantly expand the number of researchers who can participate in large language model research, even if many of them can only participate at the hypothesis stage[^2].

[^1]: I describe the "hypothesis arxiv" idea using the language of empirical science, but in principle the idea could be applied to entirely theoretical fields as well. In that setting, the idea would be to make space for unproven conjectures to be shared more freely.

[^2]: And if a hypothesis submitted to the hypothesis arxiv by one group is being evaluated by another group, then it would make sense to me to include the first group closely in the evaluation process. In this way, the "hypothesis arxiv" may open up LLM research even more than described in the main text.

##### (2) Quality

By moving the discussion of hypotheses as a community earlier in the cycle of the scientific method, we can be more selective and focused in what hypotheses we dedicate significant resources to.
Ideas that are obviously true or obviously false can be identified by the review process; these ideas need not consume significant effort by the community. The best ideas will be identified as such, and lower quality ideas can improve through the feedback they receive during review and discussion. By getting more viewpoints involved in selecting and evaluating ideas, the best ideas (to a wider range of researchers) will rise to the top and garner more attention.

When a hypothesis finally is confirmed or rejected, since it will already have been discussed by the community, we will also have a _more accurate idea of how surprising the result truly is_. Without this discussion first, we can only use hindsight to estimate how surprising findings are. This is an important idea, which other research communities adopt partially through the concept of pre-registration, but which is somewhat lacking in machine learning research today.


##### (3) Coordination

Putting hypotheses out in public before running experiments also allows for improved coordination. In particular, it can *decrease overlap* in ideas pursued. This can in turn allow more different research directions to be pursued.

Additionally, improved coordination can allow for the formation of larger efforts around the most promising directions. For example, if a researcher proposes a large language model experiment that is promising but which they cannot evaluate themself, a large research org might choose to work directly with that researcher to collaboratively evaluate the hypothesis.


##### (4) Speed

There are two senses in which the hypothesis journal could accelerate the research process. One is by allowing new ideas to be born sooner, and the second is by increasing competition.

1. Tighter iteration cycle

Today an idea doesn't spawn child ideas until it is published, which comes after the experiments have been run and the hypothesis evaluated.
In principle, these child ideas could be born much sooner if the hypothesis were shared sooner, even if the hypothesis has not been demonstrated true yet.
Of course the amount of downstream work that can be done is limited before a result has been confirmed, but it is limited in how limited it is.

2. Competition to evaluate ideas

For the "hypothesis journal" idea to work, there has to be some prestige or other motivations attached to submitting surprising, useful, high quality hypotheses that turn out to be true (or false in an interesting way). Even so, there will still be lots of motivation remaining for the groups that actually carry out the experiments and confirm or reject the hypotheses. Once a strong hypothesis paper has been submitted, the idea is public, and if it is a good idea there could be competition to evaluate the idea as quickly as possible.


##### Other benefits

Those four factors (quantity, quality, coordination, and speed) collectively suggest the hypothesis journal could accelerate the pace of machine learning research, and improve the quality of the collective portfolio of projects of the machine learning community. Other possible benefits of a hypothesis journal include:

* Increasing representation. (e.g. allowing groups to partake in the research process even when running experiments may be prohibitively expensive)
* Lowering the barrier to writing, thinking through thoroughly, sharing, and discussing ideas.
* Decoupling incentives, which could lead to more honest science. Specifically, if people are evaluating the hypotheses of others rather than their own hypotheses, then negative results suddenly become less unappealing. I could see this acting as a force that e.g. reduces p-hacking. Pre-registering ideas also comes with statistical benefits even if you're the same person submitting the idea and doing the experimental science, because it reduces cherry-picking of results and similar effects.
* Decoupling the skill sets of hypothesizer from experimenter has value as well. It allows people to specialize, focusing their skill set and becoming better at their selected role.


#### A Strong Hypothesis

What constitutes a complete hypothesis? What feedback can reviewers / the community provide about a hypothesis?

When a researcher submits a "hypothesis paper", it should be similar to a research paper that stops abruptly after proposing experiments, rather than continuing on to execute the experiments and analyze the results.

It should include the hypothesis, stated precisely in a falsifiable way. It should motivate why it is a reasonable thing to believe, and why the authors expect it to be true, as well as why we do not already know that it is true. It should propose specific experiments, that in principle could be carried out (although perhaps at a budget exceeding that of the authors) to evaluate the hypothesis. It should include in the description of the experiments precisely what would be measured and why.

My description here is perhaps a bit myopic, and the types of hypotheses researchers might submit might not conform to this set of criteria precisely, but I hope this conveys the sense of hypotheses that I have in mind. In a future snippet I can think at greater length about exactly what criteria make for a strong hypothesis.

Here's a short incomplete checklist of ways a reviewer or the public might evaluate a submitted hypothesis.

* Do you believe it is true/false? Elaborate.
* Is it precisely stated?
* Is it feasible to evaluate? Does the proposed evaluation actually evaluate the hypothesis?
* Is it ethical?
* Is it worthwhile to pursue?
  * Cost
  * Impact
  * Downstream research unlocked
* Is it interesting / surprising?

The notion of "likely to be surprising" is interesting, and is an important one for a strong hypothesis.

#### Implementation details

As I mused in the introduction, "Hypothesis OpenReview" may be a more fitting name for the idea than "Hypothesis Arxiv", and a journal or conference named "Machine Learning Hypotheses" is an appealing way to frame the venue for me. Perhaps OpenReview is already well suited for this idea. Instead of developing a new website, one possible implementation is to organize a new _conference_, with submissions collected and discussed on OpenReview, where the gimmick of the conference is as discussed in this snippet: the authors need not perform the experiments they advocate for.

How do we get people to (A) submit hypotheses, (B) review hypotheses, and (C) do both in a scholarly manner? The first step is to circulate this idea so we can discuss and improve upon it. If we can gather support (either for the idea as is, or a future modified version of it), from well respected researchers, their support could be instrumental in getting a "hypothesis journal" off the ground.


#### Similar ideas

I'm aware of three ideas most similar to this one that have been tried in the past.

1. Grants
2. Preregistration
3. Medical Hypotheses

The *grant application process* is similar in many ways to the submission of a hypothesis paper. We can probably learn quite a bit from this process to inform how we implement the hypothesis journal idea. The key difference between our idea and a grant application is that there is not financing attached to submission of a hypothesis in our idea, and the person submitting a hypothesis need not be the same person who eventually evaluates it.

Certain fields have a practice of pre-registration. In this practice, researchers publicly commit to a research plan before beginning the research. Wikipedia suggests preregistration can reduce p-hacking, publication bias, data dredging, inappropriate post hoc analysis, and HARKing. A hypothesis journal can have many similar benefits as preregistration. A key difference between submitting a hypothesis and pre-registering a research plan is that submitting a hypothesis does not commit you to performing the research, and in fact it may be appropriate for someone else (or no one at all) to perform the hypothesis evaluation, rather than its author.

Finally there is one journal _Medical Hypotheses_ that has a similar motivation (albeit less similar than the journal's name suggests) to our hypothesis journal idea. _Medical Hypotheses_ was designed to allow discussion of unconventional ideas, which is a different goal than we are pursuing. Like with our idea, the experiments to validate the ideas need not be run yet. This journal published controversial papers on AIDS denialism, and for most of its existence largely forwent peer review.
We can probably learn quite a bit from the history of _Medical Hypotheses_. One lesson is that peer review and the publication of hypotheses are orthogonal; I suggest we keep peer review, while still encouraging the submission of hypotheses before they have been evaluated.


#### Concerns

In my brainstorming, I anticipate a handful of potential concerns about the idea.

* Flag-planting
* Scooping
* Prestige / Motivation for participation
* Collapsing of the idea space (need divergence and convergence; don't want to be left with an overabundance of convergence and insufficient divergence)
* Ideas are a dime a dozen

Personally, I am not so concerned about *flag-planting*. The primary purpose of the idea is to share hypotheses and inspire others to evaluate or build off of them. Flag-planting is a problem if it involves people claiming overly broad ideas prematurely so that they get future credit once the idea is more carefully analyzed and the specific instantiation of the idea that is most important comes to light.
Credit is a finicky thing, but from my perspective it is rare in modern science that full credit is attributed to a single individual or single group; the story is always more complicated. If someone proposes an overly broad hypothesis, effectively flag-planting, then perhaps they will in turn receive a portion of the credit for the specific important idea that develops from it. I do not find this objectionable. I would be curious to discuss this with you if you find flag-planting a larger concern than I am making it out to be with this idea.

A fear of *scooping* could certainly prevent people from submitting ideas to the "Machine Learning Hypothesis" journal. However, I expect that most researchers have a long line of hypotheses that they will never have the time to evaluate. So, my hope is that researchers who fear scooping could choose to keep the hypotheses they are actively working on a secret, while still opening up and sharing the many others that they possess.
For many researchers, even publishing the hypotheses that they are actively working on will be worthwhile. This allows them to get (partial) credit for the idea earlier (in effect preventing a form of scooping) than if they had to finish the research paper before submitting the idea, and it allows for earlier feedback on their research which usually leads to higher quality research overall.

Next comes the issue of *motivating* people to submit to the conference. I think that we could actually make this conference the most interesting and most fun of the machine learning conferences. Discussing half-baked ideas with researchers is always enjoyable, and I am optimistic a significant fraction of the ML research community could enjoy both submitting to this journal, and reviewing for it, because doing both is a great exercise in research creativity. Prestige and funding are other motivators for researchers; I do not think a hypothesis journal could ever be as prestigious as typical top ML conferences, but I do think that with the backing of strong players and institutions in the research community, sufficient prestige could be attached to strong submissions to the conference/journal.

The next concern is about *collapsing of the idea space*. In order for a group to come up with the best possible ideas, there needs to be space for the group's thinking to diverge, as well as space for discussion leading to some amount of convergence on good ideas. The hypothesis journal idea increases the amount of convergence. Some might argue we actually need more divergence in our thinking. I would be interested to discuss this with you if you have this concern.

Finally, a possible concern is that hypotheses without experiments are not on their own valuable, e.g. that "ideas are a dime a dozen". To address this concern, I think we merely need to raise the bar about what constitutes a good hypothesis. We're not looking for just any old idea, but rather ones that will advance the science of machine learning, backed up by the evidence the machine learning community has collected, and likely to be impactful on future science. Coming up with a good hypothesis is not easy, but a popular hypothesis journal could be an effective tool for improving our collective ability to do so.

If you share these concerns of have additional ones not discussed here, please get in touch. I'd love to discuss.
