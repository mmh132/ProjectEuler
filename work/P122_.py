def binexplen(n):
    if n == 1:
        return 0
    if n%2 == 1:
        return binexplen(n//2) + 2
    else:
        return binexplen(n//2) + 1

mem = {}
def f(have, want, l):
    if want in have:
        return len(have)-1
    if len(have) >= l:
        return l
    if max(have)*(2**(l - len(have))) < want:
        return l
    if (tuple(have), want) in mem: return mem[(tuple(have), want)]
    
    available = set()
    for i in have:
        for j in have:
            available.add(i+j)
    for i in have:
        if i in available:
            available.remove(i)
    m = l
    for i in available:
        have.add(i)
        x = f(have, want, l)
        if x < m:
            m = x
        have.remove(i)
    mem[(tuple(have), want)] = m
    return m

tp = 0
for i in range(1, 201):
    print(i, f(set([1]), i, binexplen(i)))
    tp += f(set([1]), i, binexplen(i))
print(tp)

print(binexplen(15))