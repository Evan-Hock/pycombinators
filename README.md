# combinators.py
Elementary combinators in Python inspired by LISP and Haskell. Mostly a convenience library for my sake.

## Installation

```
pip install pycombinators
```

## Sample Usage
```py
from pycombinators import flip
from functools import partial

# returns true if all values in xs are numbers
def is_all_numbers(xs: list) -> bool:
    isinstanceof = flip(isinstance)
    return all(map(partial(isinstanceof, float), xs))
```
