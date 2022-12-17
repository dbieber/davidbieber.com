// MIT License
// Copyright (c) 2019 Fabian Tamp
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

import { docReady, onWindowResize } from "./margin-notes-utils.js";
import { ResizeObserver } from '@juggle/resize-observer';

var ARTICLE_CONTENT_SELECTOR = "#article-content";
var FOOTNOTE_SECTION_SELECTOR = "section.footnotes[role=doc-endnotes]";
var FLOATING_FOOTNOTE_MIN_WIDTH = 1620;

// Computes an offset such that setting `top` on elemToAlign will put it
// in vertical alignment with targetAlignment.
function computeOffsetForAlignment(elemToAlign, targetAlignment) {
    var offsetParentTop = elemToAlign.offsetParent.getBoundingClientRect().top;
    // Distance between the top of the offset parent and the top of the target alignment
    return targetAlignment.getBoundingClientRect().top - offsetParentTop;
}

function setFootnoteOffsets(footnotes) {
    // Keep track of the bottom of the last element, because we don't want to
    // overlap footnotes.
    var bottomOfLastElem = 0;
    Array.prototype.forEach.call(footnotes, function (footnote, i) {

        // In theory, don't need to escape this because IDs can't contain
        // quotes, in practice, not sure. ¯\_(ツ)_/¯

        // Get the thing that refers to the footnote
        var intextLink = document.querySelector("a.footnote-ref[href='#" + footnote.id + "']");
        // Find its "content parent"; nearest paragraph or list item or
        // whatever. We use this for alignment because it looks much cleaner.
        // If it doesn't, your paragraphs are too long :P
        // Fallback - use the same height as the link.
        var verticalAlignmentTarget = intextLink.closest('p,li') || intextLink;

        var offset = computeOffsetForAlignment(footnote, verticalAlignmentTarget);
        if (offset < bottomOfLastElem) {
            offset = bottomOfLastElem;
        }
        // computedStyle values are always in pixels, but have the suffix 'px'.
        // offsetHeight doesn't include margins, but we want it to use them so
        // we retain the style / visual fidelity when all the footnotes are
        // crammed together.
        bottomOfLastElem = offset + footnote.offsetHeight + parseInt(window.getComputedStyle(footnote).marginBottom) + parseInt(window.getComputedStyle(footnote).marginTop);

        footnote.style.top = offset + 'px';
        footnote.style.position = 'absolute';
    });
}

function clearFootnoteOffsets(footnotes) {
    // Reset all
    Array.prototype.forEach.call(footnotes, function (fn, i) {
        fn.style.top = null;
        fn.style.position = null;
    });
}

// Contract: this is idempotent. It won't wreck anything if you call it
// with the same value over and over again. Though maybe it'll wreck performance...
function updateFootnoteFloat(shouldFloat) {
    var footnoteSection = document.querySelector(FOOTNOTE_SECTION_SELECTOR);
    var footnotes = footnoteSection.querySelectorAll("li[role=doc-endnote]");

    if (shouldFloat) {
        // Do this first because we need styles applied before doing other
        // calculations
        footnoteSection.classList.add('floating-footnotes');
        setFootnoteOffsets(footnotes);
        subscribeToUpdates();
    } else {
        unsubscribeFromUpdates();
        clearFootnoteOffsets(footnotes);
        footnoteSection.classList.remove('floating-footnotes');
    }
}

function subscribeToUpdates() {
    var article = document.querySelector(ARTICLE_CONTENT_SELECTOR);
    // Watch for dimension changes on the thing that holds all the footnotes so
    // we can reposition as required
    resizeObserver.observe(article);
}

function unsubscribeFromUpdates() {
    resizeObserver.disconnect();
}

var notifySizeChange = function () {
    // Default state, not expanded.
    var bigEnough = false;

    return function () {
        // Pixel width at which this looks good
        var nowBigEnough = window.innerWidth >= FLOATING_FOOTNOTE_MIN_WIDTH;
        if (nowBigEnough !== bigEnough) {
            updateFootnoteFloat(nowBigEnough);
            bigEnough = nowBigEnough;
        }
    };
}();

var resizeObserver = new ResizeObserver(function (_entries, observer) {
    // By virtue of the fact that we're subscribed, we know this is true.
    updateFootnoteFloat(true);
});

export default function enableFloatingFootnotes() {
    docReady(function () {
        var footnoteSection = document.querySelector(FOOTNOTE_SECTION_SELECTOR);
        var article = document.querySelector(ARTICLE_CONTENT_SELECTOR);
        var allowFloatingFootnotes = article && !article.classList.contains('no-floating-footnotes');

        // only set it all up if there's actually a footnote section and
        // we haven't explicitly disabled floating footnotes.
        if (footnoteSection && allowFloatingFootnotes) {
            onWindowResize(notifySizeChange);
        }
    });
}

window.enableFloatingFootnotes = enableFloatingFootnotes;
enableFloatingFootnotes();