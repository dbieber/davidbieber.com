+++
title = "Distraction detection: Proto acquired!"
date = 2021-01-08T00:00:00
uid = "js34VMN3G"

+++

I'm __inching__ my way toward writing a distraction detector that will allow Bieber Bot to notice when I'm distracted on my phone and stage an intervention. (Wow!, I first pitched this idea (to myself) [in one of my very first snippets](/snippets/2019-12-30-analyzing-my-browser-history/), back in 2019.)

Most recently [I figured out where Chrome's "Tabs from other devices" data is stored](/snippets/2021-01-01-programmatically-accessing-chromes-tabs-from-other-devices-data/). However, I couldn't parse the data because I didn't know what the protocol buffer definition being used was.

Today, I heard back from someone who works on Chrome. I've acquired the proto definitions!

The [proto definitions are here](https://source.chromium.org/chromium/chromium/src/+/master:components/sync/protocol/session_specifics.proto) and [the code that persists the data to disk is here](https://source.chromium.org/chromium/chromium/src/+/master:components/sync_sessions/session_store.cc). I can successfully bulid the protos (using protoc) and I can parse my session data from the leveldb database. Progress!

The trouble now is my phone seems to have stopped syncing its tabs two days ago. Weird! One more mystery to solve I guess...
