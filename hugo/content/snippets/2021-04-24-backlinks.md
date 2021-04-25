+++
title = "What links here?"
date = 2021-04-24T00:00:00
tags = ['snippets', 'roam-research', 'tech-tips']
keywords = ['backlinks']
+++

I wanted to write about backlinks today but didn't get a chance (except you're reading it, so of course I _did_ get a chance in the end).

Quick outline of what I was hoping to write about:

- Backlinks appear in Roam Research
- I have a BrowserFlow flow that uses Google search to produce backlinks for any website
- And I saw that either some of Gwern's writing or Less Wrong includes a "What links here?" section (it wasn't clear to me which of Gwern or LessWrong was providing this functionality)

A backlink on a page X is an indication of what other content links to X. Seeing a list of backlinks can be mildly interesting, and I was curious to see what pages link to my own writing.

I have some visibility into this through a couple different mechanisms. This website uses Google Analytics, so I can see where traffic comes from. This provides a decent view into what other websites are linking to my content. I can also see how traffic flows through my own site, which gives a limited view of the links between snippets.

The second mechanism I can use to see what links to a snippet is Google Search's exact match feature. Searching for a [complete URL in quotes, optionally with "-site:urlgoeshereagain" in the query to remove links from the same domain,](https://www.google.com/search?q=%22https://davidbieber.com/snippets/%22+-site:https://davidbieber.com/snippets/&filter=0&biw=1648&bih=946) will show you what websites link to the page of interest. For example, the query ["davidbieber.com/post/2019-12-29-track-your-life-in-a-spreadsheet/" -site:davidbieber.com](https://www.google.com/search?q=%22davidbieber.com/post/2019-12-29-track-your-life-in-a-spreadsheet/%22+-site:davidbieber.com&filter=0&biw=1648&bih=946) shows links to [my Track Your Life in a Spreadsheet blog post](/post/2019-12-29-track-your-life-in-a-spreadsheet/).

I was toying with the idea of adding some curated backlinks to snippets. Each snippet would show what other snippets reference it, as well as selected pages from around the web that reference it. Of course, there aren't really pages around the web that reference my snippets, so this idea is moot at the moment.
