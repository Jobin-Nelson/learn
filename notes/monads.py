from abc import ABC, abstractmethod
from functools import partial
from typing import TypeAlias, TypeVar, Callable, Generic

T = TypeVar('T')  # Success type
E = TypeVar('E')  # Error type
U = TypeVar('U')  # Return success type


class Maybe(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def map(self, f: Callable[[T], U]) -> 'Maybe[T] | Maybe[U]':
        if self.is_empty():
            return self
        return Maybe(f(self.value))

    def flat_map(self, f: Callable[[T], 'Maybe[U]']) -> 'Maybe[T] | Maybe[U]':
        if self.is_empty():
            return self
        return f(self.value)

    def is_empty(self) -> bool:
        return self.value is None


class EitherABC(ABC, Generic[T, E]):
    def is_left(self) -> bool:
        return not self.is_right()

    @property
    @abstractmethod
    def value(self) -> T | E:
        raise NotImplementedError

    @abstractmethod
    def is_right(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def map(self, func: Callable[[T], U]) -> 'EitherABC[T, E] | EitherABC[U, E]':
        raise NotImplementedError()

    @abstractmethod
    def flat_map(
        self, func: Callable[[T], 'EitherABC[U, E]']
    ) -> 'EitherABC[T, E] | EitherABC[U, E]':
        raise NotImplementedError()


class Left(EitherABC[T, E]):
    def __init__(self, value: E) -> None:
        self._error = value

    def is_right(self) -> bool:
        return False

    def map(self, func: Callable[[T], U]) -> EitherABC[T, E]:
        return self  # No transformation on Left

    def flat_map(self, func: Callable[[T], EitherABC[U, E]]) -> EitherABC[T, E]:
        return self  # No transformation on Left

    @property
    def value(self) -> E:
        return self._error


class Right(EitherABC[T, E]):
    def __init__(self, value: T) -> None:
        self._value = value

    def is_right(self) -> bool:
        return True

    def map(self, func: Callable[[T], U]) -> EitherABC[U, E]:
        return Right(func(self._value))

    def flat_map(self, func: Callable[[T], EitherABC[U, E]]) -> EitherABC[U, E]:
        return func(self._value)

    @property
    def value(self) -> T:
        return self._value

Either: TypeAlias = Left | Right


# Example usage
def safe_divide(a: float, b: float) -> EitherABC[float, str]:
    if b == 0:
        return Left("Division by zero")
    return Right(a / b)


def return_left(_: float) -> EitherABC[float, str]:
    return Left('Division by zero')


result1: EitherABC[float, str] = safe_divide(10, 2).flat_map(partial(safe_divide, b=0))
result2: EitherABC[float, str] = safe_divide(10, 2).flat_map(partial(safe_divide, b=2))
result3: EitherABC[float, str] = safe_divide(10, 2).map(lambda x: x + 10)


def check_result(res: EitherABC[float, str]) -> None:
    if res.is_right():
        print("Result:", res.value)  # Output: Result: 5.0
    else:
        print("Error:", res.value)  # Not reached


check_result(result1)
check_result(result2)
check_result(result3)

print(Right(10).map(lambda x: x + 15).value)
print(Right(10).flat_map(return_left).is_right())
