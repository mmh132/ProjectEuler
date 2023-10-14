from math import isqrt

def FIinc(n):
    i, la = 1,0
    while i <= n:
        la = n//(n//i)
        yield la
        i = la + 1
        
def FIdec(n):
    i, la = 1,0
    while i <= n:
        la = n//(n//i)
        yield n//la
        i = la + 1

def fastt(n):
    L = int(n**(2/3))
    F = list(range(L+1))
    for i in range(2, L + 1):
        if F[i] == i:
            F[i] -= 1
            for k in range(i+i, L + 1, i):
                F[k] //= i
                F[k] *= (i-1)
    for i in range(2,len(F)):
        F[i] += F[i-1]
    
    S = [0]*(2*isqrt(n))
    i = 0
    for v in FIinc(n):
        if v < L: S[i] = F[v]
        else:
            inn = v*(v+1) >> 1
            for x in range(1, isqrt(v) + 1):
                inn -= (F[x] - F[x-1])*(v//x)
                if x != 1:
                    inn -= F[v//x]
            inn += F[isqrt(v)]*isqrt(v)
            S[i] = inn
        i+=1
    while S[-1] == 0: S.pop(-1)
    return S[-1]

print(fastt(10**12))


