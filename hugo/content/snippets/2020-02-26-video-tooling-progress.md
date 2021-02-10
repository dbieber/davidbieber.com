+++
title = "Video Tooling Progress"
date = 2020-02-26T00:00:00
tags = ["automatic-video-editing", "python"]
+++

Over the last week and a half I've been making screen recordings of myself programming. Mostly what I've been programming is tooling to help myself make better screen recordings. Here's an overview of what I've put together so far.

## Auto Auto-Jumpcutter

This springboards directly from carykh's [jumpcutter](https://github.com/carykh/jumpcutter) project, which uses [ffmpeg](https://www.ffmpeg.org/) and AudioTSM to speed up the silent sections of a video. Auto Auto-Jumpcutter has two "auto"s in its name because jumpcutter already does automatic jumpcutting of videos, and Auto Auto-Jumpcutter uses [watchdog](https://pythonhosted.org/watchdog/) to automatically apply jumpcutter the moment a screen recording is captured.

The result is that my typing appears superhuman in speed, but slows down while I'm speaking, without me needing to do any manual editing to the video to achieve this effect.

## Auto-Commit

I also made for myself a git auto-committer. Every time I save a file during a screen recording session, the change is immediately and automatically committed. The commit message is selected automatically from the diff. The result is that I have a timestamped log of all changes made during the recording. This is super useful for editing the recordings (both automatically and manually) because I can pinpoint exactly where in the recording any change took place. It also works hand-in-hand with the next piece of tooling.

## Keyboard Shortcuts

Just using Auto Auto-Jumpcutter goes a long way toward having automatically edited videos, but it doesn't completely eliminate the need for manual editing.
For example, it provides no way to do multiple takes and stitch together the good parts of each. For this I've set up a keyboard shortcut system for myself using the Python [keyboard](https://pypi.org/project/keyboard/) module. This way I can indicate via keyboard shortcuts to remove a selection of footage during the recording session, and have it automatically be removed during the automatic editing phase. This last step -- using the keyboard shortcuts to guide automatic editing -- is an active work in progress.
