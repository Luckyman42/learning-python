hw = "Hello World"
print(id(hw))
a = hw
print(id(a))

def f() -> int:
    return 42

x = f()
y = f()
print(f"x:{x} y:{y}")
print(f"id(x):{id(x)}\nid(y):{id(y)}")


class Box:
    value: int
    def __init__(self, value: int):
        self.value = value
    def __repr__(self) -> str:
        return str(self.value)

def g():
    return Box(42)

x = g()
y = g()
print(f"x:{x} y:{y}")
print(f"id(x):{id(x)}\nid(y):{id(y)}")
