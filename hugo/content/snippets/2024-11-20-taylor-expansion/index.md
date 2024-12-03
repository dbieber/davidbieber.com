+++
title = "How Good are Taylor Series?"
date = 2024-11-20T01:00:00
tags = []
keywords = []
plugins_js = ["2024-11-20-taylor-expansion.bundle"]
+++

Let's use Claude to look at how good an approximation a Taylor series expansion is for sin(x).
After a bit of back and forth, it has produced these plots for us, and we can immediately see
that the "good region" is growing linearly as we add additional terms to the Taylor series.
This initially feels  surprising, like each additional term is somehow more powerful than I would expect in its ability to correct the distant errors while leaving the inner region relatively unchanged.

The increment in the size of the good region seems to be about .72, and seems quite similar (after an initial step or two) regardless of the accuracy bound we use.

<div id="root"></div>

Reflections on the process: This was such a delightful way to explore the Taylor series!
It allowed me to follow my curiosity pretty freely, probing properties that came up along the way on a whim, to develop an intuition for how these mathematical objects worked. I didn't realize the "trust region" was going to grow so smoothly like this, so it felt rewarding seeing this elegant property pop out of my explorations.
This was also an early test of embedding Claude Artifacts on my website. It was pretty smooth!
