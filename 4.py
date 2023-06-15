S = set()

def palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

for n in range(1000):
    for m in range(1000):
        N = n * m
        if palindrome(str(N)):
            S.add(N)
print(max(S))