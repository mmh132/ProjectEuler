def bt(f):
    p = 0
    for i in range(1001):
        if pow(1+2*f, i)*pow(1-f, 1000-i) >= 1_000_000_000: p = 1000-i; break
    return p/1000
print(bt(1/4))

def rb(depth, curpow, curnum):
    if depth == 0: return curnum
    i = 0
    while bt(curnum + i*pow(10, -1*curpow)) <= bt(curnum + (i+1)*pow(10, -1*curpow)): i+=1
    return rb(depth-1, curpow+1, curnum + i*pow(10, -1*curpow))
magicnum = rb(15,1,0)
print(magicnum)
print(bt(magicnum))

from math import log10, comb
c = [log10(comb(1000, n)) for n in range(1001)]

def bt(f):
    w = 0
    for h in range(1001):
        x = h*log10(1+2*f) + (1000-h)*log10(1-f)
        if x >= 9: w += c[h]
    return w

def ter(a,b,c):
    