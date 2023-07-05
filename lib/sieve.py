from math import sqrt, ceil

class Sieve:
    def __register_prime(self, prime):
        for i in range(prime * 2, self.capacity, prime):
            self.sieve[i] = False

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.sieve = [True] * (self.capacity+1)
        self.sieve[0] = False
        if capacity > 0:
            self.sieve[1] = False

        for i in range(capacity):
            if self.sieve[i]:
                self.__register_prime(i)
    
    def primes(self):
        return [i for i, v in enumerate(self.sieve) if v]

class Primes:
    def next_prime(self):
        p = 2 if self.index < 2 else self.index + 1 + self.index % 2
        while not self.is_prime(p):
            p += 2
        self.primes += [p]
        self.index = p
        return p

    def __init__(self, precomputed=Sieve(2**15).primes()) -> None:
        self.primes = [2] if precomputed == [] else precomputed
        self.index  = max(self.primes)
    
    def __len__(self) -> int:
        return len(self.primes)

    def __iter__(self):
        for prime in self.primes:
            yield prime

    def is_prime(self, n):
        if next((True for p in self.primes if n % p == 0), False):
            return False
        while self.primes[-1] < sqrt(n):
            if n % self.next_prime() == 0:
                return False
        return True

class Factor:
    def __init__(self, n, precomputed=Sieve(2**15).primes()) -> None:
        self.n = n
        self.primes = Primes(precomputed)

    def __lowest_factor(self, n):
        assert n > 1
        for p in list(self.primes):
            if n % p == 0:
                return p
        while n % self.primes.next_prime() != 0:
            pass
        return max(self.primes)
    
    def factors(self):
        F = []
        while self.n > 1:
            f = self.__lowest_factor(self.n)
            F += [f]
            self.n //= f
        return F

    def divisors(self, n):
        def products(factors):
            head, *tail = factors
            if tail == []:
                return [head]
            else:
                return [a * b for a in [1, head] for b in products(tail)]
        F = self.factors(n)
        if F == []:
            return F
        else:
            return products(F)