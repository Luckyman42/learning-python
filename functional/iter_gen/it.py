import itertools as it
import time

# count : infinit counter
print("Infinit counter")
counter = it.count()
print("it.count():", end=" ")
print(next(counter), end=" ")
print(next(counter), end=" ")
print(next(counter), end=" ")
print("...")

ct = it.count(5,2)
print("it.count(5,2):", end=" ")
print(next(ct), end=" ")
print(next(ct), end=" ")
print(next(ct), end=" ")
print("...")


# cycle: infinit loop for the given iterator 
print("Infinit cycle")
cycle = it.cycle("\\|/-")
for i in range(10):
    time.sleep(0.2)
    print(f"it.cycle: {next(cycle)}", end="\r")
print()

# repeat object n times
print("Repeat object n times")
print("it.repeat:", end=" ")
for x in it.repeat("Hello", 3):
    print(x, end=" ")
print()

# Accumulate, sum elements or other operations
nums = [1, 2, 3, 4]
print(f"it.accumulate({nums}) -> {list(it.accumulate(nums))}")
import operator
print(f"mul -> {list(it.accumulate(nums, operator.mul))}")

# concat more iterations
nums = [1,2,3]
chars = ["a","b"]
print("nums: ", nums)
print("chars: ", chars)
chain = list(it.chain(nums, chars))
print(f"it.chain: {chain}")

# Combination
print("it.combinations(nums, 1): ", list(it.combinations(nums, 1)))
print("it.combinations(nums, 2): ", list(it.combinations(nums, 2)))
print("it.combinations(nums, 3): ", list(it.combinations(nums, 3)))
# Combination with replacemant
print("it.combinations_with_replacement([1,2], 2): ", list(it.combinations_with_replacement([1,2], 2)))
# Permutation
print("it.permutations(nums, 2): ", list(it.permutations(nums, 2)))
# Descartes product
print("it.product(nums, chars): ", list(it.product(nums, chars)))

# Making slice of the iteration
numbers = range(10)
first_three = list(it.islice(numbers, 3))
second_three = list(it.islice(numbers, 3,6))
evens = list(it.islice(numbers, 0,10,2))
print("it.islice(numbers, 3)", first_three)
print("it.islice(numbers, 3, 6)", second_three)
print("it.islice(numbers, 0, 10, 2)", evens)

# Grouping by consecutive repetitions.
data = [(1, "a"), (1, "b"), (2, "x"), (2, "y")]
print("Data: ", data)
for key, group in it.groupby(data, key=lambda x: x[0]):
    print(f"key={key}, group:{list(group)}")
