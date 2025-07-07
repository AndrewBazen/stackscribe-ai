## Python
In [[Python]], the built-in [map](https://docs.python.org/3/library/functions.html#map) [[Function]] takes a function and an [[Iterable]] (in this case a list) as inputs. It returns an [[Iterator]] that applies the function to every item, yielding the results.

With `map`, we can operate on [[List]]s without using [[Loops]] and nasty stateful [[Variables]]. For example:
```python
def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = map(square, nums)
print(list(squared_nums))
# [1, 4, 9, 16, 25]
```

_The [[List]] [[Type]] [[Constructor]], `list()` converts the `map` object back into a standard list._