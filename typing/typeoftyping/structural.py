# Stucture based typing
from typing import Protocol

class Vehicle(Protocol):
    wheel : int

class Car(Vehicle):
    wheel : int = 4

class Motor():
    wheel : int  = 2

# You can define or not it doesn't matter

def f(vehicle: Vehicle):
    print(type(vehicle).__name__, '| wheel count: ', vehicle.wheel)

# v = Vehicle() # you can't do this because Protocol is not implementable
c = Car()
m = Motor()

f(c)
f(m)

# inheritance be structure, base class like blueprints.

class ShoppingCart():
    wheel : int = 4

sc = ShoppingCart()
f(sc) # Totaly fine
