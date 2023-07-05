from math import sqrt
from lib.sieve import Sieve

P = Sieve(2000000)
print(sum(P.primes()))