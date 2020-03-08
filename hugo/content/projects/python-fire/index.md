+++
active = false

title = "Python Fire"
weight = -20170301
date = 2017-03-01T00:00:00

summary = "Automatically generate CLIs from Python objects."
tags = ["Software", "Productivity"]

external_link = "https://github.com/google/python-fire"

[image]
  caption = "Python Fire"
  focal_point = "Smart"
+++

Python Fire is a Python library for automatically creating command line interfaces (CLIs) from absolutely any Python object.

Check it out at https://github.com/google/python-fire.

I originally wrote Python Fire after joining Google Brain in 2016. In March 2017 we open sourced the project, and I proud and delighted by the growth and reception it has seen since.

To give it a try, simply `pip install fire`, and then call `fire.Fire()` as the main of any Python program.

Here's a simple example to pique your interest, and then if you want to learn more, you should read the [Python Fire Guide](http://google.github.io/python-fire).

```python
import fire

def gcd(a, b):
  """Calculates the greatest common divisor of a and b."""
  if a < b:
    a, b = b, a
  if b == 0:
    return a
  return gcd(a % b, b)


if __name__ == '__main__':
  fire.Fire(gcd)
```

Saving this file as `gcdfire.py`, we can run at the command line:

```
$ python gcdfire.py 45 50
5
$ python gcdfire.py 34 90
2
```

Just by calling Fire, we've turned our gcd function into a command line utility.

Fire works on functions, classes, objects, lists, etc. Any Python object at all will be turned into a sensible CLI just by calling `fire.Fire` on it. Learn more from the [documentation here](http://google.github.io/python-fire).
