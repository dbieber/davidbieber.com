+++
title = "Python hoist: immediate locals only"
date = 2021-01-18T00:00:00
tags = ["python", "taking-silly-ideas-seriously"]
keywords = ["python hoist"]
+++

The implementation of `hoist` in my [earlier snippet](/snippets/2021-01-16-python-hoist/) returned the values of local variables of all functions called by the hoisted function. This new version only returns the locals of the hoisted function.

As before, you can use it like this:

```python
def f(x):
  y = x + 1
  z = y * 2
  return z + 1

f(4) == 11
hoist(f)(4) == {'x': 4, 'y': 5, 'z': 10, 'return': 11}
```

Here's another usage example:

```python
def f(x):
  y = messy_g(x + 1)
  return y + 1

def messy_g(z):
  q = z * 9
  w = q / 3
  return w + 1

f(1) == 8
hoist(f)(1) == {'x': 1, 'y': 7, 'return': 8}
```

Notice in this example that the local variables used by `messy_g` are not returned by `hoist(f)`. Only `f`'s local variables are returned.

Here's the implementation.

```python
import functools
import inspect
import sys

def make_trace(results, f, original_trace_fn):
  def trace_local(frame, event, arg):
    # event: 'call', 'line', 'return', 'exception' or 'opcode'
    if event == 'line':
      arg_info = inspect.getargvalues(frame)
      results.update(arg_info.locals.copy())
    if event == 'return':
      arg_info = inspect.getargvalues(frame)
      values = arg_info.locals.copy()
      results.update(values)
      results['return'] = arg
    if event == 'call':
      return original_trace_fn

  def trace_global(frame, event, arg):
    if event == 'call':
      info = inspect.getframeinfo(frame)
      info_parent = inspect.getframeinfo(frame.f_back)
      if info.function == f.__name__ and info_parent.function == 'hoisted_f__':
        return trace_local
  return trace_global


def hoist(f):

  @functools.wraps(f)
  def hoisted_f__(*args, **kwargs):
    original_trace_fn = sys.gettrace()

    results = {}
    trace_fn = make_trace(results, f, original_trace_fn)

    sys.settrace(trace_fn)
    f(*args, **kwargs)
    sys.settrace(original_trace_fn)

    return results

  return hoisted_f__
```
