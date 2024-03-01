from math import comb
def f(n, k):
    rv = 0
    for z in range(n//5 + 1):
        if n-5*z <= 0: continue
        rv += (-1)**z * comb(k, z)*comb(n-5*z+k-1, k-1)
    return rv

print(f(11, 3))