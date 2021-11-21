+++
title = "Save my spot! Finer-grained bookmarks for incremental reading"
date = 2021-11-20T01:00:00
tags = ["browserflow", "note-taking"]
keywords = ["incremental reading", "bookmarks"]
+++

When I find articles on the web, often I only read a small portion of an article before browsing away.
Instead of giving up on the article, I would like to leave a little visual marker on the page indicating the part of the page that I reached.
I'd then also like to automatically add a link to this marker to my notes.
So, if I'm ever reviewing my notes, I'll be able to jump right back into the article where I left off.

If I later continue reading the article, I'd like to move the marker to whatever spot I reach. (It's OK if the old links keep linking to the old location, but I want a new link to whatever spot I've reached.)

I think this should be possible to build with Browserflow. Let's consider how.
I think I would do this with two flows, one to save my spot on a page (and add it to my notes),
and a second flow to restore to that spot on the page from the link in my notes.

The biggest decision is how to represent a spot on a page. One option is the scroll position. Another option would be to remember a unique element id. Both approaches have drawbacks. Using scroll position doesn't work well with dynamic content. Element ids aren't guaranteed to be unique. I am leaning toward the scroll position approach to start, and then I'll see how fragile it is. Even though it isn't perfect, it will work in most situations.

When I run the first flow, it will grab the URL of the current page and the current scroll position, and it will write that into my notes. This requires changing tabs, which is easy to do with Browserflow, but not easy to do with a standard JavaScript script. That flow will be run on the website where I am reading the article.

The other flow will be run while I'm reading my notes. It would be great if just clicking on a link in my notes could trigger this flow and take me to the correct spot in the article, but this isn't possible (by default) with Browserflow today. One way to work around this limitation of Browserflow is to write an always-on flow that listens for when I've clicked the link. Unfortunately, always-on flows are not great with Browserflow's pricing plans.

When I run the flow to restore my spot in an old article, the flow will first open a new tab to that article's webpage. Then it will scroll to the specified position. When the flow starts, it will first need a way to determine which of the links on the notes page to follow. With the current version of Browserflow that I have (0.72 I think), you can just click on the link to specify this. This option is removed unfortunately in the latest version of Browserflow. Instead, we can probably use a clever selector to select the user-selected link. This should work in later Browserflow versions.

Once these two flows are implemented, saving and loading my point in an article to and from my notes will become much easier. The next improvement will be adding in a bit of visual flourish (e.g. a visual marker in the article to draw my eye to where I left off). Certainly a smoother UX is feasible than the one I've planned here, but I think this Browserflow prototype hits a sweet spot of quality-to-effort ratio, and will be a satisfying prototype to build and use for myself.
