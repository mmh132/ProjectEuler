from math import isqrt
from functools import cache

N = 5*10**15
rt = isqrt(N)

isp = [0,0] + [1]*(rt-1)
for i in range(2, isqrt(rt) + 1):
    isp[i*i::i] = [0]*((rt - i*i)//i + 1)

primes = [i for i in range(2, rt + 1) if isp[i]]

@cache
def h(p, e):
    if e < 2: return 1 if e == 0 else 0
    rv = pow(p, e if not e%p else e-1)
    for i in range(e):
        rv -= h(p, i)
    return rv

rv = 0
stk = [(1,1,0)]
while stk:
    c = stk.pop(0)
    nn, hn, i= c[0], c[1], c[2]
    if i >= len(primes) or primes[i]*primes[i] > N//nn: 
        rv += hn*(N//nn)
        continue
    stk.append((nn, hn, i+1))
    e = 2
    while nn*primes[i]**e < N:
        stk.append((nn*primes[i]**e, hn*h(primes[i],e), i+1))
        e += 1

print(rv - 1)
