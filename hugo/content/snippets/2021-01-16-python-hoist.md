+++
title = "Python hoist()"
date = 2021-01-16T00:00:00
tags = ["python", "taking-silly-ideas-seriously"]
keywords = ["python hoist"]
icon = "star"
+++

I wrote a little decorator function called `hoist`. Calling `hoist(f)` transforms `f`, such that instead of returning the return value of `f`, it returns the values of all local variables in addition to the return value of `f`.

You can use it like this:

```python
def f(x):
  y = x + 1
  z = y * 2
  return z + 1

f(4) == 11
hoist(f)(4) == {'x': 4, 'y': 5, 'z': 10, 'return': 11}
```

Make sense? The result of `f(4)` is just the return value, whereas `hoist(f)(4)` gives the values of all local variables.

This can be a useful debugging tool, allowing access to the internal state of a function. It works by setting a trace function with Python's `sys.settrace`, as you can see in its definition.

Here's the definition of `hoist`:

```python
import inspect
import functools


class Collection(object):
  """The full set of variables over time."""

  def __init__(self):
    self.values = {}

  def update(self, values):
    self.values.update(values)

  def set_return(self, arg):
    self.values['return'] = arg

  def __repr__(self):
    return repr(self.values)


def make_trace(results, fn):
  def trace_local(frame, event, arg):
    # event: 'call', 'line', 'return', 'exception' or 'opcode'
    if event == 'line':
      arg_info = inspect.getargvalues(frame)
      results.update(arg_info.locals.copy())
    if event == 'return':
      arg_info = inspect.getargvalues(frame)
      values = arg_info.locals.copy()
      results.update(values)
      results.set_return(arg)
    if event == 'call':
      return fn

  def trace_global(frame, event, arg):
    if event == 'call':
      return trace_local
  return trace_global


def hoist(f):

  @functools.wraps(f)
  def new_f(*args, **kwargs):
    original_trace_fn = sys.gettrace()

    results = Collection()
    trace_fn = make_trace(results, original_trace_fn)

    sys.settrace(trace_fn)
    f(*args, **kwargs)
    sys.settrace(original_trace_fn)

    return results

  return new_f
```

Some ideas for extensions to `hoist` follow. Feel free to go ahead and implement these.

(1) Modify `hoist` so the outputs are accessible via dot-notation.

(2) Modify `hoist` so it returns all values taken on by all variables during the execution of `f`.
Make it so that `hoist(f)(x)['value.3']` returns the third value taken on by the variable `value` in the call to `f(x)`.
