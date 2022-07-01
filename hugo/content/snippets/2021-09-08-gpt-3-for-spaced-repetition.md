+++
title = "GPT-3 for Spaced Repetition"
date = 2021-09-08T00:00:00
tags = ["spaced-repetition", "machine-learning", "browserflow"]
+++

Lately I've been using Browserflow to create spaced repetition flashcards quickly while browsing the internet.

To create a card, I highlight a bit of text and press "c". This copies the sentence containing the highlight into the card, with the part I highlighted masked out.
It's a cloze task, as in a masked language model.
If instead I push "b", it copies the full paragraph containing the highlight, again with the highlight masked out.

Usually this is a great way to quickly create my flashcards. However, sometimes I get sentences where the subject is unclear without context, e.g. "this" in "Usually this is a great way to quickly create the flashcards." For these, it would be great to automatically rewrite the sentence with the subject pulled in from the surrounding context.

For example, "Usually this is a great way to quickly create the flashcards" could be rewritten as "Usually <mark>using "b" and "c" with Browserflow</mark> is a great way to quickly create the flashcards."

As a second example, consider this [HyperPhysics page on the Murchison Meteorite](http://hyperphysics.phy-astr.gsu.edu/hbase/Solar/meteor.html#c3). Speaking about the Murchison Meteorite, the page says "Seventy four amino acids were found in it, compared to the 20 which are characteristic of life." I'd love to make a card saying "Seventy four <mark>amino acids</mark> were found in the Murchison Meteorite, compared to the 20 which are characteristic of life."

However, if I highlight <mark>amino acids</mark> and press "c", the generated card instead reads: "Seventy four <mark>amino acids</mark> were found in _it_, compared to the 20 which are characteristic of life."

So, the challenge I present you with is: write a program that takes a sentence, and it's surrounding context, and rewrites the sentence so that it is clear even out of context.

Having played with GPT-3 and Codex recently, this seems well within the scope of large pretrained language models. I expect that with some careful prompting, a large language model could excel at this task without even any fine-tuning, just taking advantage of few shot learning. Is this the best or simplest approach? Likely it isn't, but it may be the approach that minimizes development time and is easiest to repurpose for other similar (or dissimilar) projects in the future.
