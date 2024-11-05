from sympy.ntheory.residue_ntheory import sqrt_mod as tonellishanks

N = 10**8
lpf = list(range(N + 1))
primes = []

for i in range(2, N + 1):
    if lpf[i] == i: primes.append(i)
    for j in primes:
        if j * i > N: break
        lpf[j * i] = j
        if i % j == 0: break

def isroot(n, p):

    m = p-1
    pfs = set()

    while m > 1:
        pfs.add(lpf[m])
        m //= lpf[m]
    
    for i in pfs:
        if pow(n, (p-1) // i, p) == 1: return False
    
    return True 

def fib(p):
    r = tonellishanks(5, p)
    if not r: return 0

    t1 = (1 + r) * pow(2, -1, p)
    t2 = (1 - r + p) * pow(2, -1, p)
    t1 %= p
    t2 %= p

    if isroot(t1, p) or isroot(t2, p): return 1
    return 0

primes.pop(0)
rv = 5
for p in primes: 
    print(p/N)
    rv += fib(p)*p
print(rv)






