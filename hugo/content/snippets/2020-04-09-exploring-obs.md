+++
title = "Exploring OBS and Virtual Cameras"
date = 2020-04-09T00:00:00
tags = ["automatic-video-editing"]
+++

This week I've been exploring [_Open Broadcasting Software_ (OBS)](https://obsproject.com/) and toying with using it as a virtual camera. I use a Mac, and historically there hasn't been a good way to use OBS as a virtual camera. With [@tobi](https://twitter.com/tobi)'s recent [$10,000 bounty](https://github.com/obsproject/obs-studio/issues/2568) for making this a core feature, however, some developers in the OBS community leapt into action and a [working prototype](https://github.com/johnboiles/obs-mac-virtualcam) of the feature was available on GitHub within days.

## Virtual Cameras

OBS is popular software among Twitch streamers. It lets you take a bunch of video sources and rearrange them into scenes. Streamers will often overlay a camera feed of their head and a live stream of a video game, maybe with cool graphics overlaid on the whole thing.

For years, OBS has let you take the scenes you create and stream them in real time to YouTube Live or Twitch or any number of other streaming services. If you wanted to use your OBS scene in Zoom or Google Meet, however, it wasn't straightforward, at least on Mac.

There were workarounds. You could project your scene to an external monitor, and then use screen sharing to share that. At times there were combinations of tools and plugins that could similarly get the job done.

Now, however, it's considerably easier. John Boiles's has made a OBS plugin that works without fuss. For now it still requires a technical background to use, following build instructions and executing commands on the terminal to get it set up. In a matter of months, however, I expect it will make its way as a core feature into OBS.

## Combining OBS with Auto Video Editing

As you may know, I've been working on [automatic](/snippets/2020-02-21-jump-cut-programming) [video](/snippets/2020-02-26-video-tooling-progress) [editing](/snippets/2020-03-02-fastbook) software. I'd like to be able to make quality content -- e.g. videos teaching interesting aspects of programming -- without needing to spend time on the video editing process. The cutting and rearranging would happen automatically. The music and audio adjustments would be added automatically. All I'd need to do is write a script and record the footage, and the auto editor would take care of the rest.

Originally I was using Mac's cmd-shift-5 screen capture capability to create these recordings. OBS lets you rearrange video feeds deliberately and use a variety of video sources. These video sources include window captures, cameras, and prerecorded media. The result is much more flexible than Mac's screen capture, and so I've switched my auto video editing software over to use OBS for recording.

As an aside, I've also discovered [NDI](https://obsproject.com/forum/resources/obs-ndi-newtek-ndi%E2%84%A2-integration-into-obs-studio.528/), a plugin for OBS. It lets me use my phone's camera as a video source with minimal setup. It was so easy to get working, in fact, that I'm convinced it must be a large security vulnerability to use it at all.

Now that I'm using OBS to record, I enabled my auto video editing software to run automatically on any recording produced by OBS. As soon as the recording gets saved, my software starts editing it automatically (preserving the original). I'd love to have my auto editing start even sooner than that though, _before_ the recording is complete. The OBS codebase is surprisingly approachable, so I may be able to get this working.

## Hacking on the OBS Codebase

When John Boiles released the Mac Virtual Cam plugin for OBS, it was initially stuck on the wrong resolution. John told me it was hard coded to 720x480, and that was the impetus for me to poke at the code. Changing the hard coded resolution proved easy enough. Then I ran into a bug where OBS would fail to capture a window if I changed tabs in that window while OBS was closed. Though there's inertia with entering any unfamiliar codebase, I found I was able to solve this issue for myself too. Through these two debugging experiences I got enough glimpses of the OBS plugin set up to think that OBS really is approachably hackable. I think, with hard work, I could integrate my auto editing code into OBS so that it runs in real time. It's not the very top of my todo list for the auto video editor, but I'm excited to give this a try.

## Replay Buffers in OBS

One neat feature in OBS is its ability to record a "replay buffer". I have it set up to record a circular buffer of the last 60 seconds of content. That means that at any given moment, OBS has recorded the previous 60 seconds of footage. Unsaved footage older than 60 seconds is gone, but at any point, if I choose to save it, I can record the previous 60 seconds of footage.

This is great because it means I can keep the camera rolling between scenes without wasting memory, and if anything noteworthy happens in that time I can capture it.

There's a second reason I'm excited about the replay buffer though; it may enable me to use auto-edited videos in conversations in _real time_. I imagine the user experience like this:
I'm in a remote meeting and we're having a discussion. By default I'm unmuted and people can hear what I'm saying. Whenever I hold down a keyboard shortcut, I'm muted in the call and OBS starts recording me. When I release the shortcut, I can continue to talk in the call. Once I've recorded a satisfactory amount of content for OBS, the auto-editing will be applied and I can use OBS as a virtual camera to send that recorded and edited content to my colleagues in the meeting.

## Looking Forward

I'm excited to become more proficient using OBS, and to explore the various plugins and overlays that streamers use with OBS. Particularly I'm excited to look into the [audio plugins](https://obsproject.com/forum/resources/vst-plugins.848/) that are available.

I also intend to continue my auto-editing plans from before: I'm still looking forward to introducing a "script" with audio auto-transcribed and key events entered via keyboard shortcuts and auto-tracked file saves. And I still want to be able to modify this script to automatically edit the video based on the modifications.

Having explored OBS for a little while now, I'm also looking forward to integrating my auto-video editing more closely with OBS, ideally resulting in real time auto editing in the end. Here's to hoping OBS continues to feel approachably hackable!
