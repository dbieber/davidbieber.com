+++
title = "SQL for the Kangaroo Auto-responder"
date = 2021-01-30T00:00:00
uid = "b8DWPQEND"

+++

I turned on the [Kangaroo Auto-responder](/snippets/2021-01-29-kangaroo-auto-responder/) this morning. The rules for when to send a kangaroo 🦘 are as follows:

You get a kangaroo if the **most-recent** message in our chat (ignoring trivial messages from you) is **non-trivial**, **read-by-me**, **written-by-you**, **not a response**, and **eight-hours old**.

Let's look at each of these criteria in more detail.

## Most-recent message

The criteria are being applied to the most recent message in our chat ignoring trivial messages from you.

In SQL, this looks like

```sql
select thread_id, max(timestamp) as timestamp
from messenger
where (author = '1409114395' or (author <> '1409114395' and LENGTH(text) > 15))
group by thread_id;
```

1409114395 is my Facebook ID.

This query selects the most recent timestamp from only a single message in each thread. It considers all messages from me, but only non-trivial (more than 15 characters) messages from the other participant.

The reason for this is that if I have sent the most recent message in a conversation (regardless of the length of the message), then no kangaroo is needed. If the other person has sent the most recent message, a kangaroo might be in order, but trivial messages should not trigger kangaroos. So we ignore them, and see if the most recent message is still from the other person even when ignoring their trivial messages.

## Non-trivial

We choose 15-characters as the threshold for what makes a message trivial. The reason we ignore trivial messages is because they often don't warrant a response. I am considering removing this constraint, as the "Not a response" constraint seems to obviate the need for it.

This shows up as `LENGTH(text) > 15)` in the query.

## Read-by-me

Unfortunately I do not have read receipt information in my messages database, so I did not include this rule in the first version of the Kangaroo Auto-responder.

## Written-by-you

Only if the most recent message is from you is a kangaroo necessary. If its from me, I've already responded!

In this query, this is a simple check:

```sql
WHERE messenger.author <> '1409114395'
```

## Not-a-response

This is an interesting piece. When I wrote out the rules for the auto-responder yesterday, I was thinking I'd ignore messages sent within 5 minutes of a message I sent. My thinking was that this small filter would prevent me from needing to get the last word in every conversation to avoid oversending of kangaroos.

Now, I'm thinking I'll ignore messages sent within _36 hours_ of a message I sent. This is a much tighter restriction. It means that I may miss sending some kangaroos that I ought to have sent, but it also means that if someone takes two hours to reply to me and that's the end of the conversation, I don't need to reply to prevent a kangaroo from going out.

It seems like striking a good balance between the non-trivial message criteria and the not-a-response criteria is key, and I may adjust these going forward.

To determine if a message is a response, I first determine the time of my own most recent message in the chat. In SQL, this is:

```sql
select thread_id, max(timestamp) as outgoing_timestamp
from messenger
where author = '1409114395' -- my FB id
group by thread_id;
```

I then compare this message's timestamp with that of the most recent message in the thread, which we selected earlier:

```sql
(  -- The reply is at least X minutes after my latest message.
  (latest_messages.timestamp - outgoing_timestamp)/1000 > 36*60*60
  or outgoing_timestamp IS NULL
)
```

## 8-hours old

The final criteria for whether to send a kangaroo is that the message must be eight hours old. Yesterday I was initially planning for 2-hours old, but I decided to give myself more time to respond manually before the kangaroo would go out. Here's the SQL for that:

```sql
-- Message is 8 hours old:
AND NOW() - to_timestamp(messenger.timestamp/1000) at time zone 'UTC' > INTERVAL '8 HOURS'
AND NOW() - to_timestamp(messenger.timestamp/1000) at time zone 'UTC' < INTERVAL '8.25 HOURS'

```

## Putting it all together

Here's the complete SQL query that finds messages which warrant an automated kangaroo response.

```sql
-- Select the most recent message per thread
-- (ignoring trivial messages from you),
-- and the most recent message per thread specifically from me.
-- If the most recent message (ignoring trivial messages from you)
-- is non-trivial,
-- written-by-you,
-- not a reply to my message,
-- and a specific age,
-- then we've got ourselves a Kangaroo!
--
-- In a future iteration we will also ensure the message has been read-by-me.

SELECT * FROM

-- The first sub-query:
-- Selects the most recent message from each thread that is either:
-- (A) from me, or (B) from you and non-trivial in length
-- And is also less than 8 hours old.
((select thread_id, max(timestamp) as timestamp
 from messenger
 where (author = '1409114395' or (author <> '1409114395' and LENGTH(text) > 15))
 -- and to_timestamp(timestamp/1000) at time zone 'UTC' > NOW() - INTERVAL '800 HOURS'
 group by thread_id) AS latest_messages
INNER JOIN
  messenger
ON
  messenger.thread_id = latest_messages.thread_id AND
  messenger.timestamp = latest_messages.timestamp)
LEFT JOIN
    -- Selects the most recent message from each thread from me:
    (select thread_id, max(timestamp) as outgoing_timestamp
     from messenger
     where author = '1409114395'
     -- and to_timestamp(timestamp/1000) at time zone 'UTC' > NOW() - INTERVAL '800 HOURS'
     group by thread_id) AS latest_outgoing_messages
ON
  messenger.thread_id = latest_outgoing_messages.thread_id
WHERE messenger.author <> '1409114395' -- David Bieber
AND messenger.author <> '1985867351654140' -- Bieber Bot
AND (  -- The reply is at least X minutes after my latest message.
  (latest_messages.timestamp - outgoing_timestamp)/1000 > 36*60*60
  or outgoing_timestamp IS NULL
)
AND thread_type = 'USER' -- Message is a 1:1 chat, not a group chat
-- Message is 8 hours old:
AND NOW() - to_timestamp(messenger.timestamp/1000) at time zone 'UTC' > INTERVAL '8 HOURS'
AND NOW() - to_timestamp(messenger.timestamp/1000) at time zone 'UTC' < INTERVAL '8.25 HOURS'
ORDER BY messenger.timestamp desc;
```

This checks all the criteria for whether a message needs a kangaroo. I've set up a script that runs this query every ten minutes, and sends kangaroos as necessary.

At the time of this writing, no kangaroos have been sent yet. I hope it works 🤞!
