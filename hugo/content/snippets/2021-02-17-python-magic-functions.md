+++
title = "Magic Functions in Python"
date = 2021-02-17T00:00:00
tags = ["python", "taking-silly-ideas-seriously"]
keywords = "magic functions"
icon = "star"
+++

In this snippet I introduce and implement, but do not condone, Python "Magic functions".
Magic functions are interesting to think about and to study, but I discourage their use in anything but the most experimental of code. You'll soon see why.

A **magic function** is a function where the arguments and return values are both implicit, handled through the magic of Python's powerful stack introspection.

Consider the following example, which implements the quadratic formula. Pay special attention to where quadratic_formula is called. No arguments are passed, and the result is not assigned to anything. Still, the program works.

```python
import math
import magic

def quadratic_formula(context):
  magic.unpack(context)
  discriminant = b**2 - 4*a*c
  x0, x1 = (
      (-b + math.sqrt(discriminant)) / (2*a),
      (-b - math.sqrt(discriminant)) / (2*a),
  )
  return magic.context()


def main():
  a, b, c = 1, -1, -12
  magic.call(quadratic_formula)
  print(f'x = {x0} or {x1}  (Discriminant is {discriminant})')

if __name__ == '__main__':
  main()
```

We say quadratic_formula is a "magic function", and it is called by invoking magic.call.

When we run this program, the result is:

```markdown
x = 4.0 or -3.0  (Discriminant is 49)
```

How did a, b, and c get passed to quadratic_formula? How did x0, x1, and discriminant find their way back to main? This is the magic of magic functions.

To implement a magic function, simply write a function that accepts a single argument `context`, calls `magic.unpack(context)` as its first line, and returns with `return magic.context()`.

To call a magic function, use `magic.call(fn)` as in the example above.

To "install" magic, so that you can import it as in the example above, simply save the following three-function Python file as `magic.py` in the directory where you'd like to use magic functions.

```python
import inspect

def call(fn, n=1):
  c = context(n=n+1)
  result = fn(c)
  unpack(result, n=n+1)

def context(n=1):
  c = {}
  caller = inspect.stack()[n]
  caller_frame = caller[0]
  caller_globals = caller_frame.f_globals
  caller_locals = caller_frame.f_locals
  c.update(caller_globals)
  c.update(caller_locals)
  return c

def unpack(c, n=1):
  caller = inspect.stack()[n]
  caller_frame = caller[0]
  caller_frame.f_globals.update(c)
```

These twenty lines of code comprise the complete implementation of the magic module.
Magic works by inspecting the stack to get the locals and globals when calling a magic function and when returning from a magic function -- this is done in the `context` function. Magic then makes use of stack inspection a second time to update the globals in the caller after a magic function returns -- this is done in `unpack`.

What purpose does this all serve? Why would you ever want to use magic functions?
The short answer is that you should _never_ use magic functions.
They will confuse readers of your code and are error prone.
Nevertheless, I will explain the situation that prompted me to write this module.

I wanted to write a machine learning training loop and reuse it for many different machine learning training pipelines. Each of the training pipelines needed to track metrics in its own way, save summaries in its own way, make plots in its own way, etc. A natural way to support all of these different needs is with hooks. A hook is a user provided callback function that the training loop library can call each iteration through the loop.

The trouble with hooks in this situation is that they require either very long argument lists, or bundling of many arguments into a single argument. If different functions need different bundles of arguments, the bundling approach can be quite cumbersome. Also, if two hooks wish to communicate with one another, that needs to be accommodated too. Magic functions provide one mechanism for dealing with this complexity. Different magic hooks can make use of different parts of the training loop's state. A magic hook can also use state set by another hook.
While this approach does satisfactorily address the complexity of writing a training loop library,
I must stress that I do not recommend this approach.


As with real magic, use `magic` at your own peril. :mage: :wink:
