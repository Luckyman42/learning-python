# Generator is a type of iterator which has a shortdef, like inline list, there is inline gen
import sys

l = [i for i in range(5)]
g = ( i for i in range(5))

print("list: ", l)
print("gen: ", g)

def print_size(n : int):
    l = [ i for i in range(n) ]
    g = ( i for i in range(n) )
    print(f"for {n:<7}: generator: {sys.getsizeof(g)}, list: {sys.getsizeof(l)}")

print("check various list and generators sizes")
print_size(10)
print_size(100)
print_size(1000)
print_size(10000)
print_size(100000)

print("works the same as iterator")

for i in g: print(i, end=' ')
print()
