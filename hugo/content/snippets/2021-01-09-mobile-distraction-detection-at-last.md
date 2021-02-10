+++
title = "Mobile Distraction Detection, at last"
date = 2021-01-09T00:00:00
uid = "yZgMHS8UV"
tags = ["attention", "browser-history", "taking-silly-ideas-seriously"]

+++

I have implemented a minimal working version of mobile _distraction detection_, complete with a simple intervention for when I visit distracting websites on my phone.

## What does "distraction detection" do?

It runs on my laptop and monitors my _phone_ for when I visit distracting websites. I give it a list of distracting websites for it to keep an eye out for. My list is: twitter, facebook, hacker news, google news, reddit, and youtube.

I can set it to perform some action whenever I'm on one of these websites. For this first iteration, I'm having Bieber Bot message me whenever it notices I'm on one of these websites. Now that it's working though, it will be easy to customize to my liking.

In future iterations, I'll have it wait until I've been spending several minutes on the website before messaging me, and I'll only have it do this during times when I mean to be focused.

## Why is this interesting?

There are excellent browser extensions that help you take control of your browsing habits on your computer. I recommend DK's [Intention](https://getintention.com) for this. However, there aren't great solutions like Intention for mobile browsing.

The challenge is that mobile browsers don't provide good ways for developers to write extensions. I've built my mobile distraction detector in spite of this limitation :).

## How does it work?

I use an iPhone and the Chrome browser. I'm logged into my Google Account on Chrome on both my phone and my laptop, and I have tab syncing turned on. With tab syncing, all my tab sessions from my phone are synced to my Google account, and are visible on my laptop, usually with a sub-minute latency. You can view this data in human-readable form at [chrome://history/syncedTabs](chrome://history/syncedTabs).

The tab session data is stored along with the rest of my Chrome data. Since I use a Mac, the path is `~/Library/Application\ Support/Google/Chrome/Profile\ 1/Sync\ Data/LevelDB/`. Note that "Profile 1" may be replaced with either "Default", or the name of your Profile, depending on how many Google accounts you have connected with Chrome.

The data is stored in a LevelDB database (this is unusual for Chrome; most of the rest of your Chrome data is stored in sqlite3 databases). LevelDB is an efficient key-value store, which was written by Jeff Dean and Sanjay Ghemawat back in 2011. The keys which contain the synced tab data are those prefixed with "session-dt". The corresponding values are `SessionSpecifics` protocol buffers. [The protocol buffer definition is available here](https://source.chromium.org/chromium/chromium/src/+/master:components/sync/protocol/session_specifics.proto).

Before parsing the sync data, I always make a copy of it first, and then I only ever open the copy. This ensures that Chrome doesn't have a lock on the database, and isn't editing it concurrently with my own program reading it.

I use the Python library `plyvel` to parse the LevelDB database: `db = plyvel.DB(path_to_copy_of_leveldb_directory)`.

In order to use the protobuf definition, I compiled it first with protoc: `protoc -I chromium/ chromium/components/sync/protocol/*.proto --python_out=dbieber/distraction_detection/`

Putting these pieces together, accessing the session data looks like this:

```python
import plyvel
from components.sync.protocol import session_specifics_pb2

db = plyvel.DB(path)

for key, value in db.iterator():
  if b'sessions-dt' in key:
	session = session_specifics_pb2.SessionSpecifics.FromString(value)

db.close()
```

From here, the key remaining piece to understand is how to figure out which tabs are open on which devices.

Each of the SessionSpecifics protos has an attribute: `session_tag` which uniquely identifies a session. For each `session_tag`, there is a single SessionSpecifics proto with a `client_name` attribute: this indicates which device the session lives on. Each of the remaining SessionSpecifics protos with that same tag correspond to a single tab, and the currently open URL for that tab comes from `session.tab.navigation[-1].virtual_url`.

From there, it's just a matter of matching the URLs against my list of distracting websites, and sending the data off to Bieber Bot. Distractions, detected. :D

## What next?

I'll tweak my own distraction detection setup to something that makes sense for me. Instead of immediate messages from Bieber Bot, I'll have him try to keep my total senseless scrolling for a day to a moderate amount. I'll have him be particularly vigilant about helping me keep my morning scrolling from going on too long.

I'll also send this snippet around to folks interested in building similar tools. While I won't be turning this into a product for the masses, I'm hopeful that the method does get picked up by projects like Intention, ActivityWatch, and other tools that aim to help people maintain healthy browsing habits.

I don't think it's common knowledge that with account syncing, rich data about your mobile browsing is available on your computer. So today, there isn't much tooling that takes advantage of this. If you work on a product in this space, well, now you've had a glimpse of what data's available and what it can do. Consider using this approach to extend the reach of your product.
