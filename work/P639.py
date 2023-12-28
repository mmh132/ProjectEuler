from math import isqrt

def seg_sieve(n):
    n = int(n)
    S = 10**5

    primes = []
    nsqrt = isqrt(n)
    is_prime = [1] * (nsqrt+2)
    for i in range(2,nsqrt+1):
        if is_prime[i]:
            primes += [i]
            for j in range(i*i,nsqrt+1,i):
                is_prime[j] = 0

    result = []
    block = [0] * S
    for k in range(n//S+1):
        block[:] = [1]*S
        start = k * S
        for p in primes:
            start_idx = (start + p - 1) // p
            j = max(start_idx, p) * p - start
            while j < S:
                block[j] = 0
                j += p
        
        if k == 0:
            block[0] = block[1] = 0
        for i in range(S):
            if start + i > n:
                break
            if block[i]:
                result += [start+i]

    return result

def powerfulnumbersext(n, h, mod):
    primes = seg_sieve(isqrt(n)+1)
    stk = [(1,1,0)]
    while stk:
        (nn, hn, i) = stk.pop(0)
        if i >= len(primes):
            yield (nn, hn)
            continue
        p = primes[i]
        if p*p > n//nn:
            yield(nn, hn)
            continue
        stk.append((nn, hn, i+1))
        e = 2
        while p**e <= n//nn:
            stk.append((nn*p**e, (hn*h(p, e)) % mod, i+1))
            e += 1



from functools import cache
mod = 10**9 + 7
k, n = 50, 10**12

def sum_nk(n, k):
    pts = [(1,1)]
    while len(pts) <= k+1:
        x = pts[-1]
        pts.append((x[0]+1, (x[1]+pow(x[0]+1, k, mod))%mod))
    rv = 0
    t = 1
    for i in pts:
        t*=(n-i[0])
        t %= mod
    for i in pts:
        b = 1
        for j in pts:
            if i==j: continue
            b*=(i[0]-j[0])
            b%=mod
        rv += pow(b, -1, mod)*pow(n-i[0], -1, mod)*t*i[1]
        rv %= mod
    return rv

tp = 0
for xp in range(1, k+1):
    ccc = dict()
    def h(p,e): 
        if e == 0: return 1
        if e == 1: return 0
        if (p, e) in ccc: return ccc[(p, e)]
        rv = p**xp 
        for i in range(e):
            rv -= h(p, i)*pow(p, (e-i)*xp)
        ccc[(p, e)] = (rv + mod) % mod
        return (rv + mod) % mod
    
    sp = [0]*(isqrt(n) + 1)
    sp[1] = 1
    for i in range(2, isqrt(n) + 1):
        sp[i] = (sp[i-1] + pow(i, xp, mod)) % mod
    
    print("here")

    for i in powerfulnumbersext(n, h, mod):
        x, hh = i[0], i[1]
        if n//x < isqrt(n):
            tp += hh*sp[n//x]
        else:
            tp += hh*sum_nk(n//x, xp)
        tp %= mod

print(tp)


