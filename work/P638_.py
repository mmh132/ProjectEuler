MOD = 10**9+7

def bin(n, k):
    num, d = 1, 1
    for i in range(n-k+1, n+1):
        num = (num*i) % MOD
    for i in range(2, k+1):
        d = (d*i) % MOD
    return (num*pow(d, -1, MOD)) % MOD

def c(a, b, k):
    if k == 1: 
        return bin(a+b, a)
    kp = k-1
    n, d = 1, 1
    for i in range(1, a+b + 1):
        if i <= a:
            d = (d*kp) % MOD
        else:
            n = (n*kp) % MOD
        kp = (kp*k + k - 1) % MOD
    return (n*pow(d, -1, MOD)) % MOD

rv = 0
for k in range(1, 7 + 1):
    rv += c(10**k + k, 10**k + k, k)
print(rv % MOD)


