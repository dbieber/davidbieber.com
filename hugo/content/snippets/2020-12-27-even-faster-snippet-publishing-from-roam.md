+++
title = "Even Faster Snippet Publishing from Roam"
date = 2020-12-27T00:00:00
uid = "f3_BH6oAq"
tags = ["snippets", "roam-research"]

+++

I've set up a GitHub action to enable even faster automatic publishing of snippets from Roam. This is a test-snippet I'm using while writing the auto-publisher.

Let's see how it behaves if I'm editing an existing snippet routinely for a while.

If it works as intended, the snippet will update itself on GitHub after I stop typing for several seconds. I've now stopped typing, we'll see what happens.

It worked! [Here's the commit](https://github.com/dbieber/davidbieber.com/commit/1f1ad4680e1d538f699cf2cd420f0c04a4bf528a) that was made automatically after I finished the previous sentence.

This will make publishing snippets __even easier__ going forward. It also means I don't need to keep a puppeteer instance constantly live with Roam open like I'd originally planned for.

The total latency from writing to publication is now just 90 seconds. So you could be reading this mere minutes after I write it!
