from math import sqrt, ceil

class Sieve:
    def __set_prime(self, prime):
        for i in range(prime * 2, self.capacity, prime):
            self.sieve[i] = False

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.sieve = [True] * (self.capacity)
        self.sieve[0] = False
        self.sieve[1] = False

        for i in range(capacity):
            if self.sieve[i]:
                self.__set_prime(i)
    
    def is_prime(self, n):
        assert n < self.capacity
        return self.sieve[n]
    
    def primes(self):
        return [i for i, v in enumerate(self.sieve) if v]

class Primes:
    def next_prime(self):
        p = 2 if self.primes[-1] < 2 else self.primes[-1] + 1 + self.primes[-1] % 2
        while not self.is_prime(p):
            p += 2
        self.primes += [p]
        return p

    def __init__(self, precomputed=Sieve(2**15).primes()) -> None:
        self.primes = [2] if precomputed == [] else precomputed
    
    def __len__(self) -> int:
        return len(self.primes)

    def __iter__(self):
        for prime in self.primes:
            yield prime

    def __getitem__(self, item):
         return list(self)[item]

    def is_prime(self, n):
        for div in range(2, int(sqrt(n))+1):
            if n % div == 0:
                return False
        return True
    
def factors(n):
    F = []

    while n % 2 == 0:
            F += [2]
            n //= 2
    d = 3
    while n > 1:
        while n % d == 0:
            F += [d]
            n //= d
        d += 2 - (d % 2 == 0)
    return F

def divisors(n) -> list:
    def products(factors):
        head, *tail = factors
        if tail == []:
            return [1, head]
        else:
            return [a * b for a in [1, head] for b in products(tail)]
    
    F = factors(n)
    if F == []:
        return set(F)
    else:
        return set(products(F))

def proper_divisors(n) -> list:
    if n < 2:
        return []
    else:
        ds = divisors(n)
        ds.remove(n)
        return ds