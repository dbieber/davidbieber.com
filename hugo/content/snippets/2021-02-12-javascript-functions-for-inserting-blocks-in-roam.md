+++
title = "JavaScript Functions for Inserting Blocks in Roam"
date = 2021-02-12T00:00:00
uid = "BG51q3IqW"
tags = ["roam-research", "javascript"]
keywords = ["datalog"]
+++

At the end of this snippet I include some helpful javascript functions for accessing and inserting pages and blocks in Roam Research. Hope you find these useful!

**getPage(page):** returns the uid of a specific page in your graph. _page_: the title of the page.

**getOrCreatePage(page):** returns the uid of a specific page in your graph, creating it first if it does not already exist. _page_: the title of the page.

**getBlockOnPage(page, block):** returns the uid of a specific block on a specific page. _page_: the title of the page. _block_: the text of the block.

**createBlockOnPage(page, block, order):** creates a new top-level block on a specific page, returning the new block's uid. _page_: the title of the page. _block_: the text of the block. _order_: (optional) controls where to create the block, 0 for top of page, -1 for bottom of page.

**getOrCreateBlockOnPage(page, block, order):** returns the uid of a specific block on a specific page, creating it first as a top-level block if it's not already there. _page_: the title of the page. _block_: the text of the block. _order_: (optional) controls where to create the block, 0 for top of page, -1 for bottom of page.

**getChildBlock(parent_uid, block):** returns the uid of a specific child block underneath a specific parent block. _parent_uid_: the uid of the parent block. _block_: the text of the child block.

**createChildBlock(parent_uid, block, order):** creates a new child block underneath a specific parent block, returning the new block's uid. _parent_uid_: the uid of the parent block. _block_: the text of the new block. _order_: (optional) controls where to create the block, 0 for inserting at the top, -1 for inserting at the bottom.

**getOrCreateChildBlock(parent_uid, block, order):** returns the uid of a specific child block underneath a specific parent block, creating it first if it's not already there. _parent_uid_: the uid of the parent block. _block_: the text of the child block. _order_: (optional) controls where to create the block, 0 for inserting at the top, -1 for inserting at the bottom.

Caution :warning: If multiple blocks with the same text exist on the page, these functions may return the uid of the wrong block.

```javascript
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

let ancestor = `[ 
  [(ancestor ?child ?parent)
   [?parent :block/children ?child]]
  [(ancestor ?child ?ancestor)
   [?parent :block/children ?child]
   (ancestor ?parent ?ancestor)]
]`;

function getPage(page) {
  // returns the uid of a specific page in your graph.
  // _page_: the title of the page.
  let results = window.roamAlphaAPI.q(`
    [:find ?uid
     :in $ ?title
     :where
     [?page :node/title ?title]
     [?page :block/uid ?uid]
    ]`, page);
  if (results.length) {
    return results[0][0];
  }
}

async function getOrCreatePage(page) {
  // returns the uid of a specific page in your graph, creating it first if it does not already exist.
  // _page_: the title of the page.
  roamAlphaAPI.createPage({page: {title: page}});
  let result;
  while (!result) {
    await sleep(25);
    result = getPage(page);
  }
  return result;
}

function getBlockOnPage(page, block) {
  // returns the uid of a specific block on a specific page.
  // _page_: the title of the page.
  // _block_: the text of the block.
  let results = window.roamAlphaAPI.q(`
    [:find ?block_uid
     :in $ % ?page_title ?block_string
     :where
     [?page :node/title ?page_title]
     [?page :block/uid ?page_uid]
     (ancestor ?block ?page)
     [?block :block/string ?block_string]
     [?block :block/uid ?block_uid]
    ]`, ancestor, page, block);
  if (results.length) {
    return results[0][0];
  }
}

async function createBlockOnPage(page, block, order) {
  // creates a new top-level block on a specific page, returning the new block's uid.
  // _page_: the title of the page.
  // _block_: the text of the block.
  // _order_: (optional) controls where to create the block, 0 for top of page, -1 for bottom of page.
  let page_uid = getPage(page);
  return createChildBlock(page_uid, block, order);
}

async function getOrCreateBlockOnPage(page, block, order) {
  // returns the uid of a specific block on a specific page, creating it first as a top-level block if it's not already there.
  // _page_: the title of the page.
  // _block_: the text of the block.
  // _order_: (optional) controls where to create the block, 0 for top of page, -1 for bottom of page.
  let block_uid = getBlockOnPage(page, block);
  if (block_uid) return block_uid;
  return createBlockOnPage(page, block, order);
}

function getChildBlock(parent_uid, block) {
  // returns the uid of a specific child block underneath a specific parent block.
  // _parent_uid_: the uid of the parent block.
  // _block_: the text of the child block.
  let results = window.roamAlphaAPI.q(`
    [:find ?block_uid
     :in $ % ?parent_uid ?block_string
     :where
     [?parent :block/uid ?parent_uid]
     (ancestor ?block ?parent)
     [?block :block/string ?block_string]
     [?block :block/uid ?block_uid]
    ]`, ancestor, parent_uid, block);
  if (results.length) {
    return results[0][0];
  }
}

async function getOrCreateChildBlock(parent_uid, block, order) {
  // creates a new child block underneath a specific parent block, returning the new block's uid.
  // _parent_uid_: the uid of the parent block.
  // _block_: the text of the new block.
  // _order_: (optional) controls where to create the block, 0 for inserting at the top, -1 for inserting at the bottom.
  let block_uid = getChildBlock(parent_uid, block);
  if (block_uid) return block_uid;
  return createChildBlock(parent_uid, block, order);
}

async function createChildBlock(parent_uid, block, order) {
  // returns the uid of a specific child block underneath a specific parent block, creating it first if it's not already there.
  // _parent_uid_: the uid of the parent block.
  // _block_: the text of the child block.
  // _order_: (optional) controls where to create the block, 0 for inserting at the top, -1 for inserting at the bottom.
  if (!order) {
    order = 0;
  }
  window.roamAlphaAPI.createBlock(
    {
      "location": {"parent-uid": parent_uid, "order": order},
      "block": {"string": block}
    }
  );
  let block_uid;
  while (!block_uid) {
    await sleep(25);
    block_uid = getChildBlock(parent_uid, block);
  }
  return block_uid;
}

window.getPage = getPage;
window.getOrCreatePage = getOrCreatePage;
window.getBlockOnPage = getBlockOnPage;
window.createBlockOnPage = createBlockOnPage;
window.getOrCreateBlockOnPage = getOrCreateBlockOnPage;
window.getChildBlock = getChildBlock;
window.getOrCreateChildBlock = getOrCreateChildBlock;
window.createChildBlock = createChildBlock;
```

To use these functions in your Roam database, create a block with the string `{{[[roam/js]]}}`, create a code block by typing triple-backticks (\`\`\`), paste the above JavaScript into the code block, and click "Yes, I know what I'm doing."

As a reminder, you get the result of an async function with `await`, e.g.

```javascript
let uid = await getOrCreateBlockOnPage(
    "February 12, 2020", "Fleeting TODOs:")
```

The create- and getOrCreate- functions are async, whereas the pure get- functions are regular functions. So, be sure to use await accordingly.
