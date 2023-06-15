from math import sqrt

P = [2]

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

while len(P) < 10001:
    P += [next_prime(P[-1])]
print(P[-1])