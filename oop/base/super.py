class A:
    __name__ = "A"
    def __init__(self):
        print("A")

class B(A):
    __name__ = "B"
    def __init__(self):
        print("B super: ", super().__name__)
        super().__init__()

class C(A):
    __name__ = "C"
    def __init__(self):
        print("C super: ", super().__name__)
        super().__init__()

class D(B,C):
    __name__ = "D"
    def __init__(self):
        print("D super: ", super().__name__)
        super().__init__()



print("D.mro(): ", D.mro())
D()