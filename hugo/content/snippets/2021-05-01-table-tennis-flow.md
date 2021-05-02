+++
title = "Making a Browserflow Flow for Eleven Table Tennis VR"
date = 2021-05-01T00:00:00
tags = ["table tennis", "browserflow"]
keywords = ["table tennis", "virtual reality"]
+++

In this snippet I chronicle making a Cloud flow that tracks my progress in Eleven Table Tennis VR, a virtual reality table tennis game I've been playing a bunch over the last month.

I took a first pass at making the flow earlier in the week, and ran into two hiccups I'll need to work around: (1) The css selectors for my ELO, Rank, etc change between visits to the website. How am I going to extract this data in the flow? (2) Some games have three rounds others have two, and the css selectors differ depending on which game we're looking at.

## Challenge 1: Stable CSS Selectors Across Page Loads

Browserflow's default CSS selector for the ELO rate on [my Eleven TT page](https://www.elevenvr.net/eleven/413682) is `div:nth-of-type(1) > .jss87 > .MuiTypography-root`. The trouble with this is that the class .jss87 isn't always there. Sometimes when I load the page, the class .jss70 is there instead. I don't know how this class is determined, but it isn't stable enough to use for my flow.

With a bit of poking around, I was able to use an [`nth-child` rule](https://css-tricks.com/almanac/selectors/n/nth-child/) to write a more stable selector. Here's what I came up with: `div.MuiGrid-container > .MuiPaper-root:nth-child(1) .MuiTypography-root`.

With this new strategy in place, I can easily complete the first half of the flow (which I'll probably actually split into two flows): regularly logging my Eleven Elo, Rank, Win and Loss count, and Win rate into a spreadsheet automatically.

Here's what the completed flow looks like:

![Complete table tennis ranking tracker flow](/snippets/2021-05-01-table-tennis-flow.png)


## Challenge 2: Varying CSS Selectors Across Rows

Next up I have the challenge of selecting game data from the [same page](https://www.elevenvr.net/eleven/413682). Browserflow makes it easy to loop over the match data with its Loop Elements command. The trouble is that some matches have three rounds while others have just two.

The default CSS selects for the game data are e.g. `$match tr:nth-of-type(1) > td:nth-of-type(3)` for the Match Score. Two of the columns: "ELO +-" and "Round 3" only show up in certain matches. "ELO +-" only shows up for ranked matches, and "Round 3" only shows up if the first two matches are split between the players.

I expect that in rare cases there are matches with only 1 round (e.g. because a player leaves early), and that in the future there might be matches with additional rounds too.

The `<td>` elements themselves don't contain any additional information indicating what column they belong to. I might have to take this slightly painstaking approach:

First, I'll use `Get Element Text` to get the text of the first six column headers, and I'll have it use blank text if there are fewer than six headers. In some cases these will be USERNAME, ELO +-, MATCH SCORE, ROUND 1, ROUND 2, ROUND 3. In other cases it will just be a subset of this information.

Then, for each player I'll get the first six entries in their row. I'll use the headers to determine what these entries describe.

*Brief programming interlude*

I've done it. Here's the completed flow. It works like a charm.

![Complete table tennis games flow with collected data](/snippets/2021-05-01-table-tennis-spreadsheet.png)

I had to make 19 `Get Element Text` actions and a `Run Script`, even though I only needed data from 13 different elements. Collecting tabular data is a pretty common task, so there's room to make this simpler for future flows.

Here's the script I ended up writing for populating fields based on the header data, just for reference:

```javascript
let $player1 = $row1field1;
let $player2 = $row2field1;

let $elo1 = "";
let $elo2 = "";
let $elo1change = "";
let $elo2change = "";
let score_index = 1;

if ($header2 == "ELO +-") {
  let elo1 = $row1field2;
  let elo2 = $row2field2;
  $elo1 = elo1.split(" ")[0];
  $elo2 = elo2.split(" ")[0];
  let elo1change = elo1.split(" ")[1];
  let elo2change = elo2.split(" ")[1];
  // Remove the parentheses (+16) -> +16.
  $elo1change = elo1change.substring(1, elo1change.length - 1);
  $elo2change = elo2change.substring(1, elo2change.length - 1);
  score_index = 2;
}

var row1fields = [
  $row1field1,
  $row1field2,
  $row1field3,
  $row1field4,
  $row1field5,
  $row1field6,
];
var row2fields = [
  $row2field1,
  $row2field2,
  $row2field3,
  $row2field4,
  $row2field5,
  $row2field6,
];

var $matchscore1 = row1fields[score_index];
var $matchscore2 = row2fields[score_index];
var $round1player1 = row1fields[score_index + 1];
var $round1player2 = row2fields[score_index + 1];
var $round2player1 = row1fields[score_index + 2];
var $round2player2 = row2fields[score_index + 2];
var $round3player1 = row1fields[score_index + 3];
var $round3player2 = row2fields[score_index + 3];

var gameidanddate_parts = $gameidanddate.split(" : ", 2);
let $gameid = gameidanddate_parts[0];
// TODO(dbieber): Parse timestamp.
let $timestamp = gameidanddate_parts[1];

// formatDate definition elided.
let $today = formatDate(new Date());
```

## Future Challenge: Record every game exactly once

The current instance of the flow just collects all the games on page 1 into the spreadsheet. What I'd really like the flow to do is collect every game once.
My flow will run once a day.

I could do this by parsing the dates, and having the flow collect all the flows less than one day old each time it runs. This wouldn't be robust to missing a day though.

Another approach would be to have the flow look in the spreadsheet for the last game collected, and then keep collecting games until that most recently collected game is reached. I'll discuss these options with DK before proceeding. For now, it'll just collect a subset of my games, or collect some games twice if I play fewer than 10 on some day.

---

You can find the flows [here](https://browserflow.app/shared/4a8c4303-ad21-420e-8414-5de57e0692d4) and [here](https://browserflow.app/shared/4e3fd160-6665-46b7-ad2b-0a6be9121649) if you have Browserflow.
