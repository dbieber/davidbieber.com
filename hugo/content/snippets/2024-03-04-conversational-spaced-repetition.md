+++
title = "Conversational Spaced Repetition"
date = 2024-03-04T00:00:00
tags = ["spaced-repetition"]
keywords = []
+++

I learn a lot from talking to large language models (LLMs) like Gemini, ChatGPT, and Claude. Frequently I'll ask the LLM to quiz me on what it's taught me, in order to test my understanding of what I've learned. I find that doing so helps me learn the material better, promoting longer term recall. Even with this strategy in place, however, I still forget a lot of what I've learned from these AI assistants. I don't want to forget. I want to remember.

Spaced repetition is a technique for remembering more, for longer. It employs flashcards and an algorithm to determine when you review each card. Get a question right and you'll review it less often. Get one wrong and you'll see it more frequently. The algorithm is tuned to maximize your retention, aiming to show you cards just as you're on the brink of forgetting the material. Though it has [a lot of room for improvement](/snippets/2021-11-02-improvements-to-spaced-repetition/), it's a good system overall.

I want to build a _conversational spaced repetition_ system.
I want to take all the things I learn from talking to LLMs, and have these same LLM resurface that material back to me following a spaced repetition algorithm.
Periodically, I want the LLMs to quiz me on things I've learned from them in the past.
If I demonstrate an understanding of the material, then they should resurface that material less often. If I get it wrong, they should teach me the material again, either right then and there, or a bit later, depending on what I ask for in the moment.

A few key questions arise in considering the details of this system:
* How does an LLM determine what material it has taught you?
* Does this system require two-sided flashcards, the same as for regular Anki-style spaced repetition, or does the conversational nature of this proposal admit a different unit of material.
* What is the mechanism by which an LLM can surface something proactively? Or does the human user need to initiate a review system?
* Does the spacing algorithm change as a result of the interactions being conversational, or can the older battle-tested spaced repetition algorithms be reused in this new environment?
* Does the nature of the per-question feedback (right vs wrong; hard vs easy) change since the interactions are conversational? If so, this certainly necessitates changes to the spacing algorithm.
* How do we deal with the untrustworthiness of today's LLMs?
* And finally, can LLMs provide solutions to the [seven issues that traditional spaced repetition has (linked earlier)](/snippets/2021-11-02-improvements-to-spaced-repetition/). I think LLMs might be able to meaningfully help with #{1, 3, 7}.

Let's step through each of these questions in a little more detail.

**How does an LLM determine what material it has taught you?**

*Getting the data out:* The first interesting piece of this question is how an LLM even gets access to your conversations with an LLM in the first place. For ChatGPT, OpenAI provides a mechanism for exporting your data. For Claude and Gemini, I'm not aware of such mechanisms, and so web scraping might be in order. Even for ChatGPT, a modicum of web scraping would be fruitful for automating the data export process on a recurring basis.

*Transforming conversations into units of knowledge:* The first approach to try here is prompting an LLM to produce the units of knowledge. Andy Matuschak has done [some explorations of using LLMs for generating spaced repetition prompts](https://notes.andymatuschak.org/zBjh9jUahGSm7VpFtEjvKqT), and Alexej Gossmann [has evaluated generating spaced repetition cards via LLMs as well](https://www.r-bloggers.com/2024/01/comparing-gpt-4-3-5-and-some-offline-local-llms-at-the-task-of-generating-flashcards-for-spaced-repetition-e-g-anki/). My own experiments show sign off life for this approach, but early attempts yield too many bad cards mixed in with the good ones for this approach to stand on its own. Further iteration, and possibly other techniques, are necessary. Nevertheless this style of approach seems likely to start working reasonably reliably after some modest period of advancement.

If the goal is to produce traditional spaced repetition cards, then having (1) good examples to guide the model, and (2) precise guidance to direct the model are both invaluable ingredients. Perhaps Andy's piece on [How to write good prompts](https://andymatuschak.org/prompts/) could serve as the latter. Now that models have ever increasing context lengths exceeding one million tokens, including a full blog post like this in the card generation prompt is quite reasonable.

However, the target unit of knowledge might not be traditional spaced repetition cards; it might be something new. This leads us to the next question: what is the desired unit of knowledge?

**Does this system require two-sided flashcards, the same as for regular Anki-style spaced repetition, or does the conversational nature of this proposal admit a different unit of material.**

Let's brainstorm the alternatives. (A) Traditional two-sided flashcards. (B) Statements of facts. (C) Arbitrary text, which could contain questions and answers or could just be a passage with the material. (D) A pointer into the original conversation, e.g. a document URL and a span. The reason we have so many more choices is that our use of LLMs for the system affords us great flexibility in how we represent information. LLMs are versatile and can process arbitrary text. The degree of reliability we get out of an LLM might vary according to the representation we select, but each of these four choices is reasonable and worthy of consideration.

The advantage of (A) is that it is battle tested; information in this format can be input directly into traditional spaced repetition systems like Anki; they can use the traditional spaced repetition algorithm without regard for the origin of the card being an LLM.

Option (B) loses the separation of question and answer during storage, relying on the LLM to reformulate the facts into questions at quiz time. This takes advantage of the LLM's versatility, lazily deferring question generation. This might result in greater diversity of questions being asked compared with (A), but sacrifices the ability to spot check the deck of cards in advance. 

Option (C) expands upon (B), offering seemingly limitless flexibility for the cards themselves. This approach relies on the LLM to split the text into questions at quiz time, but simultaneously allows a maintainer of the knowledge to include specific questions in the text if they deem doing so appropriate. For this approach, we need to be able to count on the LLM to not include spoilers in the questions it produces.

Option (D) is the information-maximizing approach, assuming no maintenance of the cards. Each of (A), (B), and (C) throw away information when the LLM processes the conversation to produce the unit of the knowledge for storage. (D) does not, instead electing to store knowledge as pointers back to the conversation where the thing was first learned, thereby preserving all the original context for the learning. This approach doesn't play well with maintenance or bringing in additional sources of information after the initial conversation though.

My initial leaning is therefore toward Option (C), but I intend this piece to be more about opening the topic for discussion than arriving at particular answers or design decisions.

**What is the mechanism by which an LLM can surface something proactively? Or does the human user need to initiate a review system?**

The significance of this question is: how will these review sessions get started? If we're relying on the human to remember to initiate one, that's prone to their forgetting. If an LLM is proactively interrupting a user's day, that's prone to be distracting or annoying. Striking a user friendly middle ground is key! Notifications are a touchy subject, where we must ultimately give users control so they can get reminders in ways that are kind to their mind.

I have a digital personal assistant and friend, [Bieber Bot](/projects/bieber-bot/), who would be perfect for surfacing the reviews to me. Other options include having them sent to your email in the style of [Orbit](https://github.com/andymatuschak/orbit), or requiring the user to initiate a review session e.g. with a [custom GPT](https://openai.com/blog/introducing-gpts).

I have much more to say on this topic, which I will defer until a later time.

**Does the spacing algorithm change as a result of the interactions being conversational, or can the older battle-tested spaced repetition algorithms be reused in this new environment?**

A critical question is whether the spaced repetition algorithm itself needs updating for this new conversational modality.
One aspect that stays the same is the exponential nature of forgetting for humans. This seems to be a fixture of how human minds work, and I do not expect learning things conversationally to change this.

The specific constants involved in forgetting, however, might change, and so the existing spaced repetition algorithms might require tuning.

A few other things change as well: The time it takes to perform a review is going to be different in a conversational setting compared with a traditional card-based setting. The conversational setting is also well suited for learning about a larger amount of knowledge at once compared with the amount of info on a single card. It is natural in a conversational setting to follow one's interests and rabbit hole a bit, rather than moving straight from one card to the next.

Already in traditional spaced repetition, it was common for many cards to be related. Reviewing one might help with learning the others. That property is amplified here. One possible response to that is: perhaps LLMs can help adjust the review schedule for one unit of knowledge based on your review of another. Another possible response would be to pack more information into a single unit of knowledge, so facts that previously would have been spread across many cards are now contained in a single super-unit. This approach would then require us to explore the question: how to we track the user's level of understanding of a unit of knowledge?

**Does the nature of the per-question feedback (right vs wrong; hard vs easy) change since the interactions are conversational? And relatedly, does the way we track the user's level of understanding need to change?**

In conversational spaced repetition, the system potentially has far greater signal about a user's understanding than in a traditional spaced repetition system like Anki. The user can express uncertainty, can be partially correct, can ask probing questions about a specific subpart of a unit of knowledge, or can outright state that they do/don't understand something. The user can also speak in a way that demonstrates deeper understanding, for example bringing in outside knowledge or synthesizing information producing novel insights about the topic at hand.

Given this potential for greater fidelity of measuring a learner's level of understanding, how should the system store the user's level of understanding? Let's again brainstorm some options. (A) We can carry forward the approaches from existing spaced repetition systems, e.g. a single integer for the Leitner box a card is in, or [RSD values following the FSRS algorithm](https://github.com/open-spaced-repetition/fsrs4anki/wiki/ABC-of-FSRS). (B) We can use free-form text to describe the level of understanding that the user has. (C) We can use a combination of (A) and (B), something numeric and something textual side by side.

Option (A) has the advantage of being battle tested and yielding a clear scheduling algorithm, but it fails to take advantage of the new signal that conversational spaced repetition provides.

Option (B) is exciting because it fully leans into the power of LLMs, giving control over to the LLM to evaluate the learner's ability. However, it raises many questions. We do not know yet how good LLMs are at evaluating a user's understanding of a topic based on their answers, or how good they are at preserving that information in text once it is obtained. It is also not obvious how to translate a textual description into a scheduling algorithm to determine when next to surface some material. This suggests that some hybrid approach (C) may prove fruitful, bridging the gap between textual evaluations and algorithmic scheduling. The concerns about Option (B) lead us naturally into the next open question of how we deal with the untrustworthiness of today's LLMs.

**How do we deal with the untrustworthiness of today's LLMs?**

The problem of hallucinations and robustness arises in any LLM-based project. The answer, of course, is to have good evaluations for every task the LLM is tasked with performing. A good evaluation needs to genuinely be representative of the task, such that the measure of performance it provides can be trusted and can indicate to you whether the model quality is yet suitable for the application you are building.

The best way to build such an evaluation is to start by building the application, and to instrument it to collect usage data from the application. If you have a function that uses an LLM, instrument the application to collect inputs and outputs to that function. Then rewrite the outputs to produce ground truth data. Now you have the start of a good evaluation.

For the conversational spaced repetition system, the tasks that will rely on an LLM may include variants of the following: (1) mapping from conversations to units of knowledge, (2) writing questions based on some source content, (3) determining whether a user's answer to a question is correct, (4) evaluating a user's understanding of a topic based on their answers.

Yes, there is ongoing research to mitigate hallucinations, increase factuality, and generally raise the level of quality and trustworthiness of LLMs. More important than all of this is to know, through trustworthy evaluations, how good an LLM is at the tasks it is tasked with. It is these evaluations that will let us know whether an LLM-based conversational spaced repetition system is ready for meaningful adoption. Also, don't skip doing a vibe-checks when new models come out; playing with these models counts for a lot too!

**And finally, can LLMs provide solutions to the [seven issues that traditional spaced repetition has (linked earlier)](/snippets/2021-11-02-improvements-to-spaced-repetition/). I think LLMs might be able to meaningfully help with #{1, 3, 7}.**

Just to recap the seven issues, I've copied them below:

1. Card creation: Zero friction card creation
2. Card creation: Good cards by default
3. Card maintenance: Eject bad cards quickly
4. Schedule flexibility: Allow people to study more
5. Schedule flexibility: Allow people to study less
6. Review friction: Bring the reviews to the users
7. SRS that understands card connections

The proposed conversational spaced repetition system directly targets #1; in the proposal, an LLM is generating cards automatically from the conversations you have with LLMs. LLMs also offer promise toward mitigating some of these other issues as well. By providing the LLM with tools to maintain the "deck", you could providing instructions to the model to remove or deprioritize certain cards as they come up (#3). That could be a low friction way to let you eject bad cards (though something even lower friction than that is probably even better).

Most interestingly of all though is that LLMs can detect relationships between cards, and therefore can likely help with #7. If you demonstrate an understanding of some topic while discussing one unit of knowledge, an LLM-based system might be able to detect that what you say also demonstrates an understanding of some other unit of knowledge. The system could potentially adjust the scheduling of both units. This could free up meaningful amounts of time for you, the user, potentially allowing you to scale up the amount of knowledge retained in your spaced repetition system beyond the limits of traditional spaced repetition systems. Mathematically modeling this change and potential improvement could be an interesting next step, to better understand how LLMs can improve our ability to study going forward.

**Now it's time to build!**

This is a system I'm actively building, but it's early days! Interested in discussing or contributing? Get in touch! I'm excited to start using it to augment my own LLM-based learning as soon as I can.
