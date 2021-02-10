+++
title = "Focused Reading Browserflow Flow Idea"
date = 2021-02-02T00:00:00
uid = "BrAgF4Rxw"
plugins_js = ["focus-bar"]
tags = ["Browserflow", "Attention"]
keywords = ["focus bar"]
+++

This idea for an assistive technology for focused reading comes from [accessiBe](https://accessibe.com/). I stumbled upon it on [tasteofhome.com](https://www.tasteofhome.com/recipes/homemade-potato-chips/). The idea is to make the web more accessible to folks with ADHD by dimming the part of the screen they're not actively looking at.

Here's a video of the accessiBe implementation in action on the tasteofhome.com website.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fplayground%2FbF12xbo8EB.gif?alt=media&token=d1cc35a1-8354-4859-9415-7a48e5283310)

As you can see, the screen is dimmed everywhere except on the lines surrounding the mouse pointer. This helps me to regain focus more quickly if my attention is drawn away from the text I was reading.

I find this way of reading helpful, and so I'm thinking about making it for myself as a Browserflow flow. It should be easy enough to do. When the flow starts, it just has to add two large transparent rectangles to the DOM, and an event handler to update their positions whenever my mouse moves.

I'll put up another snippet if and when I build this.

Update Feb 5, 2021: As you may have noticed, I've now implemented this idea. It's enabled on this page, and also available as a Browserflow flow. [See the snippet here](/snippets/2021-02-05-focused-reading).
