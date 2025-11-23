from typing import Protocol

class HasWheel(Protocol):
    wheel : int

class HasDoor(Protocol):
    door : int

class Vehicle(HasWheel, HasDoor, Protocol):
    # This is also a protocol (last parameter) but it has hierarchy for two other protocol
    # making the Protocol inheratince nominal -> but the instance referred as structural
    sound : str = "brrmm"

class Car(Vehicle):
    wheel : int = 4
    door : int = 4 # try to delete this and see what happend in pylance

class Motor():
    wheel : int  = 2
    door : int = 0

# You can define or not it doesn't matter

# v = Vehicle() # you can't do this because Protocol is not implementable
c = Car() 
m = Motor()

def w(wheel_owner: HasWheel):
    print(type(wheel_owner).__name__, '| wheel count: ', wheel_owner.wheel)

w(c)
w(m)

def v(vehicle: Vehicle):
    print(type(vehicle).__name__, '| wheel count: ', vehicle.wheel)

v(c)
v(m) # This makes error because sound are not presented in motor

# but you don't need nominal inheritance because Vehicle is a Protocol
# Just Car inherit from it so it gets it immediately
class LoudMotor():
    wheel : int  = 2
    door : int = 0
    sound : str = "brmbrmBRRMM" 

lm = LoudMotor()
v(lm)