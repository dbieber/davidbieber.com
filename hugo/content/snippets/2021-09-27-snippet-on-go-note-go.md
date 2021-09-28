+++
title = "Writing a Snippet with Go Note Go"
date = 2021-09-27T00:00:00

tags = ["go-note-go", "snippets"]
+++

I've been developing and concurrently using Go Note Go for two weeks now, and in that time I have come to love the frictionless way it allows me to dump thoughts into the machine. I don't have a chance to reread what I've written. There's no going back and rewording something. And more than that, there's no waiting for the characters to show up, or switching tabs, or spell checking or anything like that.

This is the first time I'm writing a snippet using Go Note Go.

I've thought about writing a snippet about Go Note Go over the last two weeks, but I decided not to until yesterday when I finally stopped keeping Go Note Go to myself.
I thought maybe there would be value in getting Go Note Go polished, e.g. writing a getting started guide or even a sales page, and _then_ publishing it once people can actually use it themselves.
But I decided against that.

Done is better than perfect.

I might not find a good way to package Go Note Go so that people can start using it with relative ease.
Certainly I can do better than I have so far − there's little help at all for someone to put together their own system.
That said, a motivated individual could in principle piece together their own Go Note Go from what I've published now.
And I'd be happy to help them do it.

And even if someone had to ask too many questions or can't reproduce the full setup, maybe they'll take the concept in a new direction.
"Headless note−taking" is a broad idea and I've just scratched the surface.
We can see from shh shell and Go Note Go alone that there are diverse approaches one can take to this broad concept.

I'd like to take it further myself, but more than that I think it's important to start the conversation about headless note−taking since it might be able to help a much broader set of people than it's helping right now.

Maybe it would be great in classrooms to avoid distractions.
Maybe there are headless audio−only applications for writers, for programmers, for producers, for lawyers and doctors and publicists and influencers and so forth that are just waiting to be developed.
Different keyboard shortcuts could be specialized for different domains. The addition of foot peddles might help some users. Whatever is needed to make this maximally useful for different applications and different people...

Maybe it's already super useful for people, but there's just no way for those people to know right now because they can't easily try it, or haven't heard of it and thought about it. This is wishful thinking of course; it might be an esoteric toy that is only useful or fun for a small group, but I'm confident that group is larger than just myself.

So I want to put this out there a little bit. I'd like to share it with Conor of Roam, and with Andy Matuschak, and with folks at IdeaFlow and with Notion users, and with Obsidian folks, etc.

One thing I'd like to get out of sharing with these groups is contributors to the extensible uploader side of Go Note Go.
I think it would be so cool if each supported note−taking system had an uploader contributed by someone working at that note−taking system's company. Conor or Bardia could make a contribution to the Roam uploader. Jacob or Linus could write the IdeaFlow uploader. Someone from Obsidian and Notion could provide uploaders for each of those. Now that the GitHub for the project is public, this is easier to start working toward.

Also, the more I think about the getting started guide, the easier it seems to write. There are only a few steps you really need to follow to get set up. Roughly, it looks like this:

1. Acquire the parts (Raspberry Pi, MicroSD card, optional battery pack, USB cords, a speaker and microphone compatible with the Pi (a Voice Bonnet is one option, but any will do.)
2. Clone Go Note Go
3. Edit config
4. Install dependencies
5. Put start script in rc.local file to start on startup
6. Be sure to configure your wifi wpa config file

Wishful thinking again: I could probably write a decent guide in under an hour.
