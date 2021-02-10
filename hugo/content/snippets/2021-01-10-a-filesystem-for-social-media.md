+++
title = "A filesystem for social media"
date = 2021-01-10T00:00:00
uid = "N95z25MWk"
tags = ["taking-silly-ideas-seriously"]
+++

[Omar Riswan](https://omar.website/) has an excellent project called [TabFS](https://omar.website/tabfs/) that takes your browser tabs and exposes them to you as a filesystem. When you run `ls`, you see a list of all your open tabs. `rm` on a tab directory closes the tab. Inspecting the tab with standard tools (`ls`, `cat`, `rm`, etc) allow you to do things like reading the title or contents of the tab (yes, the whole tab's contents!), closing the tab, or running javascript in the tab. The whole thing is quite clever.

Inspired by TabFS, I envision another non-conventional filesystem: Social Media FS.

First you mount smfs and authenticate with your social media providers. Then if you `ls` the mounted directory, you can see each of the places you can read from and write to on social media.

There's a directory full of your chat threads. The timestamps indicate when they were created and when they were most recently modified. You can read the contents of the chat, or send a new message just as easily (and via the same tools) as you would write a file to disk.

There's a directory of all the Facebook posts made by all your friends and all the groups you follow. Each post has a file with its contents, and also one with all the comments and reactions to it. You can make a new post or add a new comment the same way you'd make a new file.

You can use standard tools for monitoring for new content. I like to use [Python's watchdog](https://pythonhosted.org/watchdog/) for this.

There's a directory for ads too, which you're welcome to peruse or delete as you see fit.

Reacting to a twitter post, sending a DM, receiving discord or slack or signal messages... all of these are organized as files and folders, and actions can be performed simply through file reads and writes.

I'd sure love to use a filesystem like this, and [Bieber Bot](/projects/bieber-bot/) would too.
