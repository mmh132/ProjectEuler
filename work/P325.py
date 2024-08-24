from functools import cache

f = [1, 1]
for i in range(100):
    f.append(f[-1] + f[-2])

def zr(n):
    rv = []
    i = len(f) - 1
    while n > 0:
        while f[i] > n:
            i -= 1
        n = n-f[i]
        rv.append(i+1)
        i -= 1

    return rv


@cache
def dp(a, b):
    if a > b: return dp(b, a)
    if a == 0: return 0
    if any((not dp(a, b-i*a)) for i in range(1, b//a + 1)):
        return 1
    return 0

L = 20
for i in range(1, L + 1):
    for j in range(i, L + 1):
        print(i, j, zr(i), zr(j), "win" if dp(i, j) else "lose")