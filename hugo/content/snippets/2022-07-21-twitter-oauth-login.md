+++
title = "Logging into a Twitter App with OAuth"
date = 2022-07-21T00:00:00
tags = ["twitter", "tech-tips"]
+++

You can log into a Twitter app with OAuth using Twython. First, make sure you have twython pip installed (`pip install twython`). Then, get the APP_KEY and APP_SECRET from the developer. This is labeled "API Key and Secret" on the app page at https://developer.twitter.com/en/portal/apps/.

Next, run the following Python code:

```python
import twython

client = twython.Twython(APP_KEY, APP_SECRET)
auth = client.get_authentication_tokens(callback_url='oob')

oauth_token = auth['oauth_token']
oauth_token_secret = auth['oauth_token_secret']
auth_url = auth['auth_url']

print(auth_url)
```

Navigate to the printed URL. Copy the pin.

Then run:
```python
pin = 'YOUR_COPIED_PIN'
client_full = twython.Twython(
    APP_KEY, APP_SECRET, oauth_token, oauth_token_secret)

auth = client_full.get_authorized_tokens(pin)

oauth_token = auth['oauth_token']
oauth_token_secret = auth['oauth_token_secret']
user_id = auth['user_id']
screen_name = auth['screen_name']
```

Voila! oauth_token and oauth_token_secret hold the credentials for the logged in account.
The app is now authorized for your account using these credentials.
If the "app" is actually just you using Twython, construct a client with these credentials via:

```python
client = twython.Twython(APP_KEY, APP_SECRET, oauth_token, oauth_token_secret)
```

See also: past-me explains OAuth2 to myself [in more detail here](/snippets/2020-03-20-understanding-oauth2/). It gets easier every time.
