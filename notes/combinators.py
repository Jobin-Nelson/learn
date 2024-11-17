from typing import Callable, TypeVar

A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')
D = TypeVar('D')

def b(f: Callable[[B], C], g: Callable[[A], B]) -> Callable[[A], C]:
    def inner(x: A) -> C:
        return f(g(x))
    return inner

def b1(f: Callable[[C], D], g: Callable[[A, B], C]) -> Callable[[A, B], D]:
    def inner(x: A, y: B) -> D:
        return f(g(x, y))
    return inner

def c(f: Callable[[B, A], C]) -> Callable[[A, B], C]:
    def inner(x: A, y: B) -> C:
        return f(y, x)
    return inner

def s(f: Callable[[A, B], D], g: Callable[[A], B]) -> Callable[[A], D]:
    def inner(x: A) -> D:
        return f(x, g(x))
    return inner

