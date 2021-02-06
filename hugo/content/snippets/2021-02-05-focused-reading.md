+++
title = "A Flow for Focused Reading"
date = 2021-02-05T00:00:00
plugins_js = ["focus-bar"]
+++

As you can see from the snippet you're currently reading, I've implemented a simple tool to help with focused reading. (It's [the idea from the previous snippet](/snippets/2021-02-02-focused-reading-browserflow-flow-idea/)). The majority of the page is dimmed, except for a few lines above and below your mouse cursor. As you move your mouse, the focused region follows. Give it a try; move your mouse (or touch) over the next paragraph, and watch as the light region follows.

This is useful for staying focused when reading. If your eyes or mind wander while reading, it's easy to quickly bring your attention back to exactly where you left off.

For the [Browserflow](https://browserflow.app) users among you (psst... DK, you need to ship Browserflow so there _are_ Browserflow users out there), you can enable this effect on any page using [this BrowserFlow flow I made](https://browserflow.app/shared/8c2f3de8-2666-4578-8b42-58f5cad105b0). Once you get the flow you can simply type cmd-J and select "Focus Bar" from the typeahead to enable this effect anywhere.

For everyone else, you can paste this script into your JavaScript console. 🤷

```javascript
var mouseY = 0;
var scrollY = 0;
var offset = 50;
var div_below, div_above;

div_below = document.createElement("div");
div_below.style.position = "absolute";
div_below.style.left = "0px";
div_below.style.top = "0px";
div_below.style.width = "100%";
div_below.style.height = "100%";
div_below.style.background = "black";
div_below.style.opacity = "30%";

div_above = document.createElement("div");
div_above.style.position = "absolute";
div_above.style.left = "0px";
div_above.style.bottom = "0px";
div_above.style.width = "100%";
div_above.style.height = "100%";
div_above.style.background = "black";
div_above.style.opacity = "30%";

document.body.appendChild(div_below);
document.body.appendChild(div_above);

function adjust_divs() {
  scrollY = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
  div_below.style.top = (mouseY + offset + scrollY) + 'px';
  div_above.style.bottom = (
      'calc(100% - ' + (mouseY - offset + scrollY) + 'px');
  div_below.style.height = (
      'calc(100% - ' + (mouseY + offset) + 'px');
}

document.addEventListener('mousemove', function(event) {
  mouseY = event.clientY;
  adjust_divs();
}, true);

document.addEventListener('scroll', function(event) {
  adjust_divs();
}, true);
document.addEventListener('touchstart', function(event) {
  mouseY = event.touches[0].clientY;
  adjust_divs();
}, true);
document.addEventListener('touchmove', function(event) {
  mouseY = event.touches[0].clientY;
  adjust_divs();
}, true);
```

Sorry about the jitter. Let me know if you know how to fix it.
