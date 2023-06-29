def factorsieve(n):
    blank = []
    rv = [blank.copy() for x in range(n+1)]
    for i in range(2,len(rv)):
        if rv[i] == []:
            exp = 1
            while i ** exp < n:
                for k in range(i**exp,len(rv),i**exp):
                    rv[k].append(i)
                exp += 1
    return rv
nfacs = factorsieve(50)
def nck(n,k):
    if n//2 > k:return nck(n,n-k)
    rv = []
    for i in range(n, k, -1):
        rv += nfacs[i].copy()
    diff = []
    for i in range(1, n-k+1):
        diff += nfacs[i].copy()
    for i in diff:
        rv.remove(i)
    return rv
def isfree(l):
    l = sorted(l)
    for i in range(len(l)-1):
        if l[i] == l[i+1]: return False
    return True
def prod(l):
    if l == list(): return 1
    rv = 1
    for i in l: rv *= i
    return rv
print(nck(0,0))
checker = list()
summ = set()
for n in range(0,51):
    for k in range(0,n+1):
        checker = nck(n,k)
        if isfree(checker):
            summ.add(prod(checker))
print(sum(summ))