+++
title = "Introducing Python Fire"
subtitle = "A library for automatically generating command line interfaces"

date = 2017-03-06T00:00:00
lastmod = 2017-03-06T00:00:00
draft = false

authors = ["admin"]

tags = ["Python Fire"]
summary = "Python Fire automatically generates command line interfaces from any Python objects."

[image]
  caption = "Image credit: [**Skitterphoto**](https://www.pexels.com/photo/fire-hell-inferno-flame-9328/)"
  focal_point = ""
+++

_Originally posted on the Google Open Source Blog_

Today we are pleased to announce the open-sourcing of [Python Fire](https://github.com/google/python-fire). Python Fire generates command line interfaces (CLIs) from any Python code. Simply call the Fire function in any Python program to automatically turn that program into a CLI. The library is available from [pypi](https://pypi.org/project/fire/) via `pip install fire`, and the source is [available on GitHub](https://github.com/google/python-fire).

Python Fire will automatically turn your code into a CLI without you needing to do any additional work. You don’t have to define arguments, set up help information, or write a main function that defines how your code is run. Instead, you simply call the `Fire` function from your main module, and Python Fire takes care of the rest. It uses inspection to turn whatever Python object you give it – whether it’s a class, an object, a dictionary, a function, or even a whole module – into a command line interface, complete with tab completion and documentation, and the CLI will stay up-to-date even as the code changes.

To illustrate this, let’s look at a simple example.

```python
#!/usr/bin/env python
import fire

class Example(object):
  def hello(self, name='world'):
    """Says hello to the specified name."""
    return 'Hello {name}!'.format(name=name)

def main():
  fire.Fire(Example)

if __name__ == '__main__':
  main()
```

When the Fire function is run, our command will be executed. Just by calling Fire, we can now use the Example class as if it were a command line utility.

```
$ ./example.py hello
Hello world!
$ ./example.py hello David
Hello David!
$ ./example.py hello --name=Google
Hello Google!
```

Of course, you can continue to use this module like an ordinary Python library, enabling you to use the exact same code both from Bash and Python. If you’re writing a Python library, then you no longer need to update your main method or client when experimenting with it; instead you can simply run the piece of your library that you’re experimenting with from the command line. Even as the library changes, the command line tool stays up to date.

At Google, engineers use Python Fire to generate command line tools from Python libraries. We have an image manipulation tool built by using Fire with the [Python Imaging Library](https://en.wikipedia.org/wiki/Python_Imaging_Library), PIL. In [Google Brain](https://ai.google/research/teams/brain), we use an experiment management tool built with Fire, allowing us to manage experiments equally well from Python or from Bash.

Every Fire CLI comes with an interactive mode. Run the CLI with the `--interactive` flag to launch an [IPython](https://ipython.org/) [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) with the result of your command, as well as other useful variables already defined and ready to use. Be sure to check out [Python Fire’s documentation](https://github.com/google/python-fire#python-fire-) for more on this and the other useful features Fire provides.

Between Python Fire’s simplicity, generality, and power, we hope you find it a useful library for your own projects.