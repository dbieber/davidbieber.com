+++
title = "Date and Time Browser History Queries"
date = 2020-04-20T00:00:00
tags = ["browser-history", "sql"]
+++

I wrote a [number of SQL queries](/snippets/2020-04-11-browser-history-queries/) for browsing my browsing history. In this snippet, I show how to amend them to filter the results by date. Google Chrome selects a slightly non-standard time storage format (microseconds since January 1, 1601 UTC), hence the need for this query stanza.

To run these queries, first make a copy of your browser history and open it in sqlite3.

```bash
cp ~/Library/Application\ Support/Google/Chrome/Default/History ~/my-history
sqlite3 ~/my-history
```

## Google Search History for Specific Date

Here's the query we had from before, for accessing our Google Search history.

```sql
select DISTINCT REPLACE(urls.title, " - Google Search", "")
from urls
where urls.url like "%www.google.com/search%" 
limit 50;
```

To filtering by a specific date, we just add.

```sql
AND
datetime(last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch')
LIKE '2019-12-25%'
```

What was I searching for on Christmas last year?

```sql
select DISTINCT REPLACE(urls.title, " - Google Search", "")
from urls
where urls.url like "%www.google.com/search%" 
and datetime(last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch')
LIKE '2019-12-25%'
limit 50;
```

## YouTube Videos Watched Today

To query for results from _today_, we can do the following.

```sql
select DISTINCT REPLACE(urls.title, " - YouTube", ""), urls.url, datetime(last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch') as d
from urls
where urls.url like "%www.youtube.com/watch%"
and datetime(last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch')
LIKE (date('now', 'localtime') || '%')
limit 50;
```

Note the use of `localtime` to account for the timezone. `||` is used here for string concatenation.

## Arxiv Papers Visited Last Month

```sql
select DISTINCT urls.title, REPLACE(REPLACE(urls.url, ".pdf", ""), "/pdf/", "/abs/")
from urls
where (urls.url like "https://arxiv.org/abs%"
or urls.url like "https://arxiv.org/pdf%")
and datetime(last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch')
LIKE (substr(date('now', 'localtime', '-1 month'), 0, 9) || '%')
limit 50;
```

Here you can see that `date` gives flexibility in adjusting the date you are requesting. `substr` is used to transform `2020-03-20` to `2020-03-`, to match any date in the month.

## HackerNews Links Followed in the Last Week

```sql
select DISTINCT urls.title, urls.url
from visits
join visits as previous_visits on visits.from_visit == previous_visits.id
join urls on urls.id == visits.url
join urls as previous_urls on previous_urls.id == previous_visits.url
where previous_urls.url like "https://news.ycombinator.com%"
and urls.url not like "https://news.ycombinator.com%"
and datetime(visits.visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch')
> date('now', 'localtime', '-7 day')
limit 50;
```

For this query, we directly compare the result of `datetime` and `date`.
[sqlite.org/lang_datefunc.html](https://www.sqlite.org/lang_datefunc.html) has more useful information about writing queries manipulating dates and times.

For more query ideas, here's the [link back to the browser history queries snippet](/snippets/2020-04-11-browser-history-queries/).
