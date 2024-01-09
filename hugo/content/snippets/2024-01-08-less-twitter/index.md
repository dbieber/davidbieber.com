+++
title = "Less Twitter. Less Facebook. Less HackerNews."
date = 2024-01-08T00:00:00
tags = ["attention", "aspirational-intent", "javascript"]
keywords = ["chrome"]
+++

Over the years I've accumulated [dozens of strategies](/snippets/2022-03-18-attention-strategies/) for managing my attention, including amazing Chrome extensions from Namu like [Intention](https://chrome.google.com/webstore/detail/intention-stop-mindless-b/dladanhaondcgpahgiflodhckhoeohoe) and [Hide feed](https://www.hidefeed.com/). Nevertheless, I continue to get sucked into the Internet's [six infinite distractions](/snippets/2020-10-01-infinite-distractions-and-getting-a-good-sear/).

So today (well, yesterday really), I'm taking matters into my own hands, and building some Chrome extensions to help me manage these distractions on my own terms.

**Twitter and Facebook.** I've noticed that when I'm scrolling on Twitter or Facebook, and I want to stop, I sometimes find it difficult because _"just one more post"_ or _"that looks interesting"_. That is, I'll see a half-visible post at the bottom of my screen, and I'll tell myself I'll just look at that one post, and then I'll be done. But by the time I've looked at that post, a different post is now half-visible, and it's captured my attention as well.

So, my proposal is: I'll only make posts visible once they are fully on the screen. No more half-visible Tweets. No more half-visible Facebook posts.

Turns out making such a Chrome extension is remarkably easy, especially with language models available to assist with the boilerplate. Let me show you some before and after photos... actually, just the after; I don't want to get any practice disabling this thing!

![I am scrolling on Twitter. Posts only appear once they are fully visible in the browser's view port.](/snippets/2024-01-08-less-twitter/less-twitter.gif)

As you can see in the gif, I am scrolling on Twitter, and posts only appear once they are fully visible in the browser's view port.

It's not perfect; I still will scroll just to bring something closer to my eye level, which can cause additional posts to appear. But I think it's a big improvement on the default. Only time will tell.

My hope is that by not having partially visible posts at the bottom of the screen, it will be less addicting, and easier to get off the site.

I did the same for Facebook. For HackerNews, I took a different tact.

**HackerNews.** On HackerNews, my obvervation is that I will sometimes continue digging, 5+ pages into HackerNews, looking for something interesting. This is silly; I don't need five pages of HackerNews content. If I don't satisfy my itch for news in thirty articles, 120 articles isn't likely to do any better. But I don't want to be heavy handed; blocking the site or removing the more button might simply cause me to learn workarounds for my blocker. For a gentler touch, I'm going to change the More link to link back to the first page. My habit is to click the more link, so I'm going to tab into that habit to help break it, gently. We'll see how this goes.

Going to post this snippet as is so I can get it out and get some sleep. But I intend on releasing the Chrome extensions too. Each one is just a small amount of JavaScript, trivial to create but hopefully significant in impact. There are three in total, called Less Twitter, Less Facebook, and Less HackerNews respectively.

Finally, I'll also note Kudos / Gratitude to Unhook for making a YouTube-management Chrome extension that I've started using as well.

Good browsing and good night!
