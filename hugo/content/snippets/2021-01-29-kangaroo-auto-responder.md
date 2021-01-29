+++
title = "Kangaroo Auto-responder"
date = 2021-01-29T00:00:00
uid = "uTT1gaOcQ"
plugins_js = ["margin-notes"]
+++

 The purpose of the Kangaroo Auto-responder is to:

1. Avoid people expecting a response from me when I don't realize they're expecting a response, e.g. because I've forgotten about their message
2. It should let me let my guard down a bit about feeling obligated to respond to people

What will it do?

It will automatically respond to messages that I've seen but haven't responded to for 2+ hours with a kangaroo[^1].

[^1]: With a picture of a kangaroo, that is. Like this one: 🦘 , or this: ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fplayground%2FtBz98tV75N.png?alt=media&token=66762cac-d0b0-43ba-91a8-eaefa6ef7626). It will not send them an actual real-life kangaroo.

The first time it sends someone a kangaroo, it will also explain:

"[Kangaroo] Hello! This is an automated reply from the Kangaroo Auto-responder. You're getting this message because it looks like David might forget to reply to your message. If you want a response, you should contact him again. (Just saying "ping" is often enough!)"

Text for the second time:

"[Kangaroo] Me again. David might forget to reply to your message. In the future I'll just send you a picture of a Kangaroo to symbolize this. 🦘  If you ever get a picture of a Kangaroo from me, it just means David may have dropped the ball on your message and you should contact him again if you're expecting a response."

Subsequent kangaroos will be unaccompanied by explanations.

The details on exactly when to send kangaroos are still a work in progress. I don't want to overwhelm anyone with kangaroos. I'm thinking about some rules: (1) only send kangaroos if there was a message of non-trivial length, e.g. more than 20 characters, (2) only send a kangaroo after I've read the message; if I genuinely haven't seen the message yet, no need for a kangaroo, as the message will still appear as unread in my inbox, (3) if you send follow-up messages, that resets the timer on the 2 hours, (4) any messages you send within 5 minutes of me sending you a message are ineligible for triggering kangaroos (this way I don't need to get the last word), and (5) obviously, don't send a kangaroo for a message I've already responded too.

To summarize, the rules of kangaroos are: You get a kangaroo if the **most-recent** message in our chat is **non-trivial**, **read-by-me**, **written-by-you**, **not an immediate reply**, and **two-hours old**.

Why kangaroos? They bounce 🤷‍♂️ ? This is kind of like a message bouncing...
