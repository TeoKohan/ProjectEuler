from math import sqrt
from lib.sieve import Primes

P = Primes()

while len(P) < 10001:
    P.next_prime()
print(P[-1])