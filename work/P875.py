from itertools import product
from functools import cache
from time import time
@cache
def q(i):
    mr = [0]*(i)
    for x in product(range(i), repeat = 4):
        mr[sum([j*j for j in x]) % i] += 1
    return sum([i*i for i in mr])

# print(q(125))

# for i in range(1,51):
#     print(i, q(i))

# 3 -> 3^3 * 83 = 2241
# 3^2 -> 3^7 * 2243 = 4905441
# 3^3 -> 3^11 * 60563 = 10728553761
    
# 5 -> 5^3 * 639 = 78625
# 5^2 -> 5^7 * 78629 = 6142890625
# 5^3 -> 5 ^ 11 * 9828629 = 479913525390625

# def factor(n):
#     rv = []5498166987641 % 1001961001
#     i = 2
#     while i*i <= n:
#         e = 0
#         while n%i == 0:
#             n//=i
#             e += 1
#         if e:
#             rv.append((i, e))
#         i += 1
#     if n: rv.append((n, 1))
#     return rv

# def opt(n):
#     rv = 1
#     for i in factor(n):
#         rv*=g(i[0],i[1])
#     return rv

# out = 0
# for i in range(1, 11):
#     print(i, opt(i) % MOD)
#     out += opt(i)
# print(out % MOD)

MOD = 1001961001

def a(e):
    return (pow(8, e, MOD) - 1)*pow(7, -1, MOD)

@cache
def g(p, e):
    if p == 2:
        return pow(2, 3 + 4*e)*a(e)
    rv = pow(p, 4*(e-1) + 3)
    if e == 1:
        rv *= (pow(p, 4) + p - 1)
    else:
        rv *= (g(p, e-1)*pow(p, -4*(e-2) - 3, MOD)*pow(p, 3) + p - 1)
    return rv % MOD

N = 12345678

func, cnt, isc, primes = [0]*(N + 1), [0]*(N + 1), [0]*(N + 1), []
func[1] = 1
for i in range(2, N + 1):
    if not isc[i]:
        primes.append(i)
        func[i] = g(i, 1)
        cnt[i] = 1
    for p in primes:
        if i*p > N: break
        isc[i*p] = 1
        if i % p == 0:
            func[i*p] = func[i] * pow(g(p, cnt[i]), -1, MOD) * g(p, cnt[i] + 1) 
            func[i*p] %= MOD
            cnt[i*p] = cnt[i] + 1
            break
        else:
            func[i*p] = func[i]*func[p] % MOD
            cnt[i*p] = 1

print("done")
out = 0
for i in range(2, N + 1):
    out += func[i]
    out %= MOD 
print(out+1)

