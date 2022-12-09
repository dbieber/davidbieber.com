+++
title = "Hugo Layouts for this Website"
date = 2022-07-20T01:00:00
tags = []
+++

This is a note-to-self about how the code base for this website, davidbieber.com, is organized. There are several "layouts" files that live in the [hugo/layouts](https://github.com/dbieber/davidbieber.com/tree/master/hugo/layouts) directories. This is what each of them does:

#### [hugo/layouts/_default/list.html](https://github.com/dbieber/davidbieber.com/blob/master/hugo/layouts/_default/list.html)

[list.html](https://github.com/dbieber/davidbieber.com/blob/master/hugo/layouts/_default/list.html) defines how [/snippets](/snippets), [/tags](/tags), and each of the individual /tags/<tag> pages are rendered. Each of these pages holds a list of links, as well as a Discussion section.

#### [hugo/layouts/_default/rss.xml](https://github.com/dbieber/davidbieber.com/blob/master/hugo/layouts/_default/rss.xml)

Defines the rss feeds for [snippets](/snippets/index.xml) and for [posts](/posts/index.xml).

#### [hugo/layouts/partials/widgets/pages.html](https://github.com/dbieber/davidbieber.com/blob/master/hugo/layouts/partials/widgets/pages.html)

Used to render the posts widget on the home page.

#### [/hugo/themes/academic/layouts/section/post.html](/Users/dbieber/code/github/dbieber/davidbieber.com/hugo/themes/academic/layouts/section/post.html)

Used to render the [/posts](/posts) page. (Part of the theme.)

#### [hugo/layouts/partials/widgets/portfolio.html](https://github.com/dbieber/davidbieber.com/blob/master/hugo/layouts/partials/widgets/portfolio.html)

Used to render the [/projects](/projects) page.

#### [hugo/layouts/partials/custom_js.html](https://github.com/dbieber/davidbieber.com/blob/master/hugo/layouts/partials/custom_js.html)

Embeds Firebase, Tumblr Embed Gist, JQuery, and React. Just the staples that appear on every page.

#### [hugo/layouts/partials/custom_js_extra.html](https://github.com/dbieber/davidbieber.com/blob/master/hugo/layouts/partials/custom_js_extra.html)

Embeds page-specific JS bundles, e.g. Ask-Me-Anywhere, or margin-notes.js. The source for the custom JS bundles lives in [assets/js-src](https://github.com/dbieber/davidbieber.com/tree/master/hugo/assets/js-src).

#### [hugo/layouts/partials/discussion.html](https://github.com/dbieber/davidbieber.com/blob/master/hugo/layouts/partials/discussion.html)

Embeds Discord on the page.

#### [hugo/layouts/partials/page_header.html](https://github.com/dbieber/davidbieber.com/blob/master/hugo/layouts/partials/page_header.html)

Renders post header data, such as a chip if appropriate, the header image, and title and subtitle headers.

#### [hugo/layouts/partials/page_footer.html](https://github.com/dbieber/davidbieber.com/blob/master/hugo/layouts/partials/page_footer.html)

Shows tags.
Includes the Discord discussion partial.
Includes 4 related pages in the footer.
Shows the author.

#### [hugo/layouts/partials/page_metadata_authors.html](https://github.com/dbieber/davidbieber.com/blob/master/hugo/layouts/partials/page_metadata_authors.html)

Empty. Overwrites the equivalent file from the Academic theme preventing author metadata from rendering.

---

Future self, hope you find that useful!