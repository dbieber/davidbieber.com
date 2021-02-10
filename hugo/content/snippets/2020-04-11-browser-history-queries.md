+++
title = "More Browser History Queries"
date = 2020-04-11T01:00:00
tags = ["browser-history", "sql"]
+++

[Previously](/snippets/2020-03-19-browsing-history) I listed out a few queries for poking at my browser history. Here are some more!

As before, I begin by making a copy of my browsing history and opening sqlite3:

```bash
cp ~/Library/Application\ Support/Google/Chrome/Default/History ~/my-history
sqlite3 ~/my-history
```

Once that's done, we can start running the queries.

## YouTube Videos Watched

```sql
select DISTINCT REPLACE(urls.title, " - YouTube", ""), urls.url
from urls
where urls.url like "%www.youtube.com/watch%"
limit 50;
```

## YouTube Search Queries

```sql
select DISTINCT REPLACE(urls.title, " - YouTube", "")
from urls
where urls.url like "%www.youtube.com/results?search_query%"
limit 50;
```

## Google Search Queries

```sql
select DISTINCT REPLACE(urls.title, " - Google Search", "")
from urls
where urls.url like "%www.google.com/search%" 
limit 50;
```

## Google Maps Usage

```sql
select DISTINCT REPLACE(urls.title, " - Google Maps", "")
from urls
where urls.url like "%www.google.com/maps%" 
and urls.title != "Google Maps"
limit 50;
```

## Wikipedia Browsing History

```sql
select DISTINCT REPLACE(urls.title, " - Wikipedia", "")
from urls
where urls.url like "%wikipedia.org/wiki/%"
limit 50;
```

## GitHub Users and Orgs

```sql
select DISTINCT
SUBSTR(
  urls.url,
  LENGTH("https://github.com/") + 1,
  INSTR(SUBSTR(urls.url, LENGTH("https://github.com/") + 1), "/") - 1
) as user
from urls
where urls.url like "https://github.com/%"
limit 50;
```

The rest of the GitHub queries ended up being quite messy, so I've placed them at the end of the document.

## Arxiv Papers Visited

```sql
select DISTINCT urls.title, REPLACE(REPLACE(urls.url, ".pdf", ""), "/pdf/", "/abs/")
from urls
where urls.url like "https://arxiv.org/abs%"
or urls.url like "https://arxiv.org/pdf%"
limit 50;
```

## HackerNews Comments Read

```sql
select DISTINCT REPLACE(urls.title, " | Hacker News", ""), urls.url
from urls
where urls.url like "https://news.ycombinator.com/item%"
limit 50;
```

## HackerNews Posts Read

```sql
select DISTINCT urls.title, urls.url
from visits
join visits as previous_visits on visits.from_visit == previous_visits.id
join urls on urls.id == visits.url
join urls as previous_urls on previous_urls.id == previous_visits.url
where previous_urls.url like "https://news.ycombinator.com%"
and urls.url not like "https://news.ycombinator.com%"
limit 50;
```

## Reddit Usage

```sql
select DISTINCT urls.title
from urls
where urls.url like "https://www.reddit.com/%"
limit 50;
```

## Reddit Links Followed

```sql
select DISTINCT urls.title, urls.url
from visits
join visits as previous_visits on visits.from_visit == previous_visits.id
join urls on urls.id == visits.url
join urls as previous_urls on previous_urls.id == previous_visits.url
where previous_urls.url like "%reddit.com%"
and urls.url not like "%reddit.com%"
limit 50;
```

## Reddit Subreddits Visited

```sql
select DISTINCT
SUBSTR(
  SUBSTR(urls.url, LENGTH("https://www.reddit.com/r/") + 1),
  0,
  INSTR(SUBSTR(urls.url, LENGTH("https://www.reddit.com/r/") + 1), "/")
) as subreddit
from urls
where urls.url like "https://www.reddit.com/r/%"
order by subreddit asc
limit 50;
```

## Twitter Search Queries

```sql
select DISTINCT REPLACE(urls.title, " - Twitter Search / Twitter", "")
from urls
where urls.url like "https://twitter.com/search%"
limit 50;
```

## Twitter Links Followed

```sql
select DISTINCT urls.title, urls.url
from visits
join visits as previous_visits on visits.from_visit == previous_visits.id
join urls on urls.id == visits.url
join urls as previous_urls on previous_urls.id == previous_visits.url
where previous_urls.url like "%://t.co%"
and urls.url not like "%twitter.com%"
and urls.url not like "%://t.co%"
limit 50;
```

## Other Domains Visited

```sql
select DISTINCT REPLACE(
SUBSTR(
  urls.url,
  INSTR(urls.url, "//") + 2, -- strips https://
  INSTR(SUBSTR(urls.url, INSTR(urls.url, "//") + 2), "/") - 1
), "www.", "") as domain
from visits
join visits as previous_visits on visits.from_visit == previous_visits.id
join urls on urls.id == visits.url
join urls as previous_urls on previous_urls.id == previous_visits.url
where not (
     domain like "%goog%"
  or domain like "%t.co%"
  or domain like "%twitter.co%"
  or domain like "%wikipedia%"
  or domain like "%youtube%"
  or domain like "%github%"
  or domain like "%arxiv%"
  or domain like "%reddit%"
  or domain like "%ycombinator%"
  or urls.url like "chrome-extension://%"
  -- or previous_urls.url like "%t.co%"
  -- or previous_urls.url like "%twitter.co%"
  -- or previous_urls.url like "%goog%"
  -- or previous_urls.url like "%reddit%"
  -- or previous_urls.url like "%ycombinator%"
)
limit 50;
```

---

## Using a Different Profile

If you want to query your search history for a profile other than the default one, you can do so. E.g.

```bash
cp ~/Library/Application\ Support/Google/Chrome/Profile\ 1/History ~/my-history
sqlite3 ~/my-history
```

## Messy Queries: GitHub Repos Visited

This query ended up being quite messy because I wasn't able to save intermediate results as a variable. So, in order to build the query, I copied and pasted intermediate queries to reuse them. The result, with intermediate queries shown in comments, follows.

```sql
select DISTINCT

-- Selects the user:
-- SUBSTR(
--   urls.url,
--   LENGTH("https://github.com/") + 1,
--   INSTR(SUBSTR(urls.url, LENGTH("https://github.com/") + 1), "/") - 1
-- ) as user,

-- Selects everything after the user:
-- SUBSTR(
--   urls.url,
--   LENGTH("https://github.com/")
--   + LENGTH(SUBSTR(urls.url,LENGTH("https://github.com/") + 1,INSTR(SUBSTR(urls.url, LENGTH("https://github.com/") + 1), "/") - 1)) -- length(user)
--   + 2
-- ) as rest,

-- Selects the repo:
-- SUBSTR(SUBSTR(
--   urls.url,
--   LENGTH("https://github.com/")
--   + LENGTH(SUBSTR(urls.url,LENGTH("https://github.com/") + 1,INSTR(SUBSTR(urls.url, LENGTH("https://github.com/") + 1), "/") - 1)) -- length(user)
--   + 2
-- ), 0,
-- INSTR(SUBSTR(
--   urls.url,
--   LENGTH("https://github.com/")
--   + LENGTH(SUBSTR(urls.url,LENGTH("https://github.com/") + 1,INSTR(SUBSTR(urls.url, LENGTH("https://github.com/") + 1), "/") - 1)) -- length(user)
--   + 2
-- ), "/")) as repo

SUBSTR(
  urls.url,
  LENGTH("https://github.com/") + 1,
  LENGTH(SUBSTR(
    urls.url,
    LENGTH("https://github.com/") + 1,
    INSTR(SUBSTR(urls.url, LENGTH("https://github.com/") + 1), "/") - 1
  )) -- LENGTH(user)
  + 1 -- + 1
  + LENGTH(SUBSTR(SUBSTR(
    urls.url,
    LENGTH("https://github.com/")
    + LENGTH(SUBSTR(urls.url,LENGTH("https://github.com/") + 1,INSTR(SUBSTR(urls.url, LENGTH("https://github.com/") + 1), "/") - 1)) -- length(user)
    + 2
  ), 0,
  INSTR(SUBSTR(
    urls.url,
    LENGTH("https://github.com/")
    + LENGTH(SUBSTR(urls.url,LENGTH("https://github.com/") + 1,INSTR(SUBSTR(urls.url, LENGTH("https://github.com/") + 1), "/") - 1)) -- length(user)
    + 2
  ), "/")))
  ) -- + LENGTH(repo)
from urls
where urls.url like "https://github.com/%"
and LENGTH(SUBSTR(SUBSTR(
    urls.url,
    LENGTH("https://github.com/")
    + LENGTH(SUBSTR(urls.url,LENGTH("https://github.com/") + 1,INSTR(SUBSTR(urls.url, LENGTH("https://github.com/") + 1), "/") - 1)) -- length(user)
    + 2
  ), 0,
  INSTR(SUBSTR(
    urls.url,
    LENGTH("https://github.com/")
    + LENGTH(SUBSTR(urls.url,LENGTH("https://github.com/") + 1,INSTR(SUBSTR(urls.url, LENGTH("https://github.com/") + 1), "/") - 1)) -- length(user)
    + 2
  ), "/"))) > 0  -- LENGTH(repo) > 0
limit 50;
```

For most of the queries on this page, you should be able to easily modify them to suit your needs. 
I wouldn't try modifying this query, though. It would be much better to build a new query from scratch using using the same technique this one was built with, than to try to modify this one to perform another task, because it would be so easy to modify something in one place but subtly miss modifying it in another location in the query that needs to also be modified.

Update (April 12, 2020): I've now learned that you can introduce intermediate "variables" in your SQL queries, so I've simplified this query [here](/snippets/2020-04-12-simplifying-sql-with-with).
