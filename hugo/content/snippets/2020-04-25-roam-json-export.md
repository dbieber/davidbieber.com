+++
title = "Roam Research's JSON Export Format"
date = 2020-04-25T00:00:00
tags = ["roam-research", "python", "javascript"]
+++

[Roam Research](https://roamresearch.com/) is a note taking tool that makes it really low-friction to take deeply interwoven notes.
One of its core features is that you can effortlessly add links between pages in your notes, just by surrounding a name with square brackets, e.g. [`[[Roam Research]]`](https://roamresearch.com/#/app/commons-db/page/wYVaowjId).

Roam allows its users to export their Roam database as a JSON file. In this snippet, I describe the JSON format used and some of its implications.

## Exporting Data from Roam

From the triple-dots menu, select Export All. Choose JSON as the export format. Then click the Export All button. Your complete Roam database will download as a JSON file.

## Roam's JSON Format

We'll refer to the Roam JSON object you just downloaded as `data`.

`data` is a list, with each entry in `data` corresponding to a single Roam `page`.

Each `page` is an object with keys: `title`, `children`, `create-time`, `create-email`, `edit-time`, `edit-email`.

### Page Schema

| Key | Type | Description |
|---------------|--------|---|
|title          | Text         | The page title. |
|children       | List[Child]  | The list of children of the page. |
|create-time    | Integer      | The time (ms since epoch) when the page was created. |
|create-email   | Text         | The email of the person to create the page. |
|edit-time      | Integer      | The time (ms since epoch) of the last edit to the page. |
|edit-email     | Text         | The email of the last person to edit the page. |

Note that only `title`, `edit-time`, and `edit-email` appear to be required fields.
`children`, `create-time`, and `create-email` appear to be omitted when not available.

### Child Schema

Each of the children in a page may have the following keys. Only the `uid`, `string`, `edit-time`, and `edit-email` keys seem universal. The rest may be omitted when not available.

| Key | Type | Description |
|---------------|--------|---|
|uid            | Text         | A short unique identifier for the child. |
|string         | Text         | The string content of the child. |
|children       | List[Child]  | The list of children of this child. |
|create-time    | Integer      | The time (ms since epoch) when the page was created. |
|create-email   | Text         | The email of the person to create the page. |
|edit-time      | Integer      | The time (ms since epoch) of the last edit to the page. |
|edit-email     | Text         | The email of the last person to edit the page. |

Some children may additionally have the following keys.

| Key | Type | Description |
|---------------|--------|---|
|heading        | Integer      | 1, 2, or 3; indicates the note is an h1, h2, or h3 heading. |
|emojis         | List[Emoji]  | A list of objects indicating who added what emojis and when. |
|text-align     | Text      | One of 'left', 'right', 'center', or 'justify' indicating the text alignment. |

Note that in Roam, children are referred to as "blocks", and a child's ID is the ID used to reference a block.

Last but not least, I include the emoji reaction schema 😂.

### Emoji Schema

Each Emoji reaction to a child is an object conforming to the following schema.

| Key | Type | Description |
|---------------|--------|---|
|emoji          | object      | An object with a single key `native` containing the emoji itself. |
|users          | List[object]  | A list of objects indicating who added this emoji and when. The keys are `time` (ms since epoch) and `email` (the email of the user who added the reaction). |

### Missing Information

Some information appears to get lost in the export. In particular, the following information appears to be dropped.

1. "View as Document" / "View as Numbered List": This formatting information doesn't seem to get exported.
2. Versions. If you're using the "versions" feature of Roam, the versions don't seem to be exported either.

## Implications of the JSON Format

Since Roam allows export of its data in such a simple format, you can easily write scripts for processing this data. For example, merging two databases is trivial. I include some simple such scripts in the following section.

The clear export also means that you will continue to be able to use your data long into the future, even if Roam shuts down or otherwise becomes unavailable to you. As long as you occasionally back up your data by exporting it, it is yours forever.

## Useful Python Snippets for Processing Roam JSON

Once you've downloaded your data as JSON from Roam, you can load and manipulate it as follows.

### Load JSON

```python
import json
filepath = '/path/to/roam-database.json'
data = json.load(open(filepath))
```

### Collect All Children

```python
children = []
blocks = data.copy()
while blocks:
  block = blocks.pop()
  if 'children' in block:
    blocks.extend(block['children'])
    children.extend(block['children'])
```

### Find All Notes Mentioning "Roam"

```python
for child in children:
  if 'roam' in child.get('string', '').lower():
    print(child['string'])
```

### Merge Two Databases

Since databases are just lists of objects, you can trivially merge them.

```python
merged = db1 + db2
```

It's possible this will result in multiple pages having the same name, but Roam deals with this just fine.

## Thank You Roam

I want to conclude with a note of thanks to the Roam developers for allowing export in such a clear and readily understandable manner. Doing so inspires confidence that I will be able to continue using the notes I take in Roam far into the future, no matter what. This makes me so much more comfortable using Roam for my note taking. Props and thank you to the Roam developers for this feature.
