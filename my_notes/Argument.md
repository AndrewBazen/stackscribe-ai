
# Args and Kwargs

In Python, [`*args` and `**kwargs`](https://book.pythontips.com/en/latest/args_and_kwargs.html) allow a function to accept and deal with a _variable_ number of arguments.

- `*args` collects positional arguments into a _tuple_
- `**kwargs` collects keyword (named) arguments into a _dictionary_

```python
def print_arguments(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print_arguments("hello", "world", a=1, b=2)
# Positional arguments: ('hello', 'world')
# Keyword arguments: {'a': 1, 'b': 2}
```

## Positional Arguments

Positional arguments are the ones you're already familiar with, where the order of the arguments matters. Like this:

```python
def sub(a, b):
    return a - b

# a=3, b=2
res = sub(3, 2)
# res = 1
```

## Keyword Arguments

[Keyword arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments) are passed in by name. _Order does not matter_. Like this:

```python
def sub(a, b):
    return a - b

res = sub(b=3, a=2)
# res = -1
res = sub(a=3, b=2)
# res = 1
```

## A Note on Ordering

Any positional arguments _must come before_ keyword arguments. This will _not_ work:

```python
sub(b=3, 2)
```