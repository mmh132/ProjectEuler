fibs = [1,1]
while len(fibs) < 24: fibs.append(fibs[-1] + fibs[-2])
def f(n):
    return fibs[n-1]
def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return [x for x in primes if x != 0]
def prod(l):
    rv = 1
    for i in l: rv*=i
    return rv
def s(n):
    primes = sieve(n)
    print(primes)
    ret = [0]
    def rb(pl, r, sv):
        if r == 0: ret[0] += prod(pl); return
        for i in range(sv, len(primes)):
            if primes[i]>r: break
            rb(pl.copy() + [primes[i]], r-primes[i], i)
        return
    rb([], n, 0)
    return ret[0]
n = 0
for i in fibs:
    n += s(i)
    print(n)
print(n%10**9)
