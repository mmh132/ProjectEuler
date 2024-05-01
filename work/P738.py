from math import log2
def partitions(n, k):
    if k == 1:
        yield [1]*n
        return
    for c in range(n//k + 1):
        for p in partitions(n - c*k, k - 1):
            yield [k]*c + p

N = 10**1
# find values of the multiplicative function
f = [0] * (int(log2(N)) + 1)

for i in range(1,len(f)):
    val = 0
    for p in partitions(i, i):
        val += N - len(p)
    f[i] = val

print(f)