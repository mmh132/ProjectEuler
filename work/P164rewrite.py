from functools import cache
@cache
def dp(a, b, l): return 1 if l == 0 else sum([dp(b, i, l-1) for i in range(10-a-b)])
print(dp(0,0,20)-dp(0,0,19))