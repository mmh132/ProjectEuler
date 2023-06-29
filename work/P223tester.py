from math import sqrt
def issq(n):
    return int(sqrt(n)) == sqrt(n)
def test(n):
    t = 0
    rs = set()
    for a in range(1,n//2):
        for b in range(a, n//2):
            ct = a**2+b**2-1
            if issq(ct):
                if a+b+sqrt(ct) < n:
                    t += 1
                    print(a,b,int(sqrt(ct)))
                    rs.add((a,b,int(sqrt(ct))))
    return rs