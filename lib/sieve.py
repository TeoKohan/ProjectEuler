from math import sqrt, ceil

class Sieve:
    def __set_prime(self, prime):
        for i in range(prime * 2, self.capacity, prime):
            self.sieve[i] = False

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.sieve = [True] * (self.capacity)
        self.sieve[0] = False

        for i in range(capacity):
            if self.sieve[i]:
                self.__set_prime(i)
    
    def primes(self):
        return [i for i, v in enumerate(self.sieve, start=1) if v]

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
        for p in self.primes:
            if n % p == 0:
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