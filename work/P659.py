def f(x):
    return 4*x*x + 1

c = f(1) - f(0)
L = 100
psieve = [f(x) for x in range(L + 1)]
mp = [0]*(L + 1)

for i in range(1, L + 1):
    p = psieve[i]
    j = i
    while j < L + 1:
        while psieve[j] % p == 0:
            psieve[j] //= p
            mp[j] = p
        j += p - (c*j % p)

print(sum(mp))