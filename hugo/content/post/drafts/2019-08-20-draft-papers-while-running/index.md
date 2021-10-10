+++
title = "Hands-free, Eyes-free, Writing Software"
subtitle = "Things I Would Like to Exist in the World: Part 1"
type = "post"

date = 2019-08-20T00:00:00
draft = true
authors = ["admin"]
math = false

tags = []
summary = "Here's how you can build a voice recognition app well-suited for drafting essays without using your hands."

[image]
  caption = ""
  focal_point = ""
+++

## Overview

One thing I would really like to see in the world is a voice recognition system suitable for writing essays while running. In this post, I'll describe why I think this is a good idea, and also how to make it a reality.

This is the first in a series of posts where I detail *Things I Would Like to Exist in the World*. In each post, I describe a thing I would like to exist, and then proceed to explain how to build it. [Read the introduction and learn about other *Things I Would Like to Exist in the World* here.](/post/2019-10-11-things-i-want-to-see)


## Drafting Essays While Running

If you're running, cooking, doing laundry, or otherwise have your hands occupied but your brain free, there ought to be a way to put that brain to use. In particular, you should be able to easily draft an essay while doing any of these activities.

Today's voice recognition apps -- Dragon, Otter, Apple Notes, etc -- are simply not up to the task.

Let's look at what a good system for drafting essays while running should look like, and then we'll see why these existing systems are insufficient today.


## The Product Vision

Your hands are occupied because you're performing a task like running or cooking. You don't want to be looking at a screen too much right now, because you have to look where you're going (or at what you're cutting).

You have a phone, tablet, or computer with you though, with the SpiritWriter app open, so writing an essay won't be a problem.

You begin to dictate "New Section. High level motivating goal of the thing. \<beat\> If you're running, cooking, doing laundry, or otherwise have your hands occupied but your brain free..."

As you speak, the section header appears, followed by the text you've written. There's minimal latency between when you speak and when the words appear. Of course, you don't notice this, because you're not looking at the screen.

You stuttered over the word laundry and so initially it appears as "lawn ..." but quickly it corrects itself once the correct word, *laundry*, becomes obvious from context.

A large number of commands are supported:

  - {Go/Delete/Read back/Copy/Mark/Select} {Up/Down/Left/Right} N {sections/paragraphs/words/characters}
  - Surround selection with {parenthesis/brackets/braces/square brackets/squirrely braces/curly braces}

<font color="red">TODO: List out explicitly the commands that are supported in this vision.</font>


## On the Market Today

There are a handful of voice recognition solutions available today: Dragon, Otter, Sphinx, Apple and Google's voice recognition, and Apple's Automator Dictation.

Why don't they solve the problem already?

<font color="red">TODO: Determine whether Dragon does in fact already solve this effectively.</font>

### Reason #1: Voice recognition quality

The quality of the automatic speech recognition in iOS's default transcription service isn't sufficient for this purpose. The same is true of CMU's Sphinx speech detector.

Fortunately, automatic speech recognition is rapidly getting _very_ good. The Google Live Transcribe app, which uses the Google Speech Recognition API <font color="red">TODO: double check this name.</font> has passed a threshold of quality that makes it all of a sudden extremely useful.


### Reason #2: The user interface / the lack of speech commands

It isn't enough to have the words you say be transcribed, in order, from left to right on the page.
Instead, there needs to be a fluid experience with a closed feedback loop between you and the computer.
If the computer makes a mistake transcribing, you need to be able to quickly correct it with your voice.

You also need to be able to issue voice commands other than simply dictating the words that should be written. You may need to delete a word or a paragraph. You may want to move the cursor up 3 paragraphs, or up 2 sections. You may want to insert a header, or a footnote. You might want to select a section, a copy it somewhere else, then seek to a word in the middle and modify it.

All of these interactions are critical to a good voice drafting experiment.

And if you're running, and so can't look at the screen often, we need to go one step further.
We need audio feedback.

You need to be able to ask the system "read that back to me", or "read back the last 2 lines."

### Additional improvements needed:
While a statement like "read back the last 2 lines" is intuitive, an experienced runner/writer will want to abbreviate that to save time.
An appropriate balance between standardization and customization must be found.
For this example, perhaps "read back the last 2 lines" should be shortenable to just "back 2".


### The State of the Market
Are the existing solutions actively evolving, or old or inactive?

Dragonfly is under development.
Voice recognition technology in general is under heavy development.
Offline voice recognition technology is under development.

### A Bit of History

What have people used to solve the problem in the past?


3. Why do I think The Thing should exist, and why I do think it doesn't already exist?
4. How to build the thing.

# How to Build a Voice Recognition Essay Writer

## Part 1: Voice Recognition

There are several options for how to build the voice recogntion engine for your essay writer.
Naturally, this is one of the most important components to making this whole project work, so it's important to get it right. At the same time, we should not deceive ourselves into thinking that this _is_ the project. We don't need to build a voice recognition system from scratch; that isn't the point of this project. People have already put a lot of hard work into making voice recognition systems and we're not here to reinvent the wheel. We're here to reinvent writing.

### Option 1: Building a voice recogntion system from scratch

I include this option here, not because you should do this. In fact, you should not do this; you should use Google's automatic transcription system instead. The reason I include this here is because it's important to know how voice recognition systems work and how you _could_ build one, if improving transcription quality were your goal.

Understanding how voice recognition systems work will be useful for debugging problems that may arise later on. Additionally if you have to take steps to improve the quality of transcription for your users, knowing how these systems work will come in handy.

### Option 2: Cloud Transcription

Google (<font color="red">TODO: see what others offer</font>) offers a Cloud service for automatic transcription of audio. The good news is that it is high quality and fast. The downside of using any cloud transcription option is that you have to a) have internet connectivity for transcription to work and b) trust the provider.

I personally have no qualms trusting Google to do the transcription, but there are users who do.
As for maintaining internet access while using the transcription system, it isn't ideal, but it may be a worthwhile tradeoff for being able to focus on the rest of the app, since building a high quality offline transcription system may not be your priority.

<font color="red">TODO: add a section on how to choose whether to prioritize building an offline transcription system</font>

When using a Cloud transcription provider, here are some technical considerations you must be aware of:

  1. The transcription provider likely has a time limit for how long an audio stream can be help open for. In the case of Google's transcription provider, that limit is 5 minutes. A team at Google has released (for free, open source) software called the Live Transcribe transcription engine that can help you deal effectively with this 5 minute limit. <font color="red">TODO: explain how Live transcribe transcription engine deals with this</font> If you're developing an Android app, you can directly use the Live Transcribe transcription engine. Otherwise, you'll be advised to take inspiration from the Live Transcribe team and build a similar system for yourself.

  2. There is latency inherant in getting the audio to the transcription provider and waiting for the transcription to come back. You must consider this latency when designing your app.

  3. Accuracy? That's an issue whether local or cloud
  3b. Personalization / fine-tunability.
  3c. Background noise correction.

  4. Privacy and security. Nobody wants their audio sent unencrypted over the web. No body wants their half-baked essay ideas leaked online. Any of the cloud providers should be forcing you to use their service via encrypted traffic, but it's something to keep in mind and double check for as you develop your system.

  5. Bandwidth. When using a cloud transcription service, the audio needs to be shipped to the cloud to be processed. This can be a meaningful amount of data if the microphone is left on and transmitting to a server for an extended period of time. A good client will stop transmitting data when it detects silence, and start transmitting again when there is something ready to be transcribed. <font color="red">TODO: check if the Live Transcribe engine does this</font> <font color="red">TODO: provide an estimate of the data transmission rate required for non-silence audio.</font>


## Part 2: The Text Editor

At first blush, adding a text editor to an app seems like the simplest thing in the world. It's just a text field, and the operating system will take care of handling keyboard inputs and cursor movement, right?

Well, there are a number of features you may have come to expect or may later want to add that make creating a text editor a much bigger ordeal than you may initially think:

  - Formatting
  - Saving files locally and to the cloud
  - Collaborating with others
  - An undo/redo history

Because of all this complexity, I suggest investigating alternatives for the text editor before deciding whether or not to build your own.

## Part 3: Voice commands

This is where the crucial work must be done, bridging the gap between the text editor (and any other features you include in your app) and the voice recognition system.


## Part 4: Improvements for Running

When running, there are some bonus features that would be nice.

- When reviewing your writing, see where you were when you wrote each word. Bonus statistics like how fast you were going and your elevation are fun too.
- Noise cancelling is doubly important when running, as the wind may be rushing into the microphone.


5. Predictions:
  - Who will build the thing?
  - When will it be built?
  - How much will it cost once its built -- how much would I be willing to pay for it?
  - How big a team will build it?
  - Is it going to be a business? Market cap for the idea?
6. Names - in this section I brainstorm silly names for the thing.
7. Variations on the theme:
  - What's the more marketable version of the idea?
  - What's the version for children? For parents?
8. Hypotheticals
  - What's the worst that can go wrong with this thing?
  - What does society look like if The Thing becomes wildly popular?
9. Let's say you want to build this but don't know how - where can you learn the skillset necessary?
