from math import isqrt
def f(n):
    p = [1]*(n+1)
    for i in range(2, isqrt(n)+1):
        if not p[i]: continue
        for k in range(i*i, n+1, i):
            p[k] = 0
    rv = 0
    checker = [1]*(n+1)
    for d in range(1, n+1):
        for nd in range(1, n//d):
            if not p[d + nd]: 
                checker[nd*d] = 0
    for i in range(len(checker)):
        if checker[i]:
            rv += i
    return rv
print(f(10**8))

