+++
title = "Programmatically Accessing Chrome's "Tabs from other devices" Data"
date = 2021-01-01T00:00:00
uid = "CYc8VlO--"

+++

I use Google Chrome on my Mac laptop and on my iPhone, and I'm logged in to my Google account in both places with syncing turned on. If I go to "chrome://history/syncedTabs" on my computer I can see what tabs I have open on my phone. Now, I'd like to access this data programatically.

With the help of `grep`, I've figured out that this data is stored in `~/Library/Application Support/Google/Chrome/Profile 1/Sync Data/LevelDB/` (Probably for most people the path would be `~/Library/Application Support/Google/Chrome/Default/Sync Data/LevelDB/`). Be careful to escape the spaces in the file path!

To read from a LevelDB database, I first installed leveldb with `brew install leveldb`, and then I installed a Python LevelDB client: `pip install plyvel`.

I then use little Python scripts like the following to access the data, though I haven't quite figured out (1) how to properly parse the data; it's probably a protocol buffer, or (2) exactly how it's organized, so I don't know exactly which keys to look at.

Note that I have copied the LevelDB folder to a new location before opening it. This ensures that Chrome doesn't have a lock on any of the files in the copy, and that even if we make a mistake we won't damage Chrome's data.

```python
import plyvel
import re
import os

db = plyvel.DB(os.path.expanduser("~/Profile1/Sync Data/LevelDB/"))

for key, value in db.iterator():
  if b'sessions-dt' in key:
    data = re.findall(b'https?://[\x20-\x7F]+', value)
    if data:
      print(key)
      print(data)
      print()

```

This script prints out the URLs of the synced tabs, plus some extra data and extra characters. To do this properly, the next step will be to figure out how to parse the data.

Why do I want to programmatically figure out which tabs are open on my phone? I want to do automatic distraction detection. When I'm on a distracting website like Twitter for several minutes during a period when I mean to be focusing on something else, I'd like Bieber Bot to be able to stage an intervention to help me focus.

The script above should be good enough for figuring out if I have any distracting websites open on my phone, so I may be able to implement the distraction detection and intervention logic even before getting the parsing done correctly.
