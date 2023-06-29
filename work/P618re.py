from math import sqrt
fibs = [0,1,1]
while len(fibs) < 25: fibs.append(fibs[-1] + fibs[-2])
print(fibs)

def isprime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def S(n):
    pl = [i for i in range(2, n+1) if isprime(i)]

    def rbn(n):
        if n == 0:
            return 1
        if n < 0: 
            return 0
        rv = 0
        for i in pl:
            if i > n: break
            rv += i*rbn(n-i)
        return rv % 10**9
    
    return rbn(n)

print(S(8))
