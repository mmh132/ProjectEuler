from math import isqrt
def ist(n):
    k = 2*n
    if k % isqrt(k) == 0 and k % (isqrt(k) + 1) == 0:
        return True
    return False
m = dict()
def dp(n, k):
    if k < 0 or n < 0:
        return 0
    if k == 0:
        if n==0 or ist(n):
            return 1
        return 0
    if (n,k) in m: return m[(n,k)]
    rv = 0
    x = 0
    for i in range(2*isqrt(n) + 1):
        x += i
        rv += dp(n-x, k-1)
    m[(n,k)] = rv
    return rv

print(dp(10**7, 2))

    