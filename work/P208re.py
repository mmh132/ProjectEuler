from math import factorial as fac

cache = dict()
def dp(rm, lm):
    if rm == 0 or lm == 0:
        return 1
    if (rm, lm) in cache: return cache[(rm, lm)]
    return dp(rm-1,lm) + dp(lm-1, rm)

print(dp(15, 10))