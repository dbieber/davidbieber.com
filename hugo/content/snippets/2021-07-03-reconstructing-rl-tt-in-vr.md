+++
title = "Reconstructing RL table tennis points in VR"
date = 2021-07-03T00:00:00
tags = ["table tennis", "virtual reality"]
+++

["Alex TT Barcelona"](https://alexttbarcelona.wixsite.com/home) makes table tennis drills for Eleven Table Tennis.
In a recently released batch of drills, he took a point played by table tennis pro Mima Ito and reconstructed it in VR. The ball machine would -- endlessly in a loop -- play the role of Mima Ito's opponent. It would launch ping pong balls from the same location and with the same trajectory that Mima Ito's opponent hit the ball during the point.

The reconstruction is a great experience; it really demonstrates the level of play, showcasing how fast and wide the ball goes during professional matches. It also highlights the potential of Eleven Table Tennis as a practice tool for real table tennis. You can reconstruct points from your own real-life table tennis matches in virtual reality, and practice them as many times as you like.

Today, the process of reconstructing a point from real life in VR is a bit slow and specialized. The way to do it is to open Eleven Table Tennis on a PC (which I don't currently have, making this difficult), and to adjust the ball machine settings on your computer in order to replicate each of your opponent's ball trajectories consecutively.
Once a full point is done, you can play against the ball machine in VR to practice.

At my last table tennis tournament, I took some footage of myself playing (and losing) a real table tennis match.
I haven't yet tried transcribing it to VR, in part because I don't have a PC. Soon though I hope to transcribe some points so I can practice the shots I'm weakest against.

I estimate that reconstructing a single shot, once you're practiced in the art of table tennis point transcription, takes about a minute. This means that transcribing a full 5-game match, which might have as many as 300-500 individual shots, could take 5-8 hours.

There are several ways to bring this time down. First, and simplest, is to merely transcribe a subset of the points. Only transcribing shots by your opponent immediately cuts the time in half, and you probably only will want to replay perhaps 10 points total anyway, further cutting down the reconstruction time drastically. Outsourcing the reconstruction to e.g. Fiverr seems plausible, but that doesn't save time overall, it merely pushes the time cost onto someone else.

Perhaps there's a way to automate the transcription process. [Stupa Analytics](https://stupaanalytics.com/) uses AI to analyze table tennis matches to provide coaching to players. It seems likely that they model the trajectory of table tennis balls as part of this analysis. Their software works using video from a single phone camera, which is ideal if it works. Perhaps we can build on top of their existing vision systems. I've reached out to them to inquire, but have not heard back. I've also tried to use their software, which promised me analysis within 72 hours, but a week later it has still not delivered.

Some projects on GitHub also show promise for enabling automated transcription. [ckjellson/tt_tracker](https://github.com/ckjellson/tt_tracker) uses OpenCV to track table tennis balls using two camera inputs. [vmarquet/table-tennis-computer-vision](https://github.com/vmarquet/table-tennis-computer-vision) also offers ball tracking for table tennis using OpenCV, though may require specialized sensors (not clear yet). [maudzung/TTNet-Real-time-Analysis-System-for-Table-Tennis-Pytorch](https://github.com/maudzung/TTNet-Real-time-Analysis-System-for-Table-Tennis-Pytorch) uses machine learning to analyze table tennis footage, including ball tracking. These three seem the most promising. Though I don't have any two camera input data currently, I look forward to trying out these projects and seeing if I can repurpose one for RL-to-VR point reconstruction.
