from math import isqrt, gcd

N, MOD = 10**2, 10**9 + 7

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

S = dict()
for i in FIinc(N):
    S[i] = i-1
for p in range(2, isqrt(N) + 1):
    if S[p] == S[p-1]: continue
    for v in FIdec(N):
        if v < p*p: break
        S[v] -= (S[v//p] - S[p-1])

cache = dict()
def sum_omega(n):
    if n in cache: return cache[n]
    rv = 0
    #small primes
    for i in range(2, isqrt(n) + 1):
        if S[i] == S[i-1]: continue
        x = i
        while x <= n:
            rv += n//x
            rv %= MOD
            x *= i

    #large primes
    for i in range(1, isqrt(n)):
        rv += (S[n//(i)] - S[n//(i+1)])*(i)
        rv %= MOD
    cache[n] = rv
    return rv

def bfomega(n):
    rv = 0
    for i in range(2, n+1):
        ti = i
        for j in range(2, isqrt(i) + 1):
            while ti % j == 0:
                rv += 1
                ti//=j
        if ti > 1: rv += 1
    return rv

def bfomegagcd(n):
    rv = 0
    for i in range(1, n+1):
        for k in range(1, n+1):
            ti = gcd(i, k)
            for j in range(2, isqrt(i) + 1):
                while ti % j == 0:
                    rv += 1
                    ti//=j
            if ti > 1: rv += 1
    return rv

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
                tot[idx] = tot[i]*j % MOD
                break
            else:
                tot[idx] = tot[i]*(j-1) % MOD
    return tot

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
            rv[i] = x % MOD
    return rv

tots = fast_tsum(N)
osieve = [0]*(isqrt(N) + 1)
for p in range(2, isqrt(N) + 1):
    if S[p] == S[p-1]: continue
    e = 1
    while p**e < isqrt(N) + 1:
        for j in range(p**e, isqrt(N) + 1, p**e):
            osieve[j] += 1
        e += 1

print(osieve)
gsum = 0
la = 1
for d in FIinc(N):
    if d == 1: continue
    print(d)
    if d <= isqrt(N):
        gsum += osieve[d] * (2 * tots[N//d] - 1)
    else:
        gsum += (sum_omega(d)-sum_omega(la)) * (2 * tots[N//d] - 1)
    gsum %= MOD
    la = d

print(bfomega(N), sum_omega(N))
print(bfomegagcd(N), gsum)
print((2*N*bfomega(N) - 2*bfomegagcd(N)))
print((2*N*sum_omega(N) - 2*gsum) % MOD)





