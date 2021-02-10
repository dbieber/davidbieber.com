+++
title = "Extracting Snippets from Roam Research"
date = 2020-11-03T15:22:00
tags = ["snippets", "roam-research"]
+++

I've been writing a lot these days inside of Roam Research. I wonder if there's a good way to identify snippet-quality items from within my Roam database.

One option would be to pick out decent-sized sections of continuous text.
If I'm taking notes in a bunch of different areas, that's probably not well suited for publishing as a snippet unless I were to clean it up first.
But if I see there's a large chunk of text that's been added in a contiguous block, there's a decent chance that its snippet-quality.
"Snippet-quality" isn't a particularly high bar. The bar is really just that we'd want text that forms a coherent thought rather than being a few lines on totally unrelated thoughts (which can also appear contiguously in Roam).

A few days ago I set up Roam-to-Git, so every hour my Roam database is backed up to a private GitHub repository. It would be easy enough to look through the git diffs to see if there's something that fits this description.
One possible issue with this though is that the backup script doesn't know if I'm in the middle of writing. So it's possible it will catch me mid-snippet.
Perhaps if I look at the diff between head and two commits back, I can avoid missing snippets that got split over multiple commits. It's an idea worth looking in to, though the number of false positives might be too high without a fair amount of tuning.
