+++
title = "Automate Your Life: Sending Emails"
subtitle = ""

date = 2013-03-13T00:00:00
lastmod = 2013-03-13T00:00:00
draft = false
authors = ["David Bieber"]

tags = ["Automation"]
summary = "Use Python to send emails programmatically."

[image]
  caption = "Image credit: [**rawpixel.com**](https://www.pexels.com/photo/photography-of-person-using-macbook-1413652/)"

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = ""
+++

_In a hurry? Scroll down and skip to the code. That's the good part anyway._

One of the beauties of programming is the elimination of redundant aspects of life that you find yourself doing over and over again. When you find yourself calling home every weekend, logging hours at your job daily, or getting your hair cut every month, it's time to learn to program. Write a short script to do these repetitive behaviors for you. Just kidding. Don't.

These are joke examples -- I strongly advise against automating discussions with your mother -- but they aren't so farfetched. Automating processes - shopping, shipping, server maintenance - save countless hours and dollars. Here, we'll do a thought experiment: imagine a team of people running Amazon.com without automation. As a crude estimate, let's suppose they sell a mere billion books each year. Let's imagine they only handle 1% of all Internet traffic. And let's pretend they only store 1 trillion objects in their S3 storage system. Then with their team of about ninety thousand, each Amazon employee would have to be selling and shipping 30 books a day on top of processing and transmitting over 100 gigabytes of Internet traffic daily, all while handling requests for a hundred thousand S3 objects that they've had to memorize. Maybe <a href="http://en.wikipedia.org/wiki/Jeff_Bezos">Jeff Bezos</a> could pull it off. But you're not Jeff Bezos, so I'd say it's worth your time to learn to automate.

Even education is being automated these days. Will the next century's robotic overloads prove to be better professors than the ones we grew up with? To which you may reply: "Oh gee whiz! I sure hope we get better robotic overloads in the future! The ones I grew up with were just miserable professors." But that's not what I meant. I'm asking whether <a href="http://khanacademy.org/">Khan Academies</a> and <a href="http://duolingo.com/">Duolingos</a> will replace our real life Ms. Frizzles and Mrs. Gorfs. A brief excursion with Duolingo makes me suspect it will be a major part of all future language educations. This seems counterintuitive. Languages are inherently about communication. The best way to learn a language should necessarily involve communicating (and the very best way will probably forever remain immersion, but often that's not an option). Conversation and human interaction are so fundamental to language learning that it seems almost absurd that a computer could be a good language teacher, at least until we have <a href="http://en.wikipedia.org/wiki/Strong_AI">strong AI</a>. But the computer manages to do one thing extraordinarily well that isn't scalable in a traditional classroom; the computer focuses entirely on me. So, yes, it lacks creativity and the personal touch of a great teacher. It doesn't tell funny stories or crack foreign language jokes. It doesn't show cute movies and it can't relate to me at all. Yet despite all these shortcomings, it's remarkably good at helping me learn the basics of a foreign language, because it can focus on me, going at my pace and not having to devote its efforts to maintaining the attention of 30 other students.

Automation has clearly been taking over everywhere for years. You have to join it. <a href="http://www.youtube.com/watch?v=nKIu9yen5nc">It's a real life superpower.</a>  So let's learn to automate something basic. We'll go with software: a Python script to send emails.

I present: the code. You can run it as is. Save it as a file and run it with Python, and it should just work out of the box. Go ahead, try it.

<script src="https://gist.github.com/dbieber/5146518.js"></script>

Awesome. You just sent me an email. What good is this code? Tweak it a bit and you can use it for personal alerts -- systematically check when you're low on milk and email yourself a reminder -- have your computer email you daily with upcoming birthdays; you can even have it buy the gifts. You can email yourself automatically when a course opens up on your registrar's website. We'll talk about auto-enrolling another time. Or you can set up a script to send different versions of emails to different people, like those spam emails that pretend to be personal by including your first name.

With great power comes great responsibility. Don't send spam.

With a new Python library in your toolbox, I hope you save yourself thousands of hours. Until next time, try to stay <a href="http://en.wikipedia.org/wiki/Don't_repeat_yourself">dry</a>.

<a href="https://news.ycombinator.com/item?id=5371430">Discuss on Hacker News.</a>
