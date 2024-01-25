from functools import cache

@cache
def dp(d, p, l):
    if l == 0:
        return 1 if d == (1<<10) - 1 else 0
    rv = 0
    if p < 9:
        rv += dp(d | (1 << (p+1)), p+1, l-1)
    if p > 0:
        rv += dp(d | (1 << (p-1)), p-1, l-1)
    return rv

tp = 0
for l in range(40):
    for i in range(1, 10):
        tp += dp(1 << i, i, l)
print(tp)