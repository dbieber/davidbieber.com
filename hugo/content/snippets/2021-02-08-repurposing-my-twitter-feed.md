+++
title = "Repurposing my Twitter Feed"
date = 2021-02-08T00:00:00
uid = "exyLoYHb7"

+++

Twitter's addicting. It's not a good use of my time, but I scroll there anyway. If I'm going to be scrolling there anyway, might as well make it worthwhile. So, I've decided to repurpose my Twitter timeline and inject things I actually care about into it.

How? You might think to do this with a Chrome extension, injecting content in between the existing tweets. There's an easier way though. I've made a new, private Twitter account, and I programmatically tweet as that.

My personal Twitter account is @Bieber, and I use a picture of myself for the profile. The new account goes by "Private Bieber", and uses a deep dream-ified version of my profile picture.

How does it decide what to tweet? It chooses tweets from my Roam Research database. I already frequently write down things I'd like to learn about, and ideas I'd like to try in Roam. It's where I keep my snippet ideas, my spaced repetition system, and my "Fleeting TODOs".

Fleeting TODOs are what I call TODO items that tug at my brain in the moment, eager to take my attention away from the task at hand. Rather than do them then, I write them down. I only ever get around to doing a small fraction of my fleeting TODOs, but its nice to have a record of them. It makes it easier to notice if I keep coming back to the same idea, in which case maybe it's worth actually pursuing.

So, I have a script that occasionally -- currently every 10 minutes -- picks out one of these items from my Roam Research database and tweets it in a way that's only visible to me.

Since I have my Twitter feed configured to show me tweets chronologically, this means there's always a tweet from Private Bieber sitting at the top, to remind me of something _I_ care about, rather than something the _Twitter algorithm_ has picked out for me to care about.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fplayground%2FxD83QrK9_D.png?alt=media&token=76f275ac-62fd-4844-829c-b44cf9cf568f)

Currently the tweet selection is random, but already in this first 20 minutes I've been happy with the tweets it's been writing. Perhaps in a future iteration I'll make some adjustments to what it tweets and when. It's nice to have this kind of control over my attention, especially in a setting like Twitter where I'm so used to mindless scrolling.

This same technique ought to work fine for taking control of my Facebook feed too, so perhaps I'll get Private Bieber an account there next.
