from math import lcm
def f(n):
    sets = {1: 1}
    for i in [1,2,4]:
        ns = sets.copy()
        for key in sets:
            nv = lcm(key, i)
            if nv not in ns: 
                ns[nv] = 0
            ns[nv] += sets[key]
        sets = ns.copy()
        print(i, sets)
    rv = 0
    for key in sets:
        rv += sets[key]*key 
        rv %= (10**9 + 7)
    return rv

print(f(6))