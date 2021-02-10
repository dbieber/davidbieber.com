+++
title = "Posting to Hacker News Programmatically"
date = 2020-05-02T00:00:00
tags = ["python", "taking-silly-ideas-seriously"]
keywords = ["hacker news", "messager"]
+++

If you run this snippet of Python code, it will submit this ["Snippet"](https://davidbieber.com/snippets/) (the one you're currently reading) to Hacker News.

```python
import getpass
import requests

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
URL_TO_SUBMIT = 'davidbieber.com/snippets/2020-05-02-hackernews-submit/'

session = requests.Session()
session.post(
    'https://news.ycombinator.com/login',
    data={
        'acct': USERNAME,
        'pw': PASSWORD,
    }
)
session.post(
    'https://news.ycombinator.com/submit',
    data={
        'title': TITLE_TO_SUBMIT,
        'url': URL_TO_SUBMIT,
    }
)
```

You can change the title and URL before running this to make a new submission, or run it as is to submit this snippet.

If you try to submit a URL that's already been submitted recently -- such as this snippet -- it won't submit a second time, so no harm done in running this.

To learn more about sessions and see why this works, you can read about them in the [_requests_ documentation](https://requests.readthedocs.io/en/master/user/advanced/).
