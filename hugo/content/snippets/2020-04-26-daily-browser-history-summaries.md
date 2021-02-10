+++
title = "Daily Summaries of Browsing History"
date = 2020-04-26T00:00:00
tags = ["browser-history", "sql", "python"]
+++

Over the [course](/snippets/2020-04-12-simplifying-sql-with-with/) [of](/snippets/2020-04-20-browser-history-date-queries/) [multiple](/snippets/2019-12-30-analyzing-my-browser-history/) [previous](/snippets/2020-03-19-browsing-history/) [snippets](/snippets/2020-04-11-browser-history-queries/), I put together several SQL queries for analyzing my browsing history.

Today, I wanted to write a script to run several of these queries in sequence to assemble a nice summary of my daily browsing histories. Maybe I'll dump the summary into my [`[[Roam Research]]`](https://roamresearch.com/#/app/commons-db/page/wYVaowjId) database so I can cross-link ideas with websites I've visited.

As a first pass, I tried to throw together a quick bash script to string the queries together. It looked a bit like this:

```bash
date=$1
if [ -z $1 ];
then
  date=$(date '+%Y-%m-%d');
fi

cp ~/Library/Application\ Support/Google/Chrome/Default/History ~/Default-History
cp ~/Library/Application\ Support/Google/Chrome/Profile\ 1/History ~/Profile-1-History

function query() {
  sqlite3 ~/Default-History $1;
  sqlite3 ~/Profile-1-History $1;
}

echo \# YouTube Videos Watched
echo

query << SQL
select DISTINCT REPLACE(REPLACE(urls.title, " - YouTube", ""), "(1) ", ""), urls.url, "$date%"
from urls
where urls.url like "%www.youtube.com/watch%"
and datetime(last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch')
LIKE "$date%"
limit 50;
SQL

# Additional queries ran here...
```

You'll notice a few things:

1. I want to run each query on two different Chrome histories.
2. I want the script to be parameterized by the date, defaulting to today if no date is specified.

If you're proficient in Bash, you may also notice something else; it doesn't work. The query is only used properly when I run sqlite3 on the first Chrome History, but an empty query is passed to the second query.

Rather than debug my Bash script, I switched over to Python. I used Python Fire to automatically expose all my functions as commands so within minutes I had a working CLI.

Here's what the Python script looks like:

```python
import datetime
import os
import subprocess

import fire


def copy_histories():
  check_output = subprocess.check_output
  check_output([
      'cp',
      os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/History'),
      os.path.expanduser('~/Default-History')])
  check_output([
      'cp',
      os.path.expanduser('~/Library/Application Support/Google/Chrome/Profile 1/History'),
      os.path.expanduser('~/Profile-1-History')])


def run_query(query):
  call = subprocess.call
  call(['sqlite3',  os.path.expanduser('~/Default-History'), query])
  call(['sqlite3', os.path.expanduser('~/Profile-1-History'), query])


def run(date=None):
  copy_histories()
  date = date or datetime.datetime.now().strftime('%Y-%m-%d')

  print('## YouTube Videos Watched')
  print()

  run_query(f"""
  select DISTINCT REPLACE(REPLACE(urls.title, " - YouTube", ""), "(1) ", "")
  from urls
  where urls.url like "%www.youtube.com/watch%"
  and datetime(last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch')
  LIKE "{date}%"
  limit 50;
  """)

  # Additional queries run here...

if __name__ == '__main__':
  fire.Fire()
```

At the command line I run this with `python historyquery.py run` or `python historyquery.py run --date=2020-04-26`.

With Python Fire I was able to quickly switch to a syntax I was more comfortable with, but keep the benefits of working from the context of a shell. I can now much more quickly make improvements to the script since I can operate more efficiently working in Python.

Now I have a script I can run that will produce a nice summary of my internet browsing activity for any date I specify. Running it over recent dates provides a nice walk down memory lane.
