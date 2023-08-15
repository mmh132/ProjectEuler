from math import sqrt, gcd
def bf(nn):
    def cop(n):
        t = 0
        L = sqrt(3)*sqrt(4*n-1)/6 + 0.5
        for y in range(1, int(L) + 1):
            L2 = (sqrt(4*n-3*y*y) - y)/2
            for x in range(1, min(int(L2), y) + 1):
                if gcd(x,y) == 1:
                    t += 1
                if x*x + x*y + y*y > n:
                    print("fuck")
        return t
    rv = 0
    for k in range(1, int(sqrt(nn)) + 1):
        rv += cop(nn//(k*k))
    return rv
print(bf(10**6))