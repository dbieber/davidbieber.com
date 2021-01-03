+++
title = "Spaced Repetition in Roam Research"
date = 2021-01-02T00:00:00
uid = "9sebyGS1e"
math = true
+++

There are many ways to do spaced repetition in Roam Research. This post describes mine. I was inspired to start this two months ago by reading [Nicky Case's comic on spaced repetition](https://ncase.me/remember/), and I highly recommend the read.

"Spaced repetition" just means studying flashcards, studying the cards you know best less often, and study the cards you struggle with more often. It's a powerful technique for learning and remembering material, whether you're a student or a lifelong learner.

The system I use is based on a classic system called the "Leitner Box" method. I'll first describe how to use the "Leitner Box" approach in Roam, and then I'll describe the adjustments I made to improve it.

## What's a "Leitner Box"?

In the "Leitner Box" system of spaced repetition, there are seven boxes numbered Box 1 through Box 7. When you create a flashcard, you place it into Box 1. Every day, you use a schedule to determine which boxes of cards to review. The cards in box 1 get reviewed most often, and the cards in box 7 get reviewed least often. When you review a card, you move it up a box (e.g. from box 1 to 2 or from box 4 to 5) if you get the card right. But if you get a card wrong, you move the card back to box 1.

The default Leitner Box schedule looks like this:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fplayground%2FpW7FsufOIr.png?alt=media&token=3cbd07b1-11e5-4389-896d-9a181f6529fc)

How do you read this schedule?

The colored circles represent the different Leitner Boxes. The red circles represent Box 1, the orange circles represent Box 2, the yellow circles represent Box 3, all the way up to the final pink circle that represents Box 7.

The numbers along the bottom are "session numbers". For your first review session, you look at the circles above "01" (Boxes 2 and 1). For your second review session, you look at the circles above "02" (Boxes 3 and 1). Always review boxes for a given day in order from highest to lowest. After completing session "64", the schedule wraps around and your next session is session "01" again.

To recap, (1) you put new flashcards into Box 1. (2) When you get a card correct, you move it up a box. (3) When you get a card incorrect, you move it all the way back to Box 1. (4) You use the schedule made of colored dots to decide which boxes to review each day, answering questions in higher boxes first.

## Setting up Leitner Boxes in Roam

This system is all well and good. How do we put it into practice? Here I'll quickly describe (1) getting set up, (2) creating new flashcards, and (3) how to do a review session.

**Setting up:** You can use my template; simply copy and paste the ["raw" text at the bottom of the page here](https://pastebin.com/GPfhcUug) into Roam Research, e.g. onto a new page named "Spaced Repetition". For this to work you need to copy from the region that says **"RAW paste data"**. You can [get the enhanced template (recommended; see below) here](https://pastebin.com/zvjFKZAb). Again, be sure to copy from the region that says "RAW paste data".

The default template creates a page for each of the seven Leitner boxes. It also puts the default schedule on the page, and gives you a place to keep track of what session number you're up to. It will also add two questions to your Leitner Box 1 (one about avocados, and one about Cloze deletions), and includes some basic instructions for how to do spaced repetition in Roam.

**Creating New Flashcards:** You can create a new card anywhere in your Roam graph simply by tagging a note with "#[[Leitner Box 1]]". Here are two ways to create cards in Roam:

1. Put the question on one bullet, and put the answer in the child bullets. Then tag the bullet with the question with "#[[Leitner Box 1]]" to add it to your spaced repetition system.

2. You can use the syntax {{=: question | answer}} in Roam to create text that remains hidden until clicked. The text "answer" wont appear until you click on the text "question." Again, tag the line with "#[[Leitner Box 1]]" to add it to your spaced repetition system.

I recommend you [read Andy Matuschak's notes on "How to write good prompts"](https://andymatuschak.org/prompts/) for tips on how to create good flashcards. [Nicky Case's comic: "How to Remember Anything Forever-ish"](https://ncase.me/remember/) also has good suggestions for how to create good questions for spaced repetition.

**How to do a Review Session:** Visit your "Spaced Repetition" page to figure out what session number to do. Increment the session number, and use the schedule to determine which Leitner boxes you'll be looking at in this session. Remember, do the Leitner boxes in decreasing order of their number.

For each Leitner box, visit its page in Roam. All your questions will appear in the Linked References section of the page.

Go through the questions one by one. If you get the answer correct, increment the box number by 1. If you get the answer incorrect or struggle with it, set the tag back to "#[[Leitner Box 1]]".

Don't worry about sending things back to box 1; you'll see those questions very often and soon they'll be back in the higher numbered boxes again!

## Enhancements Beyond the Default System

I've made several changes to the default Leitner Box system to improve it to my taste. You're welcome to use them!

**Leitner Boxes 0 and $\infty$:** I use an extra box, "Leitner Box 0" for flashcards that I'm not ready to put into my rotation yet. I try to only add at most 10 cards a day to keep the total review workload low. If I have more cards than this, I keep them in Box 0 until I'm ready to start studying them, at which point I move them to Box 1.

Leitner Box $\infty$ is for cards that have graduated from Box 7. In theory, I will remember these cards for the rest of my life.

**Extra box 5s, 6s, and 7s:** I have decided to create two Box 5s (named 5A and 5B), four Box 6s (6A, 6B, 6C, and 6D), and eight Box 7s (7A through 7H). This prevents any individual review session from accumulating too many cards.

I ran a simulation and under the default system, adding 10 new cards a day and getting 95% of cards correct, some review sessions will require reviewing over 700 cards! Under the enhanced system, the longest review session will only ever be 140 cards (and most review sessions are much shorter than that).

Here's the modified schedule that allows me to use these extra boxes:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fplayground%2F_dSM-MMp85.png?alt=media&token=b3682748-8ea4-4444-97df-0c4592beb1ff)

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fplayground%2FhFRPfzGpwy.png?alt=media&token=20b7f689-4117-4901-a806-846b0d099d7d)

To use this enhanced schedule, first use the review session number to figure out which column of colored circles to look at. As before, a red circle indicates Leitner Box 1, a yellow circle indicates Leitner Box 2, etc. If the circle has a letter inside it, that means to review that particular variant of the box. E.g. a blue circle with a "B" inside means to review Leitner box 5B. The arrow to the right of a box indicates which box you should move the card to if you get it correct. E.g. in review session "51" you should review box 5B and move correct cards to box 6D; you should then review boxes 2 and 1 as usual.

**Embed the box list:** I use Roam Research's "embed block" feature to embed a list of all Leitner Boxes onto all my Leitner Box pages. This makes it easy to quickly navigate from any box to any other box. I couldn't think of a good way to include this in the template, so you'll have to add this yourself if you want to include it.

**Enhanced Template**

You can [access the enhanced version of the template here](https://pastebin.com/zvjFKZAb). It includes more Leitner boxes and the more complicated schedule. To use it, simply paste it into a new page in Roam Research, e.g. "Spaced Repetition".

## Spaced Repetition Alternatives

There are multiple ways of doing spaced repetition in Roam, of which this is just one. Note that most spaced repetition systems in Roam Research use the "delta" feature. However, we are not using this feature. CortexFutura provides [a way of using the delta feature for spaced repetition here](https://www.cortexfutura.com/preliminary-spaced-repetition-roam/). Roam Toolkit provides another system for doing spaced repetition in Roam, which you can [view on YouTube here](https://www.youtube.com/watch?v=08o8q_bOedw).

One of the most popular spaced repetition systems is called [Anki](https://apps.ankiweb.net/). It's great for language learning. I'd be remiss not to mention it. The reason I prefer doing spaced repetition directly in Roam is that the friction to creating cards is much lower in Roam for me, since I'm taking notes and writing my ideas in there already.

Additionally RemNote, a competitor note-taking tool to Roam, also offers a highly configurable spaced repetition system out-of-the-box.

For more, consider joining the conversation in the [Roam Research Slack](https://roamresearch.slack.com/) "spaced-repetition" channel.

## Two advantages of this system over traditional spaced repetition systems

1. **Lower friction:** Creating cards directly in your note-taking app is substantially easier than needing to task switch to create cards. This lower mental overhead makes it easier to keep using spaced repetition for an extended period of time. I started using it two months ago myself, so finger's crossed it indeed is something I keep up for much longer! 🤞 

2. **Robustness to vacations:** In traditional spaced repetition systems, taking a break for a day, week, or month, can be ruinous to your spaced repetition rhythm. After coming back from the break, you find you have too many cards to review all at once, which can be a real motivation drain. Instead of organizing cards by __date__, my system organizes them by __review session number.__ This means that if you skip a day or a week, your reviews simply get pushed back. The review session number won't go up while you're away. You can even split a review session over multiple days if you like. No trouble! You'll never be left with a review session that's too big to handle.

## Additional Resources

[Nicky Case's comic: "How to Remember Anything Forever-ish"](https://ncase.me/remember/) is what inspired me to start using spaced repetition in my life.

[Andy Matuschak's "Orbit" system](https://withorbit.com/) enables writers to incorporate spaced repetition directly into their writing, to help their readers remember what they learned forever. You can read [Quantum Country](https://quantum.country/) to learn quantum computing and give it a try. You could also [read his tips for "How to write good prompts"](https://andymatuschak.org/prompts/), which is also written with Orbit.

You can [get Anki here](https://apps.ankiweb.net/) or [try RemNote here](https://www.remnote.io/). I also have a dozen+ other [snippets about Roam here](https://davidbieber.com/snippets/) ([what's a “snippet”?](https://davidbieber.com/snippets/2019-12-25-introducing-snippets/)).

## Get in touch

I love a good discussion about spaced repetition. You can email me at [david810+spaced-repetition@gmail.com](mailto:david810+spaced-repetition@gmail.com), find me on Twitter ([@Bieber](https://twitter.com/@Bieber)), or join the [Roam slack](https://roamresearch.slack.com/) to keep the conversation going.
