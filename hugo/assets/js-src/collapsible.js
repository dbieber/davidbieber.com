// Collapsible Blog Posts
function swap(e1, e2) {
    e1.fadeOut(400).promise().done(function() {
        e2.fadeIn(400);
    });
}
function register_swap(e1, e2) {
    $(e1).on("click", function(e) {
        var srcEl = e.srcElement? e.srcElement : e.target;
        if (srcEl.tagName.toUpperCase() == "A") return;
        swap($(e1), $(e2));
    });
}
function register_pair(e1, e2) {
    register_swap(e1, e2);
    register_swap(e2, e1);
}
function addBorder(e1, style) {
    $(e1).css("border-left", style + " 1px lightgray");
    $(e1).css("padding-left", "5px");
}

document.addEventListener('DOMContentLoaded', function() {
  var paragraphs = $('.article-container *');
  for (var cv = 0; cv < paragraphs.length; cv++) {
      var keyId = paragraphs[cv].id;
      if (keyId.charAt(0) == "_") {
          register_pair('#' + keyId, '#' + keyId.substr(1));
          addBorder('#' + keyId, "dashed");
          addBorder('#' + keyId.substr(1), "solid");
      }
  }
}, false);
