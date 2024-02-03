from functools import cache
N, MOD = 10**1, 11**8

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

cmp, mu, primes = [0]*(N+1), [0]*(N+1), []
mu[1] = 1  
for i in range(2, N+1):
    if not cmp[i]:
        primes.append(i)
        mu[i] = -1
    for j in primes:
        idx = i*j
        if idx > N: break
        cmp[idx] = 1
        if i%j == 0:
            mu[idx] = 0
        else:
            mu[idx] = mu[i]*-1



MOD = 10**9+7

@cache
def M(n):
    rv = pow(n+1, 3, MOD) - 1
    la = 1
    for i in FIinc(n):
        if i == la: continue
        rv = (rv - (i-la)*M(n//i)) % MOD
        la = i
    return rv % MOD

# print(M(1), M(2))
# print(M(100))

#elements of M such a > b and a > c
@cache
def M2(n):
    rv = (n)*(2*n + 1)*(n+1) // 6
    la = 1
    for i in FIinc(n):
        if i == la: continue
        rv = (rv - (i-la)*M3(n//i)) % MOD
        la = i
    return rv

#elements of M such a = b and a > c
@cache
def M3(n):
    rv = n*(n+1)//2 
    la = 1
    for i in FIinc(n):
        if i == la: continue
        rv = (rv - (i-la)*M3(n//i)) % MOD
        la = i
    return rv

def E(n, mod):
    eq = M3(n)
    g = M2(n)
    m = M(n)
    print(eq, g, m)
    rv = pow(2, m, mod) - 1
    pie = 0
    #do the l=r + l + r
    pie += 3 * (pow(2, eq + 2*g, mod) - 1)

    #do the l=r + l=m + l
    pie += 3 * (pow(2, 2*eq + g, mod) - 1)
    print(pie)

    #do the l=r + l
    pie -= 6 * (pow(2, eq + g, mod) - 1)

    #do the l = r
    pie -= 3 * 2 * (pow(2, eq, mod) - 1)
    #do the l 
    pie -= 3 * 2 * (pow(2, g, mod) - 1)
    print(pie)

    #add back the 1 case
    print(pie)

    return (rv - pie) % mod

print(E(10000000, 11**8))