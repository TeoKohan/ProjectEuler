from math import sqrt

def divisors(n):
    return [i for i in range(1, int(sqrt(n)) + 1) if n % i == 0]

n = 0
term = 1
while len(divisors(n)) * 2 < 500:
    n += term
    term += 1
print(n, len(divisors(n)))