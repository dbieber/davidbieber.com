+++
title = "Dealing with Giant Group Chats"
date = 2022-07-05T00:00:00
tags = ["messager", "machine-learning", "note-taking"]
+++

Sometimes -- usually because of Alex K Chen -- I am added to a giant group chat (GGC).
Today it was a 200+ person highly active chat with folks talking about AI programming tools, aging, and movies.
I love being added to such a chat. It makes me feel thought of, and my opinions respected. So, do keep adding me to GGCs.
However, with being added to a GGC comes some struggles. I haven't fully figured out how to handle a GGC just yet.

I think some people handle these situations in a more natural way than myself. Here's what I imagine. They're doing something else on the computer, messages are open in the background or in a side window. If they have a conversation-adjacent thought, they share it. If they see a message that looks interesting, they read it. Otherwise, they do their other activities and get on with their life.

> If they have a conversation-adjacent thought, they share it.

This part is Struggle #1.

> If they see a message that looks interesting, they read it.

This part is Struggle #2.

----

### Struggle #1: Sharing thoughts casually in a 200+ person setting

Why is this a struggle? I think slowly. I edit. I rethink relevance as the conversation moves away.
The hypothetical person who handles GCCs as described above "just" types and hits enter, relatively unencumbered.
I think about the permanence of putting something on the internet.
I think about confidentiality of work-adjacent stuff.
I think about whether what I'm saying is true, and about how true it is.
This kind of thought can make participation a challenge.

### Struggle #2: Staying abreast of 200 messages per hour

I don't want to read all these messages.
They glimmer and my attention is drawn to them, but that doesn't reflect my conscious decision making.
I'd much rather read a summary of the messages or a digest of the topics discussed once a week or so.
Then, only if a topic of interest was discussed, I might want to dive deeper and read the individual messages, and
contemplate leaving a reply.

----

### Tooling for Struggle #1

tl;dr Draft messages outside of conversation UI. Use "approve for dealyed send" model for sending messages.

Struggle #1 is a personal psychological struggle.
It isn't first and foremost something for which tooling seems relevant.
If I'm not comfortable sharing something with 200 people in a chat, why would tooling change that?
Well, as I've learned from adding [Messager in Go Note Go](/post/2022-01-08-new-messager-setup/) tooling can actually make a huge difference in this type of space.
If instead of feeling like I'm sending a message to a massive group, I instead feel like I'm writing a draft of my thoughts, something I'll maybe send later but maybe not, suddenly it becomes so much easier to write.
And then, once it's written, it also becomes much easier to send.
This is the same lesson I've learned over and over with snippets since I initially decided to set up this system as [writing for no audience](/snippets/2019-12-30-writing-for-no-audience/) back in 2019.

So, what would the tooling look like for dealing with Struggle #1 in GGCs?
I would click a message to start drafting a response,
it would copy the message and context into an editor -- Roam Research, say -- and maybe even stick in the template for writing a snippet.
Then, completely outside the context of the group thread I could compose my thoughts.
If I decide to share it back to the group, great.
If I decide to instead post that thought as a snippet, great.
And if it remains relegated to my notes forever and never sees the light of day, that's a fine outcome too. 

[Aside: The acceptability of that outcome is what makes the writing easier. The very possibility of that outcome diminishes the possibility of that outcome by making the other outcomes more likely. It's the opposite of a self-fulfilling prophecy. A self-fulfilling prophesy is an expectation whose existence leads to its own fulfillment; this is an expectation whose very existence works to prevent its fulfillment.]

One of the lessons I learned from my Go Note Go messager-queue was the value of the "approve for delayed send" model.
Psychologically it was easier for me to mark a message as approved for sending, and have an automated system later send the message on my behalf once it was approved, rather than directly sending it myself.
Marking something as approved for sending (1) admits the possibility that I make further revisions to the message, and (2) internally relieves myself of some of the responsibility of sending the message. Of course, I am still fully responsible for the message and I accept this responsibility, but nevertheless that perception of decreased responsibility is a relaxing feeling that makes message sending easier.
It also (3) prevents me from actively waiting for replies to come it, a behavior I'd like to avoid. It does this because my messages go out without my awareness in the moment, so I cannot sit refreshing or watching for new messages. This way I don't need to expend effort diverting my attention away from waiting for messages; my own unawareness has taken care of this for me.
So, having this "approve for delayed send" model for dealing with GGCs would be appreciated.

### Tooling for Struggle #2

Struggle #2 has psychological components, but is also more directly about capabilities.

The psychological bit:
Keeping up with 200 messages per hour isn't even desirable. Why? It's not that it's a lot of noise -- though sometimes there is a lot of noise.
But even when there's a lot of high quality interesting fun messages, it's not stuff I'm actively looking to read or learn about or people that I'm choosing to keep in touch with. Instead, it's whatever the group collectively has steered toward.
I'd rather be more intentional about what I read and discuss, rather than being at the whims of 200+ people, many of whom I haven't met.
However, there is tension between that desire for intentionality and the desire to hear folks' interesting ideas and share my own.
Adding to the tension further is a natural inclination toward reading messages as they come in, because they're attention-grabbing even if they aren't where I'd like to place my focus.

The capabilities bit:
Even if I decided I did want to stay abreast of the conversation, there's simply too much to reasonably process.
People are discussing topics about which I have a lot to learn.
I don't have the bandwidth to think deeply -- or even shallowly -- about what folks are saying, while also maintaining normal human functions.

So, what tooling can help?

Summarization:
A machine learning system that categorizes messages by topic would be super helpful.
It could send a weekly digest listing the topics discussed, and clicking on a topic could bring me to a summary of the messages, with the option to drill down into the individual messages.

Notification settings:
Right now I've simply turned off all notifications. If I could turn back on notifications for specific topics, that would be nice. E.g. "notify me if people start talking about programming tools again, but only if we haven't talked about programming tools in at least a day since the last time you notified me." This type of notification seems straightforward to build combining my Messager system with LLMs. Perhaps I'll give it a go.

Messenger UI: Even with notifications disabled, GGCs appear first in my list of Messenger chats because FB orders them by message recency, and GGCs always have a recent message. I'd prefer a way to keep them out of this default view, so I can see genuine conversations with individual people in their place.

Browsing UI: The existing UI is unhelpful for trying to get an overview of the conversation. There's a lot of whitespace, so only a few messages are visible at once. Replies for different topics are all mixed together.

---

If you're working on anything like the toolings mentioned here, don't hesitate to get in touch. There's a Discussions section below, or feel free to ping me in a GGC!
