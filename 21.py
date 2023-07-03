from math import sqrt, ceil
from collections import Counter
M = { }
P = [2]

def is_prime(n):
    for d in range(2, ceil(sqrt(n))):
        if n % d == 0:
            return False
    return True

def next_prime(n):
    if n == 1:
        return 2
    n += 1 + (n%2)
    while not is_prime(n):
        n += 2
    return n

def factor(n):
    global P

    if n == 1:
        AssertionError
    for p in P:
        if n % p == 0:
            return p
    while n % P[-1] != 0:
        P += [next_prime(P[-1])]
    return P[-1]

def factors(n):
    F = Counter()
    while n > 1:
        f = factor(n)
        F.update([f])
        n //= f
    return F

def divisors(n):
    F = list(factors(n).items())

    def products(head, tail):
        n, p = head
        powers = [n**k for k in range(p+1)]
        if tail != []:
            return [p * m for p in powers for m in products(tail[0], tail[1:])]
        else:
            return powers
    
    if F == []:
        return F
    else:
        return products(F[0], F[1:])

def proper_divisor_sum(n):
    return sum(divisors(n)) - n if n > 1 else 0

def amicable(a):
    global M
    if not a in M:
        M[a] = proper_divisor_sum(a)

    b = M[a]
    if not b in M:
        M[b] = proper_divisor_sum(b)
    
    return a == M[b] and b == M[a] and a != b 

amicables = [n for n in range(10000) if amicable(n) and M[n]]
print(sum(amicables))