#bF(n) = R'(n) - sum of F(k)R'(n-k)
from math import comb
def R(n):
    if n == 0: return 0
    if n == 1: return 1
    x = 2**(2**n-1)-1
    for m in range(n):
        x -= comb(n, m)*R(m)
    return x
print(R(4))