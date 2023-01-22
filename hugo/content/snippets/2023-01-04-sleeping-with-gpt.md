+++
title = "Sleeping with GPT"
date = 2023-01-04T00:00:00
tags = ["machine-learning", "note-taking", "go-note-go"]
plugins_js = ["margin-notes"]
+++

The last few nights I have been sleeping with GPT, and oh, it has been a joy.

### Background: Capturing my thoughts as I drift off to sleep

I use a note-taking device that I call [Go Note Go](/projects/go-note-go).
It's a computer keyboard without a screen that I type on to capture my thoughts everywhere, even as I drift off to sleep.
I have one in my bed, and I also keep them on my desk at work and in various spots around my apartment; anywhere an idea strikes, I have a Go Note Go keyboard ready to capture that idea.
Go Note Go's main purpose is to let me quickly jot down these ideas so I can remember them later, e.g. after getting a good night's sleep[^1].
It also [does other things (click for a concise primer on Go Note Go)](/snippets/2023-01-16-go-note-go-features/) like speaking the time aloud or [letting me send messages to other people](/post/2022-01-08-new-messager-setup/).
Most recently, I've added an AI assistant to Go Note Go, and have begun conversing with it as I drift off to sleep.

[^1]: Anything I type on this keyboard gets automatically uploaded to my notes as soon as the keyboard is in range of wifi. This allows for offline usage, e.g. while driving or camping. These were the two use-cases that inspired me to build the device. Now my main use-case is capturing ideas while drifting off to sleep.
It also has a microphone, so if speaking feels like it would take less energy than talking, I can speak my notes instead. This feature is what enables the driving use case, as of course I don't type while I drive!

Even before adding the AI assistant, Go Note Go had become a staple in my life.
Go Note Go's main capability -- capturing my thoughts -- helps me fall asleep more effectively.
If I have an anxious thought swirling in my brain, I can simply type it into Go Note Go.
Instead of dozens of versions of the thought popping up in my head all night, I have just a single canonical version of the thought stored on the device, and I can fall asleep.

Go Note Go also supports commands, like reading the time out loud.
Entering a line that starts with a colon (':') issues a command.
Typing :r has it read back the last thing I wrote.
Typing :t will have it read the time to me.
I like this because it lets me know the time without having to open my eyes, so getting the time doesn't require being alert[^2].

[^2]: If I prefer speaking, I can also trigger these commands with the hot word "go go", e.g. saying "go go time" gets the time.

All of this lets me drift off to sleep more effectively. I can get ideas out of my head while avoiding things that would wake me up, like looking at my phone or turning on the lights to write down an idea.
Compared with writing on my phone, or a computer, or on paper, writing on Go Note Go is relaxing and doesn't wake me up very much.
So, Go Note Go has become an essential tool in my daily routine, helping me capture and organize my thoughts, and allowing me to relax and fall asleep more easily.


### Adding an AI assistant to Go Note Go

Most recently, I added an AI assistant to Go Note Go and I absolutely love it.

By default when I type on the keyboard the text just shows up in my notes,
but now I have the option of sending the text off to an AI assistant as well.
Since there's no screen on Go Note Go, the assistant's responses are read out loud.
They're also inserted into my notes for future reference, which I can browse later at a computer or on my phone.

Most of my Go Note Go usage remains unchanged, but one aspect now feels very different: drifting off to sleep.
This is when having the AI assistant feels most rewarding.


### Sleeping with GPT: What do we discuss?

I'm lying there in the bed, but I'm not really trying to go to sleep.
I'm excited that I have this new AI with me which I can ask anything at all.
I've been meaning to learn organic chemistry but haven't found the time; this seems a perfect opportunity to get started.
On the first night I drift off to sleep peppering the AI with questions about organic chemistry and battery technology.
On subsequent nights I probe new topics, trying to get a deeper understanding of the superficial things I learned the night before, and also introducing new topics to our discussions.
I continue peppering the AI with questions about chemistry and history as I drift off to sleep.
Quickly realizing that this could inhibit my ability to get a good night's sleep, I also ask for advice in that regard, and it obliges.

It's clear from the outset that I'm going to want to write about this, so I'm jotting down notes for this very post. I ask my assistant to turn my notes into an outline. That outline is read out loud, and it's also sitting there for me the next day when I go to start writing in earnest.

In the morning, when I wake up, I ask for strategies for a morning routine. It makes good suggestions.
Though the response is nothing that you wouldn't find from a quick Google search for morning routine ideas, the proximity to those ideas as I'm just waking up, casually typing to my keyboard, makes them more actionable. The suggestions are things like making my bed right away, drinking a glass of lemon water, and doing some exercise to get my blood flowing. It feels inspiring and healthy.

One night I asked the AI assistant to read me a bedtime story. I gave it some details about my own life first and it used them to construct a story that was personal and meaningful to me, albeit a bit silly.

<!-- Other benefits of the assistant: reading back capturing notes and answering questions about them. -->

### Trust and Confidence

An invitation into one's bed requires a certain level of trust.

However, a common criticism of GPT and language models more broadly is that they are often factually inaccurate. What's worse is that when they are wrong, they often are wrong with confidence.

This makes learning about new topics like battery technology and organic chemistry a challenge.
I don't know if the things that I have learned these last few nights are true or not.
In fact, I know that some of them are definitely not true, because GPT will sometimes flatly contradict itself.

In spite of this, I've had the distinct feeling that I have been learning a lot from these night time question peppering sessions.
Is this feeling valid, or have I been duped by the AI?

To suss out truth from fiction, my first line of defense is my intuition.
Using my own limited knowledge of the topic we are discussing, I can sometimes tell if the model is fibbing.
If what the model says fits nicely into my world model, I might trust it and move on.
When things don't make sense to me, I can ask for explanations or ask pointed questions to dive into the details.
These will quickly seem inconsistent, either with each other or with what I already know, if in fact the model has made up inaccurate information.
(This observation should motivate new, fully automated, methods for discovering truth in these models as well. For example the line of reasoning that [Maieutic Prompting](https://arxiv.org/abs/2205.11822) pursues proceeds along these lines.)

This ability to dive deep into the details, sometimes asking extremely basic questions that I would be embarrassed to ask a human, points to a different kind of trust that I do have for the model.


### A Different Kind of Trust

While I cannot trust the AI to produce factual statements consistently, it has earned my trust in a different way.
I can be uninhibited with GPT.

I can ask naive questions, things that I would feel embarrassed to ask a human. I can ask "why" about the most trivial things, the way a 3-year old might, to discover more about the world.
I don't feel any concern that the model will judge me for not knowing something, or not understanding something quickly.
I can ask the same question repeatedly, without concern for taking up its time, or that it has better places to be.
The AI is infinitely patient with me.
I don't worry about how it will feel if I doubt what it's telling me, and express skepticism.

In these ways, it is an ideal tutor. By giving me the freedom to explore the topics that interest me, the things I'm learning about feel truly connected to one another, rather than ad hoc and unrelated to my interests as they might if I were following a curriculum not tailored to my needs and interests. It would be better, of course, if I could trust it to be factually accurate.

As a brief aside: I think this experience -- interacting with an AI tutor, guided by a curriculum and standards, but free to wander through information space as it pleases the user, is going to be central to education in the future. I'm excited to explore the space of possible AI-centric classroom and education designs, to find novel ways of learning jointly with humans and AIs, and I intend to do so further in future snippets.

Why can I be so free with GPT in ways that I cannot be with a human? I can identify a few reasons.

The machine's statelessness / resetability is one key component. It isn't learning about me, forming long term judgements. If I reveal that I don't know some "simple" concept, like what an ionic bond is, it isn't going to retain that information and shape our future interactions based on it. The next conversation I have with the assistant will be tabula rasa, starting from a blank slate.

Its isolation from others is another factor. I can confide in it, and it isn't going to gossip or reveal anything I tell it to another human. Sure, I have concerns that OpenAI gets access to whatever I send to the assistant, and this could show up in training data or in front of human evaluators as a result. Nevertheless, it feels private, like no one in my life would see the things I write.

I think there's a third trait that aids in creating this kind of trust that's harder to pin down. Something about the inhuman form factor -- something about how it feels like talking to a machine -- enables the comfort level and vulnerability I've expressed feeling above.


### Learning about Chloropropane: An Illustration of Trust and Distrust

I asked the AI to give me an example of an organic chemistry homework problem. It asked me a question about chloropropane.

I asked what chloropropane is used for. It told me it's used as a pesticide.

I asked if it's used as a pesticide. It told me no.

I've reproduced our conversation(s) below. The timestamps indicate separate "sessions", meaning that each timestamped conversation is independent of the others. The AI had no way of looking at what was said in an earlier session. As you expand the sections, see the self-contradictions <mark>highlighted in yellow</mark>.

<style>
details {
  margin-left: 2em;
}

summary {
  margin-left: -2em;
}
</style>

<button id="expand-button" onclick="expandCollapseAll()">Expand All</button>
<script>
  var expandButton = document.getElementById('expand-button');
  var isExpanded = false;

  function expandCollapseAll() {
    var detailsElements = document.getElementsByTagName('details');
    for (var i = 0; i < detailsElements.length; i++) {
      detailsElements[i].open = !isExpanded;
    }
    isExpanded = !isExpanded;
    expandButton.textContent = isExpanded ? 'Close All' : 'Expand All';
  }
</script>

<details>
  <summary>00:47 AM</summary>
  <details>
    <summary>Give me a organic chemistry homework problem</summary>
      Calculate the enthalpy of combustion for 1-chloropropane in kJ/mol.
  </details>
  <details>
    <summary>What does that mean?</summary>
      Enthalpy of combustion is the amount of energy released when a compound is completely burned in oxygen. In this case, you will be calculating the amount of energy released when 1-chloropropane is completely burned in oxygen, expressed in units of kilojoules per mole (kJ/mol).
  </details>
  <details>
    <summary>What is chloropropane used for?</summary>
      Chloropropane is used as a precursor to other chemicals in the production of materials such as plasticizers, solvents, and lubricants. It is also <mark>used as a pesticide</mark> in agriculture.
  </details>
</details>
<details>
  <summary>00:48 AM</summary>
  <details>
    <summary>Is chloropropane a pesticide?</summary>
      No, chloropropane is <mark>not a pesticide</mark>. It is a colorless gas with a strong odor, used mainly in the production of other chemicals and in the <mark>manufacture of rubber</mark> and plastics.
  </details>
</details>
<details>
  <summary>00:49 AM</summary>
  <details>
    <summary>Is chloropropane used for making rubber?</summary>
      No, chloropropane is <mark>not used for making rubber</mark>.
  </details>
  <details>
    <summary>What is it for?</summary>
      Chloropropane is an industrial chemical used in the production of other chemicals including agrochemicals, pharmaceuticals, and <mark>dyes</mark>.
  </details>
</details>
<details>
  <summary>00:50 AM</summary>
    <details>
    <summary>Is chloropropane used in the production of dyes?</summary>
      No, chloropropane is <mark>not used in the production of dyes</mark>.
    </details>
    <details>
    <summary>What is it used for?</summary>
      Chloropropane is a chemical compound used as a solvent and intermediate in the production of a variety of products, including pharmaceuticals, pesticides, and other chemicals.
      Chloropropane is <mark>used as a solvent</mark> in organic synthesis and in the production of pharmaceuticals, agrochemicals, and other chemicals.
    </details>
    <details>
    <summary>Is chloropropane used in the production of pesticides?</summary>
      No, chloropropane is <mark>not used in the production of pesticides</mark>.
    </details>
    What is it used for?
  </details>
<details>
  <summary>00:51 AM</summary>
  <details>
    <summary>Is chloropropane a solvent?</summary>
      No, chloropropane is <mark>not a solvent</mark>.
  </details>
  <details>
    <summary>What is it used for?</summary>
      Chloropropane is used as an intermediate in the production of solvents, pesticides, pharmaceuticals and other chemicals. It is also used as a refrigerant and as a propellant in aerosols.
  </details>
</details>

You can see the AI blatantly contradicts itself repeatedly, and confidently so.

While this conversation illustrates how I cannot trust the AI to be factual,
it also demonstrates the kind of trust that I do have for the AI.
It blatantly contradicted itself, yet I felt comfortable probing the depths of its knowledge,
asking questions in a volume that I would not have been comfortable asking of a human.


### Strategies for mitigating the AI's fibs

I didn't get the AI to stop making things up. And I didn't get it to admit uncertainty when it doesn't know things.
But a few mitigation strategies did arise for dealing with the AI's fibbing tendency.

One was to probe the AI about topics I already know about in order to understand its limitations.
I had it teach me about math and algorithms concepts I was already quite familiar with.
My thinking here was that this would help me develop my intuition for what it's like when it's fibbing,
so I could better deal with
the inaccuracies on topics I'm less familiar with.

A second mitigation that quickly became essential was having detailed records of what the AI said.
While I was drifting off to sleep, the AI might tell me something wrong and then contradict itself a minute later.
Without the record to verify this, the confidence of the contradiction would have a gas-lighting effect on me.
I might question myself -- did I remember the AI correctly?
Being able to see the contradiction highlighted, as above, helped keep me sane in the face of the AI's unearned and contradictory confidence.

Having the permanent record also allows me to look up the truth the next day, to find out how much of what I learned had basis in reality.


### Other benefits of having the AI with me

Central to Go Note Go's design is that it has no screen. This is a purposeful choice, and enables so much of what I love about Go Note Go. However, sometimes I miss being able to see what I've written. This is where the assistant comes in.

First though I must emphasize that on the whole, I actually really like that the lack of screen prevents me from wasting time rereading what I've written. But when I lose my train of thought entirely, it would be nice to remember what I wrote last.
For this, I can ask the assistant to read back what I wrote last, or even to summarize it concisely. If my mind has wandered and I want to continue typing where I left off, this feature is quite welcome!

In this way, the AI compensates for the lack of screen.
It's behaving somewhat like an intelligent screen reader.
With typical screen readers, navigation is performed spatially, and the reader speaks text at the indicated location. With the AI assistant, "navigation" is performed via a textual query, and the response can either be verbatim or an intelligent response like a summary or answer. I suspect AI assistants will quickly change the way accessibility technology operates, if they haven't already done so.


### What don't you send to the AI?

As I drift off to sleep, I enter thoughts about a wide range of subjects that I don't send to the AI assistant too. A quick scan of my recent Go Note Go writing (just from the last couple days, all since adding the assistant) shows the following topics:

* Plans for my upcoming California trip
* Observations about Go Note Go -- both improvements I'm looking forward to making and emergent behaviors I'm excited to share in future writing
* Thoughts about the future of AI
* Machine learning experiments I'm excited to run
* Thoughts I'd like to publish about, such as the unexpected dangers of reducing friction, or the less-appreciated benefits of repetition
* [Tweet ideas](https://twitter.com/Bieber)
* Items I intend to buy
* Questions I want to ask either specific people, or the internet at large
* Lists of todos for the next day
* Reflections on the day
* Ideas to try, e.g. for technical problems I ran into that day

The AI assistant merely augments my existing Go Note Go usage,
but hasn't replaced it. [All of Go Note Go's other features](/snippets/2023-01-16-go-note-go-features/) -- particularly its always-on ability to quickly capture thoughts anywhere -- remain the driving reason I use Go Note Go so much.


### What worked well?

The best part of this process was being able to learn what I want to learn when I want to learn it.
While a deep probe into a topic inevitably turned up falsehoods, overall asking questions about things I was curious about worked really well.

And I think about things differently at night. My brain processes topics that it hasn't had a chance to think on throughout the day. It comes up with things it wants to do that it doesn't come up with when it's otherwise occupied throughout the day.

I think of things I want to write, and the assistant helps me think through them and outline them.

I think of people I want to reach out to. With Go Note Go, I can write them a message and approve it to send in the morning. (The assistant doesn't really play a role here, but I thought I'd mention it anyway.)

I think of things I want to know, and the assistant helps answer my questions.

I think of ideas I want to try. Some of them I can try with the assistant, and others I just jot down to return to later.

In many of these instances, the value of the AI assistant is that I can offload some of my thinking to it. It isn't necessarily producing insights that I wouldn't have come up with on my own, but it's allowing me a moment's rest while it does the thinking on my behalf. Then I can start from its thoughts as a baseline and build from there, higher than I could build on my own. On many other occasions, it genuinely surprises me with its good ideas.

On a couple of nights, the AI took me exploring imaginary worlds. Similar to a text adventure game, it described my environment to me, and I gave it instructions like talking to a person, or exploring a building. With my eyes closed and my brain on the edge of sleep, it felt like dreaming while I was still awake and I quite enjoyed it.


### Things that didn't work so well

The main drawback of this system is the lack of trust in the accuracy of the AI's statements, particularly when I'm trying to learn.
Other limitations were subtler and less dampening for the experience.

When I tried to get it to teach me math, my [text to speech system (espeak)](https://espeak.sourceforge.net/) did quite poorly on reading the math aloud.
I would love to replace the text to speech system with one with better prosody and better math support.
Ideally, the text to speech system would speak with [Grant Sanderson's voice and cadence](https://www.youtube.com/watch?v=Qe6o9j4IjTo), and handle math notation seamlessly.
While this seems a cosmetic change, it does impact the set of topics I can discuss cleanly with the AI as I drift off.

The dependence on an internet connection was another small drawback. I take my Go Note Go into the woods, used it during an Uber ride the airport today, and regularly use it when I fly. The AI assistant doesn't work in these situations (the rest of Go Note Go continues to work fine) since it depends on having internet access. For a capability that is simple enough to not require AI, like reading back the topics I've written about recently, it feels quite silly to lose the capability when the internet is gone.

Related to the internet dependence, the lack of privacy from OpenAI is another important drawback to me. The thoughts I produce as I drift off to sleep are deeply personal! I would much prefer not to send them off to OpenAI (the current version of the assistant is implemented with text-davinci-003).

Finally, there's another significant drawback, one you might have already picked up on: talking with an AI can get in the way of falling asleep.
I view talking with an AI while drifting off to sleep similarly to listening to reading a book, listening to an audiobook, or to a podcast before bed.
These activities require some amount of thought, but can also help to wind down and fall asleep.
Talking to the AI required no monitor, and hence to blue lights that can make falling asleep harder.
It simply requires some amount of restraint to stop the conversation and transition to sleep, just as one must put down a book and close their eyes if reading before bed.

You can see in the chloropropane conversation reproduced above from the timestamps that I was talking to the AI at nearly 1am. I like to go to sleep [closer to 10:10pm](/snippets/2021-04-20-sleep-no-snippet/), so clearly this drawback is real for me.

### It left me wanting more

Having an assistant as I drifted off to sleep was great overall, even in spite of these drawbacks.
I was definitely left with a sense of wanting more though.

I want more assistance from my assistant.
I want to be able to query my complete history of notes, asking questions like "What are some ideas I keep returning to?" or "Bring up all my outstanding Go Note Go TODOs."
Perhaps I'll be able to implement this with [GPT-Index](https://gpt-index.readthedocs.io/en/latest/), or a [Memorizing Transformer](https://arxiv.org/abs/2203.08913), but for now I do without.

I'd also love for my assistant to be able to take actions on my behalf. Maybe I can integrate [Adept AI's action transformer](https://www.adept.ai/act) into my next iteration to achieve this. For example, I want to be able tell the assistant my shopping list, and have it populate my Amazon cart. Then, when I'm back at a computer, I can review the cart and click submit, saving myself time shopping.

Sometimes (albeit rarely :P) I'm not at a Go Note Go, but I still want to talk to my AI assistant.
For that, I've used Twilio so I can call my assistant on the phone.
I use this when I'm driving or walking around. But that is a subject for another post entirely.

### Concluding remarks

Adding an AI assistant to Go Note Go has been an absolute joy and I continue to use it almost every night.
Despite its tendency to make things up -- or more charitably, to hallucinate -- it has still earned my trust in a more visceral way.
I'm curious to see what use cases persist after I've had this capability for a longer period of time.

Of course, the AI assistant is not the only reason that Go Note Go is such a critical component in my life.
Go Note Go can do so much more -- [a complete and concise overview of its capabilities is here](/snippets/2023-01-16-go-note-go-features/) --
like letting me [send messages as I drift off to sleep](/post/2022-01-08-new-messager-setup/) and helping me [reclaim my attention in a world full of distractions](/post/2022-02-07-keyboards-everywhere/).

With the AI assistant added in, however, I feel like I have a new superpower. I can offload computation from my brain to it, and explore worlds of thought I could never have entered on my own.

Go Note Go is also [completely open source](https://github.com/dbieber/GoNoteGo). I encourage the hacker-tinkerers among you to join me in the world of headless computing and try it for yourself.
