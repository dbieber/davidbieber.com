+++
title = "Letting Adriana put things in my Leitner Box"
date = 2020-11-07T08:14:00
tags = ["roam-research", "spaced-repetition", "taking-silly-ideas-seriously"]
+++

I’ve been using spaced repetition for 2-3 weeks now. I’m not using Anki or any of the prebuilt systems that track your queue of items for you. Instead, I’m keeping the things I want to study in Roam Research and using a make-shift system of tags and Browserflow Flows to make the spaced repetition system relatively frictionless.

I’ll save the details of the system for another snippet. Today, I just want to jot down the idea of allowing Adriana (through the use of Bieber Bot) to add items to my spaced repetition system.

The idea is relatively simple, but it does involve one new component that may be tricky to implement robustly. Under this idea, Adriana would be able to send Bieber Bot a message saying e.g. “help David to learn the names of the planets” and a card would be added to my spaced repetition system saying “learn the names of the planets. -Adriana”. I could then split this card into multiple cards as I usually do when I encounter a card with too much content simultaneously, or Adriana could have Bieber Bot add smaller cards one at a time.

The new component that would be necessary is giving Bieber Bot edit access to my Roam Research database. Currently he has delayed read access through Roam-to-Git, but giving him write access might mean teaching him how to use Roam in a (headless, most likely) browser. Nothing he can’t handle, but it would increase the amount of time needed to get this system up and running.

Once Adriana (or any of Bieber Bot’s friends) can add cards into my spaced repetition system, this can be a fun way to learn about new topics and share new ideas.
