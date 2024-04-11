from math import isqrt

def tonellishanks(n, p):
    print(n, p)
    n %= p
    if p%4 == 3:
        r = pow(n, (p+1)//4, p)
        if (r*r) % p == n:
            return r
        return -1

    #test if its a quadratic residue
    if pow(n, (p-1)//2, p) == -1: return -1
    
    #find a quadratic non-residue for z. im being lazy. cry about it
    z = 2
    while pow(z, (p-1)//2, p) == 1: z+=1
    
    #find p-1 = Q*2**k
    q, k = p-1, 0
    while q%2 == 0: 
        q //= 2
        k += 1
        
    #set our variables for the loop on invariant R and t
    m = k
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q+1)//2, p)
    while t>1:
        
        #find least i<m such t^2^i = 1
        testbase, i = t, 0
        while i<m and testbase != 1:
            testbase = (testbase * testbase) % p
            i += 1
            
        #we should exit with an i<m or we fucked up
        assert i < m
        assert testbase == 1
        
        #manage looping invariants
        b = c
        for i in range(m-i-1): b = (b*b) % p
        m = i
        c = (b*b) % p
        t = (t*b*b) % p
        r = (r*b) % p
        
    #if we fail we fail, otherwise we didnt
    if t == 0: return 0
    if t == 1: return r
    return -1 

def segsieve(n):
    S = 10000
    primes = []
    rt = isqrt(n)
    isp = [1]*(rt + 1)
    for i in range(2, rt + 1):
        if not isp[i]: continue
        primes.append(i)
        for j in range(i*i, rt + 1, i):
            isp[j] = 0
    rv = []
    block = [1]*S
    for k in range(n//S + 1):
        block = [1]*S
        start = k*S
        for p in primes:
            startidx = (start + p - 1) // p
            j = max(startidx, p) * p - start
            while j < S:
                block[j] = 0
                j += p 
        if k == 0:
            block[0] = block[1] = 0
        for i in range(min(S, n-start + 1)):
            if block[i]:
                rv.append(start + i)

    return rv

L = 10**2
sieve = [4*k*k + 1 for k in range(L + 1)]
mp = [0]*(L + 1)

cp = segsieve(isqrt(4*L*L + 1))
cp.pop(0)
for p in cp:
    target = (p-1)*pow(4, -1, p) % p
    np = tonellishanks(target, p)
    onp = p-np
    for i in range((L-np)//p + 1):
        mp[np + i*p] = p
    for i in range((L-onp)//p + 1):
        mp[onp + i*p] = p

print(mp)


