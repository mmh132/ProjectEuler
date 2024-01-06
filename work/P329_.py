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