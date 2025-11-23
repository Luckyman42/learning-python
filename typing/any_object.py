from typing import Any

def n(nothing):
    reveal_type(nothing)

def a(any : Any):
    reveal_type(any) 

def o(obj : object):
    reveal_type(obj)

# Object -> everythings base like Java
# Any -> Totally turn off the type checker