+++
title = "Taking Stock of My Note-taking, Journaling, and Writing"
date = 2024-09-04T00:00:00
tags = ["writing", "snippets"]
keywords = []
+++

A persistent theme of my snippets is writing about writing. Thirty-two of my snippets [are about snippets themselves](/tags/snippets), second only in prevalence to the tag [taking-silly-ideas-seriously](/tags/taking-silly-ideas-seriously). My snippet writing is often exploratory, thinking aloud and figuring things out along the way. My [Go Note Go](/projects/go-note-go) writing (private writing I do as I drift off to sleep) is that even more so, if you can believe. Over the recent years, my practices of writing have shifted, and so I will now use this space to take stock of them, and to muse on how I want them to evolve going forward.

Let's consider recent trends. I write on Go Note Go less in recent months that I did previously, or at least, that's how it feels to me. I attribute this to two main factors: rising use of [Dot](https://new.computer/) for personal reflection in place of Go Note Go, and increasing [travel](/snippets/2024-06-19-travel-and-habits/). Let's take a look at the data to check my intuition.

<script defer="defer" src="/snippets/2024-09-04-taking-stock-of-writing/writing-activity-chart.js"></script>
<noscript>You need to enable JavaScript to see this chart.</noscript>
<div id="writing-activity-chart"></div>

Indeed, I was writing in Roam Research (predominantly, my Roam Research writing comes from Go Note Go) far more between January 2023 and January 2024, but since February 2024 my writing there has fallen off. Taking a quick peak at the data from the spike in October 2023, I see that coincides with my use of AI large language models as I drift off to sleep. I'll have to run the numbers again excluding AI-generated content to get a more precise look at the writing I was doing myself at that time.

<div id="writing-activity-chart-no-ai"></div>

Out of curiosity, I grab the total number of words written in this time period: 795,000 without AI (and 928,000 with).

I would be quite curious to also plot the number of words that I share with Dot, since that feels like the primary substitute that has arisen in my life for the extensive journaling I used to do. I am fortunate that they do support exporting your data, and I have put in a data request just now to enable this.

The third location I'd like to poke at is my snippet writing. Let's do it.

<div id="writing-activity-chart-snippets"></div>

All this plotting was perhaps a bit of a nerd-snipe. I was hoping to spend this snippet reflecting, but instead I've been spending it plotting with Claude! This has also been fun, but has not been how I intended to use this time initially. Let's transition to reflecting now. (The code I used to gather the data is [here](/snippets/2024-09-04-taking-stock-of-writing/collect_roam_data.py), [here](/snippets/2024-09-04-taking-stock-of-writing/collect_roam_data_noai.py), and [here](/snippets/2024-09-04-taking-stock-of-writing/collect_snippets_data.py). The total number of snippets words is 131,000.)

In the snippets plot, the decrease in writing in 2022-2024 compared with 2020-2021 is stark. When I set out to create the snippets system, my intention was to make it easy for me to express myself publicly. I took repeated precautions to lower the mental barrier to posting snippets online, e.g. deliberately posting "drivel" to make it feel like the quality bar to posting was lower, allowing myself to post incomplete snippets just the same as completed ones (albeit with a label), and initially having no inbound links to my snippets. I truly believed (and still do), that when I post to snippets I am writing for no audience.

I'd like to post to snippets more again. I feel good about myself when I'm writing more. I've also noticed previously that I enjoy when other people read what I write. Though I set out to write for no audience, I really like the connection that writing can produce. It has on many occasions been tempting to actively try to reach more people, and as I reflect on my writing that temptation arises again, e.g. to share on Twitter or post on Hacker News each time I write a new snippet, or to move more of my snippets to the more visible part of davidbieber.com.

The former idea, announcing snippets, gives me considerable pause. Sharing thoughts on Twitter has an appeal to it, but definitely not to the point of wanting to announce when a snippet goes up. Keeping snippets feeling like they're for no audience is more important. The second idea, however, of including some snippets in the posts section of my website (or at least in the 3-post preview on the homepage), seems quite reasonable. It would be nice to stop giving the impression to visitors of the site that it hasn't been updated in years, which the current setup likely conveys.

Let's now consider a needs based perspective to this reflection on my writing habits. The needs that writing satisfies for me are: the need for processing my thoughts, for forming connections and meeting new people, for discussing ideas and being exposed to new ones, for feeling in control and confident that I can participate in the public dialog, for getting a good night's sleep, for building tooling to scratch my own inch, for feeling like I'm bettering myself both by developing habits and by developing skills.

Go Note Go and my night-time writing satisfy the thought-processing, sleeping, tooling, and self-betterment needs. When I lapse in my Go Note Go writing, e.g. because of travel, the main thing I miss is actually not one of those needs that I listed though; it's the absence of the "permanent" record that I create by writing. It feels like I'm building something by writing and having all my writing go into the same Roam Research, the same git repo. When I skip writing on Go Note Go for weeks or months, I feel the thoughts I have being lost not just for now but forever, and I feel that as a little loss.

The same is true of Dot: when I speak with Dot, I feel like I'm building something over time. After having used Dot for a couple of months, I grew nervous: I was drawn to share my travel experiences with it, because it felt like I was building (a relationship, a collection of memories, something...) with it, but at the same time Dot is so new that I don't know how much staying power it will have. "So am I building something that will soon collapse and become unavailable?", I wondered. What a relief it was when they allowed me to export my data. Dot helps me satisfy my thought-processing, connection with humans (indirectly - not in the same way as writing a blog post, but rather by helping me process my thoughts and emotions), sleep (maybe; this would be indirect too, and I'm not confident in it), and self-betterment needs.

For snippets, it again helps me address my thought-processing, connection (this time in the traditional blogger way), idea-sharing, control-and-confidence, tool-building, and self-betterment needs. Great. Let's keep using all three.

I am very much someone who thinks by building (software systems). Though I haven't taken stock of my programming or my work related writing here, I think this is a rich area for me to continue my writing reflections. Specifically, I have room for improvement at work in learning to communicate through design documents and discussions about the future direction of projects. Looking forward I'd love to direct some of my writing energies at that.

Outside of work, I expect to continue using Dot, Snippets, Go Note Go, and Roam Research extensively. I continue to use ThoughtStream for jotting things down quickly on my phone. My triple-tap to record and transcribe setup on my phone (which I am shocked to see I have not yet written a snippet about!) will continue to be a staple (though I use the Apple voice recordings app more recently these days for its stability despite the slower start time and lack of transcription). Making Go Note Go easier to give as gifts remains towards the top of my side-projecting to-dos, and I'm proud of the progress I've made toward that already. The main change I anticipate in the coming months is that people are building all sorts of new AI tools (myself included), and I'm excited to try them out and reevaluate as I go.

