from math import isqrt
N = 10**2

isc, lpf, cnt, primes = [0]*(N + 1), [0]*(N + 1), [0, 1] + [0]*(N-1), []
for i in range(2, N + 1):
    if not isc[i]:
        primes.append(i)
        cnt[i] = 1
        lpf[i] = i
    for j in primes:
        if i*j > N: break
        isc[i*j] = 1
        if i % j:
            cnt[i*j] = cnt[i] + 1
            lpf[i*j] = lpf[i]
        else:
            cnt[i*j] = 1
            lpf[i*j] = lpf[i]
print(lpf)
print(cnt)