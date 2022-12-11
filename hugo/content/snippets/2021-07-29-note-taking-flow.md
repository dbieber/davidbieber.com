+++
title = "Browserflow Note-taking Flow"
date = 2021-07-29T00:00:00
tags = ["browserflow", "note-taking", "roam-research", "spaced-repetition"]
icon = "star"
+++

Quick update on the note-taking Browserflow flow I've been building: [https://browserflow.app/shared/51b5b7af-3124-4989-9771-36e9f236e1e7](https://browserflow.app/shared/51b5b7af-3124-4989-9771-36e9f236e1e7):

## How it works

When you run it, it injects some js into the page you're viewing enabling a handful of keyboard shortcuts to enable clipping text into Roam from anywhere on the web.

If you navigate to a new page, it will run that js on the new page. So it keeps the keyboard shortcuts active even if you follow links.

It also removes the status overlay, so you can interact with the page more easily.

## The keyboard shortcuts currently are:
- `enter`: saves the current selection as a note to Roam
- `q, !, @, *, >`: saves the current selection as a note to Roam tagged as a {question, "Wow", Share, key idea, or block quote} (I don't really use these)
- `p`: saves the paragraph containing the selection to Roam, with the selection highlighted
- `s`: Asks for an element in browserflow. Saves a screenshot of the element to Roam. Doesn't work. (hmm... why not?)
- `h`: saves the sentence containing the selection to Roam, with the selection highlighted
- `c`: saves the sentence containing the selection to Roam as a "cloze" (fill-in-the-blank) task for spaced repetition, with the selection as the fill-in-the-blank
- `b`: (big cloze) saves the paragraph containing the selection to Roam as a "cloze" (fill-in-the-blank) task for spaced repetition, with the selection as the fill-in-the-blank
- `.`: quit (I use this to reenable keyboard shortcuts for tab switching)

## Some feature requests / debug things
- Would be nice to keep some status indicator, just in the corner or page title instead of blocking the full page.
- It depends on a couple other flows. Would be nice to be able to share just a single link.
- It switches to the roamresearch.com tab and back whenever you save a note. Would be nice if this worked even if roam were in a different window. The user shouldn't have to care about exactly where roam is open.
- Why doesn't the element screenshotting work?
- Would be nice to allow tab switching in a flow without having to quit the flow.
- For a note-taking flow like this, it can easily be running for hours. Doesn't mix super well with the free tier of billing.
- A few of these could be solved with an "Enable interaction with page" action

## The dependency flows needed to check it out are:
- https://browserflow.app/shared/ba6eb2f0-a3d1-4bc3-9f21-5ca18af0b247
- https://browserflow.app/shared/486ef3eb-8d2b-48bf-8fee-22963dc74b88
- https://browserflow.app/shared/8e066128-2f87-468f-842f-3f006f0a2e71

To try out the flow, you'll need Browserflow, an open Roam tab, and all four flows linked in this snippet. Run the first flow ("Roam: Highlights") on a web page (with Roam open in a different tab in the same window). Highlight some text, (say, the words "some text" in this sentence), and hit enter. You can try any of the shortcuts listed above. Notice as the flow copies your selection into your daily notes organized by time and website.
