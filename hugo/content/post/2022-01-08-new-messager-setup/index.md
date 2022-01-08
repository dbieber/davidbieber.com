+++
title = "Sending messages as I drift off to sleep"
date = 2022-01-08T00:00:00
tags = ["go-note-go", "roam-research", "note-taking", "messager", "browserflow", "automation"]
keywords = ["communication"]
summary = "My new Messager setup, allows me to send messages directly from Roam Research _or_ from a standalone keyboard (with no monitor) that I keep at my bedside as I drift off to sleep."
+++

In this post I describe my new Messager setup,
and how it allows me to send messages directly from Roam Research _or_
from a standalone keyboard (no monitor) that I keep at my bedside as I drift off to sleep, and which I take driving and camping.

Currently my setup supports sending messages to
Facebook Messenger, Twitter,
Slack, Discord, and iMessage.
I intend to add gChat and email support next, since there are still a handful of people I want to message that don't use any of these.

Above all else, the beauty of this project to me is its usability,
which is hard to communicate in a write-up like this.
Some of the usability comes from the way the components integrate with my existing workflows.
Some of the usability comes from design choices
(like using a keyboard with no monitor for note-taking and message drafting).
I'll try to point out these usability elements along the way.
Bear in mind I designed this primarily for myself
(though I have a handful of friends along for the ride as well, trying it out and making their own contributions).

Let's dive in.


### Go Note Go: The Headless Keyboard

For some background, I developed Go Note Go, a headless keyboard designed for note-taking on the go.
Go Note Go is a note-taking system for when you're on the go, with a focus on driving and camping.
You can [read all about Go Note Go here](/projects/go-note-go) and learn more on [its GitHub page](https://github.com/dbieber/gonotego).

Go Note Go's main purpose is note-taking.
Anything you type into Go Note Go or voice-record into it gets transcribed and uploaded to your notes as soon as it gets an internet connection.
For me, Go Note Go uploads to Roam Research. It also supports RemNote, IdeaFlow, Mem, and Notion, and adding additional systems isn't too difficult.

One of the usability perks of Go Note Go is that there is no monitor. This means you can't get distracted browsing the internet while writing on Go Note Go. You also can't get distracted wordsmithing your own writing. It makes writing pleasurable, even if it comes at the cost of having typos and stray thoughts in your writing; you can always clean those up later.

Go Note Go does a lot more, so I do encourage you to [learn more about it](/projects/go-note-go), but it isn't the focus of this post, which is about sending messages.
For the purposes of this post, Go Note Go is a data entry system for Roam. And since I've also built a system that allows sending messages directly from Roam, this means I can now send messages directly from Go Note Go. So, I can send messages when driving, camping, and as I drift off to sleep at night.

To send a message in Go Note Go, you simply "@" the person you are writing to. To send a message to Adriana, I would write "@Adriana Message goes here". To send a message to David Dohan (using first and last name), I could write "@David Dohan: Message goes here". You can @ someone at any point in the message. You can also @ multiple people, and Messager will send them a group message.

Go Note Go acts as an outliner now too; this is both a big usability improvement for Go Note Go on it's own, and doubly so for using Go Note Go as a messager. An "outliner" is a system for taking notes as a series of nested bullets. You can push tab to indent notes underneath other notes; I've developed a user experience that makes this moderately natural, even in the absence of a monitor or any other visual feedback. For sending messages, the outliner feature is a boon. Any notes you nest under an @'d note will also register as additional messages for the @'d recipients. This makes writing longer multiline messages a pleasure, even without a monitor.

The default behavior of my messaging system is to hold the messages for approval before sending them. So, the messages that I write as I drift off to sleep don't send as I drift off to sleep. Instead, I see them in the morning and approve them, and only upon being approved are they sent automatically.

This delayed-approve-then-send approach is particularly well suited for Go Note Go, where I likely make typos and want to clean up the messages before they are sent, since I am writing them without a monitor. Later in the post I'll dive into what the approval process looks like (tl;dr there's a spreadsheet where I can mark a message as "OK" to send), but first I want to share additional benefits of being able to send messages directly from my note-taking app, which is currently Roam Research.


### Drafting Messages in Roam Research

Anything I write on my Go Note Go appears in Roam Research, but I can also take notes directly in Roam.
Just like on Go Note Go, the way to draft a message in Roam is to "@" the person you are writing to.
Messager has some heuristics it uses to translate your @'s into proper recipients.
So, the syntax for @'ing someone isn't too strict.

Using Roam offers some possibilities beyond what I can do on Go Note Go, such as including images in messages.
Like on Go Note Go, you can use nested bullets to create longer messages,
and you can @ as many people as you want for a message.
In Roam, however, you can also include images in your messages.
Messager will intelligently send those in the native format used by the underlying messaging service,
rather than blindly sending the markdown stored in Roam.
I find this feature, being able to use images naturally in Roam, and then have them send naturally as messages,
quite pleasant.

One future direction I'd like for this project is to add a "send" button in Roam next to any messages I've drafted there,
as well as to display the status of the messages inline in my notes. That's not implemented now, but would be a nice-to-have for the future.

Today, all messages are automatically added to my "messager queue" where they wait for approval before being sent.
I like having this approve-before-sending approach as the default, since it psychologically frees me up to write things I might not otherwise write if I was instead using a send button that sent immediately.
However, sometimes being able to send something immediately is desirable, and that's not a clean option in the current setup.


### Roam to Sheets: The Messager Queue

Any messages in Roam (whether entered directly into Roam, or entered via Go Note Go), are automatically added to a spreadsheet, the "Messager Queue". These are the spreadsheet's columns:

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| Service | Recipient | Text |  Date |  Time  | Approval |  Status |  Metadata

The Messager Queue sheet is filtered by default to show all pending messages. For each message it shows the *Service* on which it will be sent and well as the *Recipient* of the message. The service can be one of FB Messenger, Twitter, iMessage, a Slack server, or Discord. The recipient can either be an individual, a list of individuals, a group, a Slack channel, or a Discord server and channel.

There's also a sheet that lists aliases, so it's easy to use a short name or informal name to refer to a longer service or recipient; e.g. I use "@Audio Tools" as a shorthand for sending to a group of 5 people on Messenger all interested in audio tools for networked thought.

The Messager Queue sheet also displays the *Text* of the message to send, so you can easily clean up the message here for any typos or clarifications before it is sent.

The *Date* and *Time* columns allow for scheduling messages to be sent at any point in the future. Leave them blank and the message will be sent as soon as it is approved. Use keyboard shortcuts cmd-; (for date) and cmd-shift-; (for time) to quickly fill out these columns if desired.

Finally, the *Approval* column is the most important. Mark a messages as OK if you want it to be sent, or as Ignored if you deside to skip it. The *Status* column is updated automatically by Messager when the message is sent (or if it fails to send, then the error appears here). You can also mark the Status manually with whatever value you want (e.g. if you send the message manually), and the Messager system will ignore that message going forward. If you want the system to retry sending a message, simply clear out the Status column and it will try again.

I include this spreadsheet as a custom service in [Ferdi](https://getferdi.com/), so it lives alongside all the messaging apps I use. (This in itself might be the subject of a future [snippet](/snippets).)

### Why the approval system over immediate messages?

Beyond allowing me to catch a bunch of typos, it's also a psychologically useful thing for me.
I am more willing to write and I feel able to say more things that I might not otherwise,
knowing I have the opportunity to cancel or change the message later.
In that way, it's like gmail's undo feature. In gmail, undo not a true undo, but having those 30 seconds after clicking send to retract the message make a big difference.

Another benefit of sending the messages only after approving them is the ability to sleep at night. If I write a message at night, I know you haven't responded yet because my messages haven't even sent yet; they'll go out in the morning, after I've had a chance to clean them up. So, I don't spend any mental effort wondering if there's a response from you. It also allows me to set the appropriate tone for the messages, by having them go out at a reasonable time, rather than appearing urgent by being sent in the middle of the night. And it does this without me needing to keep the message draft in my head as I sleep. So, I sleep better.

This is why, while the ability to send messages immediately would also be a good feature to add, I am inclined to leave approve-in-the-morning messages as the system's default behavior.

### Notifications from Bieber Bot

One additional small usability feature is that Bieber Bot will message me in the morning or evening whenever there are messages in the Messager Queue awaiting my approval.

This sounds like a small convenience, and in fact has proven even more useful than it might at first sound.
When I wake up in the morning, I sometimes don't remember that I've written messages the preceding night.
So, having Bieber Bot send me the link to the Messager Queue and gently remind me to approve the messages has been
consistently charming and welcome. Thanks, Bieber Bot.


### Automatic Sending from Sheets with Messager

Messager is the underlying system that sends the messages in the Messager Queue system.
As noted previously, it supports 
Facebook Messenger, Twitter,
Slack, Discord, and iMessage.
It also supports Hacker News, which hasn't been so useful for this project.
And I am thinking I may add gChat and email support next.

I use Messager for more than just sending messages from the Messager Queue spreadsheet;
it also backs other projects like my [Kangaroo Auto-responder](/snippets/2021-01-30-sql-for-the-kangaroo-auto-responder/) and [several parts of Bieber Bot](/projects/bieber-bot/).
Its purpose, in the most broad sense, is to support programmatically sending and receiving messages in a uniform manner across all the messaging systems I use.

For Facebook Messager, it uses [fbchat](https://fbchat.readthedocs.io/en/stable/) to enable programmatically sending and receiving messages as myself. It also uses Facebook's API to allow sending messages as Bieber Bot.

For Twitter, it uses the API to support public tweets, private tweets (using a separate account; [see here for how I use this to reclaim my attention](/post/2021-03-07-roam-twitter-bot-dev-guide/)), and DMs.

For iMessage, it uses AppleScript.

Slack and Discord are the most recent additions, and they currently live outside the core Messager system;
they are implemented using Browserflow flows.
This means that I am effectively sending Slack and Discord messages as myself, rather than using an API to do so.
The messages are sent in a browser using clicks and keyboard presses,
all in the same human-centric UI that I would use if I were to send the messages manually.
I'm so grateful to Browserflow for making this possible, as Slack and Discord have been really key additions to this project.

### Reflections on the setup

I've been using the setup for only a few days so far, and am continuing to actively develop it.
So far, I absolutely love it.

The headless typing experience provided by Go Note Go makes for a great environment for drafting messages.
So too does using Roam Research while scrolling through social media. (I'm the sort of person who doesn't usually like replying publicly to social media posts, but does enjoy engaging with them in 1:1 or small group chat messages.)
Drifting off to sleep has proven to be another excellent time to share thoughts with friends.
I don't want to start _a conversation_ with friends as I drift off to sleep, but loads of thoughts come to mind that I do want to share with people, and so adding them to my Messager Queue to send the next day has been quite satisfying.

If this interests you, feel free to get in touch.
If you do, I'll do my best to get back to you, likely as I'm drifting off to sleep.
