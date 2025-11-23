from typing import TypeGuard, TypeIs

class Zero():
    value : int
class Positive():
    value : int
class Negative():
    value : int

# Lets see the isinstace function deeper, try to write a function like that

def f(num : Positive|Negative|Zero):
    if isinstance(num, Positive):
        reveal_type(num) # Positive


# Try to write our owm function
def is_zero(num : Positive|Negative|Zero) -> bool:
    return num.value == 0

def f2(num : Positive|Negative|Zero):
    if is_zero(num):
        reveal_type(num) # Positive|Negative|Zero

# It will not knows the type if num
# We didn't say anything just write a bool return function

# We can specify Guards which is like an alias for bool but with the metainformation of the type
# Its working the following way
# TypeGuard[T]: If the result is True -> the type is T
def positive_guard(num : Positive|Negative|Zero) -> TypeGuard[Positive]:
    return num.value > 0
def negative_guard(num : Positive|Negative|Zero) -> TypeGuard[Negative]:
    return num.value < 0

def g(num : Positive|Negative|Zero):
    if positive_guard(num):
        reveal_type(num) # Positive
    elif negative_guard(num):
        reveal_type(num) # Negative
    else:
        reveal_type(num) # Positive | Negative | Zero

# this just Guard tells me information only when its true
# Lets try again with TypeIs[T]:
# If the result is True -> the type is T
# If the result is False -> the type is not T
def is_positive(num : Positive|Negative|Zero) -> TypeIs[Positive]:
    return num.value > 0    
def is_negative(num : Positive|Negative|Zero) -> TypeIs[Negative]:
    return num.value < 0

def g2(num : Positive|Negative|Zero):
    if is_positive(num):
        reveal_type(num) # Positive
    elif is_negative(num):
        reveal_type(num) # Negative
    else:
        reveal_type(num) # Zero


# The isinstance use TypeIs for result type
def reference(num : Positive|Negative|Zero):
    if isinstance(num, Zero):
        reveal_type(num) # Zero
    else:
        reveal_type(num) # Positive | Negative
