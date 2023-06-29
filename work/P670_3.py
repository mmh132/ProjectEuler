target = 1

def f(n, d, s):
    if n >= target:
        return 1 if n == target and d == 0 else 0
    rv = 0
    if d == 0:
        rv += (3 if s else 2)*f(n+1, d, True)
    if d == 0 and not s:
        return rv
    for i in range(1, 4):
        rv += (6 if d == 0 else 2)*f(n+min(i, d), abs(d-i), False)
    return rv

print((4/3)*(f(0,0,True)))
