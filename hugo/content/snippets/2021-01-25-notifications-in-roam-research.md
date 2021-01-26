+++
title = "Notifications in Roam Research"
date = 2021-01-25T00:00:00
uid = "zA0iyJXpl"
plugins_js = ["margin-notes"]
+++

[#RoamGames](https://twitter.com/hashtag/RoamGames) are upon us! The challenge: *project management* in Roam.

So, let's talk notifications. They're going to be essential for any multiplayer Roam scenario. They're also ruthless attention vampires that kill productivity. We've got to get this right.

Let's disentangle _what_ you get notified about, _when_ you get notified about it, and _where/how_ you're notified. This leads us to a vision where users can define _notification strategies_ and take control of their attention[^users].

[^users]: And still provides sensible defaults and easy configs for non-power users.

## **What** to notify on (References and Queries)

What do we want to get notified about? First, three scenarios to motivate our discussion. Then, the primitives: references and queries.

#### Scenario 1, Chat:

You're working on Secret Project X, conversing asynchronously with your teammate Abhay about Feature XX. It's gonna be big. While you're off working on something else Abhay responds to a bunch of your earlier messages. You want to get notified about this, for sure.

#### Scenario 2, Blockers:

You're working on Task A. But it's blocked by Tasks B and C. You represent this in your Roam graph like this:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fplayground%2FjLpcHwI9aQ.png?alt=media&token=eeb11581-2466-4824-a725-35a0bd720eff)

(As an aside, being able to embed a tiny piece of my Roam graph in my blog would be super helpful.)

Once Task B and Task C are marked DONE, you want to get notified so you can resume working on Task A.

#### Scenario 3, Topic Tracking:

You're in a big multiplayer graph and you've carefully curated a page about your own project [Python Fire](https://github.com/google/python-fire). You're excited when people talk about Fire, so you want notifications when people reference it.

#### The Primitives: References and Queries

Basic usage: Notifications when someone responds to me[^1], notifications when someone references a particular page or block (linked or unlinked)

Advanced usage: Roam queries and Datalog queries[^2] are extremely expressive. I should be able to set up a query and get notified whenever the query results change.

[^1]: This one, while a basic use case, is actually tricky to express as a query. But we can do it, I'm confident.

[^2]: See my [two](/snippets/2020-12-22-datalog-queries-for-roam-research/) [snippets](/snippets/2021-01-04-more-datalog-queries-for-roam/) for lots of examples of what you can do with datalog queries.

Now that we've set out what we want to get notified about, let's talk about when we want to receive the notifications. We'll get to how we want to configure the notifications a little bit later on.

## *When* to notify (Immediately, Batched, Delayed, At specific times?)

Most apps have minimal options for when you receive notifications. A typical message board config offers "every individual email", "daily digest", "weekly digest." This is Roam. We can do better than that.

For the messages from Abhay about Project XX, I want notifications to pop up immediately.

When I become unblocked on a task, I want a notification within the hour, but if multiple tasks become unblocked they the notifications can totally be bundled. I don't need an _individual notification_ per task. That would just be overkill.

And for references to Python Fire, a daily digest at 9am is more than sufficient.

#### Primitive: Notification Strategies

Anyone with a bit of JavaScript or Clojure knowledge can define a notification strategy. A notification strategy defines the rules for how notifications should be handled. The interface for a notification strategy is: stream of notifications in, stream of notifications out (_soni-sono_ for short).

By allowing users to define and share notification strategies, we can empower uses to take back their attention and get more out of their Roam experience.

The "Notification strategies" approach benefits non-programmers too, because notification strategies can be shared in the Roam-depot. I'm hoping for a future where RoamHacker and David Vargas and others have developed both simple and sophisticated "notification managers": UIs where non-programmers can configure their notification settings in the level of detail best suited for them.

#### Primitive: Tags connect references and queries to notification strategies

That is, tags connect _what_ to _when_.

When you write a notification strategy, you name it. Tag a reference of a query with the name of a notification strategy to run that strategy on that reference or query.

Let's clarify with an example.

Say I have a query ("all Tasks with 'Blockers' where all Blockers are 'DONE'"), and a notification strategy named "Bundle on the Hour" ("bundle all incoming notifications and emit them on the hour as a single notification"). Then I can tag the query with #[[Bundle on the Hour]] to start applying that notification strategy to the results of the query.

Once I've added that tag, the notification strategy will be called every time the query results change, and it will be able to start emitting notifications.

Similarly if I write [[Python Fire]] and tag it with #[[Digest at 9am]], then _that_ notification strategy will be called whenever the references to or contents of the Python Fire page change.

## Sending notifications

Great, we've talked about how to decide what to notify about, and when to send the notifications. How/where do the notifications actually get sent?

A sensible default for the first pass is to use browser notifications. But we're thinking long term, so I won't dwell on this "first pass" for too long.

If you do want to use browser notifications, it's easy to do so[^mozilla]. You can try this in your Roam graph (or browser console[^3]) right now:

```javascript
function notify(text) {
  // Let's check if the browser supports notifications
  if (!("Notification" in window)) {
    alert(text);
  }

  // Let's check whether notification permissions have already been granted
  else if (Notification.permission === "granted") {
    // If it's okay let's create a notification
    var notification = new Notification(text);
  }

  // Otherwise, we need to ask the user for permission
  else if (Notification.permission !== "denied") {
    Notification.requestPermission().then(function (permission) {
      // If the user accepts, let's create a notification
      if (permission === "granted") {
        var notification = new Notification(text);
      } else {
        console.log(text);
      }
    });
  } else {
    // At last, if the user has denied notifications, and you
    // want to be respectful there is no need to bother them any more.
    console.log(text);
  }
}

notify("You've got mail.");
```

[^3]: Cmd-option-i to open your browser console on Chrome on Mac. [Look it up here](https://www.google.com/search?q=how+to+open+the+browser+console) for other browsers or operating systems.

[^mozilla]: Code courtesy of [MDN](https://developer.mozilla.org/en-US/docs/Web/API/notification).

I don't want browser notifications though. I want my personal digital assistant [Bieber Bot](/projects/bieber-bot/) to send me notifications. Now, this is no trouble in a private graph. I can use a webhook to send myself a message as Bieber Bot. In a public graph, however, this would be dangerous. Anyone could see the code and start impersonating Bieber Bot. A travesty!

So, we need Roam to support *secrets*. Ideally this would come from the Roam core team, not the community. First class secrets would enable me to use write roam/js that communicates securely with my own services, like Bieber Bot and others, without giving others the capability of doing the same.

As an alternative approach to secrets, having all Roam graphs be *one giant graph* with a good permissions model would also be sufficient. Then I could put my notifier code in my graph (private), but have the queries that trigger the notifier apply to a graph I share with my team.

How does specifying a notifier (browser notifications vs Bieber Bot) fit in with writing queries and enabling notifications? You can set your default "notify" function just by defining the function "notify" and tagging it / nesting it under roam/notify. You can also set a notify function whenever you define notifications just by adding an extra reference with the name of the notify function.

## Some Examples

This was a lot, and reading the above it might sound complicated. And that's because it _can_ be complicated; you can have as complicated a notification strategy as you like. But it doesn't have to be complicated, and for most users it won't be.

Ideally turning on notifications for messages could be as simple as adding a block in your graph that says:

`[[roam/messages]] #[[Notify me immediately]]`

Turning on notifications for unblocked tasks could be as simple as (1) getting the unblocked tasks query from the Roam depot, and then (2) adding a block `[[Unblocked tasks]] #[[Bundle on the Hour]]`.

And turning on notifications for references to Python Fire should simply mean adding a block `[[Python Fire]] #[[Digest at 9am]]`.

## Let's build it

Want to build this with me? I'm @Bieber on Twitter and active as dbieber on the [Roam Slack](https://roamresearch.slack.com).
