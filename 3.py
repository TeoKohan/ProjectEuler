from lib.sieve import Factor

N = 600851475143
factors = Factor(600851475143).factors()
print(max(factors))