__all__ = ['identity', 'comp', 'const', 'flip', 'sbst']

from functools import reduce

def identity(x):
    """Trivial I combinator -- the identity function

    >>> identity(float('inf'))
    inf
    >>> identity(identity)
    <function identity at <memory location>>
    """
    return x

def comp(*fs):
    """B combinator -- function composition

    >>> fog = comp(lambda x: x + 1, lambda x: x * 2)
    >>> fog(2)
    5
    """
    match fs:
        case []:
            return identity
        case [f]:
            return f
        case [f, g]:
            return lambda *args, **kwargs: f(g(*args, **kwargs))
        case _:
            return reduce(comp, fs)

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
    return lambda *args, **kwargs: f(args[1], args[0], *args[2:], **kwargs)

def sbst(f, g):
    """S combinator -- substitutes the result from g(x) into the second argument of 'f' with 'x' preapplied

    >>> from functools import partial
    >>> from itertools import islice
    >>> from operator import mul, xor
    >>> def iterate(func, start):
    ...     x = start
    ...     while True:
    ...         yield x
    ...         x = func(x)
    ... 
    >>> for x in islice(iterate(sbst(xor, partial(mul, 2)), 1), 16):
    ...     print(''.join(map(lambda x: ' ' if x == '0' else '\u25b2', format(x, 'b'))))
    ... 
    ▲
    ▲▲
    ▲ ▲
    ▲▲▲▲
    ▲   ▲
    ▲▲  ▲▲
    ▲ ▲ ▲ ▲
    ▲▲▲▲▲▲▲▲
    ▲       ▲
    ▲▲      ▲▲
    ▲ ▲     ▲ ▲
    ▲▲▲▲    ▲▲▲▲
    ▲   ▲   ▲   ▲
    ▲▲  ▲▲  ▲▲  ▲▲
    ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲
    ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
    """
    return lambda x: f(x, g(x))
