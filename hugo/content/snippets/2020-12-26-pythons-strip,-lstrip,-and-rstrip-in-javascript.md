+++
title = "Python's strip, lstrip, and rstrip in JavaScript"
date = 2020-12-26T00:00:00

+++

Python provides some convenient functions for manipulating strings: `strip`, `lstrip`, and `rstrip`. Recently I was writing some JavaScript and wanted to use `rstrip`. So, I've implemented all three. Here they are:

## The Python strip method in JavaScript

In Python, `strip` removes whitespace from the beginning or end of a string. This is commonly called "trim" in JavaScript, and is provided as a builtin in most modern browsers. You may need to implement it yourself if you want to support older browsers though. Here's one possible implementation, [courtesy of W3Schools](https://www.w3schools.com/python/ref_string_strip.asp).

```javascript
function trim(x) {
  return x.replace(/^\s+|\s+$/gm, '');
}
```

The Python `strip` method optionally accepts an argument, "characters", and strips all instances of those characters from the left and right sides of the input string. We implement that here.

```javascript
function trim(x, characters) {
  var start = 0;
  while (characters.indexOf(x[start]) >= 0) {
    start += 1;
  }
  var end = x.length - 1;
  while (characters.indexOf(x[end]) >= 0) {
    end -= 1;
  }
  return x.substr(start, end - start + 1);
}
```

This may not be the most efficient implementation (the calls to indexOf in particular could be made faster), but it gets the job done.

## The Python rstrip method in JavaScript

The rstrip method behaves like strip, but only removes spaces (or the specified characters) from the right side of the input string. We implement this in JavaScript now, calling it "rtrim" for consistency with the name "trim".

```javascript
function rtrim(x) {
  // This implementation removes whitespace from the right side
  // of the input string.
  return x.replace(/\s+$/gm, '');
}
```

We now implement rtrim a second time, now accepting "characters" as input:

```javascript
function rtrim(x, characters) {
  var start = 0;
  var end = x.length - 1;
  while (characters.indexOf(x[end]) >= 0) {
    end -= 1;
  }
  return x.substr(0, end + 1);
}
```

## The Python lstrip method in JavaScript

Finally we provide a port of Python's lstrip to JavaScript, calling it ltrim. We again provide one version that strips only whitespace, and a second that strips the provided "characters" input.

```javascript
function ltrim(x) {
  // This implementation removes whitespace from the left side
  // of the input string.
  return x.replace(/^\s+/gm, '');
}
```

We now implement rtrim a second time, now accepting "characters" as input:

```javascript
function ltrim(x, characters) {
  var start = 0;
  while (characters.indexOf(x[start]) >= 0) {
    start += 1;
  }
  var end = x.length - 1;
  return x.substr(start);
}
```

## Example Usage

Here are some example usages of the above functions.

First, using the implementations that strip spaces:

```javascript
trim('   Hello world!   ') === 'Hello world!';
ltrim('   Hello world!   ') === 'Hello world!   ';
rtrim('   Hello world!   ') === '   Hello world!';
```

Second, using the implementations that strip the specified characters:

```javascript
trim('Buzzzzzz', 'Bz') === 'u';
ltrim('Buzzzzzz', 'Bz') === 'uzzzzzz';
rtrim('Buzzzzzz', 'Bz') === 'Bu';```
