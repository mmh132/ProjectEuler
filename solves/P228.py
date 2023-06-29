from Frac import fraction
from math import gcd
print(len(set([(i//gcd(i,k), k//gcd(i,k)) for k in range(1864, 1910) for i in range(0, k)])))