+++
active = false

title = "at Scheduler"
weight = -20150101
date = 2015-01-01T00:00:00

summary = "A minimal command line task scheduler."
tags = ["Software", "Productivity"]
external_link = "https://github.com/dbieber/at-scheduler/"

[image]
  caption = "at-scheduler"
  focal_point = "Smart"
+++

The at-scheduler is a simple command line scheduler.

For installation instructions, see the [README](https://github.com/dbieber/at-scheduler/) on GitHub.

Once it's installed, using the at-scheduler is simple. From your shell, just run a command `at <when> <command>`. This will schedule your command to be run at the time specified.

The syntax for `<when>` is lenient. Specific times like "9:30am" work, as do named dates like "tomorrow at 10pm" or "next Tuesday at 3pm".

The syntax for `<command>` is simply whatever is supported by your shell. Whatever you put for `<command>` will be run in a shell at the time specified.

Learn more on [GitHub here](https://github.com/dbieber/at-scheduler/)!
