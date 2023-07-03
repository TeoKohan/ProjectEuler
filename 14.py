L = { 1: 0 }

def collatz(n: int) -> int:
    return n//2 if n%2 == 0 else (3*n+1)

def collatz_length(n: int) -> int:
    return L[n] if n in L else (1 + collatz_length(collatz(n)))

for n in range(1, 1000000):
    if not n in L:
        L[n] = collatz_length(n)

print(max(L, key=L.get))