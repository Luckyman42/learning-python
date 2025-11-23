# Example: How do you add type annotations to a decorator that:
# - accepts any function
# - returns a new function with the *same parameters*
# - but modifies the return type OR modifies the parameter list?

from typing import TypeVar, ParamSpec, Callable, Concatenate

# Callable[[Param1, Param2, ...], ReturnType]
# Callable[ParamSpec, ReturnType]

P = ParamSpec("P")   # Special type used to represent a function’s parameter list
R = TypeVar("R")     # Generic return type


# --- Example 1: Decorator that preserves the function signature exactly ---
def add_log(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print("Called:", func.__name__)
        return func(*args, **kwargs)
    return wrapper


# --- Example 2: Decorator that *adds a new first parameter* ---
def add_logging(
    func: Callable[P, R]
) -> Callable[Concatenate[str, P], R]:
    def wrapper(prefix: str, *args: P.args, **kwargs: P.kwargs) -> R:
        print(prefix, ":", func.__name__)
        return func(*args, **kwargs)
    return wrapper

# Meaning:
# - The wrapper always introduces a new first argument of type `str`.
# - After that, it forwards all parameters from the original function (P).
# This is an example of a signature-manipulating generic decorator.
