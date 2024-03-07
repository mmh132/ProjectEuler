from sympy.ntheory import sqrt_mod

def I(n):
    rts = sqrt_mod(1, n, True)
    rts.remove(n-1)
    return max(rts)
N = 2*10**7
rv = 0
for i in range(N, 2, -1):
    if not i%10000: print(100*i/N)
    rv += I(i)
print(rv)
