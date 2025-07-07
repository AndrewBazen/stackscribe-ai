## Python

The built-in functools.reduce()  [[Function]] takes a function and a [[List]] of values, and applies the function to each value in the list, _accumulating a single result_ as it goes.

```python
# import functools from the standard library
import functools

def add(sum_so_far, x):
    print(f"sum_so_far: {sum_so_far}, x: {x}")
    return sum_so_far + x

numbers = [1, 2, 3, 4]
sum = functools.reduce(add, numbers)
# sum_so_far: 1, x: 2
# sum_so_far: 3, x: 3
# sum_so_far: 6, x: 4
# 10 doesn't print, it's just the final result
print(sum)
# 10
```

Notice that we are passing the function `add` without the `()`.

It means that `reduce` will take care of the execution and pass the [[Parameter]]s for you.

Think of passing `add` like handing someone a recipe (the instructions), instead  
of the finished dish (the result of the execution).