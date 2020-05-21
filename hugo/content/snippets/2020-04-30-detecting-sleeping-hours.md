+++
title = "Detecting My Sleeping Hours from Data"
date = 2020-04-26T00:00:00
+++

Between my [Chrome browsing history](/snippets/2020-04-20-browser-history-date-queries/) and my [Facebook Messenger message logs](/snippets/2020-04-12-fb-messenger-sql/), I should be able to get a good estimate of when I'm awake and asleep.

Here's a quick attempt using only Messenger data.

```sql
SELECT * FROM
  (SELECT to_timestamp(timestamp / 1000), (timestamp - lag(timestamp) over (ORDER BY timestamp DESC)) / 1000 / 60 / 60 AS diff_hours
   FROM messenger WHERE messenger.author = '1409114395' ORDER BY timestamp DESC LIMIT 100000) AS foo
WHERE diff_hours < -6;
```

Unfortunately, my late night and early morning Messenger usage doesn't appear to be as consistent as I'd imagined, especially since COVID-19 induced shelter-in-place began.
I'll have to introduce additional sources of data if I want to infer good sleep time estimates.
