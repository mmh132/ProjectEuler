from math import gcd
def tripct(cap):
    m,n = 1,1
    tot = 0
    while m**2+n**2 < cap:
        while m**2 + n**2 < cap:
            if gcd(m,n) == 1 and (m%2,n%2) != (1,1): tot += 1
            n += 1
        m += 1
        n = m+1 
    return tot
print(tripct(10**6))
