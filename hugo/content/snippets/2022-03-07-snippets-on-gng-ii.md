+++
title = "Writing Another Snippet on Go Note Go"
date = 2022-03-07T01:00:00
tags = ["snippets", "go-note-go"]
+++

After thinking through [the tension between Go Note Go and snippets](/snippets/2022-03-06-gng-snippets-divide/) yesterday,
I now wonder if there's a good way to write a snippet draft on Go Note Go.
I've done so [once before](/snippets/2021-09-27-snippet-on-go-note-go/), when Go Note Go was only two weeks old, so I know it's possible. But five months later I've written many snippet-worthy ideas on Go Note Go, but no additional snippets, which leads me to ask "why?".

The first question I would need to answer is at what point during the writing of a snippet draft do I have to know that I'm writing a snippet draft. If I have to know upfront, that suggests one interface, whereas if I discover halfway into writing something that I think I'm writing a snippet draft, that suggests a different UX.

If I know upfront, I can create a new session (in the Roam uploader) using shift-enter, and then I can simply type the full snippet draft. That's what I'm doing now.

If, however, I discover midway into typing something that I'm typing a snippet draft, then it may begin in the middle of a session. This isn't such a big deal; when I clean up the draft I can remove the initial segment that isn't meant to be part of the snippet. The start of the snippet, when I didn't know I was writing a snippet, might be muddier than the rest, but that doesn't stand in the way of producing snippet-quality content.

In both cases, I'll want a way to indicate that I've written a snippet draft so that I can find it later.
(At this point in the snippet writing I encountered a bug -- notes that contained quotation marks were being dropped! I've now [fixed this bug](https://github.com/dbieber/GoNoteGo/pull/32), and am recreating the lost content from this snippet as follows.)

A simple option is to use a hashtag to indicate where a snippet draft lives. If I were working in Roam directly, I would use a two-word hashtag, "#[[Snippet draft]]". However, this is a mouthful to type on Go Note Go, which lacks autocomplete (how do you design an autocomplete experience suitable for a headless keyboard?), since getting all that syntax exactly correct is tricky (a hash _and_ double-brackets!).

If instead we adopt the hyphenated #snippet-draft then the double-brackets become unnecessary. Still simpler is the single word #draft. This seems the easiest to get right consistently if I'm going to be typing it in the dark while half asleep.

So, I think I'll adopt that convention for now, and revisit later as needed (it seems unlikely it will be needed.)

#draft

This system seems great for writing snippet drafts at GNG when I'm in a comfortable typing position, such as at a desk. There does seem to be something missing for when I'm drifting off to sleep though, as I often am when using GNG. I'm currently comfortably stationed at a desk, so I'll defer thinking through the sleep-GNG-usage snippet writing scenario until after I sleep on it some.

Having now completed this snippet draft, I'm going to head to a computer with a monitor in order to publish it.

(Hello from the computer-with-monitor! This snippet is headed for publication now!)
