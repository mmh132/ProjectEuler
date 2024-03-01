from math import gcd
from functools import cache
# def topt(n):
#     assert 0 <= n < 16
#     return (n//4, n%4)

# def ton(pt):
#     assert 0 <= pt[0] < 4 and 0 <= pt[1] < 4
#     return pt[0]*4 + pt[1]

# @cache
# def dp(mask, last, lastslope):
#     lp = (last//4, last%4)
#     rv = 1
#     for dir in range(16):
#         if mask & (1 << dir): continue
#         fp = topt(dir)
#         d = gcd((fp[0] - lp[0]), (fp[1] - lp[1]))
#         if d == 0: 
#             print(fp[0] - lp[0], fp[1] - lp[1], fp, lp, bin(mask))
#         slope = ((fp[0] - lp[0])//d, (fp[1] - lp[1])//d)
#         if slope == lastslope: continue
#         nm = 0
#         for i in range(d + 1):
#             nm += 1 << ton((lp[0] + slope[0]*i, lp[1] + slope[1]*i))
        
#         rv += dp(mask | nm, dir, slope)
#     return rv

# out = 0
# for i in range(16):
#     out += dp(1 << i, i, (0,0))
#     pass
# print(out - 9)
# print([ton(topt(i)) for i in range(16)])


# from math import gcd
# from functools import cache
# def topt(n):
#     assert 0 <= n < 16
#     return (n//4, n%4)

# def ton(pt):
#     assert 0 <= pt[0] < 4 and 0 <= pt[1] < 4
#     return pt[0]*4 + pt[1]

# @cache
# def dp(mask, last):
#     lp = (last//4, last%4)
#     rv = 1
#     for dir in range(16):
#         if mask & (1 << dir): continue
#         fp = topt(dir)
#         d = gcd((fp[0] - lp[0]), (fp[1] - lp[1]))
#         if d == 0: 
#             print(fp[0] - lp[0], fp[1] - lp[1], fp, lp, bin(mask))
#         slope = ((fp[0] - lp[0])//d, (fp[1] - lp[1])//d)
        
#         nm = 0
#         for i in range(d + 1):
#             nm += 1 << ton((lp[0] + slope[0]*i, lp[1] + slope[1]*i))
        
#         rv += dp(mask | nm, dir)
#     return rv

# out = 0
# for i in range(16):
#     out += dp(1 << i, i)
#     pass
# print(out - 9)
# print([ton(topt(i)) for i in range(16)])

