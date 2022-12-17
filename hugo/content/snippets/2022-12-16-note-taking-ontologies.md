+++
title = "Explicit Ontologies in a World Without"
date = 2022-12-16T00:00:00
tags = ["note-taking"]
plugins_js = ["margin-notes"]
+++

## Background: Ontologies in Note-taking

I'll do my best to get the context for this thought down quickly, but I don't think I'll do a good job. Feel free to ask me if you'd like to understand the context better.

In a note-taking system like C. or Tana, objects exist in an ontology[^1]. This means that an object can have a type. That type definition can have properties. For example my notes might be full of people. Each person might have a birthday and contact info and a height and a handedness.

[^1]: Bear in mind I've used neither of these systems! Take my thoughts with grains of salt.

Having ontologies be explicit can provide a lot of value in a note-taking system.
In particular: (1) This can enable powerful auto-complete / templating features. (2) This can enable powerful search functionality. (3) This can enable integrations with other specialized features (like a calendar, a contacts view, a shopping experience[^2], whatever) or external software.

[^2]: I just chose a random example. But anyway, the idea is that you might build a shopping widget that uses the data about your contacts' preferences to surface gift ideas for them while you're shopping. The ontology way to do this is for each Person in your notes to have a Likes or Interests field, which the shopping experience can access.

## Agenda: Three Key Points

Next I want to make a series of points that interact a bit:

* Ontologies take time to maintain, and are difficult to design well.
* Large language models may be able to provide all three value propositions without actually needing the explicit ontology.
* Even if the above two points are right, there's still value to explicit ontologies in a world where we don't spend much time being explicit about our ontologies.

It's this third and final point, which I realize I haven't made clear just yet, that is the main thought I wanted to share in this snippet. Before we get there though, let's expand on the first two points.

## Doing Ontologies Manually is Hard

Coming up with useful ontologies is hard. Take the Person example from above.
Is it important that every person has an Interests field? Almost certainly not; you might not care to write down the interests of your dentist, for example. If you don't like that example, consider an Education field. You probably don't care to write down the educational history of everyone that shows up in your notes.

But if you're building a gift recommender, then an interests field might be critical. And if you're building a job recommender, an education field might be critical.

A risk you might run having an ontology in your notes is that it might discourage you from putting something in your notes because it doesn't fit the ontology.
Suppose you avoid this risk, though, and manage to freely add information to your notes undeterred by the ontology's constraints.
A second possible risk you run is that your ontology winds up being extremely sparse.
You add fields as you need them, but lots of fields only apply to a single instance, rather than to the majority of instances of a type. Is your ontology still useful at that point?

A third potential risk, which extends the second, is that as your ontology grows... you might end up with a type having two very similar fields. E.g. Person could end up with both a "Likes" field _and_ an "Interests" field. Why might this happen? Two reasons come to mind: One is that you simply have a bunch of fields, and so you accidentally use a new name ("Likes") when referring to an existing attribute ("Interests"). The second is that "Likes" and "Interests" might mean slightly different things to you. That's fine, if you want to track them separately. But these are highly correlated! And now you're left with a dilemma ("Risk 4", let's call it): do you put the information in both the "Likes" and the "Interests" field? That would increase the maintenance burden of your note-base substantially (if you care about completeness/having the info you enter be maximally useful, which you might, in order to get the benefits of ontologies listed above). Or do you only put the information in one of the two fields? If you do that, then you risk your use of the ontology failing when you search for "Person with Interest in Table Tennis" only to find that half your table-tennis friends "Like" Table Tennis while the other half have an "Interest" in it.

Finally, building ontologies takes time. Let's turn our attention[^3] to large language models, because you might not need to spend your time on ontologies in the near future.

[^3]: I was planning on squeezing a reference to "Factory factories" into this section, but then it didn't fit in, so just sticking this in a footnote.

## LLMs reduce the need for explicit ontologies

Large language models[^4] may be able to provide many of the benefits of ontologies without the need for explicit ontologies. These models can understand and extract relevant concepts and relationships from unstructured text, allowing one to search and retrieve information without the need to pre-define an ontology.

[^4]: I'm using the term large language model here in a loose sense. I basically mean tech largely dependent on deep learning, including advances expected to come in the next few years. It's easier to just say LLM though, even though that oversimplifies.

Recall the three benefits of ontologies that we're interested in: auto-complete/templates, search, and integration with specialized systems.

#### Search

It's easiest to imagine how large language models are going to be useful for search first.
Imagine that instead of having ontologies in your note-base, you simply have free-form text.
You still might say that David is interested in table tennis, but there would be no formal "Interests" attribute linking David and Table Tennis.
If a large language model understands that text, then it will still be able to handle queries like "what is David interested in?" and "contacts who like table tennis?"

You can even try this on a small scale today in [ChatGPT](https://chat.openai.com/). Paste the following text into ChatGPT and it answers the questions correctly. I wont argue the case here, but I fully expect this to work on the scale of a full note-base in the coming months-years.

```text
Mary likes hockey, collects coins, and reads sci-fi.
Glenn plays table tennis, collects rocks, and reads fantasy.
My dentist recommends the book "Jaws". Next apt is March 6.
Peter plays scrabble and enjoys table tennis. Hanging out next Tuesday (Dec 20)

Who likes table tennis?
What are my dentist's interests?
Does my dentist like table tennis?
```

#### Integration with Specialized Systems

One of the key reasons ontologies are useful is they allow for specialized systems to access the information stored in the ontology/notes, in order to provide a quality domain-specific experience using the data from the notes.

This could take the form of a specialized contacts view of the contacts data found in your notes. It could be a specialized calendar view of time-annotated data in your notes. It could be the shopping experience I described in a footnote, which uses your contacts' interests to surface gift suggestions. The possibilities are numerous.

If search is robust (and it's not totally clear that LLM search is going to be robust enough, but I suspect that it will be), then the data access requirements for these specialized integrations could be satisfied by the search described in the preceding section.

Two ways to think about this:
(1) The specialized system issues queries -- possibly even natural language queries -- about the notebase. It gets structured results back. It uses the structured results to render the specialized domain-specific experience.
(2) The raw text in <mark>the note-base is being projected onto a temporary domain-specific ontology just for the specialized system</mark>. E.g. the shopping experience might require an ontology where each Person has interests, while a separate job matching system might require an ontology where each Person has an educational background. Using the magic of LLMs, the raw text data is projected into the structured ontology needed by each system. But there's no "one" ontology living in the note-base that the note-taker needs to maintain.

Maybe these two ways are actually the same. :shrug:

At this point we've seen the first place where ontologies are useful even in this raw-text focused LLM-centric world. I've <mark>highlighted</mark> it. We'll come back to it shortly.

#### Auto-complete / Templating

We come now to one of the main value-adds of an ontology: having a nice template to fill in about an object. Do we lose this in a raw-text LLM-centric world? By default, yes. But we can (very likely) use LLM-ish tech to implement an auto-complete / templating feature, arguably one that's (in some ways) better than we get in an ontology-centric world.

How? We can <mark>use the LLM-ish to suggest fields for an entity when we create it</mark>. For example, when we mention a person, we can have our system insert fields (with blanks to be filled in) for the attributes that seem relevant to the person in the given context.
If we're writing about how we met someone at a dinner party, it might provide an Interests field. Whereas if we're writing about people we met at a career fair, it might provide an Education field.

In this setting, the fields aren't there to enable datalog search queries or populate a database; rather, the fields are there for human purposes: to prompt us to write the things we would want to write, and relieve us a bit of typing and a bit of cognitive load.
The search and integrations are going to work just fine whether the field is called "Interests" or "Likes" because the LLM understands that these are (in most contexts) synonyms.

We've now introduced the second place where ontologies are useful even in a raw-text focused LLM-centric world, again <mark>highlighted</mark>.

In what ways is this proposed hypothetical templating feature better than an ontology-based templating feature? Recall the risks we discussed earlier: ontology maintenance runs the risk of there being lots of little-used fields in an ontology. In a naive ontology-based templating system, all these extra fields would clutter the interface, whereas in our proposed hypothetical templating feature, only a relevant subset of the fields show up by default.

In what ways is this proposed hypothetical templating feature worse? Well, it loses the explicit association between objects of the same type. If later you decide you want all people to have a "Formal Name" attribute, there's no clear source-of-truth place to add this attribute to all people. You could query for a list of all people, and then add to your notes "X's formal name is Y" for each of the people. Just brainstorming; maybe this isn't a drawback after all; I'll have to keep thinking on this one.

## Explicit Ontologies in a World Without

Looking back over the <mark>highlighted</mark> text, we can see that there are at least two places where explicit ontologies remain useful even in a raw-text focused LLM-centric world (that is, in a note-base full of raw text, not backed by an explicit ontology).

The first was during querying for domain-specific experiences. There we saw the value of having the raw text in he note-base projected onto a temporary domain-specific ontology just for a specialized system.

The second was for templating/auto-complete, one of the main values of an ontology. Using LLMs we can provide the appearance of there being an ontology without the note-base actually being backed by an explicit ontology.

All of this relies on some amount of speculation about where our LLM[^4] technology is going and what its coming capabilities will be. I'm happy to stand by this speculation, and happy to discuss.
