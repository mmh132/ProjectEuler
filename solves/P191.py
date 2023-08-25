from functools import cache

@cache
def f(la, bl, t):
    if t == 0: return 1
    if t < 0: return 0
    rv = 0
    if not la:
        rv += f(True, bl, t-1)
        rv += f(True, bl, t-2)
    if not bl:
        rv += f(False, True, t-1)
    rv += f(False,bl,t-1)
    return rv
print(f(False, False, 30))