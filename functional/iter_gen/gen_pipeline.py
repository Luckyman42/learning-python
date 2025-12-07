a_g = (x for x in range(10))
b_g = (a ** 2 for a in a_g)
c_g = (b for b in b_g if b % 2 == 0)

result = list(c_g)
print(result)