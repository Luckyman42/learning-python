# TypeVarTuple – Variadic Generic Classes
# This is essentially the generic equivalent of Python's built-in TUPLE type.
# It allows creating generics that accept an arbitrary number of type parameters.

from typing import TypeVarTuple, Generic

Ts = TypeVarTuple("Ts")  # a tuple of types, e.g. (int), (int, str), (int, float, str), ...

# class Vector(Generic[*Ts]):
#     pass
#
# v1: Vector[int]
# v2: Vector[int, str]
# v3: Vector[int, float, str]
#
# This is revolutionary because previously we only had Tuple[T, U, ...] with fixed length.
# A TypeVarTuple must always be expanded when used.


from typing import Unpack, Tuple
from typing import cast

# You can reference the variadic type like this:
# -> tuple[Unpack[Ts]]
def make_tuple(*values: Unpack[Ts]) -> Tuple[Unpack[Ts]]:
    return cast(Tuple[Unpack[Ts]], tuple(values))


class Vector(Generic[*Ts]):
    # Here Ts represents a tuple of types, e.g. (int, str, float)
    _data: tuple[Unpack[Ts]]

    def __init__(self, *values: Unpack[Ts]) -> None:
        # Explanation:
        # - Ts is NOT itself a type, it's a *tuple of types*
        #   e.g. Ts = (int, str, float)
        # - Without Unpack, writing "*values: Ts" would mean
        #   "*values: (int, str, float)" which is invalid as a type annotation.
        #
        # By using Unpack:
        #    *values: Unpack[Ts]
        # is expanded to:
        #    *values: int, str, float   (in this exact order)
        #
        # So values becomes a tuple[int, str, float].
        self._data = cast(tuple[Unpack[Ts]], tuple(values))

    def get(self) -> Tuple[Unpack[Ts]]:
        return self._data

    def set_value(self, pos: int, value: object) -> None:
        # Simple setter with runtime type checking.
        if pos < 0 or pos >= len(self._data):
            raise IndexError("Index out of range")
        if isinstance(value, type(self._data[pos])):
            list_repr: list[object] = list(self._data)  # convert to mutable list
            list_repr[pos] = value
            self._data = tuple(list_repr)  # convert back to tuple
        else:
            raise TypeError("Invalid type")


vec: Vector[int, str, float] = Vector(1, "hello", 3.14)
print(vec.get())  # (1, "hello", 3.14)
vec.set_value(1, "world")
print(vec.get())  # (1, "world", 3.14)
