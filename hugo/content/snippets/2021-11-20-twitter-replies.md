+++
title = "Organizing a Twitter Discussion: Gathering Twitter Replies"
date = 2021-11-20T00:00:00
tags = ["note-taking", "twitter", "python", "messager"]
+++

I [tweeted](https://twitter.com/Bieber/status/1461128201485402112) about spaced repetition earlier this week, sharing and summarizing [my latest snippet on the subject](/snippets/2021-11-02-improvements-to-spaced-repetition/). A bunch of people left thoughtful replies, and I was quite pleased with the discussion. Now I want to look over the discussion holistically, but I don't see a great way to do this. I don't even see a way to look at all the replies to my thread in one place. I want to see not just this, but also replies to replies. TweetDeck might be able to help, but I don't see how.

I think what I'd like to do is write a little script that takes a tweet as input, and outputs links to all the replies and replies to replies in a little tree that I can put into Roam.
Then I can make notes on the full thread, and even link together different parts of the conversation.

Let's give this a try.

```python
import twython
from messager import settings

client = twython.Twython(
        settings.TWITTER_CONSUMER_KEY,
        settings.TWITTER_CONSUMER_SECRET,
        settings.TWITTER_ACCESS_TOKEN,
        settings.TWITTER_ACCESS_TOKEN_SECRET)

def get_replies(status_id):
  status = client.lookup_status(id=status_id)[0]
  return get_replies_to_status(status)

def get_replies_to_status(status):
  status_id = status['id']
  screen_name = status['user']['screen_name']
  results = client.search(
      q=f'to:{screen_name}', sinceId=status_id, count=128)
  candidates = results['statuses']
  replies = []
  for candidate in candidates:
    if candidate['in_reply_to_status_id'] == status_id:
      replies.append(candidate)
  return replies

def get_recursive_replies(status_id):
  status = client.lookup_status(id=status_id)[0]
  all_replies = []
  to_search = [status]
  searched = set()
  while to_search:
    status = to_search.pop()
    if status['id'] not in searched:
      replies = get_replies_to_status(status)
      all_replies.extend(replies)
      to_search.extend(replies)
      searched.add(status['id'])
  return all_replies

status_id = 1461128201485402112
replies = get_recursive_replies(status_id)
```

Aside: I would love for this file (the markdown file I'm writing this snippet in) to double as a Python file.
When I run it, just the Python code block(s) would get run.

To my surprise the Twitter API did not make it easy to query for replies to a tweet. So, I'm using the workaround on display above.
To get all replies to a tweet, I query for all tweets to the tweet author, and then filter for those that are actually replies.
Since the number of search results is limited, this might not always work; it depends on what order Twitter decides to sort tweets by. If Twitter returns the oldest tweets first, this method will work consistently.

It does seem to be working for now, fortunately. There are 60 recursive replies to my tweet, and with this method I was able to lay them all out in a row. Pasting the urls into Roam, I find the default rendering of each tweet in Roam takes up a bit too much space though and provides too much context. So, I may need to modify the display a bit more.

My hope is that I can lay out the entire conversation compactly, and then start marking it up with my own notes, e.g. tagging replies that express similar ideas so I can reply to them together rather than individually.
