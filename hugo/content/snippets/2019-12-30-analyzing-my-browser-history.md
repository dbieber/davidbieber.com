+++
title = "Planning to Analyze My Browsing History"
date = 2019-12-30T00:00:00

summary = "I'm planning to analyze my browser history. This is my plan."
+++

I've learned recently that programmatically accessing your browsing history is rather straightforward. Really exciting! This is rich data, from which I think I'll be able to learn a lot and hopefully combat unwanted distractions.

First let me describe what information is available, and how you can access it. Then, let's discuss what you can do with this data. As I've written about previously [[1]](/projects/bieber-bot/) [[2]](https://davidbieber.com/post/2019-12-29-track-your-life-in-a-spreadsheet/), I already have a chat bot system in place, which will be able to take advantage of this data to e.g. help me stay focused.


#### Accessing Your Browser History

Thank you to GitHub user [dropmeaword](https://github.com/dropmeaword) for compiling [this gist](https://gist.github.com/dropmeaword/9372cbeb29e8390521c2) explaining how to access your browser history via sqlite3. The gist covers Safari, Chrome, and Firefox. In this post, I'll just focus on Chrome on OSX, since that's my primary mode of browsing.

My Chrome browsing history is located at `~/Library/Application Support/Google/Chrome/Default/History`. Since I use multiple profiles in Chrome, each profile gets its own browsing history, e.g. located at `~/Library/Application Support/Google/Chrome/Profile 1/History`. 

Each browsing history is stored as a sqlite3 database. Before analyzing the data, I recommend making a copy of it (`cp ~/Library/Application\ Support/Google/Chrome/Default/History my-history`); this way your history database (a) wont be locked by Chrome while you're trying to access it, and (b) wont change while you're looking at it, which could cause confusion and inconsistencies in your results.

This means you can browse it interactively using the sqlite3 REPL by running `sqlite3 PATH_TO_DATABASE`.

There are also libraries available for accessing sqlite3 databases in just about every language. For Python, there's the [sqlite3](https://docs.python.org/3/library/sqlite3.html) library. Go has [go-sqlite3](https://godoc.org/github.com/mattn/go-sqlite3). JavaScript has [this sqlite3 module](https://www.sqlitetutorial.net/sqlite-nodejs/). However you most like scripting, you'll have a familiar way of accessing the data.

#### The Available Data

Running sqlite3 macro `.tables`, we see the following tables are available.

| | | |
|---|---|---|
|downloads              |  meta                      |urls  |                   
|downloads_slices       |  segment_usage             |visit_source  |           
|downloads_url_chains   |  segments                  |visits  |                 
|keyword_search_terms   |  typed_url_sync_metadata |  |

We'll be most interested in the `urls` and `visits` tables.

The `urls` table has these columns (found with `.schema urls`):

| Column | Type | Description |
|----------------|--------|---|
|id              | Integer Id | The `id` of the URL in the database. |
|url             | Text       | The URL of the website. |
|title           | Text       | The title of website. |                 
|visit_count     | Integer    | The number of times you've visited the URL. |
|typed_count     | Integer    | The number of times you've visited the URL by typing in the address (as opposed to by following a link.) |
|last_visit_time | Integer (milliseconds since the epoch)       | The time of the most recent to the URL. |
|hidden          | Boolean    | I'm not sure what this is about. |

And the `visits` table has these columns (obtained via `.schema visits`):

| Column | Type | Description |
|----------------|--------|---|
|id                               | Integer Id | The `id` of the visit in the database. |                   
|url                              | Integer Id | The `id` of the url in the `urls` table. |           
|visit_time                       | Integer (milliseconds since the epoch) | The time of the visit. |                 
|from_visit                       | Integer Id | The `id` of the visit that lead you to this one. |
|transition                       | Bit vector | Represents the [transition type](https://developer.chrome.com/extensions/history#transition_types) (how you got to the URL) |
|segment_id                       | Integer Id | The `id` of the segment in the database. I'm not quite sure what a segment is, but there is a `segments` table you can look at. |
|visit_duration                   | Integer (microsecodns) | The amount of time spent at the website, or 0 if not available. |
|incremented_omnibox_typed_score  | Boolean    | I do not know what this is about. |


As you can see, we can access every visit to every website that we've made since the last time we cleared our browsing history. We can see what website we visited (`visits.url`), when we visited it (`visits.visit_time`), how many times we've visited it (`urls.visit_count`), and how long each visit was (`visits.visit_duration`).

We can even use `visits.from_visit` to figure out what website linked us to each url, if that interests us.


#### What Can We Deduce?

We can (1) perform a historical analysis on the data, as well as (2) do real-time monitoring of the data.

Here I brainstorm some of the historical trends we will be able to uncover:

- Most frequently visited websites
- Websites where we spend the majority of our time
- Websites that frequently lead to known-distractor websites (e.g. Reddit, Hacker News, Twitter, YouTube)
- We can do an analysis by time of day (or day of week), to figure out what sites occupy my time late at night vs during daylight hours.

These are somewhat interesting, but what I'm particularly excited for is the ongoing analysis that [Bieber Bot](/projects/bieber-bot) can provide by accessing the data.

Here is a brainstorm of the more real-time actionable insights we might extract from this data.

- Bieber Bot could ping me if it looks like I'm spending too much time on a distraction website.
- He could try to detect if I went to a website with a particular purpose, but ended up getting distracted and not completing the purpose I set out to do.

For example, if I'm on a productive website and then switch to a distraction website for more than a few minutes, particularly during work hours, Bieber Bot might message asking if I got distracted. Think you could do that for me Bieber Bot?

- I could signal that I want to view a website later by opening it and immediately closing it again.
- Perhaps we could detect if I'm researching a particular topic, and then Bieber Bot could try to help me with my research.


#### Related Idea

In order to reduce distractions, I'd like to be able to switch my browsing mode from "clicking opens links" to "clicking saves a link for later". When in this new mode, whenever I click a link it wouldn't open that link; instead, it would save the link to a list of deferred links.
Then I would be able to view my "saved for later" links when I have time that I've explicitly set aside, rather than during the time that I would rather be doing something more productive.


#### Next Steps

So far I've done a little bit of manual exploration of my browsing history data. I've set up a little Python script to be able to access the data programmatically.

Next, I'll do more manual analysis, and then I'll see if I'm able to give Bieber Bot the real-time access to the data that I described above. I'm particularly excited to see if I can get the "looks like you've gotten distracted" messages set up with Bieber Bot. As a bonus, since Bieber Bot can message other people too, this system could help me leverage social accountability to stay on task.


Want to see where this project leads? You can subscribe for infrequent email updates.

{{<mailchimp>}}
