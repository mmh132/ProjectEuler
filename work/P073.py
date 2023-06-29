from math import gcd
from math import floor
best = 1
for d in range(1_000_000, 0, -1):
    n = floor((3*d)/7)
    if gcd(n,d) == 1:
        if abs(3/7 - n/d) < best:
            best = abs(3/7 - n/d)
            print(n)

