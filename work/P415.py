from math import gcd
def f(pts):
    return 2**pts - pts*(pts-1)//2 - pts - 1
def bf(n, mod):
    rv = 0
    for m1 in range(1, n+1):
        for m2 in range(1, n+1):
            if gcd(m1, m2) == 1:
                for x in range(n+1):
                    for y in range(n+1):
                        if x-m2 >= 0 and y-m1 >= 0: continue
                        pts = min((n-x)//m2, (n-y)//m1) + 1
                        rv += f(pts)
                        rv = rv%mod
    return rv

def solve(n, mod):
    rv = bf(n, mod)
    rv *= 2
    #size2
    rv += (n+1)*2*f(n+1)
    #size1
    rv += (n+1)**2 + 1
    return (pow(2, (n+1)**2, mod) - rv) % mod

print(solve(111, 10**8))