from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')
Us = TypeVarTuple('Us')
V = TypeVar('V')

def identity(x: T) -> T:
    return x

def const(x: T) -> Callable[[*Us], T]:
    return lambda *ys: x

def flip(f: Callable[[T,U],V]) -> Callable[[U,T],V]:
    return lambda x, y: f(y, x)

def comp(f: Callable[[U],V], g: Callable[[T],U]) -> Callable[[T],V]:
    return lambda x: f(g(x))

def on(f: Callable[[U,U],V], g: Callable[[T],U]) -> Callable[[T,T],V]:
    return lambda x, y: f(g(x), g(y))

def dupl(f: Callable[[T,T],U]) -> Callable[[T],U]:
    return lambda x: f(x, x)
