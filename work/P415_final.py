from math import gcd, isqrt
import time

start = time.time()

nottest = True
MOD = 2*10**8
N = 10**11
Y = int((N+1)**(2/3))

#sum of kth powers
def sumpowers(n, k):
    if k == 0:
        return n
    elif k == 1:
        return n*(n+1)//2
    elif k == 2:
        return n*(n+1)*(2*n+1)//6
    elif k == 3:
        return n*n*(n+1)*(n+1)//4
    else:
        print("you fucked up")

#compute the linear sieves for F0, F1, F2
if nottest:
    F0lsieve = list(range(Y+1))

    for i in range(2, Y+1):
        if F0lsieve[i] == i:
            F0lsieve[i] = i-1
            for k in range(i+i, Y+1, i):
                F0lsieve[k] //= i
                F0lsieve[k] *= (i-1)

    F1lsieve = F0lsieve.copy()
    F2lsieve = F0lsieve.copy()
    for i in range(2, Y+1):
        F1lsieve[i]*=i
        F2lsieve[i]*=i*i

    #accumulate values
    for i in range(2, Y+1):
        F0lsieve[i] += F0lsieve[i-1]
        F1lsieve[i] += F1lsieve[i-1]
        F2lsieve[i] += F2lsieve[i-1]

#prefix sums of totient(n), using totient(n) * u = N
def F0prefix(n):
    F0sum = dict()
    for v in range(1, isqrt(n) + 1):
        F0sum[v] = F0lsieve[v]
    for z in range(isqrt(n), 0, -1):
        v = n//z
        if v < Y:
            F0sum[v] = F0lsieve[v]
            continue
        x = sumpowers(v, 1)
        for i in range(1, isqrt(v)+1):
            x -= (F0lsieve[i]-F0lsieve[i-1])*(sumpowers(v//i, 0))
            if i!=1:
                x -= F0sum[v//i]
        x += F0sum[isqrt(v)]*sumpowers(isqrt(v), 0)
        F0sum[v] = x
    return F0sum

#prefix sums of n*totient(n)
def F1prefix(n):
    F1sum = dict()
    for v in range(1, isqrt(n) + 1):
        F1sum[v] = F1lsieve[v]
    for z in range(isqrt(n), 0, -1):
        v = n//z
        if v < Y:
            F1sum[v] = F1lsieve[v]
            continue
        x = sumpowers(v, 2)
        for i in range(1, isqrt(v)+1):
            x -= (F1lsieve[i]-F1lsieve[i-1])*(sumpowers(v//i, 1))
            if i!=1:
                x -= F1sum[v//i]*i
        x += F1sum[isqrt(v)]*sumpowers(isqrt(v), 1)
        F1sum[v] = x
    return F1sum

#prefix sums of n^2*totient(n)
def F2prefix(n):
    F2sum = dict()
    for v in range(1, isqrt(n) + 1):
        F2sum[v] = F2lsieve[v]
    for z in range(isqrt(n), 0, -1):
        v = n//z
        if v < Y:
            F2sum[v] = F2lsieve[v]
            continue
        x = sumpowers(v, 3)
        for i in range(1, isqrt(v)+1):
            x -= (F2lsieve[i]-F2lsieve[i-1])*(sumpowers(v//i, 2))
            if i!=1:
                x -= F2sum[v//i]*i*i
        x += F2sum[isqrt(v)]*sumpowers(isqrt(v), 2)
        F2sum[v] = x
    return F2sum

fF0 = F0prefix(N+1)
fF1 = F1prefix(N+1)
fF2 = F2prefix(N+1)

print(fF0[18409], fF1[1840], fF2[123])
def F0(n, m):
    if n == 0: return 0
    return (2*fF0[n]-1) % m
def F1(n, m):
    if n == 0: return 0
    return (3*fF1[n]-1) % m
def F2(n, m):
    if n == 0: return 0
    return (fF2[n]) % m

def mm(k, m):
    return (((pow(2, k, m) - k*(k-1)//2 - k - 1)%m)+m)%m

def f(n, k, m):
    if n<=k: return 0
    x = (4*n*(n-k) + 4*n*n*F0(n//k, m) - 4*k*n*F1(n//k, m) + 4*k*k*F2(n//k, m)) % m
    return x

def sum2tok(n, m):
    return (pow(2, n, m) - n - 1 + m) % m

def sumk2tok(n, m):
    return (n-pow(2, n+1, m)+2)*(1-n)//2

def sumkk2tok(n, m):
    return (((pow(2, n, m)*((n-2)*n + 3) - n*(n+1)*(2*n+1)//6 - 3)%m) + m)%m

def weirdextrasum(n, m):
    return ((2*n*(-n*n - 3*n + pow(2, n+1, m) + 2))%m)

def Tbad(n, m):
    rv = pow(2, (n+1)*(n+1), m) - (n+1)*(n+1) - 1
    #print(rv)
    x = 0
    #subtract the sum(4n*(n-k)*(2^(k-1)-1))
    x += weirdextrasum(n+1, m)
    #subtract the other random shit you have to: f(3)m(2), f(2)m(3), f(n)m(n+1), f(n+1)m(n)
    #signs are flipped from whiteboard because you are subtracting twice, T = c- sum, sum = newsum - this
    #print(x)
    x -= (f(n+1,3,m)*mm(2,m) + f(n+1,n+1,m)*mm(n+2,m)) % m
    x += (f(n+1,2,m)*mm(3,m) + f(n+1,n+2,m)*mm(n+1,m)) % m
    #print(x)
    for k in range(3, n+2):
        x += 4*(n+1)*(n+1)*F0((n+1)//k, m)*(pow(2, k-1, m) - 1)
        x -= 4*(n+1)*F1((n+1)//k, m)*(k*(pow(2, k-1, m) - 1))
        x += 4*F2((n+1)//k, m)*(k*k*(pow(2, k-1, m) - 1))
        x %= m
    #print(x)
    return (rv - x//2 + m)%m

def T(n, m):
    rv = pow(2, (n+1)*(n+1), m) - (n+1)*(n+1) - 1
    x = 0
    #subtract the sum(4k*(n-k)*(2^(k-1)-1))
    x += weirdextrasum(n+1, m)

    x -= (f(n+1,3,m)*mm(2,m) + f(n+1,n+1,m)*mm(n+2,m)) % m
    x += (f(n+1,2,m)*mm(3,m) + f(n+1,n+2,m)*mm(n+1,m)) % m

    for k in range(3, isqrt(n+1) + 1):
        x += 4*(n+1)*(n+1)*F0((n+1)//k, m)*(pow(2, k-1, m) - 1)
        x -= 4*(n+1)*F1((n+1)//k, m)*(k*(pow(2, k-1, m) - 1))
        x += 4*F2((n+1)//k, m)*(k*k*(pow(2, k-1, m) - 1))
        x %= m
    for z in range(1, isqrt(n+1) + 1):
        k = (n+1)//z
        if (n+1)//z == z: continue
        fixedfor = (n+1)//z - (n+1)//(z+1)
        x += 4*(n+1)*(n+1)*F0((n+1)//k, m)*(sum2tok(k, m) - sum2tok(k-fixedfor, m))
        x -= 4*(n+1)*F1((n+1)//k, m)*(sumk2tok(k, m) - sumk2tok(k-fixedfor, m))
        x += 4*F2((n+1)//k, m)*(sumkk2tok(k, m) - sumkk2tok(k-fixedfor, m))
        x %= m
    return ((rv - x//2)%m + m) % m




print(T(N,MOD) % 10**8)
print(time.time() - start)
