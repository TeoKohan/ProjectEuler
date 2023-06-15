b = 0
a = 0
while a*a + b*b != (1000-(a+b))**2:
    b += 1
    a = 1
    while a < b and b < (1000-(a+b)) and a*a + b*b != (1000-(a+b))**2:
        a += 1

print(a, b, 1000-(a+b))