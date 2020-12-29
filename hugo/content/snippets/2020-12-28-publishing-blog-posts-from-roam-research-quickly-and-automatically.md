+++
title = "Publishing Blog Posts from Roam Research Quickly and Automatically"
date = 2020-12-28T00:00:00
uid = "v8Dfy7xMZ"

+++

I thought today I would attempt a proper treatment of my latest automatic "[snippet](/snippets/)" publishing system. It uses JavaScript embedded directly in Roam Research to publish snippets to my website with minimal latency as I write them.

## Prior methods

Previously I've written a system to allow [Bieber Bot to publish snippets that I send him](/snippets/2020-09-27-posting-snippets-from-my-phone/), and followed that up with a [snippet queue](/snippets/2020-10-06-introducing-the-snippet-queue/) to allow me to schedule the publication of my snippets.

I've then also implemented two previous automatic snippet publishers from Roam. The first used my roam-to-git backup to detect new or updated snippets. The second used a puppeteer instance to occasionally check Roam for new or updated snippets.

That makes this my third implementation of automatic snippet publishing from Roam, and my fifth automatic snippet publishing project to date. It's the fastest yet, going from Roam to live on the website in just 90 seconds.

## Room for improvement

Why was publishing through Bieber Bot not enough? Roam is a natural place to write, and I find I write quite a bit more here than I do elsewhere. Since snippets are [all about lowering the barrier of entry to writing](/snippets/2019-12-30-writing-for-no-audience/), supporting writing snippets in Roam seems natural.

Why was the roam-to-git backup based automatic publication system insufficient? While, adequate, the latency between writing a snippet and having it show up on my website was multiple hours. The roam-to-git backups only trigger every hour, and fail about 30% of the time. The script to use those backups to publish to my website would also only run every hour. Their combined schedules meant it could be 2-3 or more hours between writing a snippet and being able to share the link to it. Lowering this latency would give me more freedom to quickly write and share snippets, and also to iterate on a published snippet. Fast iteration is powerful.

Finally, why was the puppeteer-based approach insufficient. While this approach had the potential to bring the publication latency down considerably, in practice I scheduled in to run about hourly, since a headless browser is a computationally heavy piece of software.

## The new approach: "roam/js"

Roam Research allows you to write JavaScript to run directly in Roam. My new approach is to run JavaScript in Roam to detect when a new snippet is written or when an existing snippet gets updated. When this occurs, the script will trigger a GitHub Action, using the snippet content and metadata as input. The GitHub Action will commit the snippet to my website's git repo, and trigger a rebuilding of my website. It does everything except the final deploy to the webserver automatically; that final step waits for me to send a message "Deploy snippets!" to Bieber Bot, upon receipt of which the final deploy step is performed and the website is updated.

Using this approach it takes only 90 seconds between writing or editing a snippet and having it live on my website.

## Detecting new snippets and snippet updates

There are two key pieces to how I detect new and updated snippets. The first is a "mutation observer". A mutation observer is an object in JavaScript that allows you to schedule events to occur when DOM changes are made to a website. In Roam, the DOM is modified when the user makes edits, and so DOM changes can indicate that the user has made a change to their notes.

We would like to detect when a snippet is created or edited. So, we write a function that detects if a snippet has been created or edited since the last time it was called, and we use a mutation observer to call this function when the DOM changes.

Since DOM changes can occur very frequently in Roam, we use a technique called [debouncing](https://davidwalsh.name/javascript-debounce-function) to limit the number of calls to this detection function during periods of many consecutive DOM changes.

How do we detect if a snippet has been created or edited? Roam Research provides a datalog API that allows us to query our entire Roam graph using a logic programming language. You can [learn more about how this works here](/snippets/2020-12-22-datalog-queries-for-roam-research/).

I mark a snippet for publication by tagging it with both the "Snippets" tag, and the "ok-to-publish" tag. This query detects those blocks that are part of a publishable snippet.

```javascript
ancestor = `[ 
 [(ancestor ?child ?parent) 
  [?parent :block/children ?child]] 
 [(ancestor ?child ?ancestor) 
  [?parent :block/children ?child] 
  (ancestor ?parent ?ancestor)]]
]`;

block_info = window.roamAlphaAPI.q(`[
  :find ?uid ?child_text ?child_uid ?parent_uid ?order
  :in $ %
  :where
  [?block :block/uid ?uid]
  [?block :block/string ?string]
  [?block :block/refs ?snippets]
  [?block :block/refs ?publish]
  [?snippets :node/title "Snippets"]
  [?publish :node/title "ok-to-publish"]
  (ancestor ?child ?block)
  [?parent :block/children ?child]
  [?parent :block/uid ?parent_uid]
  [?child :block/uid ?child_uid]
  [?child :block/order ?order]
  [?child :block/string ?child_text]
]`, ancestor);```

Let's break down what's happening in this query. First, there's the `ancestor` rule. The Roam datalog schema only includes a blocks immediate children; the `ancestor` rule allows us to query for all a block's descendants or ancestors, not just the immediate ones. It does this through the recursive definition of "ancestor" shown, which you can read as "An ancestor of ?child is ?parent if ?parent has a child ?child, AND ALSO an ancestor of ?child is ?ancestor if there exists some ?parent satisfying both ?parent has a child ?child, and ?parent has ?ancestor as an ancestor."

The rest of the query (lines 10-24) finds blocks that are the descendants of a block ?block that's tagged with both "Snippets" and "ok-to-publish."

Since Datalog returns the results in an arbitrary order, we need to use the :block/order attribute to reconstruct the proper order of the blocks that comprise the snippet. The logic for this isn't shown, but don't hesitate to reach out if this interests you!

Finally, our mutation observer keeps track of the text of each of the snippets, and if any of them change or if a new snippet is introduced, it triggers a GitHub Action to deploy the snippet to my website.

## Writing a GitHub Action to update my website

My website uses a static site generator, Hugo. So, updating my website consists of adding a markdown file to [its GitHub repo](https://github.com/dbieber/davidbieber.com), rebuilding the site by running Hugo, and then pushing the generated static files up to my server. All of these steps can be automated in a GitHub action.

### Triggering a GitHub Action from Roam Research

To trigger a GitHub Action from Roam Research, I set up the action to trigger on "repository_dispatch" events. I created a personal authentication token, and then use the following JavaScript to trigger the GitHub Action:

```javascript
function publishSnippetRaw(uid, title, date, content) {
  const data = {
    "event_type": "snippet-update",
    "client_payload": {
      "uid": uid,
      "title": title,
      "date": date,
      "content": content,
    }
  };
  fetch(
    "https://api.github.com/repos/dbieber/davidbieber.com/dispatches",
    {
      headers: {
        Accept: "application/vnd.github.everest-preview+json",
        Authorization: "token PERSONAL_AUTHENTICATION_TOKEN",
      },
      method: 'POST',
      body: JSON.stringify(data),
    }
  );
}
const publishSnippet = debounce(publishSnippetRaw, 15000, true);```

This call to `fetch` starts the GitHub Action running on a GitHub server within seconds.

### Accepting inputs in a GitHub Action

You will notice that `data` contains a "client_payload" in the above JavaScript. To accept inputs in the GitHub Action, I access the data from the client_payload and set it to an environment variable in the Action YAML like this:

```yaml
env:
  SNIPPET_UID: ${{ github.event.client_payload.uid }}```

Environment variables like this can then be used by the steps in the action. This allows me to pass the contents of the new/modified snippet to the GitHub Action, which is everything needed for automating its publication.

The GitHub Action writes the markdown file, commits it to the repository, runs hugo to regenerate the static files for the website, and commits those to the appropriate part of the repo as well. The only step remaining at this point is pushing the new files up to my server to serve.

## Deploying with Ansible

I use [Ansible](https://www.ansible.com/) to deploy my website to its lone server. [Bieber Bot](https://davidbieber.com/projects/bieber-bot/) is also quite capable of using Ansible. So, we have an arrangement where I tell Bieber Bot when to redeploy my website, and he does so for me. This way I can deploy my website even when I'm on the go and not at a computer; I just message him using my phone.

All steps, from the last keystroke of writing a snippet to having it show up live on my website, together take about 90 seconds. This is a significant quality-of-life improvement over the multi-hour latency of just a few days ago. I'm hopeful that the result is I'll write even more.
