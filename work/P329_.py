<<<<<<< Updated upstream
from fractions import Fraction

p = [1]*(500+1)
for i in range(2, len(p)):
    if not p[i]: continue
    for j in range (i+i, len(p), i):
        p[j] = 0
p[1] = 0

target = "PPPPNNPPPNPPNPN"

def psq(seq):
    pb = 1
    for i in range(15):
        if (p[seq[i]] == 1 and target[i] == "P") or (p[seq[i]] == 0 and target[i] == "N"):
            pb += 1
    return Fraction(2**pb, 3**15)

t = [Fraction(0)]*(500+1)
w = [0]*(500+1)
def allseq(ls):
    if len(ls) == 15: 
        t[ls[0]] += psq(ls)
        w[ls[0]] += 1
        return
    ls = list(ls)
    if ls[-1] != 500:
        allseq(tuple(ls + [ls[-1] + 1]))
    if ls[-1] != 1:
        allseq(tuple(ls + [ls[-1] - 1]))
    return

out = Fraction(0)

for i in range(1, 501):
    print(i)
    allseq((i,))
    out += t[i]*Fraction(1, w[i])
    
print(out*Fraction(1/500))
=======
from fractions import Fraction as frac
from functools import cache

want = [1,1,1,1,0,0,1,1,1,0,1,1,0,1,0]
want.reverse()

isp = [0,0] + [1]*(500 - 1)
for i in range(2, 500+1):
    if not isp[i]: continue
    for k in range(i+i, 500+1, i):
        isp[k] = 0

@cache
def dp(p, l):
    if l == -1:
        return 1
    rv = 0
    if p < 500:
        rv += (frac(1, 3) if isp[p]==want[l] else frac(1, 6))*dp(p+1, l-1)
        if p == 1: rv *= 2
    if p > 1:
        rv += (frac(1, 3) if isp[p]==want[l] else frac(1, 6))*dp(p-1, l-1)
        if p == 500: rv *= 2
    return rv

tp = frac()
for start in range(1, 501):
    tp += dp(start, 14)
print(tp/500)
>>>>>>> Stashed changes
