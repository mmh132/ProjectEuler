primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
L = 10**14
vals = set()
def bfbuild(n, cidx):
    if n > L:
        return
    if cidx == len(primes): 
        vals.add(n)
        return
    tm, v = 1, primes[cidx]
    while tm*n < L:
        bfbuild(n*tm, cidx+1)
        tm *= v
bfbuild(1, 0)
print(len(vals))

s = 0
for i in vals:
    if i+1 in vals:
        s += i
print(s)