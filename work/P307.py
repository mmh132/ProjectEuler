from math import log, exp
N, K = 10**7, 20*10**3
f = [0, 1]
i = 2
while len(f) <= N:
    f.append(f[-1] + log(i))
    i+=1
def choose(n,k):
    return f[n] - f[n-k] - f[k]

p = 1
for x in range(K//2, K+1):
    power = choose(x, K-x) + choose(N, x) + f[K] - K*log(N)
    print(power)
    p -= exp(choose(x, K-x) + choose(N, x) + f[K] - K*log(N))
print(p)
