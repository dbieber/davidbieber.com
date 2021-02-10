+++
title = "Facebook Messenger SQL Queries"
date = 2020-04-12T00:00:00
tags = ["sql"]
keywords = ["messager"]
+++

Last week I dumped all my Facebook messenger messages into a Postgres database. I have it set up so that new messages are added the the database in real time as they are sent. Like I did in a [previous snippet](/snippets/2020-04-11-browser-history-queries) for analyzing my browsing history, I'll use this snippet to sketch out some useful queries for analyzing my message history.

## Table Schemas

I have two tables of messages. `messenger_archive` contains all messages from when I first joined Facebook in August 2008 through February 2020. `messenger` contains messages from February 2020 through now, and is updated in real time.

Using the commands `\d messenger` and `\d messenger_archive`, I inspect the table schemas.

### Schema: messenger

|   Column    |   Type  | Description
|-------------|---------|---------
| text        | text    | The message content
| uid         | text    | A unique message id
| author      | text    | The _fbid_ of the message author
| timestamp   | number  | The timestamp in milliseconds
| forwarded   | boolean | Whether the message is a forwarded message
| thread_id   | text    | A unique thread id
| thread_type | text    | GROUP or USER, indicating the thread type

### Schema: messenger_archive

|        Column        |  Type     | Description
|----------------------|-----------|---------
| sender_name          | text      | The message author's name
| timestamp_ms         | number    | The timestamp in milliseconds
| content              | text      | The message content
| type                 | text      | One of: Payment, Call, Share, Generic, Unsubscribe, or Subscribe
| title                | text      | The thread title, often the name of the other participant
| is_still_participant | boolean   | Whether I was still in the conversation at the time of the archive (Feb 2020)
| thread_type          | text      | One of: RegularGroup, Regular
| thread_path          | text      | A unique identifier for the thread

### Schema Caveats

- The `messenger_archive.thread_path` is not the same as the `messenger.thread_id`.
- The `messenger.author` is an integer id, whereas the `messenger_archive.sender_name` is a string name. 
- There may be a few overlapping messages between the two tables (?), and there may be a few messages not captured in either table.

## Message Queries

Let's start sketching some useful queries.

### Finding Links

Listing domains from the archive:

```sql
select distinct
substring(content from '.*://([^/]*)') as domain
from messenger_archive
limit 1000;
```

Counting unique domains:

```sql
select count(*) from (select distinct
substring(content from '.*://([^/]*)') as domain
from messenger_archive) domains;
```

Listing links from the archive:

```sql
select distinct
substring(content from '([a-z]*://[^/\s]*[a-zA-Z/]*)') as domain
from messenger_archive
limit 1000;
```

Counting unique links:

```sql
select count(*) from (select distinct
substring(content from '([a-z]*://[^/\s]*[a-zA-Z/]*)') as domain
from messenger_archive) foo;
```

### Email Addresses

```sql
select distinct
substring(content from '([a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+)') as email
from messenger_archive
limit 100;
```

### Looking Forward

I have a number of additional queries I'd like to write.
However, they will have to wait until a future snippet.
