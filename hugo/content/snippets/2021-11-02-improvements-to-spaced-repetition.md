+++
title = "Potential Improvements to Spaced Repetition"
date = 2021-11-02T01:00:00
tags = ["spaced-repetition"]
+++

Spaced repetition is not super widespread. It's popular among med school students and language learners, but frequently people find the benefits outweighed by the costs, the friction too high, and they stop.

I believe the following are the most pressing issues to solve for spaced repetition to allow for wider adoption:

1. Card creation: Zero friction card creation
2. Card creation: Good cards by default
3. Card maintenance: Eject bad cards quickly
4. Schedule flexibility: Allow people to study more
5. Schedule flexibility: Allow people to study less
6. Review friction: Bring the reviews to the users

If we solve these six issues, I think that could open up spaced repetition to a much wider audience. In this snippet I'll elaborate briefly on all six ideas. I then also want to share one additional idea, which I think is the most important issue to solve for improving spaced repetition for existing users:

7. SRS that understands card connections

Let's dive right in.

#### 1. Card creation: Zero friction card creation

We need to make it so easy to create new flashcards that it becomes as common and quick as making a Google search.

People tend to use spaced repetition systems in one of two ways. They either create cards themselves, one by one, or they import existing decks of flash cards made by someone else. My hunch is that the latter use case is currently more common, because for most people creating a deck of cards themself is too much friction.

Deck reuse can be a good thing; if there is a high quality deck for precisely what you want to learn, it can save you a lot of time just using that deck rather than making a new one. I think we need to change this, though. We need to reduce the friction to creating new cards substantially. This is because so much of what people learn is specific to their own experiences -- the articles they read, the vocabulary that interests them, the specific things they find important to remember.

Machine learning and automation will each play critical roles here. Here are some ideas:

* Create cards just by highlighting the important fact you want to remember. [I do this today using Browserflow](/snippets/2021-07-29-note-taking-flow/). If I highlight a phrase and press "c", a flashcard is created with the sentence containing the highlight, with the highlighted part masked out.
* Machine learning can be used to improve the quality of the generated cards, for example by ensuring the card has all the necessary context from the website to make sense on its own.
* Create cards just by browsing the web. Using machine learning, we can generate flashcards from the websites you visit and the search queries you make. I believe we can design a user interface that requires minimal effort from the user and still generates high quality cards that the user cares about and wants to study.

#### 2. Card creation: Good cards by default

When people create flashcards for themselves, they often create bad cards. A good card is a card that is small, meaningful, and connected. It's quick to recall or quick to fail, but either way doesn't bog down the person studying. When people have cards that are too big, they get bogged down, review sessions become a chore, and people drop the habit of spaced repetition.

One way to ensure good cards by default is to build good properties directly into the low friction card generators. Fill-in-the-blank cards generated by the highlighting method mentioned above are usually good by default. Image occlusion cards that blank out a small piece of text make good cards, and a tool can steer people toward making these good kinds of cards.

A common failure mode is to make open ended cards or cards with long answers. My suspicion is that these cards lower the effectiveness of spaced repetition and lead to people dropping the habit.

It's also important that users know what makes a good card. For this, they can read Andy Matuschak's [How to Write Good Prompts](https://andymatuschak.org/prompts/). Education isn't the full story though. We need our tools to be proactive in guiding people to make good cards and recognizing when they have or have not done so.

#### 3. Card maintenance: Eject bad cards quickly

A common habit of experienced spaced repetition users is to remove cards that take too long from their deck. The most popular spaced repetition tools allow users to do this, but they should go further. They should proactively encourage users to eject bad cards.

In fact, I think these system should go even further than that. They should eject detected bad cards by default, giving users an opportunity to preserve these cards only if they explicitly choose to do so.

How can a spaced repetition system detect bad cards? The main way is by looking at the time spent reviewing it. Other clues come from the length of the answer, and other properties of the answer. Getting this exactly right is a challenging problem, but I'm confident that we have the tool set (e.g. natural language processing, Quizlet user data) to make significant progress on this. Even a rough heuristic approach to detecting bad cards, coupled with active encouragement for people to eject bad cards, I think would go a long way.

#### 4. Schedule flexibility: Allow people to study more

This and the next item go hand in hand; spaced repetition scheduling algorithms need to admit significantly greater flexibility than they do today. There isn't a single best time to review some item. There is usually a wide and fuzzy range of good times to review something. And extra review, while it might mess with the scheduling, is almost always a good thing.

If someone is motivated to study extra, spaced repetition systems should encourage it. The scheduling algorithm should adapt.

This is especially important because people's levels of motivations change from day to day. And most people can't do review sessions everyday anyway (see next item, studying less). We should build tools that work for people, not ones that constrain people. In the context of spaced repetition, this means we want to amplify people's motivations.

If someone is really into a particular topic on a particular day, their spaced repetition system should help them study that topic to their heart's content. In today's spaced repetition systems that might just mean studying the cards related to that topic over and over. In tomorrow's spaced repetition system, this might be giving them new related content to learn (but, while fun and futuristic, that's a less pressing enhancement to make than the six I've listed here).

#### 5. Schedule flexibility: Allow people to study less

As mentioned, people's motivations and availability to study fluctuates. Spaced repetition systems should never make their users feel bad about not studying. This demands both UI changes and algorithmic changes.

First, missing a single day of studying should not feel like a giant impenetrable wall of a backlog has been erected. The reviews for most of the cards you missed can be smoothed out over several days or weeks anyway, with minimal degradation to your memory quality. The UI should not make you feel like you've built up a full day's backlog when you miss a single day of review.

And this shouldn't just be a cosmetic change either; missing review sessions should be a normal thing. Week-long or month-long (or longer!) vacations should be a normal scenario. Obviously, the more time you spend studying the more you can learn and the better you can remember things, but daily studying is not a strict requirement for getting the benefits of spaced repetition. Those benefits scale gracefully up or down with the amount of time you're willing to put in, and the software that implements spaced repetition should expose this smooth scaling property.

Spaced repetition systems should handle people taking vacations gracefully. One way to achieve this is by using ranges rather than specific dates when scheduling card reviews. The acceptable range of times for studying a card should grow considerably as you become more familiar with that card.

If a user does choose to study less that is needed to learn all the material they want to learn, then another possible response is to thin out the material. With the user's input, remove some material such that the amount of material being studied is in line with the amount of study time being put in. This relates directly to idea 7., which I believe can increase the study material to study time ratio significantly for existing spaced repetition users.

#### 6. Review friction: Bring the reviews to the users

The final significant way we can reduce the friction to using spaced repetition systems is to move the review system to the person's primary inbox. That might be their email, or their text messages, or somwehere else -- wherever it is they maintain inbox zero.

This is the same philosophy I use with Bieber Bot -- if Bieber Bot sent me messages to a system I never checked, or one with hundreds of backlogged messages, it wouldn't be useful to me. Instead, he sends messages to FB Messenger where I already read every message. So I don't miss messages from Bieber Bot and his messages have continued to be useful for years.

When people have to switch apps to e.g. Anki, it is easier for them to fall out of the habit of doing spaced repetition. If instead, spaced repetition were built directly into an app they were already using constantly and already responding to all notifications for, it would be easy to develop into a habit.

For me, this place is Roam Research. I take notes in Roam throughout the day, and so it's natural for me to do a review session in Roam. No extra app needed.

For most people, I think baking spaced repetition directly into an email client probably makes the most sense. Who knows though? Maybe TikTok spaced repetition is even better :).

---

Together these six issues can move the needle significantly in reducing friction to using spaced repetition. I expect just solving these six could for many people bring spaced repetition across the chasm from "not practical" to "practical".

There are still further major improvements that can be made to spaced repetition beyond these though. Here is the one I think is most important, which could potentially save a significant amount of time or increase people's capacity to review material substantially:

#### 7. SRS that understands card connections

We need a smarter scheduling algorithm that understands the connections between cards. If you review many related cards over many years, those cards start to become related in your head. Reviewing one will also jog your memory about others. However, today's spaced repetition systems schedule each card independently. Getting one card right should push back the schedule not only for that card, but also for related cards.

Consider a flashcard about conjugating a verb. This card tests two things: (1) do you know the vocab, and (2) do you know how to do the conjugation. Other cards might test the same vocab in a different way, and still other cards might test the same conjugation rule but on a different verb. Getting the card right is (partial) evidence that you will also get other cards testing the same underlying skills correct. We need a spaced repetition scheduling algorithm that can take advantage of these connections.

Another example is learning 2-digit addition. When you're first learning the skill, you might have hundreds of distinct cards with 2-digit addition questions. Years later, it might be good to occasionally review 2-digit addition to make sure you've still got the skill, but you only need to do a small number of cards to convince yourself and the system that you've still mastered the skill. The other cards can get pushed back each time you demonstrate their review isn't going to be helpful to you since you've retained mastery of the skill.

With a scheduling algorithm that understands these connections between cards, I believe that overall reviews can be made less frequent than today's algorithms allow for. Over the long term, the total review time for vocabulary and conjugation cards might be reduced by a substantial factor. The total review time for mathematical skill cards might be reduced even more. This can free up time for spaced repetition users to either study for less time, or to study more material. This would be a significant win for the technique.