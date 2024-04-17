from functools import cache

@cache
def dp(mask, l):
    if l == 0: return 1 if mask == 7 else 0
    rv = 13 * dp(mask, l-1) 
    rv += dp(mask | 4, l-1) + dp(mask | 2, l-1) + dp(mask | 1, l-1)
    return rv

rv = 0
for i in range(2, 16):
    rv += dp(4, i) + dp(2, i) + 13*dp(0, i)
print(str(hex(rv)).upper()[2:])