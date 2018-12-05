+++
title = "Collapsible Blog Posts"
subtitle = ""
collapsible = 1

date = 2012-09-04T00:00:00
lastmod = 2012-09-04T00:00:00
draft = false
authors = ["David Bieber"]

tags = []
summary = "This is my Hello World blog post of sorts."

[image]
  caption = "Image credt: [**Zero Gravity**](https://commons.wikimedia.org/wiki/File:Accordion_in_SVG_format_(vector).svg)"
  focal_point = ""
+++

<p id="cbp_hello">This is my Hello World blog post of sorts. It's my introduction to the world of blogging, the blog post likely only read by my family and a few techie friends. It's the post in which I make an unrealistic commitment to blog frequently, which I later fail to live up to. And it's the post in which I introduce a new form of blogging, <u>Collapsible Blogging</u>. Here's the tl;dr.</p>
<p id="_cbp_hello">Hello World!</p>

<p id="cbp_tldr"><b>Click any part of this post to see it in condensed form.</b><br>
Source is here: <a href="https://gist.github.com/3616675">https://gist.github.com/3616675</a>
</p>
<p id="_cbp_tldr"><b>Click stuff to collapse. Click again to expand.</b></p>

<p id="cbp_commit">Before we get into the details of Collapsible Blogging, let's start with that commitment to blog. Every half-baked blog has it, so here's mine. Once a month. I know my life is sufficiently not boring that something blog-worthy will come along each month. Why, just last Tuesday I ran with <a href="http://en.wikipedia.org/wiki/Tyson_Mao">Tyson Mao</a> (yeah, the Rubik's Cube guy) and had a near encounter with <a href="http://en.wikipedia.org/wiki/Richard_Hammond">Top Gear's Richard Hammond</a> (he came by Twitter while I was interning there). This post counts for September. So you'll be hearing from me next at least before Halloween's end. Here's to a happy, healthy, blogging career!</p>
<p id="_cbp_commit">I'll blog once a month. And I like name dropping.</p>

<p id="cbp_skim">
So, how's this whole Collapsible Blogging thing work, why is it awesome, and how can you try it out? Collapsible Blogging works well with my own internet content consumption habits, which I believe I share with many of the other Hacker News obsessed entrepreneurial spirited folks out there on the internet. Possibly you. I choose an interesting Hacker News article, I read a bit, and I quickly lose interest in favor of another well titled article. My goal is really just to consume quickly the highlights of the web. Collapsible Blogging let's me skim faster. But maybe that's a not a good thing. I'm rereading Fahrenheit 451- and there's a passage this reminds me of:<br><br>

"I sometimes think drivers don't know what grass is, or flowers, because they never 
see them slowly," and<br><br>

"Have you seen the two-hundred-foot-long billboards in the country beyond town? Did you know that once billboards were only twenty feet long? But cars started rushing by so quickly they had to stretch the advertising out so it would last."
<br><br>
I don't want Collapsible Blogging to be those two-hundred-foot-long billboards.
</p>
<p id="_cbp_skim">
Use Collapsible Blogging to make your content easier to skim.
</p>

<p id="cbp_expand">
So with that in mind, I introduce the second use of Collapsible Blogging. Diving deeper into a topic. If you'd like to learn more about diving deeper into a topic, click this passage.
</p>
<p id="_cbp_expand">
Collapsible Blogging let's people who aren't interested in the topic read quickly, while people like yourselves who want the full blog post can read more in a single click, as you just discovered. 
<br><br>
One application of this is resumes. On my resume I list that I have experience with Java, Python, etc. An employer may care just about my <a href="http://www.quora.com/Have-I-fallen-in-love-with-Python-because-she-is-beautiful">lovely Python</a> experience, but my resume doesn't go into details about each technical skill and where I've used them. If I build my resume with Collapsible Blogging, I can make it so that with a single click potential employers can learn more about my experience with just the skills that interests them. They can learn what matters to them without me cluttering my resume with every project I've ever worked on.
<br><br>
Likewise, say I write a blog post about my experiences at Twitter and Facebook. You might be interested in reading about the technical challenges I faced and the programming concepts I learned, while another reader might be more curious about the pool party I attended at Zuck's house. If I write my post using Collapsible Blogging, you, the reader, can choose to read about the parts of my experience that interest you most, or you can choose to just skim the collapsed form of the post.
</p>

<p>Some paragraphs don't have collapsed forms. You can only collapse the passages with a left border. There isn't really a shorter way to say that!
</p>

<p>
If you're interested in using Collapsible Blogging yourself, it's remarkable easy. I include the <a href="https://gist.github.com/3616675">source as a gist</a> below. Each passage that I want to collapse, I give an id. Then I create an element with the same id but preceded by an underscore. The CSS below hides elements with ids starting with underscores, and the JS below uses JQuery to handle the swapping in and out of elements. If you're blogging with Tumblr, just paste the code into your theme and you're good to go! Anywhere else, it should be as simple as adding the JS and CSS to your page.
</p>

<p id="cbp_tryit">Try it. You'll like it.</p>
<p id="_cbp_tryit">Inspired to try blogging by a few of my friends: <a href="http://www.dskang.com">Dan Kang</a> and <a href="http://www.harvestzhang.com">Harvest Zhang</a>. Thanks guys! Keep on writing!</p>

<a href="http://news.ycombinator.com/item?id=4477488">Discuss on hacker news.</a>

<script src="https://gist.github.com/dbieber/3616675.js"></script>
