+++
title = "What's Next for Ask Me Anywhere?"
date = 2020-01-26T10:00:00

summary = "Next stepps for Ask Me Anywhere"
plugins_js = ["collapsible", "ask-me-anywhere"]
+++

Yesterday I put up an early version of [Ask Me Anywhere](/snippets/2020-01-25-ask-me-anywhere/). You'll notice it's in the snippets section of the website, rather than part of the main blog. This gives me the freedom to post it even though I know it's not as polished as it could be.

Now that this first pass is published, it's time to start thinking about where to go next with Ask Me Anywhere.

## Short Term: Stylistic Improvements

On mobile, the "Click to React" text shows up and is improperly styled. I didn't intend for it to show up at all. On certain mobile devices and browsers, it seems there are even larger issues than this, such as double tapping sometimes not working at all. Let me know if it doesn't work with your browser so I can fix it.

The "Click to React" text also sometimes causes the flow of the text to change, which interrupts the reading experience somewhat. I would like to fix this so that the text flow is never changed by the presence of this message.

I also would like to tweak the styling to minimize the friction someone feels in deciding to leave a message. I think adding a question-mark icon, which when moused-over gives an explanation of why this feature is there in the first place could be useful. This could strike a good balance between being non-intrusive and letting people know that their thoughts are warmly welcomed.

## Longer Term: "Socratic Tutorials"

"Ask Me Anywhere" is really an MVP that came out of a larger idea: "Socratic Tutorials".

My idea is that a _Socratic Tutorial_ is a blog post structured in a very particular way. It begins with a brief introduction to a topic, followed by a series of questions you might want to ask about that topic. Click a question to reveal an answer to that question, followed by additional questions you might have about the topic. In this way, you can explore the contents of the post in the order that best suits your interests. I also hope that by having to click questions to view the answers, it will help motivate what you're reading, since you'll be actively wondering about the question when you read the response.

If a reader of a _Socratic Tutorial_ doesn't understand something, or has a question that isn't already addressed, they can choose to ask that question. The author can then add it to the list of questions available during reading if they choose to do so. In that way, "Ask Me Anywhere" is almost a subset of the features planned for Socratic Tutorials.

<p id="cbp_example">
My very first blog post ever was about <a href="/post/2012-09-04-collapsible-blog-posts/">Collapsible Blog Posts</a>. The premise was that you could click on a paragraph, and it would be replaced with a summary of that paragraph. This paragraph is an example; click on it, and it will be replaced with a summary.
</p>
<p id="_cbp_example">
This was a
<a href="/post/2012-09-04-collapsible-blog-posts/">Collapsible Blog Post</a> paragraph. Click to un-collapse.
</p>

I learned early on from this experiment that the reverse process actually is more useful. Present the user with a short summary, and let them click if they want to read additional details.

<p id="cbp_reverse">
Here's an example of a short paragraph that you can click to reveal additional details.
</p>
<p id="_cbp_reverse">
The reason it makes more sense to show the summary first is that it empowers the user to choose how to spend their time. If they are interested in understanding more about a topic, they can choose to expand the paragraph and read the details. If instead they read the extended paragraph first, there isn't much value to them also reading the summarized version. And if they just want the summarized version, having them see the full version first isn't too useful either.
</p>

In some ways the idea for "Socratic Tutorials" is a spiritual descendent of Collapsible Blog Posts. They both share a goal: give the user control over the information they're consuming, as they're reading. Socratic Tutorials and Ask Me Anywhere take an additional step though, giving the user the ability to communicate directly with the author while they're reading.

You'll likely have noticed that this post uses "Ask Me Anywhere". That means you can double click any paragraph, or click between two paragraphs, in order to send a note directly to the author.
I hope you do this, as I'd love to hear any thoughts you may have.
