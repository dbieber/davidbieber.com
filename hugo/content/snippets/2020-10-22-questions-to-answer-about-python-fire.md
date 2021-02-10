+++
title = "Questions to Answer About Python Fire"
date = 2020-10-22T20:31:00
tags = ["python-fire", "python"]
+++

Tomorrow I'm giving a talk to Women Who Code on Python Fire. Python Fire is a Python library I wrote back in 2017 that makes command line interfaces automatically out of any Python object you give it.

I have my talk planned but there are a few pieces of the story I haven't included in my talk yet. They are 1) Why did I build Python Fire? 2) How are people using Python Fire in the real world? 3) What's it like maintaining an open source project?

To the first question, I should explain how we used Boom at Nest. Boom was the proto-version of Fire that inspired Fire's development. At Nest we had an ETL pipeline consisting of several distributed systems. For example data would pass through SQS, Kafka, Storm, and Pentaho while it was being ingested. We wanted to write tests for this complex series of systems. And we also wanted to be able to manually operate the systems. So we wrote Python functions for controlling each part of the system.

Using Python's inspect feature we then turned this collection of functions automatically into a CLI. This allowed us to reuse the same code both for writing tests and for giving the operators control over the ingestion pipelines without needing to do duplicate work. This was the inspiration for Fire.

To question two: there are thousands of uses of Fire on GitHub. OkCupid uses it for data analysis. One person I corresponded with uses Fire to control after market engines. About 10% of uses on GitHub are for machine learning projects, including the GPT codebase. There are also a couple hundred uses within Google too, though gflags (aka abseil) is the Google standard for CLIs still.

And finally to question three, it's really nice to be appreciated! I built Fire to scratch my own itch from working at Nest and Google, but after releasing Fire it's gotten quite popular. Over 17k stars on GitHub, thousands of open source projects using it, and over ten million installs from every country around the world. It's really nice to see my effort appreciated.

My favorite is that someone has written a blog post explaining why Fire is a good tool for teaching Python, because it lets the beginner start programming without needing to understand any boilerplate. I'm hopeful that Fire is indeed helping people learn to program.

Time permitting I will add these questions and answers to my talk tomorrow.
