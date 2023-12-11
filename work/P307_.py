from numpy import log, exp
from decimal import Decimal, getcontext

getcontext().prec = 50

N, K = 10**6, 20000
lgs = [0,0] + [Decimal(log(i)) for i in range(2, N+1)]
logfacs = [0,0]
for i in range(2,N+1): logfacs.append(logfacs[-1] + lgs[i])

def c(n, k):
    return logfacs[n] - logfacs[n-k] - logfacs[k]

rv = Decimal(1)
for t in range(K//2+1):
    tmp = c(N, t) + c(N-t, K-2*t) + logfacs[K] - t*lgs[2] - K*lgs[N]
    rv -= exp(tmp)
print(round(rv, 10))
