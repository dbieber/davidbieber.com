+++
title = "Writing with GPT-3"
date = 2020-07-22T00:00:00
tags = ["writing", "machine-learning", "taking-silly-ideas-seriously"]
+++

GPT-3 is a language model developed at Open AI, and I've been having a lot of fun playing with it. In fact, I've written this post in collaboration with GPT-3. See if you can spot which parts are written by me and which parts come from GPT-3.

## Part 1: Brainstorming

The first thing I did when I got access to GPT-3 is use it to brainstorm uses for GPT-3. I gave it these 5 ideas:

1. Explain mathematics more simply (why is X true?)
2. Generate programs from input/output examples
3. Generate questions about a paper I read
4. Create a list of machine translation tips and tricks
5. Create an adventure game

And it came back with 15 more:

6. Create a list of Tor commands to run to defend against an attack
7. Create a cheat sheet for screenwriters
8. Generate advice for a scene
9. Generate XKCD comics
10. Create a crib sheet for an arbitrary Python API
11. Make a list of movies to watch
12. Make a list of scholarly algorithms/heuristics worth reading
13. Make a list of generic questions about Pedagogy
14. Make a list of cognitive exercises
15. Show patterns generated by awesome people
16. Generate small cooking tasks
17. Generate characters for a project
18. Generate configuration options
19. Generate flashcards
20. Organize my computer/files

And then 15 more:

6. Explain things to my parents via messenger
7. Explain things to my children via messenger
8. Explain mathematical algorithms
9. Automated interface design
10. Mechanize a Nagihara Kan Airlines website
11. Clickbait generator
12. Music description (Herbie Hancock is playing "Dolphin Dance" live in London on the 18th March 1968)
13. Tell me not to waste my time looking at x
14. Interesting facts about Wikipedia
15. Explain something to someone while my attention is elsewhere
16. Detect adverts in x
17. Image caption/caption game
18. Speculate about the true utility function of x
19. Auto-generate tests for a program
20. Explain why my code is currently failing tests.

And then 15 more:

6. Generate plots or character/story summaries
7. Generate legal examples
8. Generate words for crosswords
9. Check my grammar
10. Supply filler text for themed writing (horror, sci-fi etc.)
11. Explain why an AI can't read (can it comprehend metaphors?)
12. Provide entertaining answers to obscure questions
13. Get writing ideas and generate word combinations
14. Create background for an NPC I need for a D&D game
15. Help a sick writer generate plots
16. Input pre-generated (from books etc.) phrases and use them for literary analysis
17. Help explain a mathematical proof
18. Develop a game/story/character I need
19. Make short stories I can "overlay" on a fictional Universe I've created (ala Ready Player One)
20. Make a short film/audio drama

What a lovely list of lists of ideas! I wonder how many of these ideas are novel.

Some of these ideas are outside the scope of what GPT-3 can do. For example, generating XKCD comics seems too difficult. Others are duplicates, such as "Explain mathematical algorithms" (duplicate of "Explain mathematics more simply"). And still others don't make sense -- "Mechanize a Nagihara Kan Airlines website"? Overall though, solid set of ideas.


## Part 2: Mathematics

Once I'd gotten GPT-3 to do some brainstorming, I realized I'd need to test its capabilities before trying its suggestions out in earnest.

I taught it how to evaluate simple expressions and take derivatives.

Here's the first prompt I used:

```md
Question: f(x) = x*x. Compute f(3).
f(3) = 3*3
f(3) = 9
Answer: 9

Question: h(x) = x*x - 2x. Compute h(5).
h(5) = 5*5 - 2*5
h(5) = 25 - 10
h(5) = 15
Answer: 15

Question: y(x) = x**3 - 2x. Compute y(3).
y(3) = 3**3 - 2*3
y(3) = 3*3*3 - 6
y(3) = 27 - 6
y(3) = 21
Answer: 21

```

I could then ask it any of the following, and it would correctly show its work.

```md
Question: f(x) = tan(x) + 1. Compute f(0).
Question: f(x) = sqrt(x) + 1. Compute f(16).
```

When I tried to give it
```md
Question: f(x) = x/2 + 2. Compute f(f(16)).
```
it treated it as just `Compute f(16)` rather than `f(f(16))`.

Interestingly this works:

```md
Question: f(x) = x*x. Compute f(3).
f(3) = 3*3
f(3) = 9
Answer: 9

Question: h(x) = x*x - 2x. Compute h(5).
h(5) = 5*5 - 2*5
h(5) = 25 - 10
h(5) = 15
Answer: 15

Question: f(x) = x/2 + 2. Compute f(f(16)).
f(f(16)) = f(16/2 + 2)
f(f(16)) = f(8 + 2)
f(f(16)) = f(10)
f(f(16)) = 10/2 + 2
f(f(16)) = 5 + 2
f(f(16)) = 7
Answer: 7

Question: y(x) = x**3 - 2x. Compute y(3).
y(3) = 3**3 - 2*3
y(3) = 3*3*3 - 6
y(3) = 27 - 6
y(3) = 21
Answer: 21

Question: f(x) = x*3 - 1. Compute f(f(5)).
```

Whereas this does not:

```md
Question: f(x) = x*x. Compute f(3).
f(3) = 3*3
f(3) = 9
Answer: 9

Question: h(x) = x*x - 2x. Compute h(5).
h(5) = 5*5 - 2*5
h(5) = 25 - 10
h(5) = 15
Answer: 15

Question: f(x) = x*3 - 1. Compute f(f(5)).
f(f(5)) = f(5*3 - 1)
f(f(5)) = f(15 - 1)
f(f(5)) = f(14)
f(f(5)) = 14*3 - 1
f(f(5)) = 42 - 1
f(f(5)) = 41
Answer: 41

Question: y(x) = x**3 - 2x. Compute y(3).
y(3) = 3**3 - 2*3
y(3) = 3*3*3 - 6
y(3) = 27 - 6
y(3) = 21
Answer: 21

Question: f(x) = x/2 + 2. Compute f(f(16)).
```

After getting it to evaluate these simple expressions correctly, I also tried having it take derivatives. With an example as priming, and again having it show its work, this worked well. I haven't performed a rigorous evaluation of its mathematical capabilities. For now, I've just begun to develop an intuition for how it works.

## Part 3: Playing Around

After doing math together, I tried many more things with GPT-3. I shared feelings with it, and it expanded on them (correctly too!). I used it to generate lists for brainstorming all manner of thing. The language model wrote love letters from inanimate objects. I tried to teach it to play Codenames, but with only very limited success. And I had it autocomplete previous snippets of mine, and had some fun cowriting with it. While I won't be sharing all of this with you, I do have one thing to share.

This is a love letter written by a frying pan:

I may not seem like much to you right now. I'm coated in grease and I'm starting to rust, but really, I have big plans. I'm going to Italian restaurants. I'll hang out with the finest (and healthiest) ingredients you can imagine. It was good knowing you, but you were never mine to keep. I'm going to cook the kind of meal you'll dream about for the rest of your life. Good luck, sweetheart. You'll need it.

## Overall Principles

Getting an intuition for how GPT-3 behaves has been interesting, and I'll try now to distill that intuition down into a few principles.

1. GPT-3 is continuing your writing, not having a dialog with you.

I've seen on Twitter lots of people asking GPT-3 questions, and sharing its response. Know that GPT-3 continues whatever prompt you give it as if it had written the prompt itself, not as if it is responding to the prompt. This is why you often see prompts like "The following is a conversation between X and Y:".

2. GPT-3 effectively puts your writing in a made up context.

If you give GPT-3 a small prompt, such a single sentence, then there are many contexts in which that prompt could be interpreted. GPT-3 is trained to marginalize over the contexts in which the text could appear. Once you start decoding GPT-3's response though, one implicit context has been selected. It might not be the context that you intended when writing your prompt.

This can happen even if you try to set the context yourself explicitly. For example you might be trying to generate a conversation or a list, and GPT-3 might decide that this conversation or list is taking place inside of a novel.

You can mitigate this context switch by using a longer prompt, or by doing more of the writing yourself.

3. GPT-3 likes lists and repeated structures.

This is the main principle behind using GPT-3 for few shot learning. Prompt GPT-3 with a few examples of performing a task, and it will usually make an effort to perform that task yet again.

4. GPT-3 cannot perform linguistic tricks like unscrambling words

It doesn't seem capable of generating new puns (I haven't tried this yet).
And it doesn't seem capable of unscrambling words (I did try this, and I couldn't even get it to unscramble 4-letter words).

5. GPT-3 benefits from "showing its work"

In my math experiments, having GPT-3 show its work was critical to getting it solving the math questions correctly. It seems that doing a single step of expression evaluation at a time is an easier task than doing it all at once. Providing examples with the steps gave GPT-3 a clearer explanation of the task than just providing input/output examples. GPT-3 also gets additional computational steps in which to solve the problem when it takes the time to show its work.

6. GPT-3 has a great breadth of knowledge and writing styles available to it

It can express love, write flowery prose, give advice, write technical documentation, latex, program, math, take the perspective of a toaster, and more. It's a great tool for brainstorming both explicitly (by having it generate ideas) and through exploration (by using it to help you generate ideas yourself).

Though it has all the facts from the internet at its fingertips (of all the ways to anthropomorphize GPT-3, why choose fingertips?), it is just as capable of generating falsehoods as truths. Do not mistake the text it generates as true or logically correct, even if in many circumstances it does generate correct information. When it transitions from generating truth to generating nonsense it does not give a warning that it has done so (and any truth it does generate is in a sense at least partially accidental).

7. Sometimes GPT-3 makes no sense

There are things that don't make sense that the language model assigns reasonable probabilities to. And there are things that don't make sense, are low probability, but come up anyway either due to chance or because the model doesn't have anything better to say. It doesn't stop generating text just because its out of its depth. Instead, it just plods on forward, saying something as reasonable as it's capable of, regardless of the situation it finds itself in.

8. GPT-3 mimics your style

If you prompt GPT-3 with typos it will continue with typos. If you prompt GPT-3 with florid prose, it will write florid prose. If you prompt GPT-3 with anaphora laden rhetoric, or any other style, it will continue in that style.

## Conclusion

I'll let GPT-3 wrap things up itself:

"And that brings us to the end, some thoughts on whether using GPT-3 was more or less crazy than getting a Ph.D.. I think that using GPT-3 to generate ideas was a higher form of Enlightenment than any Ph.D. I'd do that again in a heartbeat, no shortage of ideas rolling around in GPT-3's natural language processing head."

Uh huh. Whatever, GPT-3. Whatever.