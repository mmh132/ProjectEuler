from math import lcm, factorial as fac, comb

def dictu(d1, d2):
    x = d1.copy()
    for i in d2:
        if i in d1: d1[i] += d2[i]
        else: d1[i] = d2[i]
    print(x, d2, d1, "union")
    return d1
def dictmul(c, d1):
    x = d1.copy()
    for i in d1:
        d1[i] *= c
    print(x, c, d1, "mul")
    return d1
def dictlcm(n, d1):
    d2 = {}
    for i in d1:
        d2[lcm(n, i)] = d1[i]
    print(d1, n, d2, "lcm")
    return d2

def dp(left, mx):
    if mx== 1:
        return {1: 1}
    #rv = dp(left, mx - 1)
    rv = dict()
    for a in range(1, left//mx + 1):
        rv = dictu(rv, dictmul(comb(left, a*mx)*fac(a*mx)/(pow(fac(mx), a))/fac(a), dp(left - a*mx, mx - 1)))
    rv = dictlcm(mx, rv)
    rv = dictu(rv, dp(left, mx-1))
    return rv

print(dp(5, 5))

    

