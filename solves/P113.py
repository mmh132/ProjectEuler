from functools import cache

@cache 
def inc(n, ld):
    if n == 1: return 1
    rv = 0
    for i in range(ld, 10):
        rv += inc(n-1, i)
    return rv

@cache
def dec(n, ld):
    if n == 1: return 1
    rv = 0
    for i in range(ld + 1):
        rv += dec(n-1, i)
    return rv

N = 100
out = 0
for i in range(1, N + 1):
    for s in range(1, 10):
        out += inc(i, s)
        out += dec(i, s)
    out -= 9
print(out)
