from math import isqrt

# sig = [e0, e1, ..., ek]
# count numbers n <= x where n = p0^e0 * p1^e1 * ... * pk^ek and p0 < p1 < ... < pk
# primeCounts is array of lucy prime counts up to n
# primes is list of primes up to √n
def countSignature(sig: list[int], x: int, primeCounts: dict, primes: list[int]):
    def rec(i,j,x,rem):
        if i == len(sig) - 1:
            w = iroot(x,sig[i])
            return max(0, primeCounts[w] - j)
        t = 0
        for k in range(j,len(primes)):
            if primes[k]**rem > x: break
            t += rec(i+1, k+1, x//primes[k]**sig[i], rem-sig[i])
        return t
    return rec(0, 0, x, sum(sig))

def iroot(n, i):
    l, h, m = 1, n, 0
    while h - l > 1:
        m = (l+h) // 2
        h, l = (m, l) if pow(m, i) > n else (h, m)
    if pow(l+1, i) <= n:
        l += 1
    return l

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

def naivemul(a, b, mod = 0):
    rv = [0]*(len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            rv[i+j] += a[i]*b[j]
            if mod:
                rv[i+j] %= mod
    return rv

#stolen from https://judge.yosupo.jp/submission/184924
def berlekampMassey(s,mod=0):
	C = [1]
	B = [1]
	L = 0
	m = 1
	b = 1
	
	for n in range(len(s)):
		d = s[n] + sum(C[i] * s[n-i] for i in range(1,L+1))
		if mod: d %= mod
		if d == 0:
			m += 1
			continue
		
		T = C[:]
		coef = d*pow(b,-1,mod) if mod else d//b
		nb = [0]*m + [coef*x % mod if mod else coef*x for x in B]
		C += [0] * (len(nb)-len(C))
		for i in range(len(nb)):
			C[i] -= nb[i]

		if 2*L <= n:
			L = n+1 - L
			B = T
			b = d
			m = 0
		
		m += 1
	
	ret = [-x for x in C[1:]]
	if mod: ret = [x%mod for x in ret]
	return ret

#coefficient c, starting values s, index k
def linearRec(c, s, k, mod = 0):
    def mul(a, b):
        rv = naivemul(a, b, mod)
        for i in range(len(rv) - 1, n-1, -1):
            for j in range(n-1, -1, -1):
                rv[i-j-1] += rv[i]*c[j]
                if mod: rv[i-j-1] %= mod
        return rv[:n]
    
    n = len(c)
    assert n <= len(s)

    a = [c[0]] if n == 1 else [0,1]
    x = [1]
    while k:
        if k&1: x = mul(x, a)
        a = mul(a, a)
        k//=2
    x = x[:n] + [0] * (n - len(x))

    rv = 0
    for i in range(n):
        rv += x[i]*s[i]
        if mod: rv %= mod
    return rv
