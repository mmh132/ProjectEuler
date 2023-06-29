from copy import deepcopy as dc
import time
from math import gcd
start_time = time.time()
def prod(l):
    rv = 1
    for i in l: rv *= i
    return rv
def factorsieve(n):
    blank = []
    rv = [blank.copy() for x in range(n+1)]
    for i in range(2,len(rv)):
        if rv[i] == []:
            rv[i].append(i)
            for k in range(i+i,len(rv),i):
                rv[k].append(i)
    return rv
def fastg(a,b,c):
    for el in a:
        if el in b or el in c: return False
    for el in b:
        if el in a or el in c: return False
    for el in c:
        if el in a or el in b: return False
    return True
def ABChits(lessthan):
    factors = factorsieve(lessthan)
    niceindices = [1]
    a,b,c = 0,0,0
    hits = []
    for i in range(len(factors)):
        if prod(factors[i]) < i or len(factors[i]) == 1: niceindices.append(i)
    for a1 in range(len(niceindices)):
        for b1 in range(a+1,len(niceindices)):
            a = niceindices[a1]
            b = niceindices[b1]
            c = a+b
            if c<=lessthan:
                if fastg(factors[a] , factors[b] , factors[c]):
                    if prod(factors[a] + factors[b] + factors[c]) < c:
                        #print(a,b,c)
                        hits.append(c)
    print(sum(hits))


print(ABChits(1000))
print("--- %s seconds ---" % (time.time() - start_time))