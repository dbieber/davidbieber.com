+++
title = "Chat by Tag"
date = 2022-06-20T00:00:00
tags = ["snippets", "ask-me-anywhere", "browserflow", "taking-silly-ideas-seriously"]
+++

I don't have a comments section on my website, but I do like when people reach out to me by email.
I am thinking about an idea for adding chat to my website, but the experience I have in mind is different from any chat or comments section that I've seen before.
Here's what I'm thinking about and why -- please do let me know if it exists.

At the end of each snippet there would be a badge for each tag associated with that snippet, as there already is today.
Each badge would indicate that there is a chat thread available for that tag.
E.g. it would show the number of active users and amount of recent activity in the chatroom.
Clicking the badge would take you to the tag's page, which would list all the snippets having that tag.
The tag page would now also house the tag's chat thread.

On the tag page you could engage in real time chat, and your messages would stay up for a week (or until I take them down, in the case of spam).

My website is not particularly heavily trafficked, but enough people email me about the things I write that this features interests me.
I don't envision any of the chats having any content the majority of the time.
I would set the lifetime of a message to just one week.
Between the low traffic and ephemerality of the messages, most of the chats would be empty most of the time.
I would set up email notifications for myself though, so that I know if someone does post a message.
So at the very least, I could reply, even if few others see the messages.

As often happens when writing a snippet about an idea I've had, I start looking into how to implement it concurrently with writing it.
I've looked at Rocket.Chat, Slack, and Discord, and am currently investigating whether using widgetbot.io to provide access to a Discord server might be a solid solution here.
What follows is my initial attempt at including Discord directly in this snippet.

<details id="chat-details-inline">
  <summary markdown="span">Expand this to see the embedded chat.</summary>
  <widgetbot
    server="695290335823265862"
    channel="988521423603654686"
    width="100%"
    height="600">
  </widgetbot>
</details><br/>

It seems to be working quite well.

So, given that this tool is readily available, I will compromise on my original vision some.
I think what I'll do now is (1) find a way to lazily load the chat so people who don't want to deal with it aren't bothered by it,
and then (2) I'll add it (behind an expandable section) to every snippet and every tags page.

I'll set up a Discord server with one channel per tag. On the tag pages, the chat will default open to that tag's channel.
On the individual snippets, the chat will default open to the first tag present on the page.
Users can easily switch to other channels if they so desire.

So, how to lazy load? This turned out to be simple enough to implement quite quickly. I added some JavaScript to the page that loads the widgetbot JavaScript only when the collapsed chat is expanded. It looks like this:

```html
<script>
let chatLoaded = false;
const details = document.querySelector('#chat-details');
details.addEventListener("toggle", event => {
  if (details.open && !chatLoaded) {
    const script = document.createElement('script');
    script.src = "https://cdn.jsdelivr.net/npm/@widgetbot/html-embed";
    document.head.appendChild(script);
    chatLoaded = true;
  }
});
</script>
```

(Why am I showing this code? It is not germane to the story. A: This is a snippet, and so I guess I do not curate the content like I would if the goal were a proper story. It's meant for future me as much as for anyone else.)

<script>
let chatLoadedInline = false;
const detailsInline = document.querySelector('#chat-details-inline');
detailsInline.addEventListener("toggle", event => {
  if (detailsInline.open && !chatLoadedInline) {
    const script = document.createElement('script');
    script.src = "https://cdn.jsdelivr.net/npm/@widgetbot/html-embed";
    document.head.appendChild(script);
    chatLoadedInline = true;
  }
});
</script>

Having set up the lazy loading, the next step was to create channels for each of the tags on my site.
There are a lot of tags, so I used Browserflow to do this quickly. A joy as always.

Finally, I'll have to update my website so that the appropriate chat gets added to the appropriate page. (I'm back, and that's done now :).)

I've tagged this post with "Ask Me Anywhere" because, like my original Ask Me Anywhere ideas, this is about allowing for more direct engagement between me and people on the site. I've also tagged this "Snippets", because it's primarily about a change to the snippets section of my website, and "Browserflow" because Browserflow was a joy to use for setting up this new system.

At this point, I'm concluding the snippet. The system is up and running. That was certainly not my expectation when I started writing this, but I'm delighted by the progress I made.

<details>
  <summary>As an aside, David, expand this for a reminder of how to add a new tag.</summary>
There will be some maintenance work necessary whenever I add a snippet with a new tag. Let me summarize the maintenance for myself here for easy reference:

1. Create a new channel in the Discord.
2. Add the tag name and channel id to the map at the top of the [discussion.html partial](https://github.com/dbieber/davidbieber.com/blob/master/hugo/layouts/partials/discussion.html).

The site won't fail to build if you forget to do this; it will just have a broken chat section.
</details>

That should be it. See you in the chats!
