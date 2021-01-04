+++
title = "More Datalog Queries for Roam"
date = 2021-01-04T00:00:00
uid = "yP0U4Rgb5"

+++

In this snippet I share datalog queries for Roam Research. For more such queries (and to see how to run these queries), [see this earlier snippet on the subject](/snippets/2020-12-22-datalog-queries-for-roam-research/).

## Pages tagged with "X" not listed on page "Y"

This query is useful when constructing an index page. Let's say you want to take all the pages you've tagged with "[[Brilliant Idea]]" and organize them on a page called "[[Brilliant Ideas Index]]". This query will find you all the pages that are tagged with "[[Brilliant Idea]]" that haven't yet been added to the "[[Brilliant Ideas Index]]" page.

```javascript
let container = "Brilliant Ideas Index";
let tag = "Brilliant";
let ancestor = `[ 
  [(ancestor ?child ?parent) 
   [?parent :block/children ?child]] 
  [(ancestor ?child ?ancestor) 
   [?parent :block/children ?child] 
   (ancestor ?parent ?ancestor)]]
]`;

var blocks = window.roamAlphaAPI.q(`
[:find ?page_title
  :in $ % ?container_title ?tag_text
  :where 
    [?container_page :node/title ?container_title]
    [?page :node/title ?page_title]
    (ancestor ?tagged_block ?page)
    [?tagged_block :block/refs ?tag_page]
    [?tag_page :node/title ?tag_text]
    (not (ancestor ?container_block ?container_page)
         [?container_block :block/refs ?page])
]`, ancestor, container, tag)

console.log(blocks.map((data, index) => {return `[[${data[0]}]]`}).join('\n'));
```

Hope this is useful for getting your Roam graph organized!

## Blocks tagged with both "X" and "Y"

I use a query like this to find blocks tagged with both "Snippets" and "ok-to-publish", in order to automatically publish snippets to my website.

```javascript
let tag1 = "Snippets";
let tag2 = "ok-to-publish";
var blocks = window.roamAlphaAPI.q(`[
	:find ?uid ?string
	:in $ ?tag1 ?tag2
	:where
	[?block :block/uid ?uid]
	[?block :block/string ?string]
	[?block :block/refs ?block_tag1]
	[?block :block/refs ?block_tag2]
	[?block_tag1 :node/title ?tag1]
	[?block_tag2 :node/title ?tag2]
]`, tag1, tag2);

blocks.map(
  (data, index) => {return `((${data[0]})): ${data[1]}`;})
.join('\n');
```

## Info about all children of any block tagged with both "X" and "Y"

This extends the previous query in two key ways: (1) it gets all children of any block with both tags, and (2) it gets more detailed information about those children. The ?uid indicates which block has the two target tags, while the ?child_uid, ?parent_uid, and ?order fields allow for reconstructing the arrangement of the child blocks. Each returned record has the text of a child block, it's uid (?child_uid), it's parent's uid (?parent_uid), and the order of that child in its parent's list of children. Together, this information allows you to fully reconstruct the tree of blocks beneath each of the tagged blocks.

```javascript
let tag1 = "Snippets";
let tag2 = "ok-to-publish";
let ancestor = `[ 
  [(ancestor ?child ?parent) 
   [?parent :block/children ?child]] 
  [(ancestor ?child ?ancestor) 
   [?parent :block/children ?child] 
   (ancestor ?parent ?ancestor)]]
]`;

let block_info = window.roamAlphaAPI.q(`[
  :find ?uid ?child_text ?child_uid ?parent_uid ?order
  :in $ % ?tag1 ?tag2
  :where
  [?block :block/uid ?uid]
  [?block :block/string ?string]
  [?block :block/refs ?block_tag1]
  [?block :block/refs ?block_tag2]
  [?block_tag1 :node/title ?tag1]
  [?block_tag2 :node/title ?tag2]
  (ancestor ?child ?block)
  [?parent :block/children ?child]
  [?parent :block/uid ?parent_uid]
  [?child :block/uid ?child_uid]
  [?child :block/order ?order]
  [?child :block/string ?child_text]
]`, ancestor, tag1, tag2);

block_info.map(
  (data, index) => {return `((${data[0]})) ${data[1]}`;})
.join('\n');
```

I use the following script to organize the blocks by their parent:

```javascript
class DefaultDict {
  constructor(defaultInit) {
    return new Proxy({}, {
      get: (target, name) => name in target ?
        target[name] :
        (target[name] = typeof defaultInit === 'function' ?
          new defaultInit().valueOf() :
          defaultInit)
    })
  }
}

var blocks_by_parent = new DefaultDict(Array);
block_info.forEach(
  (info) => {
    [uid, child_text, child_uid, parent_uid, order] = info;
    blocks_by_parent[parent_uid].push(info);
  }
);
```

And then the following function `blocksInOrder` to place the children in their proper order.

```javascript
function blocksInOrder(blocks_by_parent, uid) {
  var blocks = [];
  var blocks_list = blocks_by_parent[uid].sort(
    (b1, b2) => {return b1[4] - b2[4];}
  );
  blocks_list.forEach((block) => {
    blocks.push(block)
    blocks.push(...blocksInOrder(blocks_by_parent, block[2]));
  });
  return blocks;
}
```

This is a key component of how I do [automatic snippet publishing from Roam to my website](/snippets/2020-12-28-publishing-blog-posts-from-roam-research-quickly-and-automatically/).
