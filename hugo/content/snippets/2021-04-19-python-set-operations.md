+++
title = "Python set operations"
date = 2021-04-19T00:00:00
tags = ["python"]
keywords = []
+++

If you Google "Python set intersection", you get a number of results about the `set.intersection` function. It isn't until the fourth result that you reach a page mentioning Python's convenient syntax for performing set operations. This was surprising to me, hence this snippet.

## Background: Collections in Python

Python has a few primitive collection types: tuples, lists, dictionaries (aka dicts), and sets. Use parenthesis to create a tuple `(1, 2, 3)`, square brackets to create a list `[4, 5, 6]`, and squirrelly brackets to create a dict or set: `{7: 8, 9: 10}` makes a dict and `{11, 12, 13}` makes a set. Just like a set in mathematics, a set in Python is an __unordered__ collection of __distinct__ elements.

## Convenient Syntax

Once you've constructed a set, the following operations allow you to perform set operations on it with clean concise syntax.

```
| for union.
& for intersection.
– for difference
^ for symmetric difference
```

## Operation Examples

Here are some examples:

```python
# Example 1: Disjoint sets (sets that have no elements in common)
{1, 2, 3} | {4, 5, 6} == {1, 2, 3, 4, 5, 6}
{1, 2, 3} & {4, 5, 6} == set()
{1, 2, 3} - {4, 5, 6} == {1, 2, 3}
{1, 2, 3} ^ {4, 5, 6} == {1, 2, 3, 4, 5, 6}
```

Notice how we cannot write `{}` to create an empty set. That would create an empty dict. Instead we write `set()`. (You can also write `tuple()`, `list()`, and `dict()` to create empty tuples, lists, or dicts.)

```python
# Example 2: Overlapping sets
{'red', 'green', 'blue'} | {'blue', 'yellow'} == {'red', 'green', 'blue', 'yellow'}
{'red', 'green', 'blue'} & {'blue', 'yellow'} == {'blue'}
{'red', 'green', 'blue'} - {'blue', 'yellow'} == {'red', 'green'}
{'red', 'green', 'blue'} ^ {'blue', 'yellow'} == {'red', 'yellow', 'green'}
```

## Set augment operations

Each of the operations `|`, `&`, `-`, and `^` has a corresponding "augment" operation: `|=`, `&=`, `-=`, and `^=`.

When you use an augment operation, the operation is applied and the result is assigned back to the variable on the left hand side of the operation.

Here's an example of how to use these operations:

```python
# Example 3: Set augment operations (|=, &=, -=, and ^=)
x = {1, 2, 3}
x |= {3, 4, 5}
print(x)  # {1, 2, 3, 4, 5}
x &= {4, 5, 6}
print(x)  # {4, 5}
x -= {5, 6, 7}
print(x)  # {4}
x ^= {6, 7, 8}
print(x)  # {4, 6, 7, 8}
```

## Set elements must be hashable

Remember, sets can contain any elements as long as they are hashable. So, a set can contain numbers, strings, and bools. A set can also contain tuples, but not lists or dicts or other sets. If you want a set to contain a dict or another set, you can use a "frozendict" or "frozenset", which are immutable hashable versions of dicts and sets.

To check if an object `x` is hashable, you can run `hash(x)`. This will return the hash of `x` if `x` can be hashed, and will raise a TypeError otherwise.
