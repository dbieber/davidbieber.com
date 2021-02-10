+++
title = "Accessing Your iMessages with SQL"
date = 2020-05-20T00:00:00
tags = ["sql"]
keywords = ["messager"]
+++

If you use a Mac and use iMessage, you can access your iMessages programmatically. They are stored by iMessage as a sqlite database, which you can easily access.

## Accessing the Database

The database is typically stored at `~/Library/Messages/chat.db`, though that location is configurable.

If you try to access the database, however, you will likely encounter this unhelpful error message: `~/Library/Messages/chat.db: Operation not permitted`

Thankfully, OSXDaily has put together a [helpful step by step guide to resolving this error](https://osxdaily.com/2018/10/09/fix-operation-not-permitted-terminal-error-macos/), which I'll summarize here:

1. Navigate to your `System Preferences > Security & Privacy > Privacy > Full Disk Access` settings.

2. Use the Lock and `+` symbol to give full disk access to the Terminal App (located in `Applications > Utilities > Terminal`).

3. You may need to relaunch Terminal for the change to take effect; I did not.

Once you've done this, you can start poking around at your iMessages programmatically.

## Taking a Look Around

I begin with making a backup:

`cp ~/Library/Messages/chat.db ~/chat.db`

Now I open the database with sqlite3.

`sqlite3 ~/chat.db`

I run `.tables` to see what tables there are:

| | |
|---|---|
|_SqliteDatabaseProperties  | kvtable                    |
|attachment                 | message                    |
|chat                       | message_attachment_join    |
|chat_handle_join           | message_processing_task    |
|chat_message_join          | sync_deleted_attachments   |
|deleted_messages           | sync_deleted_chats         |
|handle                     | sync_deleted_messages   |

There are some interesting tables in there: `message` seems most important. It looks like we'll also be able to look up attachments using tables `attachment` and `message_attachment_join`. Strangely, there's a table present for deleted messages, which suggests a sort of "trash can" where messages are not permanently deleted immediately upon deletion.

`.schema message` is the command for viewing the schema of the message table.
We can also jump right in with `SELECT * FROM message;` to see what sort of data is contained within. Sure enough, human readable messages are present.

This will all be interesting to investigate further at a later date.
One perk of understanding this mechanism for me is that I'll be able to write events that are triggered in response to iMessages. This enables me to write custom notification criteria. For example, I can have messages that start "URGENT" notify me immediately, but I can have all other messages programatically withheld from notifying me until 9pm.

This lets me receive the messages at the time and location that I want, rather than at the time Apple chooses for me. Thanks Bieber Bot.
