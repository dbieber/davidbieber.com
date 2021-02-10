+++
title = "Tips for Effective OBS"
date = 2020-04-11T00:00:00
tags = ["automatic-video-editing"]
+++

As a newcomer to OBS, I've been regularly discovering new features that make my OBS experience better. Here are a handful of things I've found useful, that perhaps weren't immediately obvious to me, from my early experiences with OBS.

## Using Media Sources

"Media Source" video sources are essential when showing prerecorded video, or using a replay buffer. However, it wasn't obvious to me how to get media sources to play their audio.

When using a Media Source, here's out to turn on the audio. In the Audio Mixer panel choose `Gear Settings > Advanced Audio Properties` then set `Audio Monitoring` to "Monitor and Output".

## Namespaces for Scenes + Turning Off the Camera

You can create multiple Profiles and Scene Collections in OBS. I only have one Profile, which I've named "Default" (rather than the default of "Untitled"). I made a few Scene Collections. Making new Scene Collections gives you a space to play around with new ideas for scenes and keyboard shortcuts, without disrupting the main setup(s) that you've put together. I like to fiddle around with new ideas in a Scene Collection I've named "Playground".

If you have any sources in a Scene Collection that use your webcam, then your webcam will stay on even when it isn't being used. If you switch to a Scene Collection with no sources using your webcam, then your webcam will turn off. I use a Scene Collection that leaves my webcam off by default, and only switch to a Scene Collection with a webcam source when I actually intend to record something that needs the webcam.

## Replay Buffer

I leave the replay buffer on in between recording scenes. By setting the replay buffer to a reasonable size like 60 seconds, I can leave it rolling without consuming too much memory (and the CPU consumption has been reasonable too, e.g. 10%). This way, if anything noteworthy happens in this period between recordings, I can still capture it.

## Virtual Cameras

If you're willing to get your hands dirty, the instructions at [johnboiles/obs-mac-virtualcam](https://github.com/johnboiles/obs-mac-virtualcam) will let you use OBS as a virtual camera on Mac.

## Transform Editing and Scene `.json` files

`cmd-e` opens the Scene Item Transform for a Scene Item. Using that, you can get pixel perfect positioning of any video source. You can also see and edit the json files that describe your scenes. On Mac, these scene json files can be found at `~/Library/Application Support/obs-studio/basic/scenes`.

## Keyboard Shortcuts

`cmd-,` opens your settings. There's a panel for setting keyboard shortcuts. This is a core OBS feature, and it's extremely valuable. I really appreciate how easy OBS has made it to set up these keyboard shortcuts for switching between scenes, starting and stopping recordings, pausing and playing media, etc. I only wish I could have extra modifier keys so I could set up more shortcuts that don't collide with the shortcuts of my IDE!
