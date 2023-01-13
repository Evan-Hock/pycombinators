def identity(x):
    """Trivial I combinator -- the identity function

    >>> identity(float('inf'))
    float('inf')
    >>> identity(identity)
    <function identity at <memory location>>
    """
    return x

def comp(f, g):
    """B combinator -- function composition

    >>> fog = comp(lambda x: x + 1, lambda x: x * 2)
    >>> fog(2)
    5
    """
    return lambda x: f(g(x))

def const(x):
    """K combinators -- encodes a constant value

    >>> always3 = const(3)
    >>> always3(*range(1000))
    3
    """
    return lambda *ys: x

def flip(f):
    """C combinator -- flips the arguments to a function around

    >>> from functools import reduce
    >>> from operator import sub
    >>> reduce(flip(sub), range(10))
    5
    """
    return lambda x, y: f(y, x)

def sbst(f, g):
    """S combinator -- substitutes the result from g(x) into the second argument of 'f' with 'x' preapplied

    >>> from functools import partial
    >>> from itertools import islice
    >>> from operator import mul, xor
    >>> take = lambda n, iterable: list(islice(iterable, n))
    >>> def sierpinski_generator():
    ...     sierpinski = sbst(xor, partial(mul, 2))
    ...     x = 1
    ...     while True:
    ...         yield x
    ...         x = sierpinski(x)
    ... 
    >>> for x in map(comp(partial(map, lambda x: '\u25b2' if x == '1' else ' '), partial(flip(format), 'b'), take(64, sierpinski_generator())):
    ...     print(''.join(x))
    ... 
    """
    return lambda x: f(x, g(x))
