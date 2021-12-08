+++
title = "The Future of Automation Software"
date = 2021-12-07T00:00:00
tags = ["automation", "browserflow"]
+++

[Browserflow](https://browserflow.app) is great.
It's beyond great.
It's one of my favorite tools, because it is so versatile and empowering.

Nevertheless, there's more that I want from my automation tools.
Here's a summary of what I'd like:

1) OS-level actions
2) Per-application actions
3) Per-website actions
4) Computer vision guided actions
5) Natural language action specification
6) Automatic action discovery
7) Automatic automation extraction
8) User-triggered, event-triggered and time-triggered automations
9) A great sharing experience


#### OS-level actions

Browserflow is (appropriately) limited in scope.
It allows automating the Browser, and that's it.
I would like to be able to use a Browserflow-like system to automate the Browser as well as everything else on my computer.
In the idealized hypothetical future I'm constructing here, I don't need to think about the boundaries between applications and operating system when I construct an automation.

Example OS-level actions include launching applications, switching between open windows of different applications, closing applications, switching between Desktops, and resizing windows.

Mac's Automator software is a good example of an automation tool that supports OS-level actions, but (to my knowledge) it does not then also provide a good browser automation experience.

An example automation that takes advantage of these actions is setting up a series of windows just the way I like them (today achievable with software like [Moom](https://manytricks.com/moom/)).
Combined with per-application actions (next section), these actions allow for powerful multi-application automations.


#### Per-application actions

The range of activities people perform on computers is extremely wide.
Each application has different actions that are possible to take in it.
I would like for automation software to reflect this.

Photo editing applications can provide actions for photo editing,
word processing applications should have their own domain-specific actions,
and gaming and music applications should similarly provide their own.

This is somewhat reflected in the state of things today in Automator.
For some software, there are actions available allowing programmatic control of the application.
Today, these actions must be provided by the application developer.

We should go beyond this; ordinary users should be able to make actions for a piece of software and share them with other users of that software.
The actions provided by the application developer that Automator can access today are often insufficient.
But developing a new action does not need to be a difficult endeavor.

An action developer should be able write a parameterized action that (1) verifies the application meets any preconditions necessary for performing the action, (2) uses menu items, buttons, the mouse and keyboard, and visual indicators (3) in order to perform a sequence of sub-actions in the application to achieve the action's overall intended behavior.
Sharing these actions with others who might use them in broader automations should be possible on GitHub or through any other means (e.g. an actions repository or actions store, for example, either of which would allow browsing actions by application.)

Critically, I would like these OS-level and application-level actions to be available in the same software as the browser-level and website-level actions that a tool like Browserflow provides.

Much of my computer activity happens in the browser, text editor, and the terminal. If this trend away from desktop applications toward browser-usage is taking place for everyone, OS-level and application-level actions may be less important than what we discuss next: per-website actions, vision-based actions, and automatic action discovery.


#### Per-website actions

Some applications, particularly browsers, do not have a clear fixed set of actions that make sense, because they can render many websites.
Each website has different things you can do on it.

So, similar to the per-application actions proposed in the previous section,
I'd also like to call for per-website actions.
DK, consider this a Browserflow feature request.

In Browserflow, a user can define a flow and call that flow from another flow.
This isn't the most well-developed feature of Browserflow;
developing and debugging flows like this requires a lot of clicking around, and it's hard to see what you're doing during development.
Nevertheless, it's a powerful feature that is the seed of per-website actions.

That you can use a flow as an action in Browserflow means you can define flows
for individual activities you might perform on a website, and use them repeatedly in many different flows pertaining to that website.
Browserflow also allows sharing flows, but there's no central repository of them yet, so it is taking solid but small steps toward the dream of user-friendly discoverable per-website actions.

Since every website has different actions to perform on it, and website authors do not provide these actions,
it is somewhat surprising that browser automation leads the automation scene in terms of its capabilities. The saving grace here is that websites conform to standards and expose structure that automation software can take advantage of, which desktop applications do not provide. Browser automation software uses CSS and XPATH selectors to take advantage of this uniformity to provide a decent automation experience.
For desktop software, or for websites that are not built in a tool-friendly manner, we turn to our next feature-request for automation software, vision-guided actions.


#### Computer vision guided actions

All the actions in automation software today operate on clearly defined data structures, but there is so much more that's possible using computer vision.
Actions that work on websites rely on CSS or XPATH queries to find the appropriate part of the page to manipulate.
Computer vision based actions can work in places where there is no DOM, and hence no notion of CSS or XPATH selectors.

An example of a computer vision based action is "Find the text X". Here, X is a parameter. When run, the action identifies the location of the screen containing the text X. The beauty is that X doesn't need to be on a webpage or in a text field. Even if X is stylized, part of a pdf, or part of an image, the action will still work. This action can be followed up with "Click" or "Screenshot" actions, that use the location found from the "Find the text X" action as a parameter.

Another example of a computer vision based action is "Find a region visually similar to X". This action is parameterized by an image, and it finds the location of that image (or similar) on the screen. This might be useful for automating a game with a custom graphic that you have to interact with; it doesn't matter if that game doesn't provide any semantic elements like buttons or a DOM, the computer vision actions will still admit automation.

I found computer vision guided actions useful when building [Scrab Blebot](https://github.com/dbieber/ScrabbleBot), a Scrabble-playing bot that could play Words With Friends on Facebook.
The bot looked for regions of the screen visually similar to an image of a Scrabble tile with a letter on it in order to figure out where to click and drag.
I had to build my own one-off actions for this project though; there was no automation software with vision-based actions available for me to use when developing this project ten (!) years ago.


#### Natural language action specification

"Click the submit button."

"Copy the first paragraph."

So far we have only spoken about allowing developers to define actions. In the next section we will move on to automatic action discovery -- where an action is detected and defined automatically by an algorithm, rather than being defined by a human.
Natural language action specification fits nicely in between these two categories.
The idea here is that we can map human natural language to an action.

If the user says "Click the submit button", we can use machine learning to infer that this translates to a single action "Click" parameterized by the selector ".submit" (or whatever the appropriate selector is for the current page).

If the user says "Copy the first paragraph", again machine learning can translate this into one or more actions that achieves the task.
Large language models will be instrumental in making this feature production quality. See for example the [Codex demo](https://www.youtube.com/watch?v=SGUCcjHTmGY) for a taste of the capabilities of large language models in this domain.


#### Automatic action discovery

We next move on to a research-level feature request: automatic action discovery.
There are billions of websites and software applications, each with its own user interface and its own set of possible actions.
It's unreasonable to expect that a developer will construct actions for each and every one of these, but that doesn't mean we can't use machine learning to detect actions automatically.

There are two types of signal that are useful for automatically detecting actions: (1) similarity in user interface to known actions, and (2) observing user behavior.

(1) Though each website and application has its own UI, there are common patterns. Taking advantage of these common patterns, an algorithm might be able to discern that a website or application provides certain actions simply from its UI elements and arrangement.

(2) By observing user behavior on a website or application (and comparing it with behaviors exhibited previously), an algorithm might be able to detect actions available on that website or application even when method (1) falls short (or in combination with method (1)).

Critical to doing automatic action discovery well is figuring out how to parameterize the discovered actions.
In many cases this is easy; when filling out a form on a website, the text typed is the parameter, while the location in the form is a core part of the action.
In other cases, it's less clear cut; in a shell, typing a command is part of an action, while typing an argument to the command is a parameter, but these are comprised of similar low-level actions (typing characters).
This is an interesting research challenge to get right.


#### Automatic automation extraction

The pièce de résistance of future automation software is automatic automation extraction.
Software will one day automatically notice when something you're doing can be automated, and it will offer to automate it for you.
It might notice this because (1) you're engaging in a repeated behavior.
Or it might notice this because (2) you're engaging in a behavior similar to one it's seen before (e.g. from data collected from other users earlier).

It's important that anyone working on automatic automation extraction respect user privacy.
The data that would be most useful for this type of project (broad computer usage data) is extremely sensitive.
It is an interesting research direction to work toward this goal of automatic automation extraction in a way that consumes little data, and which can be deployed in a privacy preserving manner.


#### User-triggered, event-triggered and time-triggered automations

I conclude with a more modest request than the previous two machine learning based feature requests: triggers.

As I see it, a good trigger experience is what makes or breaks the value of automation software. This is because the triggers are the largest potential source of friction for a user of automations, outside of constructing the automation to begin with.

For user-triggered automations (automations instigated by a user),
I really liked the typeahead UI that Browserflow initially used.
I remain hopeful that DK will bring that back.
Keyboard shortcuts are the other clear contender for a good triggering experience.

Event-triggered automations are also extremely useful.
In my own day-to-day, I use email triggered automations (for handling emails from banks), and chat-triggered automations for all sorts of things.
If-this-than-that is probably an excellent source of inspiration for other events. You can also see [this list of Bieber Bot's capabilities](https://davidbieber.com/snippets/2020-02-04-bieber-bot-capabilities/) which breaks the capabilities down by whether they're timer-triggered, chat-triggered, or credit-card-swipe-triggered.

Time-triggered automations can be broken down further into one-off automations (e.g. "send this email tomorrow morning") and recurring ones ("every morning, email me a digest with the news, weather, and a cat video to watch").

Triggers don't need to be provided directly by the same software that allows creating automations, but it is sensible to bundle these two things together, since automations are a common thing to want to trigger. Separate trigger software and automation software is in many ways actually desirable, but it is critical that the experience of setting up triggers for an automation be clean and user friendly.


#### A great sharing experience

Finally, automation is a superpower, and so I want to be able to share it with others.
If I write a note-taking automation, I want my fellow note-takers to be able to use it.
If someone writes a Farmville automation tool, other Farmville players should be able to use it too.

However, sharing comes with concerns: you don't want to give untrustworthy strangers unfettered access to your machine. Arbitrary code execution is dangerous.

So, my ideal sharing experience is a hybrid of "app store" and "GitHub".
A curated collection of automations that are audited and trustworthy, easy to search, and easy to discover would be very welcome. If automations from this collection were automatically surfaced when I was browsing on a website that had such an automation built for it, I would be delighted.

Then, for automations that haven't gone through any vetting process, it should still be easy to share. It should be possible to host an automation on GitHub or to send an automation to a friend without ever needing a central body to vet the automation.

By supporting both of these sharing models, we can ensure a healthy ecosystem of automations
useful both for programmers and automation builders, and for people who simply want to experience the joy of computing using the automations of others.

---

Interested in working on any of these aspects of automation software? Get in touch. I'm always eager to discuss.
