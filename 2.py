f = 1
F = 2

sum = 0

while F < 4000000:
    if F % 2 == 0:
        sum += F
    f, F = F, f + F
print(sum)