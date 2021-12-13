+++
title = "We Could Use Augmented Reality to Simulate Prosopagnosia"
date = 2021-12-12T00:00:00
tags = ["virtual reality", "brains"]
+++

I was watching [Lecture 4 of Nancy Kanwisher's class "The Human Brain"](https://www.youtube.com/watch?v=vFZY--lgmHs),
and it occurred to me that we could use augmented reality to simulate prosopagnosia.
Prosopagnosia, for those unfamiliar with the term, is "face blindness".
It affects about 2% of the population with varying degrees of severity,
and those with prosopagnosia cannot recognize faces.

In the in-person version of the course,
the students observe demos to show off the importance of motion in vision, and color in vision.
Those demos aren't available online; they only work in person.
The color vision demo puts students in a room without colored light, thereby only permitting gray-scale vision.
The importance of color then becomes immediately apparent, no pun intended; color is useful for distinguishing safe food from spoiled, and healthy faces from sickly ones.
This exercise helps motivate Marr's theory of computation: that you can reason about brain function by thinking about what the brain must compute, and why.

In a similar spirit to these demos,
there could also be a demo for the students showing what it's like to have prosopagnosia.
This would help students feel more viscerally "what is computed and why" when it comes to facial recognition,
and it could also be used for people to better understand the condition.
Fostering empathy and understanding is always a good thing!

How would we do it? With augmented reality, it would be possible to overlay or distort faces in a way that makes them unrecognizable.
The naive implementation would be to simply cover up all faces with a rectangle.
To make it a closer approximation of the prosopagnosia experience,
it would be essential to work with people with prosopagnosia.
Perhaps applying a light distortion to a face, but critically applying a different distortion to a face every time it is observed, would be a solid way to disrupt the user's ability to recognize faces without being too distracting.
It's difficult for me to know a priori whether this could create a convincing prosopagnosia experience,
so I will leave this snippet here, merely as food for thought, rather than pursuing the idea.[^1]

Do you think this effect could be convincing, approximating the experience of someone with prosopagnosia in someone without?

In writing this snippet I Googled "prosopagnosia augmented reality" to see if anyone had tried this idea already.
Of course what I found was not my idea, but rather the reverse: using augmented reality to help those with prosopagnosia, rather than using it to help those without. That makes a lot of sense, and I feel a bit silly for it.


[^1]: Maybe it could be a good class project for someone to dive deeper into this idea though. If you do, do let me know!!
