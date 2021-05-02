+++
title = "Keeping Track of My Life in a Spreadsheet"
date = 2019-12-29T00:00:00
type = "post"
draft = false

summary = "I use a daily activity log to track my habits and plan future activities."

tags = ["google apps script"]

[image]
  caption = ""
  focal_point = ""
+++

As many of my friends know, I keep track of much of my life in spreadsheets. There are several pieces to this system, but fortunately it's the kind of system that you can adopt (and discard) incrementally. So, rather than explaining the whole thing in one go, I will explain one core piece in this post.

In this post, I will detail how I use a spreadsheet as a _daily activity log_.

My spreadsheet lets me keep a record of all the things I've done.
It then also rolls up this data in interesting ways that help me with reflecting on and planning my life. Finally, it interacts with a bot system I've written for myself to help me keep my life on track.

I will answer all of the following questions in this post:

- What's the organizational system?
- What are the main benefits of this system?
- Why is this system easy to adopt?
- Why is this system easy to keep doing for months on end, without forgetting?
- How does this system help me with planning my life?


### The System

I have a single spreadsheet with columns *Evening*, *Morning*, *Keywords*, *Weekday*, *Date*, *People*, *Notes*. In this sheet, I have a single row _per day_.

The essense of the system is to jot down (1) what I do, and optionally (2) who I engage with each day.

I don't update the spreadsheet every day, usually just once a week or so I'll fill in the activity from all of the missing days.

This system serves several purposes, the main one being a journal of sorts so I can see a historical log of my activities. As you'll see in the Planning and Notifications sections, it also helps me remember to regularly do all the activities I enjoy doing.

I'll start by providing a brief description of each column in the spreadsheet. Then we'll get to discuss how I use the spreadsheet, and you'll see why they're each important to me. We'll then also dive into all the benefits I get from this spreadsheet and the infrastructure I've built up around it.


#### Column Descriptions

| Column     | Type  | Description |
|------------|-------|-------------|
| *Evening*  | Text  | A single cell in which to put the main activity I did in the evening (e.g. after work) on that day.  |
| *Morning*  | Optional, Text, infrequently used| The main activity I did in the morning (e.g. before work) on that day.  |
| *Keywords* | Optional, comma separated | Keywords describing the activities of that day.
| *Weekday*  | Filled automatically | The day of the week, e.g. Thursday
| *Date*     | Filled automatically | The date
| *People*   | Names, comma separated | A list of the people I engaged with on that day
| *Notes* | Optional, Text | A bit like a diary, this is a place to jot down additional notes about the day.

Really all of the columns are optional, but the ones that are particularly optional are marked as such.


### Usage

Now I'll describe the data entry process, and then all the ways I take advantage of this data.


#### Data Entry

About once a week on average I'll go to the spreadsheet, and fill in all the activities I did since the last time I updated the sheet.

For each day, I try to capture just the main one to two outside-of-work activities that I engaged in. It's totally fine if I don't capture every little thing, and it's also fine if there are some days that I didn't do anything of note.

I said above that I do this about once a week, but there's no strong rhythm to it; sometimes I do it every day for multiple consecutive days, and sometimes I'll go multiple weeks between updating the sheet.

I've been using this system reliably since mid-2018, and it's served me well. The notifications that we'll get to shortly, combined with the simplicity of the method (just one cell to fill in per day), have allowed me to keep using this system without being disrupted by travel or high-workload parts of life.


#### Planning

I have a second sheet that is updated automatically using data from the sheet I've been describing so far. This sheet has one row _per activity_ that I enjoy engaging in.

The most important columns in this sheet are:

| Column     | Type  | Description |
|------------|-------|-------------|
| Category   | Text  | The category of the activity (e.g. Athletic).
| Activity   | Text  | An activity that I enjoy engaging in. (e.g. Skiing)
| Last Date  | Filled automatically | The most recent date on which I engaged in the activity.

The `Last Date` column is filled automatically using the data from the main sheet. The Google Sheets formula that fills in this column is a query a bit like this one:

```javascript
=IFERROR(QUERY(scheduled,
   "select E
    where A contains '" & C2 & "'
      OR B contains '" & C2 & "'
      OR C contains '" & C2 & "'
    order by E desc
    limit 1
    label E ''"
))
```

- `C2` refers to the `Activity` from the current sheet
- `A` is the `Evening` column from the Data Entry sheet
- `B` is the `Morning` column from the Data Entry sheet
- `C` is the `Keywords` column from the Data Entry sheet
- `E` is the `Date` from the Data Entry sheet

This lets me quickly see, for each activity that I enjoy, how recently I've done that activity. For example, I see that I haven't gone camping since 2019-07-05, I haven't played tennis since 2018-07-31, and I haven't gone swimming since 2019-10-07. Really overdue for some tennis!

My spreadsheet also rolls up this data further, by category. I can quickly see how recently I've done any activity in a given category.

The categories I use are:
"Athletic", "Civic Something Or Other", "Day Trips", "Educational", "Entertainment", "Family", "Financial", "Food", "Music + Arts", "Outdoorsy", "Personal Projects", "Puzzles", "Social", "Social Games", and "Well being".

Here you can see how recently I've done something in each of the categories.

{{<figure
  alt="A two-column spreadsheet showing how recently I've done an activity in each of the 15 activity categories."
  src="i-activities-by-category.png"
  width="200px"
>}}

As you can see, I'm doing a pretty good job of doing most of the categories of activities. When I go to make plans next, I'll most likely schedule activities from the bottom categories. For example, I may do a financial review, schedule a board game night, and plan to attend a City Council meeting.

#### Notifications

I've also given [Bieber Bot](/projects/bieber-bot/) (my digital personal assistant and robot friend) access to this data, and he helps me make better use of it.

If it's been too long since I've scheduled an activity in any particular category, Bieber Bot will message me on FB Messenger reminding me to schedule something in that category.

{{<figure
  alt="A message from Bieber Bot reminding me that it's been a while since I scheduled a Financial activity."
  src="i-bieberbot-financial.png"
  width="350px"
>}}

Similarly BieberBot will remind me each day of any upcoming activities planned for that day.
And if I don't have any activity planned for a particular day, BieberBot may take the liberty of suggesting an activity.

{{<figure
  alt="A message from Bieber Bot suggesting I take a walk along the Hudson River."
  src="i-bieberbot-hudson.png"
  width="350px"
>}}


Finally BieberBot will also remind me if I haven't been entering activities into the spreadsheet in a while, so I don't fall too far behind on the logging system.

Setting up these notifcations is a bit outside the scope of this post, but if it interests you how BieberBot works, you can subscribe for future posts here:

{{<mailchimp>}}

You can also learn a bit more about BieberBot [here](/projects/bieber-bot/), but there's so much more to be written.


#### Archiving Old Events

To keep things clean, my spreadsheet also uses Google Apps Script to archive old events. You can see the code I use for the auto-archiving [here](https://gist.github.com/dbieber/42153e6a27382ba6193f108c13b84cf9).


#### Getting Started

If this system sounds appealing to you, it's very simple to get started.

Simply create a new Google sheet with the columns you'd like to track. I use the following:


| *Evening*  | *Morning*  | *Keywords* | *Weekday* | *Date* | *People* | *Notes* |
|------------|------------|------------|-----------|---------|---------|---------|

But for just getting started you might be satisfied with something simpler, say just these three columns:

| *Activity* | *Weekday* | *Date* |
|------------|-----------|--------|

You can use the formula `=TEXT(WEEKDAY(E3), "dddd")` to autopopulate the `Weekday` column, where E3 represents the date (tip: you can use cmd-; to enter today's date into a cell).

I also create a second sheet called `Archive` with the same columns as the main sheet, and use the [auto-archiving feature](https://gist.github.com/dbieber/42153e6a27382ba6193f108c13b84cf9) mentioned earlier to prevent the main sheet from getting cluttered.

Next create the analysis sheet with the columns:

| *Category* | *Activity* | *Last Date* |
|------------|------------|--------------|

The first two columns you can fill in with whatever categories and activities you like, and you can add new categories and activities at any time. No need to fill this in too much until you start to see how you're using the main sheet.

To autofill the `Last Date` column, the full formula I use is:

```javascript
=MAX(
  IFERROR(QUERY(scheduled, 
    "select E
    where A contains '" & C2 & "' OR B contains '" & C2 & "' or C contains '" & C2 & "'
    order by E desc
    limit 1
    label E ''"
  )),
  IFERROR(QUERY(archive, 
    "select E
    where A contains '" & C2 & "' OR B contains '" & C2 & "' or C contains '" & C2 & "'
    order by E desc
    limit 1
    label E ''"
  ))
)
```

This searches both the main sheet (scheduled) and the archive sheet for the most recent occurrence of each activity (C2). For this to work, the rows in the archive and main sheet need to be in reverse chronological order.

Finally, to get the roll-up by category, I use the following Google Sheets formula:

```javascript
=QUERY(A:E,
       "select B, max(D), count(B) where B<>'' group by B order by max(D) desc
        label max(D) 'Last date',
              count(B) 'Count'
       ", -1)
```

Though I would like to, I won't go into how to set up the notifications in this post. For now, that's just between me and [BieberBot](/projects/bieber-bot/).


### Conclusion

As a quick recap of my system:
(1) I manually enter the activity(s) I do each day; (2) the spreadsheet automatically figures out how recently I did each category of activity; (3) bonus: BieberBot uses this data to help me keep my life on track.

I've been using this system for about 18 months now, and I've been quite happy with the insight it provides and how helpful it is for planning.

Still, there are many pieces of my system left undiscussed: tracking financial transactions, taking notes on academic papers, staying in touch with friends and colleagues, dealing with social media, and more! I'd love to tell you about the rest, so stay tuned. And don't hesitate to [reach out](mailto:david810+blog@gmail.com) if you'd like to discuss anything you read. I hope you find this useful, and do let me know if you start using a spreadsheet to track your own life or have a system of your own.
