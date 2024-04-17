from functools import cache

def update(t, i):
    t = list(t)
    t[i] -= 1
    if i < 3: 
        t[i + 1] += 1
    return tuple(t)

@cache
def dp(c, l):
    if sum(c) == 0:
        return 52
    t = 4*c[0] + 3*c[1] + 2*c[2] + c[3]
    rv = 0
    if l < 4 and c[l] > 0:
        c = list(c)
        c[l] -= 1
        rv += (4-l)/t * (52 - t - 1)
        c = tuple(c)
    for i in range(4):
        if c[i] > 0:
            rv += ((4-i)*c[i]/t) * dp(update(c, i), i+1)
    return rv

print(round(dp((13,0,0,0,0), -1),12))

