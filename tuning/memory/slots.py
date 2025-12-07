from pympler import asizeof

class Basic:
    identitiy: int
    name : str
    name1 : str
    name2 : str
    name3 : str
    def __init__(self, identitity : int, name: str):
        self.identitiy = identitity
        self.name = name
        self.name1 = name
        self.name2 = name
        self.name3 = name

class Fix:
    __slots__ = ("identitiy","name")
    identitiy: int
    name : str
    def __init__(self, identitity : int, name: str):
        self.identitiy = identitity
        self.name = name


b = Basic(42,"Hello")
s = Fix(42,"World")


print("memory used for basic class: ", asizeof.asizeof(b)) # type: ignore
print("memory used for slots class: ", asizeof.asizeof(s)) # type: ignore