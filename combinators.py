from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')
Us = TypeVarTuple('Us')
V = TypeVar('V')
W = TypeVar('W')

# Trivial I combinator -- the identity function
# identity(x) == x
def identity(x: T) -> T:
    return x

# B combinator -- function composition
# fog = comp(f, g)
# fog(x) == f(g(x))
def comp(f: Callable[[U], V], g: Callable[[T], U]) -> Callable[[T], V]:
    return lambda x: f(g(x))

# K combinator -- encodes a constant value
# const(x, y) == x
# const(x, y, z) == x
# etc.
def const(x: T) -> Callable[[*Us], T]:
    return lambda *ys: x

# S' combinator
def frk(f: Callable[[U, V], W], g: Callable[[T], U], h: Callable[[T], V]) -> Callable[[T], W]:
    return lambda x: f(g(x), h(x))

# W combinator -- duplicator
# dupd = dupl(f)
# dupd(x) == f(x, x)
def dupl(f: Callable[[T, T], U]) -> Callable[[T], U]:
    return lambda x: f(x, x)

# C combinator -- flips the argument order of its input function
def flip(f: Callable[[T, U], V]) -> Callable[[U, T], V]:
    return lambda x, y: f(y, x)

# ψ combinator -- "filters" the inputs to one function through another function
def on(f: Callable[[U, U], V], g: Callable[[T], U]) -> Callable[[T, T], V]:
    return lambda x, y: f(g(x), g(y))

# S combinator -- "substitution"
def sbst(f: Callable[[T, T], U], g: Callable[[T], U]) -> Callable[[T], U]:
    return lambda x: f(x, g(x))
