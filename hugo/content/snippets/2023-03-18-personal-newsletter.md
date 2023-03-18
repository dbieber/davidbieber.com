+++
title = "Personal Newsletter (Just for me)"
date = 2023-03-18T00:00:00
tags = ["writing", "ai"]
keywords = ["newsletter"]
+++

I write a lot. Every night. Every day. I'm constantly writing. And, unlike many of the people I know who similarly take lots of notes, I also regularly read what I write. However, the nature of how I write leaves my writing messy (full of typos) and disjointed (writing on one topic might be scattered across dozens of pages, with lots of unrelated thoughts interspersed between).

About a year ago, I had the idea to hire an editor / writer to help me use all this writing a bit more effectively. My idea at the time was that once a month, I would bundle up everything I'd written that month, and send it to my editor. They would read through it, clean up all the typos, and also assemble a monthly newsletter of sorts, just for me. The newsletter would have a section for each major topic in my notes -- each idea that I revisited more than once -- and it would provide a quick recap of my thinking on that topic.

I never hired that editor. Instead, GPT-4 was released, and I implemented this newsletter idea for myself instead.


## The Newsletter

I now receive, courtesy of Bieber Bot and my messager server, a personalized newsletter twice a week. The newsletter contains a bunch of sections: upcoming plans, things I've been thinking about, the dominant emotions from the week, etc. Each section is presented in a nice little round-cornered box, with concise text showcasing the highlights from my notes.

This isn't a newsletter that I would ever send out to an audience -- it's highly personal! But receiving it in my inbox is a joy. It reminds me of the people I want to reach out to. It reminds me of all the clever little ideas I had throughout the week, that I might not have thought about again for a while. It reminds me of things I'd been meaning to buy or do.

Receiving this newsletter helps me connect better with myself by resurfacing all these old ideas I'd had throughout the week.


## Newsletter Features

**Questions.** In my first pass at creating the newsletter, I've given GPT-4 a list of questions to answer using the last 5 days of my notes. The newsletter contains one section per question. Here's the list of questions I started out with, which I expect to refine over time.

* What are all my open TODOs?
* What are all the things I want to buy?
* What are all my upcoming plans?
* What are some ideas I seem to keep revisiting?
* What are my accomplishments from the past week?
* List all the people I wanted to reach out to and what I wanted to say to them.
* What are the most interesting ideas from my notes?
* What are the big recurring themes in my notes?
* Are there any things in my notes that didn't make sense to you?
* What are the dominant emotions found in the notes?

**Digestability.** For each question, GPT-4 prepares concise content that's easy to digest. It arranges the sections in a 2-column layout.

**Citing sources.** I've also asked GPT-4 to include links back to the original notes that it is using to answer the questions. To do this, I include in GPT's view of my notes a unique ID for each note (essentially one ID per block of text). I then have GPT use these ids to cite which notes its using in every sentence that it writes. To me, it's remarkable that this works.


## Why are you writing all this to begin with?

One of the personal projects I've gotten the most value out of is called [Go Note Go](/projects/go-note-go/). It's a headless keyboard (a computer keyboard with no screen) that I can write on or speak to, and anything I write on it (or say to it, after pushing the record button), gets transcribed into my notes (for me, this is Roam Research, but Go Note Go supports 7-8 different note-taking systems, so if you want to use it, I'm sure wherever you like to keep your writing is fine.)

I've found Go Note Go incredibly rewarding. Whether I'm driving somewhere, drifting off to sleep, sitting at my desk, or taking a shower, it's there to help me capture any thoughts I want to remember. Unlike a voice memo or Apple Notes, using it isn't disruptive (to myself or others). Even when just sitting at a desk, I get a great sense of relief turning away from my computer monitor toward Go Note Go to write; it's freeing, and helps me think clearly. I could go on about Go Note Go indefinitely, and if you want to learn more or to build your own, [you can do so here](/tags/go-note-go/).

A second personal project that I also use to take notes on the go is my personal Voice Assistant. I have a phone number I can call to either leave myself notes or to talk with GPT. These notes / conversations also end up in my notes in Roam, and hence can end up in my newsletter. I prefer this over a standard voice note-taking app because it works well with car play, so I can use it while I'm driving.


## Building the Newsletter

Actually building the newsletter was delightful. Using GPT-4 to process my notes was simple using OpenAI's Python API. Despite this simplicity, I found it faster to have GPT-4 itself write the code that constructs the newsletter than to write it myself.

I also wanted the newsletter to be stylized nicely, not just a wall of text. I haven't done much front-end development work in recent years, but GPT-4 was happy to write the HTML and CSS to make the email exactly as desired (2 columns of rounded corner sections, each with header and content). The email-sending library I was using (a part of my Messager platform) didn't support sending HTML emails though, but GPT-4 had no trouble updating the library to support this.

Overall GPT-4 made building both the automatically-writing-the-newsletter and assisting-me-writing-the-software-that-creates-and-sends-the-newsletter pieces simple and quite fun.
It reminds me of the childhood joy of learning to program; computers are magic, once again.


## Newsletter Upkeep

I expect that over the next few weeks, as the first installments of the newsletter start showing up in my email, I'll have lots of tweaks and improvements I'll want to make. For one, I look forward to iterating on the list of questions and sections in the newsletter. I'm also likely to add some filtering to my notes before they get sent to GPT, to ensure that personal or confidential pieces aren't sent to OpenAI. I'm also likely to refine the "preamble" and prompts GPT sees, so it has more context about topics I write about frequently, and to better align GPT's output with my morning interests and needs.

As an example, I'm excited to try having GPT use HTML's summary/details feature to create a cleaner newsletter layout while allowing deep dives by expanding the summaries. Additionally, I'm enthusiastic about adding deep linking back into Roam, so that I can quickly access my raw notes from anything in the newsletter.

I'd also love to create an experience where simply by clicking on a piece of text in the newsletter, I can start to take the appropriate action on that item. For instance, clicking on a reminder to reach out to someone could open a Gmail draft or Facebook Messenger message draft started by GPT. And If I click on a reminder to buy a backpack, it could open Amazon search results.

For some items in my notes, it might even make sense for GPT to propose or take actions independently. I'm keen on exploring this idea and transforming the newsletter into more of a personal assistant experience for myself.

I'm confident that I'll have a dozen more ideas and feature requests for myself and for GPT in these coming weeks, and I'm delighted to use Go Note Go to keep track of all of them -- only to have them show up in my personal newsletter later in the week. I fully anticipate working with GPT to implement these feature requests to continue improving my newsletter experience.


## Conclusions, courtesy of GPT-4

In conclusion, using GPT-4 to create a personal newsletter has proven to be an effective and enjoyable solution for organizing and revisiting the wealth of ideas and thoughts from daily note-taking. The AI's capabilities in processing and compiling content, as well as its assistance in coding and designing the newsletter, have demonstrated its incredible potential as a developer tool. The resulting personalized newsletter not only helps me in connecting better with myself but also serves as a powerful reminder of my ideas, emotions, and plans that would have otherwise been lost in the chaos of daily life. As GPT-4 continues to evolve, there are endless possibilities for future improvements and applications, making it an invaluable resource for both developers and individuals alike.
