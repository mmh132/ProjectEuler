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


from math import isqrt
def FIinc(n):
    i, la = 1,0
    while i <= n:
        la = n//(n//i)
        yield la
        i = la + 1

MOD = 998244353
N = int(input())
Y = max(int(0.55*N*(2/3)), isqrt(N) + 1)
primes, cmp, tot = [],[0]*(Y+1),[0]*(Y+1)
def solve():
    tot[1] = 1
    for i in range(2, Y+1):
        if not cmp[i]:
            primes.append(i)
            tot[i] = i-1
        for j in primes:
            idx = i*j
            if idx > Y: break
            cmp[idx] = True
            if i%j == 0:
                tot[idx] = tot[i]*j
                break
            else:
                tot[idx] = tot[i]*(j-1)
    
    del primes, cmp
    
    for i in range(2, Y+1):
        tot[i] = (tot[i] + tot[i-1]) % MOD
    rv = dict()
    for i in FIinc(N):
        if i < Y:
            continue
        else:
            x = (i*(i+1)//2 - i) % MOD
            rt = isqrt(i)
            for j in range(2, rt+1):
                x -= rv[i//j] if i//j > Y else tot[i//j]
                x -= (tot[j] - tot[j - 1])*(i//j)
                x %= MOD
            x += (rv[rt] if rt > Y else tot[rt])*isqrt(i)
            rv[i] = x % MOD
    print(rv[N])

solve()
    
    
