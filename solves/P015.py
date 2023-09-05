from math import comb
from functools import cache
@cache
def dp(x,y):
    if x == 0 or y == 0: return 1
    return dp(x,y-1) + dp(x-1,y-1)

print(dp(20,20))
print(comb(40,20))