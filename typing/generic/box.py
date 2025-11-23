from typing import Generic, TypeVar

T = TypeVar("T")

class Box(Generic[T]):
    content: T
    def __init__(self, content: T):
        self.content = content
    def get_content(self) -> T:
        return self.content

reveal_type(Box(42))
reveal_type(Box("Hello"))
int_box : Box[str] = Box(42) # This makes error for pyright
str_box = Box[str]("Hello")


class ModernBox[P]:
    content: P
    def __init__(self, content: P):
        self.content = content
    def get_content(self) -> P:
        return self.content

reveal_type(ModernBox(42))
reveal_type(ModernBox("Hello"))


# You can define it in functions 
def template(value : T ) -> T:
    reveal_type(value)
    return value

result = template(42)
reveal_type(result)