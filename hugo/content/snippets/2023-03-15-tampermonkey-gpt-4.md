+++
title = "Writing a Tampermonkey Script with GPT-4"
date = 2023-03-15
tags = []
+++

Today I used [GPT-4](https://openai.com/research/gpt-4) to implement my first ever [Tampermonkey](https://www.tampermonkey.net/) script. It took well under half an hour, which is likely many times faster than it would have taken me alone. I am blown away by GPT-4's programming capabilities.

It started with [a simple feature request](https://github.com/hypothesis/h/issues/7868) for [the Hypothesis browser extension](https://hypothes.is/). For context, Hypothesis is a tool for taking notes on the web, including on PDFs.
I use it to take notes on machine learning pdfs on Arxiv. It's a great tool, but it has a limitation: when browsing my notes, it only shows the ID of the pdf, not the name of the PDF. This makes it hard to find what I'm looking for.
So, I made a feature request on GitHub, asking if the developers of hypothesis could make the titles of pages editable. This would allow me to replace the useless IDs with the more useful titles on pdfs whenever I take notes on them.

Someone suggested I could write a Greasemonkey script to do this. Their exact suggestion was:

```text
You can write a Greasemonkey script which parses the Arxiv PDF links on Hypothesis pages, gathers their ArxivID, queries the Arxiv ATOM API with one HTTP call (using an aggregated list of ArxivIDs as a search parameter) and updates Arxiv PDF links titles on Hypothesis pages.

Example of an API query with multiple ArxivIDs: https://export.arxiv.org/api/query?id_list=2007.12026,1706.03741,1603.00022
```

At first I thought this wasn't such a helpful suggestion. Writing a Greasemonkey script is time consuming and it wouldn't be worthwhile for such a small usability improvement. Then I remembered GPT-4. So, I decided to proceed.

Greasemonkey is for Firefox. Tampermonkey is the equivalent for Chrome. I use Chrome, so I would need a Tampermonkey script.

I used GPT-4 to write the script. This is not a trivial script by any stretch of the imagination. It involves parsing the DOM on the Hypothesis page to find references to Arxiv, querying the Arxiv API (but only after dividing the IDs into batches), parsing the XML results returned by the API, and again parsing and updating the DOM on the Hypothesis page to update the results. In order to do all this, the developer needs to understand what the DOM looks like on the Hypothesis page, and what the format of the Arxiv API results XML looks like, in order to get the parsing correct. It took a few back-and-forths, but GPT-4 did a remarkable job of writing the script.

Here's what our interaction looked like:

```text
1. Me (Initial prompt): `Write a tampermonkey script that parses the Arxiv PDF links on Hypothesis pages, gathers their ArxivID, queries the Arxiv ATOM API with one HTTP call (using an aggregated list of ArxivIDs as a search parameter) and updates Arxiv PDF links titles on Hypothesis pages.`

GPT-4: <Attempt 1 at script>

2. Me: `The HTML for one of the rows on the hypothesis page is:
...
In this example the text to update is "1904.09751.pdf" which should be replaced with the title`

GPT-4: <Attempt 2 at script>

3. Me: How do I view the script's logs if it isn't working?

GPT-4: Explains how to get the logs

4. Me: _<pastes error message>_

GPT-4: _<Fixes error message>_

5. Me: Here is the format returned by the arxiv.org api call we're making: _<pastes example Arxiv API output>_

Notice the arxiv id can end with e.g. v1 -- we can safely strip that part.
Let's also add debug logging, e.g. logging the arxivIDs found on the hypothesis page and any other useful debug info

GPT-4: _<Fixes the v1 stripping and adds logging>_

6. Me: The arxiv API only returns the results for the first 10 ids passed to it.

GPT-4: _<Adds batching of API calls>_

7. Me: _<Describes an edge case>_: The title can also be something like 1607.06450v1.pdf -- in that case we should get the id as 1607.06450, dropping the "v1" part

GPT-4: _<Handles the edge case>_
```

[Here's the final script it came up with.](https://gist.github.com/dbieber/c3198a1ceeb86fa823df305a76907afa). It's 112 lines of reasonably well organized Javascript. And it gets the job done. Now, when I visit my Hypothesis notes, the title of every paper is shown clearly, not just its inscrutable Arxiv ID.

As you can see from the abbreviated transcript above, there were only seven back-and-forths between me and the model. In that time, the model behaved sensibly all throughout. It never once made a silly slip-up, which was common behavior for previous models.

In those seven back-and-forths, I used one (1) to share the overall task, four (2, 5, 6, and 7) to share information about the data being manipulated, one (3) to ask for help, and one (4) to paste an error message for GPT to debug.
If I'd had more foresight, I expect I could have included the data from (2, 5, 6, and 7) all in my initial query.

During development, I would manually copy GPT-4's code into Tampermonkey, save it, and refresh Hypothesis to see the changes. If I got an error, or if the behavior wasn't exactly what I wanted, I simply told GPT and waited for it to update the code. GPT-4's output generation is slow compared to other AI models, and there was some waiting time as it wrote its responses. I really felt like I had delegated work to an AI worker, and could easily see myself managing a fleet of such workers, all working toward different goals concurrently. I can also see a future where one AI worker is itself responsible for delegating work to a fleet of such workers; it doesn't need to be a human doing all that delegation.

Overall, GPT-4 behaved as a professional and speedy developer throughout the entire duration of the task. I would be delighted to work with them again on future projects.
