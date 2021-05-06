+++
title = "Lighthouse"
date = 2021-05-03T00:00:00
+++

[web.dev](https://web.dev/measure/) (former known as Lighthouse) is a tool for measuring your website's performance and getting tips for how to improve it. I'm in the process of following some of its suggestions right now.

*Working session...*

Progress so far:

One of web.dev's suggestions was to enable gzip compression of the pages on my website.

Tornado supports this, but only starting at version 4.0 and newer. I'm on an older version. So, I'd like to upgrade tornado.

I try to install a newer version of tornado with pip, but I cannot. I receive an InsecurePlatformWarning when I try to do so. I can upgrade to a newer version of Python to solve this, it says.

I try to install Python 3 with apt-get, but I cannot. dpkg encounters an error during the apt-get install.

Why? I'll figure that out next time.
