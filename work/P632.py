from math import isqrt
def f(n):
    #sieve to sqrt
    rt = isqrt(n)
    s = [0]*(rt+1)
    for p in range(2, rt+1):
        if s[p] != 0: continue
        for i in range(p, rt+1, p):
            if s[i] != -1:
                s[i] += 1
        for j in range(p*p, rt+1, p*p):
            s[j] = -1
    print(s)

f(20**2)