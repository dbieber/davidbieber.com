+++
title = "Two Snippets I want to write about GNG and Messager"
date = 2022-01-08T02:00:00
tags = ["snippets", "go-note-go", "messager"]
+++

I have two new ideas for snippets I want to write. They're about Go Note Go and Messager Queue, both side projects I've been putting a bunch of time into the last few days. The snippet ideas are:

1. Using Go Note Go as an outliner
2. Adding Hacker News to Messager Queue, and then auto-queuing Twitter and HN posts for snippets.

The first is about _using Go Note Go as an outliner_. This is a new feature I've added to Go Note Go just in the last day or so. Before yesterday, each note entered via Go Note Go was it's own bullet in your note-taking system. Now (at least for Roam), you can also use tab to indent and dedent notes.
This sounds simple, but thinking through the user experience, taking into consideration that there is no screen, was a fun experience.
It also sounds like an only marginal improvement, but for me it's been rewarding more than I expected. It has interesting interactions with the [new message sending feature](/post/2022-01-08-new-messager-setup/) -- making sending messages even more enjoyable.
And it lends itself well to progressive summarization and chronologically organized notes;
with the current implementation, each note-taking "session" has a timestamp and blank space for a summary at the top of the session. I can fill in the blank space and then collapse the notes, making it easier to skim through them later.
Perhaps these summaries will serve as training / fine-tuning data for an autosummarizer later.

The second snippet idea is a new script I am thinking of writing that will add messages to my new Messager Queue automatically.
I've toyed with the idea of sharing more of my snippets publicly in the past.
Currently, I only share them very rarely.
Only partially is this an active decision; it is also partially inertia and there being an activation energy and unnaturalness for me in posting publicly.
While the active decision reasons will remain, having auto-generated messages populate my Messager Queue periodically will really dilute any inertia / activation energy / unnaturalness reasons for not sharing snippets, and those are precisely the reasons I want to eliminate.
Doing this will require a small change to the Messager Queue to support Hacker News; this should only take a few minutes, as HN is already supported by Messager.
Then, it will likely take a few hours to write a script that periodically adds messages about my snippets to my Messager Queue.
One source of these messages will be the "message" field at the top of some of my snippet frontmatters.
For others I can just make a templated message using the snippet title; the beauty of Messager Queue is I don't need to autogenerate the perfect message, since I can tweak or rewrite it before approving the message to go out.

So, I've now put down all the things I wanted to say about those two snippets. Does it still make sense to write them? I don't know; I might turn them into new snippets anyway.
