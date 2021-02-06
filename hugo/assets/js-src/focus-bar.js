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
