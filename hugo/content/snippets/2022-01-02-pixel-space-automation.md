+++
title = "Go Note Go Messager without Pixel-Space Automation"
date = 2022-01-02T01:00:00
tags = ["automation", "browserflow", "messager", "go-note-go", "roam-research"]
+++

_This snippet was originally going to be about pixel-space automation. Then I found I didn't need it for what I wanted to do: sending messages to Twitter, Facebook, Slack, and Discord from Go Note Go, Roam Research, and Bieber Bot._

Happy New Year! I'd really like to automate Mac apps that don't expose actions to Automator
using pixel-space navigation and clicks and typing to control the automation. This is why and how.

(Update from the end of the snippet: By the time I finished writing the snippet, I had automated everything I intended to using browser automation in Browserflow, never once needing to automate Ferdi. I still think pixel-space automation would be wonderful, but my initial motivation for it turns out to be insufficient.)


### Motivation: Improving Messager by Automating Ferdi

I have a side project "Messager" that allows for programmatically sending and receiving messages
across a wide variety of messaging services.
I also use Ferdi for manually managing an even wider variety of messaging services.

Currently Messager supports
Facebook Messenger (as myself and as Bieber Bot),
Twitter (public tweets, private tweets, and DMs),
HackerNews,
and it has limited support for Slack and Discord.
Ferdi, on the other hand, supports a much wider range of services, but doesn't offer programmatic access;
I use Ferdi with
Facebook Messenger (as myself and as Bieber Bot),
Twitter (public tweets, private tweets, and DMs),
multiple Slacks,
Discord,
Gitter,
WhatsApp,
Telegram,
as well as for non-messaging services like Roam Research,
multiple spreadsheets,
supervisord,
and other adhoc use cases.

I would like to extend Messager to have wider support,
particularly to improve support for Slack and Discord.
To do this, <mark>I'd love to automate Ferdi</mark>.

### Motivation: Go Note Go - Messager Bridge

Why do I want to improve Messager _now_? It's because of [Go Note Go](/projects/go-note-go).

I'm adding messaging support to Go Note Go. The main use case I'm targeting is this:

I'm drifting off to sleep and realize I want to tell someone something.
So I write in Go Note Go something along the lines of "Tell John Smith Hey John, I have this new idea for Go Note Go where you can send messages as your drifting off to sleep -- maybe I can tell you about it tomorrow".

When I wake up the following morning, Bieber Bot has messaged me with a link to a spreadsheet.
It has all the messages I drafted the previous night (they haven't been sent yet).
There, I can clean them up for any typos and "approve" them (mark them as OK to send).
And once they're approved, they'll be sent automatically using Messager.

It's in support of this project that I'd love for Messager to support a wider variety of services.
Ideally the system will intelligently select the service to use to send the message based on the recipients.
It will include the service in the spreadsheet, so that I can adjust the service if needed before approving the message.

So this is going to be a Go_Note_Go-Sheets-Messager-Bieber_Bot collab.

tl;dr Go Note Go adds draft messages to a spreadsheet. Bieber Bot uses that spreadsheet to message me about new draft messages, and to message friends on my behalf with approved messages.


### Motivation: Going beyond

For the Messager application described so far, pixel-space automation is not necessary.
All of the services I want to automate can be opened in the Browser,
and so existing Browser automation techniques are sufficient.
I would use Browserflow for this if it supported programmatic triggers, but it does not.
(Psst... DK, can you add the ability to programmatically trigger a local flow please?)

Given this, why is pixel-space automation interesting?
It's because it would enable
(1) easier automation construction for the automations I'm interested in
and (2) it enables a much larger class of automations, and empowerment is key.
[See here for my dreams for the future of automation.](/snippets/2021-12-07-future-automation-software/)

### Ferdi Actions

The main actions I want for the Messager application are: 

- Ferdi: Navigating to different services
- Discord: Choosing a server, channel, or recipient
- Discord: Sending and receiving messages on that channel
- Slack: Choosing a channel or recipient
- Slack: Sending and receiving messages on that channel

### The Challenge

##### Why are the Discord and Slack APIs not sufficient?

Both Discord and Slack have policies against using self-bots. Their APIs don't allow you to programmatically control your own user account. So, controlling your account as a human would, through the provided chat client, is a natural way to approach the problem.

The advantages of using Ferdi over the browser are: (1) it uses service hibernation, so you can skip loading the pages and logging in each time you start using a website, (2) maybe you can keep using the browser while Ferdi automates in the background.

Each of these actions is doable using existing browser automation tools. Navigating to different services in the browser requires authentication though, if you're not already logged in (which I would be in Ferdi). Perhaps with Browserflow's cookie sharing feature, I can also already be logged in at the start of a Browserflow flow even on Cloud.

### Current Status

I took a break in the middle of writing this flow and now I've implemented sending messages via Browserflow in both Slack and Discord.
I've also gone further toward the Go Note Go-Messager bridge,
implementing a few of the other steps.
Whenever I use "@Person" in Roam, Bieber Bot automatically copies the message into a spreadsheet.
The spreadsheet has an "Approval" column, where I can mark messages as OK to send.
Bieber Bot will then use Messager to send any approved messages.
Since Go Note Go sends it's notes to Roam, this completes the circuit.

I can now send messages from Go Note Go to any of Facebook Messenger, Twitter, Slack, and Discord.
I'm still excited about pixel-space automation, but I'll have to save that excitement for a future snippet; for now, Browserflow was sufficient.
