from math import lcm
from itertools import combinations


def bf(m,n):
    rv = set()
    for i in range(1, n+1):
        for k in range(i, m*i+1, i):
            rv.add(k)
    return len(rv)

#print(bf(345, 12))

def llcm(list):
    if len(list) == 1:
        return list[0]
    if len(list) == 2:
        return lcm(list[0],list[1])
    x = list.pop(0)
    return lcm(x, llcm(list))

def intersection(a_i, n):
    x = llcm(a_i.copy())
    return (n*min(a_i))//x

def bf2(a, b):
    rv = 0
    for s in range(1, a+1):
        for a_i in combinations(list(range(1, a+1)), s):
            rv += intersection(list(a_i), b)*pow(-1, s)
            print(a_i, intersection(list(a_i), b))
    return rv

#print(bf2(12, 345))

def build(n, z):
    subsets = {(1,1,1) : 1}
    for j in range(2, n+1):
        new = subsets.copy()
        new[(j, j, 1)] = 1
        for i in subsets:
            toadd = (i[0], lcm(i[1], j), i[2]*-1)
            if toadd in new:
                new[toadd] += subsets[i]
            else:
                new[toadd] = subsets[i]
        subsets = new.copy()
        print(len(subsets), j)
    rv = 0
    for i in subsets:
        rv += i[2]*subsets[i]*((z*i[0])//i[1])
    return rv

print(build(64, 10**16))
        
