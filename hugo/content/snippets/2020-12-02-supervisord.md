+++
title = "Supervisord"
date = 2020-12-02T00:00:00
+++

Supervisord has been the single best quality-of-life improvement for software development for me in 2020.

Many thanks to [Vik Bhandari](https://vikb.com/) for suggesting that I use it.

What is supervisord? It's a "process control system," meaning that it's software that starts, stops, and monitors other software that you want to run. 

Here's an example. Let's say you have a program `check_for_sales` that periodically pings Amazon looking for sales on that new shoe-phone you've had your eye on. When it notices a drop in prices, it sends you a text.

Without supervisord, you might start the program, and find the next day that it has hit an error (maybe one of the requests to Amazon timed out in a way you weren't anticipating), the program terminated, and the item sold out while you weren't looking!

With supervisord, you can have `check_for_sales` automatically restart on failure. Supervisord will notice the failure, and restart the program for you.

I've been using supervisord for all sorts of things, like monitoring Bieber Bot for new messages, keeping my website's development server live, automatically posting snippets from Roam (like this one), and auto-processing screenshots and screen recordings that I take. I have 15 processes monitored by supervisord in total across a number of side projects.

Before supervisord, I had half the number of processes always-on in the background on my computer. I would keep extra terminal windows open to keep them running. And restarting my computer was a pain because I had to bring up these processes one at a time.

Now, with supervisord, restarting my machine is no big deal. This let's me use my computer more freely, and I feel much less hesitation in starting a new project that requires having an always-on process.

You can learn more about supervisord from their website [supervisord.org](http://supervisord.org/).
