from lib.sieve import Sieve, proper_divisors

def is_abundant(n):
    divisor_sum = sum(proper_divisors(n))
    return divisor_sum > n

abundant = []
for i in range(28124):
    if is_abundant(i):
        abundant += [i]

abundant_sum = {i: False for i in range(28124)}
for a, b in [(a, b) for i, a in enumerate(abundant) for b in abundant[i:] if a+b <= 28123]:
    abundant_sum[a+b] = True

print(sum([n for n, v in abundant_sum.items() if not v]))