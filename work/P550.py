from math import isqrt
def mex(s):
    i = 0
    while i not in s: i+=1
    return i
def isprime(x):
        for i in range(2, isqrt(x) + 1):
            if x%i==0: return False
        return True
def bf(n):
    seq = [0,0]
    for i in range(2,n+1):
        if isprime(i):
            seq.append(0)
        else:
            s = set()
            for d in range(2, i+1):
                if i%d == 0:
                    s.add(d)
            seq.append(mex(s))
    return seq

def lpf(n):
    for i in range(2, n):
        if n%i == 0: return i
    return False

L = 1000
x = bf(L)
for i in range(2,L):
    if x[i] != lpf(i) and not isprime(i):
        print(i)

    