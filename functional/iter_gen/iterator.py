class MyIter:
    start : int
    end : int
    def __init__(self, start : int, end : int):
        print(f"init my iterator with {start} -> {end}")
        self.start = start
        self.end = end

    def __iter__(self):
        print("__iter__")
        self._current = self.start - 1
        return self

    def __next__(self) -> int:
        print("__next__")
        if self._current < self.end:
            self._current += 1
            return self._current
        raise StopIteration


mi = MyIter(1,5)

for i in mi:
    print(i)

try:
    next(mi)
except StopIteration:
    print("The next will call the __next__ function")

print("If you run it again in a for loop it will call __iter__ -> returns an iterator object")
for i in mi: print(i)


print("\nYou can create an iterator from any iterable, with iter()")

it = iter(['a','b','c'])
for i in it: print(i,end=' ')
print()