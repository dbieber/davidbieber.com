+++
title = "Improving Roam Snippet Publishing Speeds"
date = 2020-12-23T00:00:00

+++

Hey folks, I have a [workflow](https://davidbieber.com/projects/bieber-bot/) for automatically publishing "[snippets](https://davidbieber.com/snippets/2019-12-30-writing-for-no-audience/)" to my website from Roam. Currently there's a multi-hour latency between writing a snippet and when it appears on my website. In this thread (click 'N replies'!) I'm going to muse about / ask questions about how to use **puppeteer** to bring this latency down considerably. This'll be my first time using puppeteer, so help appreciated. Read on!

![:open_mouth:](https://a.slack-edge.com/production-standard-emoji-assets/10.2/apple-small/1f62e@2x.png)

The current system relies on my git-to-roam backup, which runs every hour and fails some fraction of the time.

So, to bring the latency down, the idea is to use pyppeteer (the python puppeteer bindings) to log into Roam in a headless browser.

This will monitor Roam for new (or modified) snippets, and will publish them to my website.

A snippet is OK to publish if its tagged with both "Snippets" and "ok-to-publish".

So, first question: has anyone done this before? B/c if someone's already gotten all the CSS/XPATH selectors for logging in, navigating, etc, that could save me some time

Another important thing I'm thinking about: are there problems keeping an instance of Roam open in a headless browser could cause?

E.g. I hear about occasional data loss which seems related to having out-of-date instances of Roam open on other machines -- e.g. maybe the out of date Roam comes back online and overwrites new content with older blank content?

I think I'll make my headless Roam instances relatively-short lived (<10 minutes) just in case.

I think the strategy I'll take will be:

- Log in to Roam in headless browser
- Run datalog query in javascript to check for new/updated snippets.
- Run that query fairly frequently (e.g. every few seconds) in order to detect snippets as soon as they're available
- Debounce, so that if a snippet is actively changing its only deployed ~twice, not 100 times

And then every 10 minutes or so I'll have it take a short breather and refresh

Abhay suggested using the alpha API for this rather than puppeteering. ![:pray:](https://a.slack-edge.com/production-standard-emoji-assets/10.2/apple-medium/1f64f@2x.png)

I think I'll get started on the puppeteer implementation now though anyway, even if the API ends up being a better way of doing this in the near future.

Update:

I have a first draft that handles log in and running the query to detect publishable material (blocks with the appropriate two tags)

Not sure how reliable login is as I had some hiccups getting it working.

And the headless browser seems very slow to notice changes to the Roam graph compared to what I'm used to.

So instead of checking every few seconds, I think I'll just check once a minute or so, refreshing either every time or every few times.

Unexpected snag: I get the children of a block but I don't know how to put them in the proper order!

(with datalog)

I could navigate to the block and look at the dom... but hopefully I don't need to do that.

Looks like there is an "order" attribute, so this will be doable. Might be messy though.

If I'm understanding right, :block/order gives the index of a block into its parents children

We're good ![:thumbsup:](https://a.slack-edge.com/production-standard-emoji-assets/10.2/apple-medium/1f44d@2x.png)
