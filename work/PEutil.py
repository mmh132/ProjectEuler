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
        
def lsievetot(n):
    primes, cmp, tot = [],[0]*(n+1),[0]*(n+1)
    tot[1] = 1
    for i in range(2, n+1):
        if not cmp[i]:
            primes.append(i)
            tot[i] = i-1
        for j in primes:
            idx = i*j
            if idx > n: break
            cmp[idx] = True
            if i%j == 0:
                tot[idx] = tot[i]*j
                break
            else:
                tot[idx] = tot[i]*(j-1)
    return tot

def lsievemu(n):
    primes, cmp, mu = [],[0]*(n+1),[0]*(n+1)
    mu[1] = 1
    for i in range(2, n+1):
        if not cmp[i]:
            primes.append(i)
            mu[i] = -1
        for j in primes:
            idx = i*j
            if idx > n: break
            cmp[idx] = True
            if i%j == 0:
                mu[idx] = 0
                break
            else:
                mu[idx] = mu[i]*-1
    return mu

def fast_tsum(n):
    y = max(int(0.55*n**(2/3)), isqrt(n) + 1)
    smalls = lsievetot(y)
    for i in range(2, y+1):
        smalls[i] += smalls[i-1]
    rv = dict()
    for i in FIinc(n):
        if i < y:
            rv[i] = smalls[i]
        else:
            x = i*(i+1)//2 - i
            for j in range(2, isqrt(i)+1):
                x -= rv[i//j]
                x -= (smalls[j] - smalls[j - 1])*(i//j)
            x += rv[isqrt(i)]*isqrt(i)
            rv[i] = x
    return rv

def fast_msum(n):
    y = max(int(0.55*n**(2/3)), isqrt(n) + 1)
    smalls = lsievemu(y)
    for i in range(2, y+1):
        smalls[i] += smalls[i-1]
    rv = dict()
    for i in FIinc(n):
        if i < y:
            rv[i] = smalls[i]
        else:
            x = 1 - i
            for j in range(2, isqrt(i)+1):
                x -= rv[i//j]
                x -= (smalls[j] - smalls[j - 1])*(i//j)
            x += rv[isqrt(i)]*isqrt(i)
            rv[i] = x
    return rv

def sieve(n):
    S = 10**4
    primes, oprimes = [], []
    rt = isqrt(n)
    
    isp = [1]*(rt + 1)
    for i in range(2, rt + 1):
        if isp[i]:
            primes.append(i)
            for k in range(i*i, rt, i):
                isp[k] = 0
    
    for k in range(n//S):
        block = [1] * S
        start = k*S
        for p in primes:
            i = (start + p - 1) // p
            for j in range(max(i, p)*p - start, S, p):
                block[j] = 0
        if k == 0:
            block[0] = 0
            block[1] = 0

        for i in range(S):
            if start + i > n: break
            if block[i]:
                oprimes.append(start + i)
    
    return primes + oprimes

