def sum_func(n : int) -> int:
    sum = 0
    for i in range(n):
       sum += i 
    return sum

def ab_func(a : int, b : int):
    a_s = sum_func(a)
    b_s = sum_func(b)
    return a_s + b_s

def fun():
    ab = ab_func(10,42424242)
    print(ab)