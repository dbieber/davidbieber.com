+++
title = "Ask Me Anywhere"
date = 2020-01-25T10:00:00
plugins_js = ["ask-me-anywhere", "margin-notes"]
tags = ["ask-me-anywhere", "snippets", "javascript"]
message = "In this post you can ask a question at _any_ point."
icon = "star"
+++

With this post, I'm demoing a new work-in-progress feature for my blog called "Ask Me Anywhere".
The feature lets you leave a comment or ask a question at _any_ point while reading my writing.
The goal is to encourage readers to respond to my writing, because I'm interested in having a conversation and hearing what you have to say.

You can try it right now. Either **double click** (double-tap on mobile) on any paragraph, or click between two paragraphs, to open a comment box. Enter your thoughts, click submit, and _voila!_, comment submitted.

You're welcome to enter your email address, name, Twitter handle, Facebook ID, or any other form of contact info if you'd like me to respond. And if you do, there is high likelihood that I will respond. If you don't, you're anonymous, and you certainly won't receive a private response.

Comments and questions that you submit are not posted publicly anywhere. This isn't a comments section for public discussion. If you want to discuss my posts publicly, submit them on Hacker News or Reddit, or head to Twitter to engage. While this website isn't the place for public discussions[^1], I am curious to know about such a discussion if it's happening. So, feel free to let me know about such a discussion via "AMA" if you're starting one.

[^1]: Update (Dec 2022): You can now also use the Discussion feature! Ever since [this snippet](/snippets/2022-06-21-using-discord/) there are now public discussions directly on my website. Give it a try today!

What happens when you leave a comment? This part's still a work in progress, but ideally my digital personal assistant [Bieber Bot](/projects/bieber-bot) will notify me of the new comment at the next convenient time. If there are many comments coming in, Bieber Bot will try to be smart about batching the notifications together, and so the notification may be delayed, but I'll soon read your message.

For now, Ask Me Anywhere is only activated for this one post. Once I've tested it out a bit, and perhaps made some changes, I'm hoping to then activate it for the [rest of my posts](/posts) [and snippets](/snippets) as well. So I'm particularly keen to get feedback early so I can iterate and improve it soon. Give it a try, let me know what you think. You know how to reach me!

If you're interested in learning more about the internals, the source is [available on GitHub](https://github.com/dbieber/davidbieber.com/blob/772b5dd87da532357a1cdf04a8caa027268bfbac/hugo/assets/js-src/ask-me-anywhere.jsx). Feel free to have a poke around.

The name of the project -- "Ask Me Anywhere" -- reflects my intention to enable readers to ask questions as they're reading. However, I welcome all types of reactions: questions, comments, feedback, corrections, new ideas, etc. I look forward to hearing what you have to say.
