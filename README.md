# combinators.py
Elementary combinators in Python inspired by LISP and Haskell. Mostly a convenience library for my sake.

## Installation

```
pip install combinators
```

## Sample Usage
```py
from combinators import flip
from functools import partial

# returns true if all values in xs are numbers
def all_numbers(xs: list) -> bool:
    isinstanceof = flip(isinstance)
    return all(map(partial(isinstanceof, float), xs))
```
