from functools import cache

MOD = 10**9 + 33

@cache
def comb(n, k):
    if n == k or n == 0 or k == 0: return 1
    return comb(n-1, k-1) + comb(n-1, k)

@cache
def T(n, m):
    if n == 0 and m == 0: return 1
    if n == 0 or m == 0: return 0
    if n == 1 or m == 1: return 1
    if m > n: return T(m, n)
    rv = 0
    for k in range(n):
        rv += T(n-k, m-1)*comb(n, k)*(pow(2, n-k, MOD) - (1 if k == 0 else 0))
        rv %= MOD
    return rv

print(T(2, 3), T(3, 2), T(0, 1))

# @cache
# #pie by fixing k basically-zero points and counting elements of T that have them
# def R(n, m):
#     if n == 0 and m == 0: return 1
#     if n == 0 or m == 0: return 0
#     if n == 1 or m == 1: return 1
#     if n == m == 2: return 5
#     if m > n: return R(m, n)
#     rv = T(n, m)

#     for k in range(1, min(n, m)+1):
#         rv += pow(-1,k)*comb(n, k)*comb(m, k)*R(n-k, m-k)
#         print(comb(n, k)*comb(m, k)*R(n-k, m-k), k)
#         rv %= MOD
#     return rv
@cache
def R(n, m):
    rv = T(n, m)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            rv -=


def S(n):
    rv = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            rv = (rv + R(i, j)) % MOD
    return rv

#print(S(5))
