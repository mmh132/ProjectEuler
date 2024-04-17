from math import isqrt

N = 10**8
f = set()
for i in range(1, isqrt(N) + 1):
    x = i*i
    for j in range(i + 1, isqrt(N) + 1):
        x += j*j
        if x > N: break
        if str(x) == str(x)[::-1]:
            f.add(x)
print(sum(f)) 
