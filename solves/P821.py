from math import isqrt

def magicfunc(n):
    if n < 243:
        if n < 54:
            if n < 24:
                if n < 6:
                    return 0
                return 1
            return 2
        return 3
    else:
        t = 0
        for k in range(2, n, 3):
            ct = t
            if pow(2, k-1)*3 <= n:
                t += 1
            if pow(3, k) <= n:
                t += 1
            if ct - t == 0:
                break
        return t

def congrange(s, tf):
    rv = 0
    rv += (tf-1)//6 
    rv += (tf-5)//6
    rv -= (s-1)//6
    rv -= (s-5)//6
    return rv

def genericplussqrt(n):
    h = 0
    for i in range(1, isqrt(n) + 1):
        if i % 6 == 1 or i % 6 == 5:
            h += magicfunc(n//i)
    for z in range(1, isqrt(n) + 1):
        if n//z != z:
            h += congrange(n//(z+1),n//z)*magicfunc(z)
    return n-h

print(genericplussqrt(10**16))