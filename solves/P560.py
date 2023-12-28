from functools import cache
def gcd(a, b):
    if a > b: a,b=b,a
    while b:
        a,b = b,a%b
    return a

def mex(s):
    i = 0
    while i in s:
        i += 1
    return i

def it(n):
    for i in range(1, n+1):
        if gcd(n, i) == 1: 
            yield i

@cache
def g(u):
    if u == 1: return 1
    if u == 0: return 0
    l = [g(u-i) for i in it(u) if i <=u]
    return mex(set(l))


N, K, mod = 10**7, 10**7, 10**9+7
N = N-1
#a or convolve b in nlogn, FWHT algorithm
def transform(a, n):
    for k in range(n):
        i = 1 << k
        for j,x in enumerate(a):
            if (i & j) == 0:
                a[j], a[i | j] = x + a[i | j], x - a[i | j]
                a[j] %= mod
                a[i | j] %= mod
    
def xorconvolve(a, b):
    n = 0
    while (1 << n) < max(len(a), len(b)):
        n += 1
    while len(a) < (1 << n):
        a.append(0)
    while len(b) < (1 << n):
        b.append(0)
    
    transform(a, n)
    transform(b, n)
    for i, x in enumerate(b):
        a[i] *= x
        a[i] %= mod
    transform(a, n)
    iv = pow(1 << n, -1, mod)
    return [(x * iv) % mod for x in a]
    
#find lpf index's
lpf = [0]*(N + 1)
idx = 0
for i in range(2, N+1):
    if lpf[i] == 0:
        idx += 1
        for j in range(i, N+1, i):
            if lpf[j] == 0:
                lpf[j] = idx

#build thing
ivals = [0]*(max(lpf) + 1)
for i in lpf:
    if i != 1:
        ivals[i] += 1
    else:
        ivals[0] += 1
ivals[1] = 1
ivals[0] -= 2

out = [1]
#binary exponentiation
while K:
    if K % 2 == 1:
        nout = xorconvolve(out.copy(), ivals.copy())
        out = nout.copy()
    nivals = xorconvolve(ivals.copy(), ivals.copy())
    ivals = nivals.copy()
    K >>= 1

print(out[0])


