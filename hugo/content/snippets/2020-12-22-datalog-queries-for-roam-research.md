+++
title = "Datalog Queries for Roam Research"
date = 2020-12-22T00:00:00
+++

[Roam Research](https://roamresearch.com/) is an excellent note taking tool. One of its core features is "back links" -- any of your notes can easily references any of your other notes, and so all your notes end up linked together in an intricate graph structure. You can quickly see all the references to a note, hence the term "back link".

Roam exposes all of the information in your graph through a **datalog API**. Datalog is a declarative programming language that lets you make queries about your graph.

## Resources

If you want to learn datalog, I recommend http://www.learndatalogtoday.org/. It teaches how to write datalog queries in 8 relatively short chapters chock full of examples.

If you want to see how to use datalog specifically for Roam, you can head over to https://www.putyourleftfoot.in/introduction-to-the-roam-alpha-api. Or keep reading!

## Examples

In this snippet I include a number of examples of useful datalog queries for Roam Research.

### How to Run a Query

Open the JavaScript console. Paste the query. Hit enter.

To open the JavaScript console in Chrome, hit cmd-option-J on Mac or Ctrl-shift-J on Windows. For other systems, [you can look up how to open it](https://www.google.com/search?q=how%20to%20open%20the%20javascript%20console).

### Pages modified today

This query returns a list of pages that have been modified today.

```javascript
let ancestorrule=`[ 
   [ (ancestor ?b ?a) 
        [?a :block/children ?b] ] 
   [ (ancestor ?b ?a) 
        [?parent :block/children ?b ] 
        (ancestor ?parent ?a) ] ] ]`;

let references = window.roamAlphaAPI.q(`[
  :find ?title
  :in $ ?start_of_day %
  :where
  [?page :node/title ?title]
  (ancestor ?block ?page)
  [?block :edit/time ?time]
  [(> ?time ?start_of_day)]
]`, new Date().setHours(0, 0, 0, 0), ancestorrule);

references.map(
  (data, index) => {return `${data[0]}`;})
.join('\n');
```

If you run it in the javascript console, it should print out a list of pages that have been modified today.

### References to a specific page

This query finds all blocks referencing a specific page. Replace "Roam Research" in the query with the name of the page that you want to find the references of.

```javascript
let references = window.roamAlphaAPI.q(`[
  :find ?text
  :in $ ?title
  :where
  [?page :node/title ?title]
  [?e :block/refs ?page]
  [?e :block/string ?text]
]`, 'Roam Research');

references.map((data, index) => {return data[0];}).join('\n');
```

### All blocks on a specific page

This query finds all blocks on a specific page. Again replace "Roam Research" with the name of the page you're interested in.

```javascript
let ancestorrule=`[ 
   [ (ancestor ?b ?a) 
        [?a :block/children ?b] ] 
   [ (ancestor ?b ?a) 
        [?parent :block/children ?b ] 
        (ancestor ?parent ?a) ] ] ]`;
let blocks = window.roamAlphaAPI.q(`[ 
  :find 
      ?string
  :in $ ?pagetitle % 
  :where 
      [?block :block/string ?string] 
      [?page :node/title ?pagetitle] 
      (ancestor ?block ?page)
  ]`, "Roam Research", ancestorrule);

blocks.map((data, index) => {return data[0];}).join('\n');
```

### All blocks with at least 100 descendants

This script finds all blocks with at least 100 descendants. The idea is that these blocks may have notes that are worth revisiting, either to summarize or reflect on. The threshold "100" is of course configurable at the top of the script.

```javascript
let threshold = 100;
let ancestorrule=`[ 
   [ (ancestor ?child ?parent) 
        [?parent :block/children ?child] ]
   [ (ancestor ?child ?a) 
        [?parent :block/children ?child ] 
        (ancestor ?parent ?a) ] ] ]`;

let large_blocks = window.roamAlphaAPI.q(`
[:find ?ancestor (count ?block)
  :in $ % 
  :where 
    [?ancestor :block/string]
    [?block :block/string]
    (ancestor ?block ?ancestor)]
`, ancestorrule).filter((data, index) => {return data[1] >= threshold});

let results = window.roamAlphaAPI.q(`[
  :find ?text ?uid ?childcount
  :in $ ?block ?childcount
  :where
  [?block :block/string ?text]
  [?block :block/uid ?uid]
]`, large_blocks)
  
results.map((data, index) => {return `((${data[1]})) (${data[2]})`}).join('\n');
```

## Support and Debugging

The "#querying" channel on the [Roam Research Slack](https://roamresearch.slack.com/) is active and the community there is quite friendly. If you're crafting or debugging a query, that's a great place to ask for help or share your progress.
