from math import gcd
def mobius(n):
    mob = [1]*(n+1)
    prime = [1]*(n+1)
    for i in range(2, n+1):
        if prime[i]:
            for j in range(i+i, n+1, i):
                mob[j]*=1
                prime[j] = 0
            for j in range(i**2, n+1, i**2):
                mob[j] = 0
    return mob

def f(n):
    cap = int(n**(1/4)+1)
    mob = mobius(cap)
    s = 0
    for i in range(1, cap+1):
        if mob[i] == 0: continue
        for k in range(1, cap+1):
            if mob[k] == 0 or gcd(i, k) != 1: continue
            x = i*i*i*i*i*k*k*k*k
            if x <= n:
                j = 1
                while x * j * j * j <= n:
                    s += n//(x*j*j*j)
                    j += 1
    return s

print(f(10**18))

