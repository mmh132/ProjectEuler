from math import sqrt, isqrt
from time import time


def sieve(n):
    p = [1]*(n+1)
    for i in range(2, n+1):
        if not p[i]: continue
        for k in range(i+i, n+1, i):
            p[k] = 0
    rv = []
    for i in range(2, n+1):
        if p[i]: rv.append(i)
    return rv

def atkin_prime_sieve(limit=1000000):
    """
    finding all prime numbers up to limit. O(n) time complexity, O(n) memory
    Sieve of Atkin, which is a much stronger version than sieve of Eratosthenes
    details see: https://en.wikipedia.org/wiki/Sieve_of_Atkin
    """

    plist = [0] * limit

    # n = 3x^2 + y^2 section
    x = 3
    for i in range(0, 12*int(sqrt((limit-1)/3)), 24):
        x += i
        y_limit = int(12*sqrt(limit-x)-36)
        n = x + 16
        for j in range(-12, y_limit+1, 72):
            n += j
            plist[n] = not plist[n]

        n = x + 4
        for j in range( 12, y_limit+1, 72):
            n += j
            plist[n] = not plist[n]

    # n = 4x^2 + y^2 section
    x = 0
    for i in range(4, 8*int(sqrt((limit-1)/4))+4, 8):
        x += i
        n = x + 1
        if x % 3:
            for j in range(0, 4*int(sqrt(limit-x))-3, 8):
                n += j
                plist[n] = not plist[n]
        else:
            y_limit = 12 * int(sqrt(limit-x)) - 36
            
            n = x + 25
            for j in range(-24, y_limit+1, 72):
                n += j
                plist[n] = not plist[n]

            n = x + 1
            for j in range( 24, y_limit+1, 72):
                n += j
                plist[n] = not plist[n]

    # n = 3x^2 - y^2 section
    x = 1
    for i in range(3, int(sqrt(limit/2))+1, 2):
        x += 4 * i - 4
        n = 3 * x
        if n > limit:
            y = (int(sqrt(n-limit)) >> 2) << 2
            n -= y * y
            s = 4 * y + 4
        else:
            s = 4

        for j in range(s, 4*i, 8):
            n -= j
            if n <= limit and n % 12 == 11:
                plist[n] = not plist[n]

    x = 0
    for i in range(2, int(sqrt(limit/2))+1, 2):
        x += 4 * i - 4
        n = 3 * x

        if n > limit:
            y = ((int(sqrt(n-limit)) >> 2) << 2) - 1
            n -= y * y
            s = 4 * y + 4
        else:
            n -= 1
            s = 0

        for j in range(s, 4*i, 8):
            n -= j
            if n <= limit and n % 12 == 11:
                plist[n] = not plist[n]

    # eliminate squares        
    for n in range(5, int(sqrt(limit))+1, 2):
        if plist[n]:
            for k in range(n*n, limit, n*n):
                plist[k] = False
    return [2,3] + list(filter(plist.__getitem__, range(5,limit,2)))

def segsieve(n):
    primes = []
    lim = isqrt(n)
    mark = [0]*(lim+1)
    for i in range(2, lim+1):
        if mark[i]: continue
        primes.append(i)
        for k in range(i*i, lim+1, i):
            mark[k] = 1
    

L = 10**8

z = time()
atkin_prime_sieve(L)
print(time() - z)

z = time()
sieve(L)
print(time() - z)

