+++
title = "Rough Note-taking Interop Requirements"
date = 2021-10-10T00:00:00

tags = ["note-taking", "roam-research", "go-note-go"]
+++

Yesterday I mused about [the benefits an interoperability standard could provide](/snippets/2021-10-09-note-taking-system-interop/) to note-taking systems. Today, I extract rough requirements for such a standard from that musing.

1. Note entry

  Note entry projects need to be able to insert notes into a notebase regardless of which note-taking system is storing the notebase.

  This is critical for projects like [my Browserflow note-taking flows](/snippets/2021-07-29-note-taking-flow/) (which only support Roam right now) and [Go Note Go](/projects/go-note-go/) to be multi-vendor.

  **"Restricted note entry"** allows an application like Go Note Go to insert notes into an application-specific section of the notes. In a "daily notes" oriented notebase like Roam, this is a "Go Note Go"-specific section on each daily notes page. In a page-oriented notebase, this can instead be an application specific page or namespace (e.g. "Go Note Go/\*") that notes can be inserted into. When using restricted note entry, an application can only insert notes into their own region of the notebase. This prevents the application from performing disruptive insertions that lower the quality of the notes outside of this region.

  **Unrestricted note entry** allows an application to perform a broader set of inserts, not limited to a specific region of the notes. For a note-taking entry system that also allows browsing the notes, where a user might want to insert new notes alongside an existing note they've pulled up, this becomes important.

2. Note reading

  **Individual note reading**

  **Batch note reading:** When notes are just text, reading large quantities of notes at a time becomes inexpensive. Often an entire text notebase is small enough to be kept in memory or transmitted over a network.

3. **Incremental export** is critical for real-time features, such as collaborative note-taking across systems. Also necessary for this is support for a **note view** and the ability to **subscribe** to updates. Consider a collaborative note-taking experience. I'm taking notes in Roam, and one of my blocks is an embed of a page from your notes in Notion. As you make edits to the page in Notion, they should appear in my notes. If I have edit access on that page, I should be able to directly edit that page in my notes too, and you should see the results reflected in Notion in real time.

  For this to work, both note-taking systems could need to support the necessary parts of the standard. If instead, Notion lacked the real-time import capability, a half-baked experience of cross-system collaborative note-taking could still be possible. As edits in Notion get saved, they appear in real-time in Roam. When edits are made in Roam, Notion would only render them upon reloading the page.

  If a conflict is introduced to the intermediate representation, it could be handled gracefully through a CRDT. If instead a conflict is introduced on the note-taking system side of things, then that note-taking system is responsible for handling the conflict resolution as it sees fit.

4. The above ideas taken together (and assumed idealized) can support the applications discussed yesterday: e.g. note entry systems like Go Note Go, advancements in spaced repetition, multiplayer spaced repetition, multiplayer note-taking, summarization features, highlight extraction features. What they don't support is the development of UI widgets that can be developed once and deployed across any note-taking system. Supporting that type of integration would require a greater degree / different type of standardization.

---

  Consider someone wanting to implement a summarization feature for note-taking systems, agnostic to the specific note-taking system being used. They train a machine learning model that can take a bunch of text notes and produce a quality summary. They implement a way for a user to efficiently select a collection of notes. The UI they choose allows searching by tags and keywords, navigating through the search results with the arrow keys and marking notes and their children for inclusion by pressing enter.

  When the user indicates they've selected the notes for summarization, they submit them to the feature's ML system, which produces a summary.
  if the user likes the summary, they accept it. When accepted, the feature inserts the summary into a dedicated Summarization specific section of the notes, complete with references to each of those notes used to produce the summary.

  This toy feature relies on having batch read access to the notes on the basis of a query, as well as restricted note entry permissions for writing notes back to the system. Using the hypothetical standard we are brainstorming toward in this snippet, such a system could be implemented once, but used by anyone with their notes in any of the note-taking systems that conform to these parts of the standard.

  An even better summarization feature would be one that doesn't require the user to select the notes to summarize. It would automatically identify chunks of notes on a related topic, and summarize those. When it generates a summary, it would offer it to the user, along with mentioning which notes were used in the generation of the summary. The user could choose to accept the summary (in which case it would be saved as explained above), or not to. This version of the features requires whole-notebase access to implement, a slightly more permissive requirement than query-based access.

---

What does such a _standard_ look like in practice? Maybe a useful analogy is thinking of it as an "LLVM" for notebases -- an "LLNB" if you will (unofficially standing for low level notebase, but not officially standing for anything...)

For each note-taking system we could implement a lossless bidirectional transform to a standard "intermediate representation". Tools and plugins could be written to operate on this shared representation, and they could then be deployed against any note-taking system with supported transformations to and from the shared representation.

The "intermediate representation" compiler analogy isn't perfect though, since I don't think it captures the desired incremental export, view, and subscription features we'd like in the LLNB system. We don't want to have to process an entire notebase to get it's LLNB form, and we don't want to have to overwrite an entire notebase to update it from a modified LLNB. Critical to this working is having the LLNB track its own updates and be able to export just what has changed, and similarly having the note-taking systems able to report either a full update (if no state about the notebase is known), or just an incremental update (if the notebase state was already exported recently). One way to achieve this would be to have an API that gives a diff between an earlier state of a notebase (say, indicated by a commit hash or timestamp) and the current state.

How about system-specific features? When features of a specific note-taking system X are used, they can appear in the intermediate representation as metadata. This metadata can be constituted appropriately when transferred back to X, or can be included as text if instead transferred to system Y. To make this concrete, support Notion has a geographic map feature that someone has used in their notes, but that is not supported by Roam. If the export their notes to LLNB, the map state is saved as e.g. {location: new jersey, zoom: 5}. If the notes are then imported back into Notion, the map will be restored. If instead the notes are imported into Roam, which lacks the map feature, the data about how the map feature will be included instead. So, if the notes are later exported from Roam and imported back into Notion, the map will be restored.

If the state of some feature is complicated and not practically serializable as a note, it can be stored outside the notebase, e.g. in Dropbox or Google Drive or whatever is appropriate, with a reference to that external storage medium used as the state.
