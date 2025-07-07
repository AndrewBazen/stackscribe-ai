# Functional Programming
[Functional programming](https://en.wikipedia.org/wiki/Functional_programming) is more about declaring _what_ you want to happen, rather than _how_ you want it to happen.
[[Declarative]]
[[Imperative]] (or procedural) programming declares both the _what_ and the _how_.

# Immutability

In FP, we strive to make data _[immutable](https://en.wikipedia.org/wiki/Immutable_object)_. Once a value is created, it cannot be changed. _Mutable_ data, on the other hand, can be changed after it's created.

## Who Cares?

[[Immutable]] data is easier to think about and work with. When 10 different functions have access to the same [[Variable]], and you're [[Debugging]] a problem with that variable, you have to consider the possibility that any of those [[Functions]] could have changed the value.

When a variable is [[Immutable]], you can be sure that it hasn't changed since it was created. It's a helluva lot easier to work with.

_Generally speaking, immutability means fewer bugs and more maintainable code._

## Tuples vs. Lists

[[Tuples]] and [[Lists]] are both ordered [[Collections]] of values, but tuples are _immutable_ and lists are _[[Mutable]]_.

You can append to a list, but you can _not_ append to a tuple. You can create a _new copy_ of a tuple using values from an existing tuple, but you can't change the existing tuple.

### Lists Are Mutable
```python
ages = [16, 21, 30]
# 'ages' is being changed in place
ages.append(80)
# [16, 21, 30, 80]
```
### Tuples Are Immutable
```python
ages = (16, 21, 30)
more_ages = (80,) # note the comma! It's required for a single-element tuple
# 'all_ages' is a brand new tuple
all_ages = ages + more_ages
# (16, 21, 30, 80)
```

# Classes vs. Functions
**If you're unsure, default to functions.** I find myself reaching for classes when I need something long-lived and stateful that would be easier to model if I could share behavior _and data structure_ via inheritance. This is often the case for:

- Video games
- Simulations
- GUIs

The difference is:

> **[[Class]]es** encourage you to think about the world as a hierarchical [[Collection]] of [[Objects]]. Objects bundle behavior, data, and state together in a way that draws boundaries between instances of things, like chess pieces on a board.

> **[[Functions]]** encourage you to think about the world as a series of data transformations. Functions take data as input and return a transformed output. For example, a function might take the entire [[State]] of a chess board and a move as inputs, and return the new state of the board as output.

_Use what feels right to you in your projects, and adjust and refactor as you improve your skills._

| Topics                                   |     |
| ---------------------------------------- | --- |
| [[First Class & Higher Order Functions]] |     |
| [[Pure Functions]]                       |     |
| [[Recursion]]                            |     |
| [[Function Transformations]]             |     |
| [[Closures]]                             |     |
| [[Currying]]                             |     |
| [[Decorators]]                           |     |
| [[Sum Types]]                            |     |
