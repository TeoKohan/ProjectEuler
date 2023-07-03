def digits_sum(n):
    return sum([int(s) for s in str(n)])

print(digits_sum(2**1000))