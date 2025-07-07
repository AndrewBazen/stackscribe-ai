## Python

The built-in [filter](https://docs.python.org/3/library/functions.html#filter) [[Function]] takes a function and an [[Iterable]] (in this case a list) and returns an [[Iterator]] that only contains elements from the original iterable where the result of the function on that item returned `True`.

In Python:

```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]
```