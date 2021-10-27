+++
title = "Writing Assistant Tool Idea"
date = 2020-01-13T00:00:00
tags = ["attention", "taking-silly-ideas-seriously"]
message = "A structured question-asking tool may be useful for writing effectively."
+++

### Background: Writing is Hard

Sometimes I find writing feels easy -- e.g. when [writing for no audience](/snippets/2019-12-30-writing-for-no-audience/), when writing something you've already thought extensively about, when telling a story in a logical order that you're deeply familiar with. Other times, I find writing very difficult.

When I'm writing a paper, I am writing explicitly for an audience, the story is not always clear immediately, and the material is something I'm becoming familiar with over time, not something about which I'm already deeply familiar.
So, I find paper writing hard.

I have an idea that I think will help me write more effectively. It's a software tool that structures the time you spend writing. I'll describe the tool, but I don't anticipate building it. Perhaps we can come up with a low-resource version of this idea, e.g. with paper and pencil, that I can try even without building this tool.


### The Writing System

The tool presents you with a prompt, a textbox, and a timer.

The initial prompt is "What do you want to write about?", and the initial timer is for 5 minutes. Subsequent prompts will be determined from what you've entered in the past.

In the textbox, you are encouraged to respond to the prompt.

As part of your response, you can issue some commands / keywords.
If you start a line with `!` or `?`, then that line will get used as a future prompt.
You can specify the relative importance of a future prompt by including a priority.
This will determine the order in which you are presented with the prompts.
E.g. `!0` is highest priority, and so such a line will become the next prompt you receive, unless there are other priority 0 prompts already queued up.

`! <topic>` is short for "\<topic\> is a topic I want to write about later"
`? <question>` is short for "\<question\> is a question I want to answer later"

There should also be a way to indicate "\<topic\> is a topic I'll need to do more research on", and then for one of the prompts to be about spending time researching a topic, rather than writing about it. Then the next prompt may be to write about what you just learned in the research section.

Other available commands include:

- `:pause` to stop the timer
- `:unpause` to start the timer again
- `:extend` to add additional time to the timer
- `:next` to skip to the next prompt

The system is easily extensible, so a writer with a programming background can easily add new commands, or modify the logic that determines when prompts are shown and when breaks are taken. A programming-proficient writer will also have programmatic access to everything they write, as well as the corresponding prompts and metadata.

Once the timer reaches 0, a short break is initiated, and then the next prompt is revealed.

The idea is to move quickly, and get all your thoughts onto the page, without getting bogged down in a DFS traversal of information about a single line of the overall text.


### Additional details

Every keystroke is logged, so if you write something, and then switch to a new version of it, you will still be able to see the original version. No need to worry about pasting in a password though, since the keylogging data is readily accessible in a plaintext format and you can edit it directly e.g. if anything sensitive does leak in.

This system has a decent amount of overlap with the [shh shell](/projects/shh-shell) project that I've already built,
and perhaps a version of this new idea could be easily added to the shh shell. Alternatively, the shh-shell could be forked to build this new system.

Calendar integration would be cool, so that it times your prompts nicely if you have a meeting coming up so you get to a good break point in time for your meeting.


### Implementation Thoughts

I'd like to build this onto an existing text editor, rather than writing my own. E.g. using Google Docs would be good.
However, the disadvantage of this is that it makes the keystroke logging feature more difficult. Fortunately, Google Docs does have good history tracking. Google Docs also provides good programmatic access. So, an agent running in the background while you write could be taking periodic snapshots too. Such an agent could also be extracting the commands and prompts you write.

However, it wouldn't be able to execute the commands immediately, the way shh shell does. For some commands this may be a real disadvantage.

I also like the idea of the agent giving the prompts being Bieber Bot -- that is, being the same _being_ as my personal digital assistant. I can picture it asking me "you've been writing continuously for over an hour; is it time for a break?" or "it looks like you stopped writing abruptly there, did you get distracted?".

### Initial Experimentation

I've been trying the idea out in a low-tech way (manually timing things, manually looking up what the next prompt should be).

Here is the main issue I've seen so far in the first half hour of testing. When the time runs out for a prompt, I'm still in the middle of the prompt. I've usually started expounding on some idea relevant to the prompt, and there are actually several ideas remaining that I haven't even started exploring for the prompt yet. So what should have happened / what should I do next time? Maybe I could have done a higher level discussion of the prompt and made new future sub-prompts along the way. Or at the end of a section, I could have the system give me a bit of time to create sub-prompts of things I'd like to address in the section but didn't get to.

I could see having a limited time to create new prompts be a good forcing function for coming up with structured high level thinking after a moderate amount of time of lower level writing. So in my next round of testing, I'll try this, and continue to iterate on the idea.
