+++
title = "The Go Note Go Story"
date = 2022-12-30T00:00:00
tags = ["go-note-go"]
summary = "A personal account of how I came to build Go Note Go, a headless keyboard (no monitor) note-taking device for when you're on the go. It begins with a castle."
+++

<small>_This story is meant to be listened to. You can also read along below._</small>

<audio
    controls
    src="/audio/go-note-go-story.m4a">
  Your browser does not support the <code>audio</code> element.
</audio>


Hi everyone. I'm David Bieber and I'm going to tell you the story of [Go Note Go](/projects/go-note-go), which you can see on the screen.

And to do this, I need to bring you back with me to 2014. It's my senior year of college.
I'm in my dorm, which is a beautiful stone building, like a castle.
I'm lying awake at the bottom bunk of a bed late at night.

My thoughts are racing. I can't sleep. There's this girl. Does she like me? Do I like her?
What will I say to her tomorrow?

Every time I finish a thought, I have a new thought, just subtle variations on the thoughts I've already had. And they won't stop.
It's getting even later and I need to fall asleep.

Fortunately, I find a trick that works for me.
If I write down what I'm thinking, then there's just one canonical version of the thought, not two hundred.
And it's on paper, not in my head, and I can sleep.

The only trouble is, I'm in a bunk bed; there's a roommate six feet above me and I can't just turn on the lights to write something down.
And I wouldn't want to anyway. It would wake me up.
Writing in the dark is no good. Can't read my handwriting that way.
And typing on my phone or computer is out too, because the lights are too bright and they would wake me up. 

So, I settle on typing on my laptop in the dark with the monitor turned completely off.

I study computer science, so I write some software to make this even better.
And [Shh Shell](/projects/shh-shell) is born.
I don't have to worry about typing and falling asleep on the delete key, or typing and having the window not being in focus.
The name Shh Shell is a pun on SSH and sleeping, and it's amusing to me.

And I pile on the bells and whistles. Shh Shell lets me set alarms, send text messages, hear the time, the works, all without ever opening my eyes.
And I love it. I use it for years.

I take it with me when I move out to California to work for Google.
I set it up in my shower so I can capture shower thoughts in addition to sleep thoughts.
Shh Shell quickly becomes my personal journal, a place I can put my most personal thoughts and then get a good night's sleep.

Fast forward five years. This is two months ago now. I'm driving in a car that I recently purchased from New Haven, Connecticut, where I live, to a campground in New Jersey to go camping.

I'm listening to an audiobook and I feel an old yearning, the desire to write something down, something important, just to get it out of my head.
It's been a few years since I've used Shh Shell. I didn't use it much after the move east, but I know exactly what I need. I need to write down my thoughts about the audiobook that I'm listening to.

As I get to the campground, the thoughts about the book have evaporated.
I set up my tent, and it's here that Go Note Go was born.
A new, improved version of Shell that supports driving and camping, as well, of course, as sleeping and showering.

I design Go Note Go right there in the woods.

It'll be like Shh Shell, but with a host of improvements. You won't need a laptop for it to work.
It's just a standalone keyboard.
It supports audio with a beautiful red button you can use to record while driving.
And it works offline. Perfect for camping.
It will transcribe your notes and upload everything as soon as it gets an internet connection.

I am so excited to build this. I order the parts right then and there from the floor of my tent in the middle of the woods.

I don't even wait for the parts to arrive. As soon as I get home, I write [the software](https://github.com/dbieber/GoNoteGo).

I configure mine to upload to [Roam](https://roamresearch.com/#/app/commons-db/page/9W2EycBcG). But a month later when [David](http://ddohan.com/), Aria, Sam, and [Aaron](https://twitter.com/aaronmayer108) are building their own, they set theirs to upload to Notion or RemNote or Ideaflow. It works with any note-taking app at all.

David Dohan has connected me with this wonderful group of people after I built the first version.
And I give them a live demo, taking my fully assembled Go Note Go out into a tent for the first time, this time to go camping in my own backyard.

I show Go Note Go to Aaron and the whole group. How it handles audio, how as I drift off to sleep I tend to switch from talking to typing the more tired I get, how you can still issue commands like asking it for the time without waking yourself up, just like you could with Shh Shell.

I feel like when I built Shh Shell for the first time.
I love it.

And now I have a group of people who love it as well, each building their own.

I finish camping in my backyard here in New Haven and I come inside. Last night, I found myself in a situation like the one from years ago. Getting ready to present today, my thoughts again were swirling. This time, though, I knew immediately what to do. I took the dozens of versions of this story that were racing through my mind, and I used Go Note Go, through a combination of typing and speaking, to put just a single version of the story down on the page. My mind was settled, and I slept.
