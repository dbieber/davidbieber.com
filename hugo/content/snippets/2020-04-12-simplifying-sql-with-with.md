+++
title = 'Simplifying SQL Queries with "WITH"'
date = 2020-04-12T01:00:00
tags = ["browser-history", "sql"]
+++

In the ["More Browser History Queries" snippet](/snippets/2020-04-11-browser-history-queries/) one of the SQL queries I wrote was particularly nasty.

Since I didn't know how to introduce intermediate variables, I had to replicate subqueries multiple times throughout the query. The result was a mess of a query. Using `WITH` clauses, the query becomes considerably more readable and maintainable.

## Cleaned up Query

Here's the cleaned up query. It selects all the GitHub repos you've visited from your browser history. To run it, first copy your browser history and open it in sqlite:

```bash
cp ~/Library/Application\ Support/Google/Chrome/Default/History ~/my-history
sqlite3 ~/my-history
```

Then, you can run this cleaned up query to see all the GitHub repos that you've visited.

```sql
WITH
data1 as (select LENGTH("https://github.com/") as len, * from urls),
data2 as (select SUBSTR(
  url,
  len + 1,
  INSTR(SUBSTR(url, len + 1), "/") - 1
) as user, * from data1),
data3 as (select SUBSTR(url, len + LENGTH(user) + 2) as rest, * from data2),
data4 as (select SUBSTR(rest, 0, INSTR(rest, "/")) as repo, * from data3)

select DISTINCT
SUBSTR(url, len + 1, LENGTH(user) + 1 + LENGTH(repo)) as user_repo
from data4
where url like "https://github.com/%"
and LENGTH(repo) > 0
limit 50;
```

## The Original Query

Here is the original query, with all its messy replicated subqueries, to emphasize just how much using `WITH` allowed me to clean this up.

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

The two queries should produce the same results.
