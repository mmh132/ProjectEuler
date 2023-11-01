from math import gcd
print(len(set([(i//gcd(i,k), k//gcd(i,k)) for k in range(1864, 1910) for i in range(0, k)])))
print(sum(1 if gcd(i,k) == 1 else 0 for i in range(1864,1910) for k in range(i)))