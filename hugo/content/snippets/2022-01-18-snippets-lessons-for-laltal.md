+++
title = "Applying Lessons from Snippets to LaLTaL"
date = 2022-01-18T01:00:00
tags = ["snippets"]
+++

[LaLTal -- short for "learn a little, teach a little"](https://www.laltal.com/)
is a novel learning app from John Cumbers
built on the extraordinary power of learning by teaching.
I tried it out tonight, and I had a great time learning a bit about blockchain and synthetic biology.
I really appreciated the opportunity to practice explaining the concepts that came up in the questions. Coming up with these explanations on the spot felt like exercising an underutilized muscle. I think I'll be doing more of this.

One thing I think could really improve the experience further though
would be if recording was decoupled from production.
The simplest way of doing this would be a "draft record" button,
and a more interesting way would be a more sophisticated but still simple audio editor, an idea I'll detail later on in this snippet.
The core of my suggestion isn't about the difference in _functionality_ between a potential "draft record" feature and the current "record" feature.
Instead, it's about the mindset that the UI induces.

Consider [snippets](/snippets/).
When I write these snippets, [I write them for no audience](/snippets/2019-12-30-writing-for-no-audience/).
I don't expect to share them, or for people to read them,
  and that makes them easier to write.

This snippet is an exception; I fully expect to share it with a few people once it's written. Maybe. There's still a piece of my mind that knows that it might just be an ordinary snippet, never shared. And certainly it won't share widely or automatically when it's published. I can put it on my website without anyone ever seeing it, at which point deciding to share it becomes a much lighter weight action than a single decision to both _write and share it_ would have been.

The lesson I've learned from writing snippets is that it's easier to produce content when you're not doing it for anyone, or with any intention to share it.
Of course, I don't know how true this is for everyone, but I suspect that since it is true for me, it applies to some reasonably sized portion of the population.

This lesson from writing snippets can be applied to LaLTaL too.
If the app put people in a mindset where they felt like they weren't recording a final explanation to be shared,
but rather were trying on the words for size,
I think people could reach a point where they understand the material better and are more capable of sharing it.
They might even produce something they want to share even if they didn't start the recording intending for it to be the version for sharing; I know that's happened to me in writing snippets loads of times.

Listening to other people's explanations in the app
  left me with a couple of observations -- possible shortcomings in people's answers that I think setting the right mindset or environment might be able to overcome.

1) People move quickly over complicated parts to keep their explanation short.

    I saw this multiple times in people's explanations of blockchain-related concepts.
    When people got to the part of the explanation about cryptographic hash functions,
    instead of recognizing the limitation in either their explanation or their understanding, they swept it under the rug in order to keep the explanation fluid and "appropriate" in length. I think the current record-once setup leaves people averse to grappling with complexity.

    If people felt like a long pause to think right in the middle of their explanation were OK, they maybe they wouldn't exhibit this sweeping-under-the-rug behavior.

2) People speak slowly to buy themselves time to think, rather than pausing to think or thinking ahead of time.

    It reminds me a bit of [Charlie Brown's "The Book Report"](https://www.youtube.com/watch?v=0cA9j2EpAHE).

    > The name of the book about which,
    > this book report is about is,
    > Peter Rabbit which is about this...
    > Rabbit.

    Now, as someone answering the questions, there's nothing wrong with this!
    It's a great way to feel your way toward a good answer. During the slow explanation, your brain is hard at work piecing together what you'll say next.
    Still, I think it's important to recognize that this is happening and that there might be a UX that leads to a better experience for both answerer and listener.

    If people felt like they could record in multiple pieces, pause as long as they like to think, and throw out individual pieces,
    perhaps they would produce even better explanations.

3) People trail off with uncertainty and apprehension

    This happened in several of the explanations I listened to.
    The speaker is explaining something, it's going well, and then they realize they're either about to repeat themself or have nothing more to add.
    So, they trail off, their voice weakens a little, and they remark that they're done.

    If instead people were recording for themselves,
    hearing themselves think through the various aspects of their answer,
    and then at the end piecing together the parts of their own musings that they like,
    it would avoid these tenuous endings.

----

All of this leads me to brainstorm possible user interface ideas.
Know that the purpose of this snippet is not to advocate for any single idea,
but rather simply to share my thinking.
My aim is for these ideas to inspire further ones, not for these ideas to win out.

##### Version 1: Multiple recordings
(This is simpler to implement, but I imagine less effective, than Version 2.)
The idea here is you can record multiple recordings -- as many as you like -- and then you can rearrange them or delete them.
With this UX, already an answerer can comfortably pause their recording if they feel they've reached a part of the explanation that their stumbling over. They can gather their thoughts, then proceed.

##### Version 2: A single multi-piece recording.
(This UX could be simpler for the user, but is more technically ambitious.)
When you start recording,
  the screen begins filling up with your recording.
Each time you pause speaking for more than two seconds,
  a boundary appears in your recording.
The boundaries effectively divide time into distinct clips.
Silence is stripped from the beginning and end of each clip automatically.
As in Version 1 of the idea, the answerer has the opportunity to rearrange or delete clips by tapping and dragging them.

---

There's a tension between these UX ideas and another important aspect of getting people to publish, that must be carefully balanced.
If people have opportunities to critique their own work, and polish it, they may be reluctant to publish because the mental quality bar they set for themselves could be too high.
This has been another critical lesson from snippets -- making the quality bar to publication as low as possible has been essential for me feeling comfortable writing and publishing my snippets.
Editing tools push the quality bar higher, and so the UX ideas I present above might have opposite the desired effect.

With this in mind, I present a third version of the UX, one that balances the desire to let people pause and think with the goal of keeping people feeling comfortable publishing rather than falling into a perfection-trap.

---

##### Version 3: One recording with a "Pause" feature

In this final variant of the idea, the user pushes to record,
  but they can pause and resume their recording at any time.
Simply by letting people pause, perhaps we can give people the freedom to think before they speak when they encounter a tough concept unexpectedly during their explanation.
At the same time, this keeps the recording UX simple, so hopefully it avoids the potential pitfall of having people avoid clicking submit because they have reached the perfect recording yet.

Hopefully the result is explanations that are both cogent, fun to produce, and plentiful.
