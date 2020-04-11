+++
title = "A Bit of Browser History Analysis"
date = 2020-03-19T00:00:00
+++

In a [previous snippet](/snippets/2019-12-30-analyzing-my-browser-history) I started looking into how to analyze my browser history. Revisiting that idea tonight, I began looking into whether I might be able to infer topics of interest from my browsing history.

Using my previous post as reference, I first made a copy of my browsing history:

```bash
cp ~/Library/Application\ Support/Google/Chrome/Default/History ~/my-history
```

Then, using sqlite3 (`sqlite3 ~/my-history`) I began poking around.

This query allowed me to pull up all my YouTube video views:

```sql
select visits.id, urls.title, urls.url
from visits
join urls on urls.id == visits.url
where urls.url like "%www.youtube.com/w%"
limit 50;
```

And this query gave me my Google Search history:

```sql
select visits.id, urls.title
from visits
join urls on urls.id == visits.url
where urls.url like "%www.google.com/search%" 
limit 50;
```

This one gave me my Wikipedia browsing history:

```sql
select distinct urls.title 
from visits
join urls on urls.id == visits.url
where urls.url like "%wikipedia.org/wiki/%"
limit 50;
```

I think it will be useful to bring in the contents of the URLs too, not just the title and url string, for determining topics of interest. Even without that, my Google Search history, YouTube history, and Wikipedia history are already an interesting start.
