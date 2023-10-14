def omega(n):
    p = 2
    rv = 0
    while n > 1:
        while n % p == 0: 
            n//=p
            rv += 1
        p += 1
    return rv
def gcd(a,b):
    if a < b: a,b = b,a
    if b == 0: return a
    return gcd(b, a%b)
def s(n):
    rv = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            rv += omega(i) + omega(j) - 2*omega(gcd(i, j))
    return rv
print(s(100))