def mex(u):
    i = 0
    while i in u: i += 1
    return i

def it(s):
    for i in range(len(s)):
        for j in [1, 2, 4, 9]:
            if s[0] >= j:
                s[0] -= j
                yield s.copy()
                s[0] += j
        z = s.pop(0)
        for i in range(1, z//2 + 1):
            s.append(z-i)
            s.append(i)
            yield s.copy()
            s.pop(-1)
            s.pop(-1)
        s.append(z)

mem = dict()
def g(s):
    td = []
    for i in range(len(s)-1, -1, -1):
        if i == 0: td.append(i)
    for i in td: s.pop(0)
    if len(s) == 0: return 0
    if tuple(sorted(s)) in mem: return mem[tuple(sorted(s))]
    rv = mex([g(i) for i in it(s)])
    mem[tuple(sorted(s))] = rv
    return rv

print([i for i in it([3,3])])

rv = 0

for i in range(1, 13):
    for j in range(i, 13):
        for k in range(j, 13):
            for h in range(k, 13):
                if g([i,j,k,h]) == 0:
                    rv += 1

print(rv)


