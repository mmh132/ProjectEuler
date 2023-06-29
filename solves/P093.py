def arithrec(ns, setsols):
    a = ns.pop(0)
    b = ns.pop(0)
    if a == 0 or b == 0: return set()
    if len(ns) == 0: return set([a*b,a/b,a+b,a-b,b/a,b-a])
    setsols |= arithrec([a+b] + ns, setsols)
    setsols |= arithrec([a*b] + ns, setsols)
    setsols |= arithrec([a/b] + ns, setsols)
    setsols |= arithrec([a-b] + ns, setsols)
    setsols |= arithrec([b/a] + ns, setsols)
    setsols |= arithrec([b-a] + ns, setsols)
    return setsols.intersection(set(range(1,int(max(setsols))+2)))

def perms(l):
    out = []
    def rec(l, o):
        if l == []: out.append(o); return
        for a in l:
            temp = l.copy()
            temp.remove(a)
            rec(temp, o+[a])
    rec(l,[])
    return out
print(arithrec([1,2,3,4],set()))

def miss(set):
    thing = list(set)
    a = 1
    while a in thing: a += 1
    return a-1

temp = set()
best = 1
cur = 1
for a in range(1,10):
    for b in range(a+1,10):
        for c in range(b+1,10):
            for d in range(c+1,10):
                for e in perms([a,b,c,d]):
                    temp |= arithrec(e,set())
                cur = miss(temp)
                if cur>best: best = cur; print(a,b,c,d)
                temp = set()
print(best)
for e in perms([1,2,3,4]):
    temp |= arithrec(e,set())
cur = miss(temp)
print(cur)