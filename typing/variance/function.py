# Function types behave in a special way:
# - They are *contravariant* in their input parameter.
# - They are *covariant* in their output parameter.
from typing import Callable

class Complex:
    float_part: float
    imagenary_part: float
    def __init__(self, float_part: float, imagenary_part: float):
        self.float_part = float_part
        self.imagenary_part = imagenary_part

class Rational(Complex):
    numerator: int
    denominator: int
    def __init__(self, numerator: int, denominator: int):
        super().__init__(numerator / denominator, 0.0)
        self.numerator = numerator
        self.denominator = denominator

class Integer(Rational):
    value : int
    def __init__(self, value: int):
        super().__init__(value, 1)


def floor(r: Rational) -> Integer:
    return Integer(r.numerator)

def to_rational(i: Integer) -> Rational:
    return Rational(i.value, 1)

def call(func: Callable[[Integer], Rational], arg: Integer) -> Rational:
    return func(arg)


# The 'call' function expects a function of type Integer -> Rational.
# Surprisingly, we can pass 'floor', which has type Rational -> Integer.
call(floor, Integer(5))  # Works, even though the types seem reversed!

# Why does this work?
# Because Integer is a subtype of Rational: Integer <: Rational.
# For function types:
# - The input is contravariant: a function that accepts a *broader* type
#   can replace one that expects a more specific type.
# - The output is covariant: a function that returns a *more specific* type
#   can replace one that returns a broader type.
#
# Therefore:
#   Rational -> Integer  is a subtype of  Integer -> Rational
#   R -> I  <:  I -> R

def call2(func: Callable[[Rational], Rational], arg: Rational) -> Rational:
    return func(arg)

def complex_to_integer(c: Complex) -> Integer:
    return Integer(int(c.float_part))

# This also works for the same reason:
# Complex -> Integer  <:  Rational -> Rational
call2(complex_to_integer, Rational(3, 4))


# Why does all this make sense? Because of the Liskov Substitution Principle (LSP).
#
# Imagine a function that expects another function of type Rational -> Rational.
# It relies on two things:
#   1) It can safely pass a Rational as input.
#   2) It will always receive a Rational as output.
#
# If we substituted it with a function that accepts only Integer,
# then it might receive a Rational, which would break the program:
# the input domain has become *smaller*, which is not allowed.
#
# But if it accepts Complex instead, the input domain becomes *larger*,
# so the function is still safe to call with any Rational.
#
# Now consider the return type:
# If the expected result is a Rational, replacing the function with one
# that returns a Complex would be unsafe—the caller might not know
# how to handle a Complex.
#
# But if we return an Integer instead, this is safe because Integer
# is a subtype of Rational. Anywhere a Rational is expected, an Integer fits.

# in the implementation the function in the parameters will be used (or passed throw where it should be used):
# p : P = params
# result : R = func(p)
# So we define the params static type -> can be the same or *broader* the the actual
# and we dfine the result type which -> needs to be the same or *more specific*
