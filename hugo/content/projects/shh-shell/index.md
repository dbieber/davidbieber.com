+++
active = false
weight = -20140803

# Project title.
title = "shh Shell"

# Date this page was created.
date = 2014-08-03T00:00:00

# Project summary to display on homepage.
summary = "The soothing shell for while you sleep."

# Tags: can be used for filtering projects.
tags = ["Software", "Productivity"]

[image]
  caption = ""
  focal_point = ""
+++

# The shh shell

The shh shell is a simple shell you can use while you drift off to sleep.

Notably, you can keep your eyes closed while you use it.

The shell is controlled by typing and the only output is audio; there are no visual components of shh. It is designed to minimize the mental energy required for use, to avoid disturbing your attempt at sleep as much as possible.


### Why is it called shh shell?

It's a play on "ssh", a common unix utility that stands for "secure shell". shh (prounced in a whisper, "shhh...") is a quiet shell that takes minimal mental energy to use, great for use while you're drifting off to sleep.


### What can the shh shell do?

My primary use of the shh shell is leaving notes for myself. I also use shh to set peaceful YouTube music alarms for myself, and to check the time without needing to open my eyes.

Here is the full list (as of 2015-11-28) of my uses of shh shell, past and present:

- Leaving notes for myself for the morning
- Checking the time
- Playing YouTube videos (I only hear the audio, of course)
- Google searching and opening webpages
- Setting alarms (usually in the form of songs on YouTube)
- Checking my email
- Sending emails
- Sending iMessages
- Scheduling emails or messages to send in the future
- Making TODOs for myself
- Setting goals for the future
- Performing calculations
- Practicing relative pitch
- Recording audio memos of myself for later
- Executing arbitrary shell commands

The current list of shh commands is [available here](https://github.com/dbieber/shh-shell/blob/master/shh_commands.py).

Of course, not all of these have proven to be useful features. The most useful features for me have been the ability to leave notes for myself for the morning, the ability to check the time without opening my eyes, and the ability to set alarms and listen to music via the shell. The audio memo feature has been occasionally useful too.

At no point did I find the ability to check my email via the shh shell useful.

I did temporarily get good at recognizing pitch intervals, but I have not sustained that ability.


## Is this a replacement for shells like Bash, zsh, and Fish?

No, this is not meant as a full replacement for Bash, zsh, Fish, etc.

That said, it does support arbitrary command execution though, via the `shell` command. That means typing `:shell rm -f important_file` _will_ cause important_file to be removed. So, you have to make sure you're not a self-sabotaging hacker in your sleep before you start using shh as your night time shell.

You can additionally add arbitrary new commands by editing the file [shh_commands.py](https://github.com/dbieber/shh-shell/blob/master/shh_commands.py).


### Where do you use the shh shell?

I use the shh shell by keeping a wireless keyboard in my bed. It is connected to my laptop, which I leave open but with the monitor turned fully off.

This means I'm not at risk of damaging my computer by rolling over on it or drooling on it :).

I leave the volume on my laptop on, so I can hear the shh shell's output, but I never need to open my eyes to use it.


### Can you use it in the shower?

Yes, I sometimes also use shh shell from the shower. I have a waterproof wireless keyboard in my shower. I am mildly embarassed by this.

The keyboard is connected wirelessly to my laptop running the shh shell in another room. There is no computer in the bathroom. For audio, I have a waterproof shower speaker connected via bluetooth to the laptop in the other room. The speaker sits in the shower next to the keyboard, which both rest on a ledge. There is a 3D-printed shaving cream holder nearby.

I know, I hear myself too.


# Using the shh shell

When you open the shh shell on your computer, you get a small black window into which you can type large white text. When you're new to the shell, it can be useful to look at this window to see what you're typing. As you become more experienced with the shh shell, you can turn your monitor off and close your eyes, relying only on the auditory feedback the shell provides.

### Getting in Focus

When you type, it's important that you're typing in the shell. If you're not in the shell, you might be typing in another application on your computer or you might not be typing in an application at all.

To assist with this, the shell will audibly say "focused" when the shell becomes your selected application, and "focus lost" when the shell loses focus. If the shh shell is not in focus, or if you're not sure if the shell is in focus, then use "cmd-TAB" to switch applications until you hear the shell announce "focused". Once you hear this sound, you can safely type knowing that the shell is receiving your input.

### Leaving Notes for Yourself

The default mode of the shell is to act as a notepad and keylogger. Every letter typed and every key pressed is logged with a timestamp when you are in the shh shell. Don't worry, this data is only saved locally and keys aren't logged when you're in other applications, so it's not going to steal your credentials for other apps.

Only if you start a line with `:` does shh interpret the line as a command. So, its unlikely you'll accidentally run commands you don't intend to if you roll over your keyboard while sleeping.

Everything you type will be there waiting for you in the morning, so leave yourself notes, dream diaries, action items, whatever it is that you need to get out of your head so late at night.

Even if you accidentally fall asleep on the delete key, thereby deleting everything you typed (ahh!), in the morning you will still be able to view the notes you typed since every character is logged.


### Running Commands

To run a command, start a new line with a colon (`:`) followed by the command name, and then the command arguments.

For example, type `:help` in the shh shell to get a full list of supported commands.

Some of my favorite commands are `time`, `m` (short for `music`), `say`, and `at`.

Here are some of the commands I'll type frequently:

- `:time`
  - This will cause the shell to read the date and time aloud.
- `:m billy joel`
  - This will immediately cause some Billy Joel music from YouTube to start playing. Most songs and artists should work.
- `:at 9:30am :m billy joel`
  - This will set an alarm for 9:30am the following morning. At that time, it will execute the command `m billy joel`, which will cause some Billy Joel music from YouTube to start playing. What a nice way to wake up!
  - The shell is forgiving about small changes to syntax such as added spaces, so don't worry about getting the commands exactly right.
- `:say hi`
  - I use this as a test that my hands are aligned properly with the keyboard. If it doesn't say "hi", that probably means my hands are offset from the keys and I typed a bit of gibberish.
  - The command `:status` serves the same purpose, but just says "ok" instead of "hi".


### Using the "at" command

The "at" command is useful because it allows you to simply schedule other commands to run at a designated time in the future.

To use the at command, type `:at <when>:<command>`. It's OK if `<when>` has a colon in the middle, e.g. `<when>` could be `7:30am`. It could also be `tomorrow at 9am` -- the syntax for `<when>` is flexible. `<command>` can be any of the commands shh supports, such as `alarm` for playing music from youtube. E.g. `:at 7:30am : alarm` would schedule a musical alarm for 7:30am the following day.


### Adding new commands

You can easily add new commands by adding new functions to [shh_commands.py](https://github.com/dbieber/shh-shell/blob/master/shh_commands.py).

Simply add a function decorated with the `@command` decorator to add a new command to your shh shell. If your command accepts arguments, include `{}` in the format string for your command, and the user's arguments will be passed to your function when the command is run.


### Troubleshooting

One common mistake is to start typing a command in the middle of a line. When in doubt about whether you are at the start of a line, just hit enter. You cannot go by the visual representation in the black box -- all that is is a text field, but it doesn't necessarily represent the internal state of your shell. So, just hit enter, then type your command, beginning with a colon.

There is no concept of a cursor in shh. The arrow keys don't do anything. So even if the cursor in the text box appears to be in the middle of a line, in practice you are always typing at the end of the current content and the logged text will reflect this.

For additional issues, please open an [Issue on GitHub](https://github.com/dbieber/shh-shell).


### Installing the Shh Shell

Head on over to [https://github.com/dbieber/shh-shell](https://github.com/dbieber/shh-shell) to use the shh shell.

If you get around to writing proper installation instructions for this before I do, send me a pull request. ([shh-shell repo](https://github.com/dbieber/shh-shell), [davidbieber.com repo](https://github.com/dbieber/davidbieber.com))


# A bit of backstory

## Why did you create a non-visual shell?

There was a time during undergrad when I was losing sleep to thoughts swirling around in my head. "Does she like me?", "I should have responded in this slightly different way," etc. Variations on a theme would rattle around in my head, each variation only slightly different from thoughts I had already thought. How could I make them stop?

I found that writing down my thoughts helped stop this rattling. Once a single canonical representation of the thought was written on paper, that was sufficient for my brain. It stopped feeling the need to iterate on the thought, and it let me get to sleep.

However, writing on paper in the dark meant that in the morning, I couldn't easily read what I had written. My handwriting at night was slanted and somewhat illegible.

I tried turning the lights on to write down my thoughts, but I didn't like how that woke me up. I tried notepad apps on my phone for writing down my thoughts, but my phone is bright and this was not much better than turning the lights on and using paper.

So, I started typing on my computer with the monitor off. This was a great solution, but it came with it's own problem: I needed to know if I was typing in the right window. Hence, shh shell was born. The gradual addition of commands over time has an added bonus that makes shh shell even more useful for me.


## Isn't the audio annoying to anyone else trying to sleep?

Yes, my college roommate [Harvest](http://harvestzhang.com) can attest to the annoyance of hearing repeated "focused", "focus lost" throughout the night.

I cannot in good conscience recommend use of shh shell when sleeping with your significant other.


## What have you typed into your shh shell?

When I first started typing at night back in 2014, I wasn't used to typing without visual feedback. So in the morning when I went to look at what I had typed, I was surprised to find a large paragraph of complete gibberish! My hands had been offset by a key or so on the keyboard as I was typing. Only the final line of the text was readable: "I hope the FBI doesn't find out about this."

What made this particularly cool for me was that I had no recollection of what I had typed the night before. What was I concerned about the FBI finding out!?

Decoding the paragrah wasn't too challenging, since each letter was just off by one or so on the keyboard, and so I was soon able to figure out what I had typed. It was an amazing experience decoding this, because as I did so, my memory came back. The text was a description of a dream that I had woken up from and typed into shh before falling back asleep. I was not involved in any criminal activity :).

Before I decoded the mysterious paragraph, I had forgotten entirely about the dream. As I decoded though, I remembered the dream, waking from it, and writing down what had happened. 

Since then, I've now gotten used to typing in the dark and using the little bumps on the F and J keys to guide my hands. So, I don't have to decode mysterious passages about hiding secrets from the FBI anymore. I have now repeatedly experienced not remembering having typed something until I see what I typed in the morning, and each time the memory of typing it comes back as I read what I wrote. This hasn't ceased to be a very cool feeling each time it occurs.

## Conclusion

While I built this for myself, I have made it open source in the hope that you too may benefit from it. I hope it helps someone out there get a better night's sleep or remember a key idea they would have forgotten. Definitely check out the [shh shell on GitHub](https://github.com/dbieber/shh-shell) and give it a try if you're Python-inclined. And as always, feel free to get in touch if you want to discuss this project or anything else.
