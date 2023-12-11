from math import isqrt, sqrt
def powerful(n):
    sfs = [1]*int(n**(1/3))
    for i in range(2, isqrt(len(sfs)) + 1):
        for k in range(i*i, len(sfs)+1, i*i):
            sfs[k] = 0
    return 1 + sum(sfs[i]*int(sqrt(n/(i*i*i))) for i in range(1,len(sfs)))

print(powerful(10**10))


