from functools import cache

@cache
def d(n, k):
    if k == 0:
        return 1
    rv = 0
    for i in range(1, n+1):
        if n % i == 0:
            rv += d(i, k-1)
    return rv

tp = 0
for i in range(1, 11):
    for j in range(1, 11):
        tp += d(i, j)
print(tp)