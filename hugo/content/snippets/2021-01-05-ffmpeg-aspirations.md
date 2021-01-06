+++
title = "ffmpeg aspirations"
date = 2021-01-05T00:00:00
uid = "LlQ7HLkgk"

+++

- turn a collection of photos into a slide show
- set it to music
- add gentle transitions, like a slow pan of the camera
- fade the music in and out to change songs
- given a file of time stamp ranges, clip to just those parts of the file
- given a file of timestamp ranges, each with a speed multiplier, adjust the speed of each clip and stitch together the clips

I have code that does this last one already, but I suspect it can be orders of magnitude faster done as an ffmpeg command compared with the way I'm doing it now.

## Turn a collection of photos into a slide show:

```shell
ffmpeg \
  -r 1/5 \
  -pattern_type glob -i "/Users/dbieber/Documents/video/raw/*.png" \
  -c:v libx264 \
  -r 30 \
  -pix_fmt yuv420p \
  output.mp4
```

Next up, I'll see if I can add some audio, and I'll work my way down the list.
