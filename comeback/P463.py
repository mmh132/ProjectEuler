
def log2(n):
    rv = 0
    while n:
        n >>= 1
        rv += 1
    return rv

def f2(n, k, z):
    l = min(pow(2, k)-1, n) - pow(2, k-1) + 1
    if k == z + 1: return l
    s = l // pow(2, z)
    rv = (l - s * pow(2, z)) * (s % 2) 
    rv += (s // 2) * 2**z 
    return rv

def f(n, k, z):
    assert z < k

    rv = 0
    for i in range(2**(k-1), min(2**k, n+1)):
        if (i >> z) & 1: rv += 1

    print(n, k, z, " -> ", rv , " or ", f2(n, k, z))
    
    return rv

def S(n):
    rv = 0
    for k in range(1, log2(n) + 1):
        for z in range(k):
            rv += 2**(k-z-1) * f2(n, k, z)
    return rv

print(S(8))
print(S(100))
print(S(3**37))