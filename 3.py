from math import sqrt

N = 600851475143
P = [2]
S = set()

def is_prime(p):
    for n in range(2, int(sqrt(p))+1):
        if p % n == 0:
            return False
    return True

def next_prime(p):
    p += 1 + (p%2)
    while not is_prime(p):
        p += 2
    return p

def lowest_factor(n):
    global P
    if n == 1:
        AssertionError
    for p in P:
        if n % p == 0:
            return p
    q = next_prime(P[-1])
    while n % q != 0:
        P += [q]
        q = next_prime(q)
    return q
    
while N != 1:
    factor = lowest_factor(N)
    S.add(factor)
    N //= factor
print(max(S))