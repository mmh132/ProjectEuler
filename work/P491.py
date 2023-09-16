from functools import cache

@cache
def f(du, s):
    if sum(du) == 0:
        s = abs(s)
        if s % 11 == 0:
            return 1
        return 0
    evenodd = sum(du)&1
    rv = 0
    du = list(du)
    for i in range(0 if sum(du) < 20 else 1, len(du)):
        if du[i] == 0: continue
        du[i] -= 1
        if evenodd:
            rv += f(tuple(du), s+i)
        else:
            rv += f(tuple(du), s-i)
        du[i] += 1
    return rv

print(f(tuple([2]*10), 0))
