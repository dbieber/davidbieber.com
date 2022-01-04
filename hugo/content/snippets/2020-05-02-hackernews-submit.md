+++
title = "Posting to Hacker News Programmatically"
date = 2020-05-02T00:00:00
tags = ["python", "taking-silly-ideas-seriously", "messager"]
keywords = ["hacker news", "messager"]
+++

If you run this snippet of Python code, it will submit this ["Snippet"](https://davidbieber.com/snippets/) (the one you're currently reading) to Hacker News.

```python
from html.parser import HTMLParser
import getpass
import requests
import time

USERNAME = (
    ''  # Put your Hacker News username here.
    or getpass.getuser()  # (But if you don't, we'll try a sensible default.)
)
PASSWORD = (
    ''  # We'll prompt you for your password, or you can enter it here.
    or getpass.getpass()
)
# You can reconfigure the title and url to submit here.
TITLE_TO_SUBMIT = 'Posting to Hacker News Programmatically'
URL_TO_SUBMIT = 'https://davidbieber.com/snippets/2020-05-02-hackernews-submit/'

# Login
session = requests.Session()
session.post(
    'https://news.ycombinator.com/login',
    data={
        'acct': USERNAME,
        'pw': PASSWORD,
    },
)

# Get the CSRF token ("FNID")
time.sleep(1)
class FNIDExtractor(HTMLParser):
  fnid = None
  def handle_starttag(self, tag, attrs):
    if tag.lower() == 'input' and ('name', 'fnid') in attrs:
      self.fnid = dict(attrs)['value']
f = FNIDExtractor()
submit_response = session.get('https://news.ycombinator.com/submit')
f.feed(submit_response.text)

# Submit
time.sleep(2)
session.post(
    'https://news.ycombinator.com/r',
    data={
        'title': TITLE_TO_SUBMIT,
        'url': URL_TO_SUBMIT,
        'fnid': f.fnid,
    },
)
```

You can change the title and URL before running this to make a new submission, or run it as is to submit this snippet.

If you try to submit a URL that's already been submitted recently -- such as this snippet -- it won't submit a second time, so no harm done in running this.

To learn more about sessions and see why this works, you can read about them in the [_requests_ documentation](https://requests.readthedocs.io/en/master/user/advanced/).
