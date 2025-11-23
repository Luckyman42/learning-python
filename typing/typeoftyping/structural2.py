# Stucture based typing
from typing import Protocol, runtime_checkable

@runtime_checkable
class Vehicle(Protocol):
    wheel : int
    door : int

class Car(Vehicle):
    wheel : int = 4
    door : int = 4

class Motor():
    wheel : int  = 2
    door : int = 0

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
f(sc) # But duck typing allows you to run it ( because the function only use the wheel parameter )
# Because of the protocol it is except that you have door property also (even if you don't use it that context) 
print("ShoppingCart is a Vehicle: ", isinstance(sc, Vehicle))
