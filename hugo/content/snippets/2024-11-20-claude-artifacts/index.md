+++
title = "Writing with Claude Artifacts"
date = 2024-11-20T00:00:00
tags = []
keywords = []
plugins_js = ["2024-11-20-claude-artifacts.bundle"]
+++

This is a snippet for me to experiment with embedding a Claude artifact into a snippet.
The main challenge I expect to encounter is that Claude builds artifacts with React, so I'll have to learn how to integrate webpack or similar into my Hugo setup. Fortunately, I have Claude here to help me with that.

<div id="jellybean-container"></div>

Success!

The [main steps](https://github.com/dbieber/davidbieber.com/pull/3/files) were to set up a webpack config that converts any per-snippet JS, JSX, and CSS files into a bundle. I can then lean on my existing plugins_js setup to pull that bundled js file into the corresponding snippet. There's room for improvement in this setup, but it's working (at least locally) for now.

