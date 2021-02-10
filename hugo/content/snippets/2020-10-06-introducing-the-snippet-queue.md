+++
title = "Introducing the Snippet Queue"
date = 2020-10-06T22:16:00
tags = ["snippets", "taking-silly-ideas-seriously"]
+++

This is my first snippet published using my [snippet queue idea](/snippets/2020-10-06-further-reducing-the-publication-barrier-with-queuing/). If all goes well, it will be (read: was) published tomorrow evening (October 7, 2020).

The system works like this. I store a queue of snippets in Redis. Each snippet has the title, content, and date associated with it, as well as an id number. I can have Bieber Bot enqueue a new snippet by messaging him with "Queue snippet!" and the snippet details. He also responds to queries to update, view, or remove an existing snippet, or to view the current queue of snippets.

Then, every evening Bieber Bot looks at the oldest item in the queue. If he's already asked me about it, and I haven't told him not to publish it, he goes and publishes it to my website. If he hasn't asked me about it yet, he asks me if its OK to publish. As long as I don't say no and remove the snippet from the queue, Bieber Bot will go forward with publishing the snippet the next day.
