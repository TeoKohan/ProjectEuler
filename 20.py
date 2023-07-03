from math import factorial

def digits_sum(n):
    return sum([int(s) for s in str(n)])

print(digits_sum(factorial(100)))