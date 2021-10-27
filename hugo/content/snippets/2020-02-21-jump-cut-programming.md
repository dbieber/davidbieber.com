+++
title = "Jump-Cut Programming: Take 1"
date = 2020-02-21T00:00:00
tags = ["automatic-video-editing", "python-fire", "python"]
message = "Inspired by @realCarykh, I jump-cut into the world of automatic video editing."
+++

I've been toying around with recording myself programming. Here's a clip.

<iframe width="560" height="315" src="https://www.youtube.com/embed/OxsuHWVtMSM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In this clip I use [Python Fire](/projects/python-fire) to create a simple two-function calculator. Nothing special about that.

What is special is that the programming has automatically been sped up by [carykh/jumpcutter](https://github.com/carykh/jumpcutter), and that I've used [moviepy](https://zulko.github.io/moviepy/) to set the programming to the music ["Dangerous"](http://incompetech.com/music/royalty-free/index.html?isrc=USUAN1100414), a clip I got from [YouTube's free Audio Library](https://www.youtube.com/audiolibrary/music).

## Lessons Learned from "Take 1"

### What worked well?

1. **External Monitor**: I purchased an external monitor. This made a huge difference. Now I can manage video-editing tools, a terminal, a browser, etc on one screen, while keeping the contents of the video (the editor and public terminal) on the other screen and recording it.

2. **[carykh/jumpcutter](https://github.com/carykh/jumpcutter)**: This tool can automatically speed up the silent parts of a video, resulting in shorter less-boring videos.

3. **Mac Screen Capture**: cmd-shift-5 lets you capture video on Mac. You can choose what directory the captured video is saved to. Before I discovered this, I used QuickTime, but this is easier to use.

4. **Using [watchdog](https://pythonhosted.org/watchdog/)** This is a Python module that can monitor your filesystem and trigger an action when files are created or modified. I use it to a) automatically rename video files as they're created, and b) to automatically apply jumpcutting to new captured videos. The filename format I use is `YYYY-MM-DD-screen-recording-###.mov`.

5. **Python Fire**: The first twenty clips I recorded (not released) were all of me building the tooling I now use as I record videos. Most of this tooling lives in Python Fire CLIs. These CLIs let me do things like composite audio, perform auto-jumpcutting, and rename videos.

### Things to improve:

1. **Zoom in!** The code is blurry and small and the video as is needs to be watched at 1080p to look OK, which is silly.

2. **Audio Quality** I have a lapel mic I'm using for new recordings and it helps.

3. **Storytelling** Is a Python Fire CLI for adding and subtracting the most compelling story? I think there's room for improvement.

4. **Manual Editing** I did no manual editing for the clip above. I think for quality videos, however, learning to do some manual editing is going to be essential. We'll see how far my inclination to automate everything takes me first though.

---

I'm really enjoying this process of recording videos. And more than making the videos, I'm enjoying building the software to help me make the videos. Next step for me is getting more familiar with moviepy. And Davinci Resolve. But one thing at a time.
