from functools import cache

@cache
def rec(a2, a3, a4, a5):
    s = a2 + a3 + a4 + a5
    rv = 1 if s == 1 else 0
    if a2 > 0: 
        rv += a2 * rec(a2-1, a3 + 1, a4+1, a5+1) / s
    if a3 > 0: 
        rv += a3 * rec(a2, a3 - 1, a4 + 1, a5 + 1) / s
    if a4 > 0:
        rv += a4 * rec(a2, a3, a4 - 1, a5 + 1) / s
    if a5 > 0: 
        rv += a5 * rec(a2, a3, a4, a5-1) / s
    return rv

print(rec(2, 0, 0, 0) - 1)
