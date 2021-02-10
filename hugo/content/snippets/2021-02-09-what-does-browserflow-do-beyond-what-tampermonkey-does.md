+++
title = "What does Browserflow do beyond what Tampermonkey does?"
date = 2021-02-09T00:00:00
uid = "o0d9MAbGW"
plugins_js = ["margin-notes"]
tags = ["Browserflow"]
+++

Someone recently asked me what [DK](https://dkthehuman.com/)'s [Browserflow](http://browserflow.app/) does beyond what e.g. [Tampermonkey](https://www.tampermonkey.net/) provides. Here's my answer.[^1]

[^1]: My experience with Tampermonkey is limited, so take this with some salt.

1. _**Way**_ easier to use both for programmers and non-programmers

2. Allows recording macros or writing them as "flows"/programs

3. Everything (okay, maybe not _everything_) "just works" -- e.g. if you want to write a for loop over tweets on Twitter, you just do. No need to deal with handling scrolling, or with race conditions about when dom elements appear and disappear, or if twitter decides to reuse dom elements, etc. Browserflow takes care of those details.

4. Provides high level commands like taking screenshots of elements, writing to csv, selecting parts of a page, looping over elements, getting input from the user, etc.

5. Easy to share flows with other users! Unfortunately there's like ~2 other users right now 😛 

6. The typeahead for running flows is super convenient. cmd-J then type a piece of the flow name, then hit enter. The flow runs.

---

Really it's (3) that sets it apart. The attention to detail in the product is impressive. Thanks DK.
