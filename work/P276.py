def isqrt(x):
    if x == 1: return 1
    a = x >> 1
    b = x
    while a < b:
        c = (a + x//a) >> 1
        a,b = c,a
    return b

def bf(n):
    s=0
    for a in range(1, n//2):
        for b in range(a, n//2+1):
            for c in range(b, n//2+1):
                if a <= b and b <= c:
                    if a+b+c <= n:
                        if a+b > c:
                            s += 1
    return s

def secbf(n):
    s = 0
    for a in range(1, n//2):
        for b in range(a, n//2+1):
            for c in range(b, min(a+b, n-a-b+1)):

                s += 1
    return s

def a(n):
    return round((((n+1)**3 + 3*(n+1)**2 -9*(n+1)*((n+1)%2))>>4)/9)

b = [1, 1, 2, 3, 5, 6, 9, 11, 15, 18, 23]
for i in range(10_000_000):
    b.append(b[-1] + b[-2] - 2*b[-5] + b[-8] + b[-9] - b[-10])

print(b[100 - 3])
print([(a(i),i) for i in range(95, 105)])

cache = dict()
def f(n):
    if n in cache: return cache[n]
    rv = b[n-3] if n >= 3 else 0
    for g in range(2, isqrt(n) + 1):
        rv -= f(n//g)
    for z in range(1, isqrt(n) + 1):
        if n//z != z:
            rv -= (n//z - n//(z+1))*f(z)
    cache[n] = rv
    return rv


print(f(10_000_000))
