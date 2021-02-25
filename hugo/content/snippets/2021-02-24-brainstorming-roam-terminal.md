+++
title = "Brainstorming: Roam Terminal"
date = 2021-02-24T00:00:00
uid = "3jSWpMmH8"

+++

In Roam Research, I'd like to be able to type "/terminal" to insert a shell into my current block. Each command issued in the shell will become a block hidden behind the terminal (nested but collapsed). The output of each command will become a block as well.

What sorts of commands do you want to be able to issue from within Roam? Deploying snippets. Querying the Roam graph. sshing into another machine and using it natively. Treating Roam like a file system.

Of course I'd like all the basic shell features (history, basic unix commands sed/grep/ls/cd/awk/..., piping).

I'd also like my commands to be able to use my Roam content as inputs. I'd like a new type of shell expansion -- expanding block references. echo $((7yNZl3Gf-)) will echo the contents of that block (precise syntax tbd).

Pages in the Roam database can be treated like files. cat [[Roam Research]] will output the full contents of the Roam Research page of my graph.

We'll have new primitives too, like the unix classics, more suited for the Roam data structure. List all references on a page. grep that list for a keyword. Sort by date. `refs Roam Research | grep Conor | sort -t`. There would be primitives for accessing a block's children, parents, refs, backrefs, etc.

Of course you can write your own commands too. Like [Python Fire](https://github.com/google/python-fire), we'll provide a mechanism to trivially translate any javascript/closure function in your roam/js into a command line utility. The function name becomes the command name. The function arguments become its flags. Help is generated automatically.

The real power comes from being able to apply the unix philosophy simultaneously on Roam and on a remote machine. How does this look? Maybe the Roam graph is mounted as a filesystem on the remote machine. /roam/pages/Roam Research.md views [[Roam Research]] as a markdown file. Also viewable as json or edn. Syntactic sugar provided by the shell allows you to operate directly on "[[Roam Research]]" allowing for natural commands like the one above.

You can write to pages and blocks via these unix utilities too. Makes it super easy to copy data between the remote machine and your graph in both directions.

How to implement this? roam/render may be essential. [Secure shell app](https://chrome.google.com/webstore/detail/secure-shell-app/pnhechapfaindjhompbnflcldabbghjo?hl=en) (chrome extension) suggests feasibility. There's a [wikipedia page on Web-based SSH](https://en.wikipedia.org/wiki/Web-based_SSH) for inspiration. [xterm.js](https://xtermjs.org/) is used in loads of places for javascript-based terminals.

Rerunning a command from your shell history? Appears as a block reference. Even works for modified commands.

This just comes for free for being in Roam: you can tag your commands to make them easy to find later. In bash # starts a comment, so the syntax for tagging tag-teams nicely with bash's syntax. Similarly using block and page references in your commands pages it easy to resurface them.

For v0 we don't necessarily need a roam/render UI. Instead we could just write some roam/js that listens for ENTER on blocks nested below "{{roam/terminal}}". When ENTER is pressed, the block's contents are parsed, the command gets run, output gets streamed to a new block nested below the command. I think a specialized UI could go a long way though. At the very least history search and tab completion are pretty essential shell features, and there are so many more (e.g. curses, colors).

As I wrap up this idea, I'll also point out the deep similarity between terminal UIs and chat UIs. Both are at their core just call and response. In one you communicate with the computer, in the other with human beings. (With [Bieber Bot](/projects/bieber-bot) and my Messager project, it's not always clear which is which 😃.) Details like the number of participants, the format of messages, and whether a response can be issued without a corresponding call are just that: details.

If we could get a solid terminal experience, legitimately enabling developers to make Roam their default shell, the fusing of note-taking, thinking, and command-issuing that would result would be super powerful. All just a half-baked idea, for now. For now.
