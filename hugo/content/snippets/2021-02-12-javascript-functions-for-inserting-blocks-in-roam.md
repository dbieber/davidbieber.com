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

<script src="https://gist.github.com/dbieber/795cf15cad6b46cfbd6cc8213900925d.js"></script>

To use these functions in your Roam database, create a block with the string `{{[[roam/js]]}}`, create a code block by typing triple-backticks (\`\`\`), paste the above JavaScript into the code block, and click "Yes, I know what I'm doing."

As a reminder, you get the result of an async function with `await`, e.g.

```javascript
let uid = await getOrCreateBlockOnPage(
    "February 12, 2020", "Fleeting TODOs:")
```

The create- and getOrCreate- functions are async, whereas the pure get- functions are regular functions. So, be sure to use await accordingly.
