from math import log as ln, exp
import decimal

decimal.getcontext().prec = 50

def val(f):
    rv = 0
    for i in range(1001):
        if i * ln(1+2*f) + (1000 - i) * ln(1 - f) > 9*ln(10):
            return i

def ternary(l, r):
    err = 10**-10
    while r-l > err:
        m1, m2 = l + (r - l) / 3, r - (r - l) / 3
        f1, f2 = val(m1), val(m2)
        if f1 > f2: l = m1  
        else: r = m2
        print(m1)
    return val(m1)

fac = [decimal.Decimal(0), decimal.Decimal(0)]
for i in range(2, 1001):
    fac.append(fac[-1] + decimal.Decimal(i).ln())

def p(start):
    rv = 0
    for i in range(start, 1001):
        rv += exp(fac[1000] - fac[i] - fac[1000-i] - decimal.Decimal(1000)*decimal.Decimal(2).ln())
    return rv

print(round(p(ternary(0, 1)), 12))
