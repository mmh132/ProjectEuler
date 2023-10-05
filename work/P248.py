from math import factorial as fac
def factor(n):
    p = 2
    f = []
    while n != 1:
        e = 0
        while n % p == 0:
            e += 1
            n //= p
        if e != 0:
            f.append((p, e))
        p += 1
    return f

print(factor(fac(13)))