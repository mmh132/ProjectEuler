def isqrt(x):
    if x == 1: return 1
    a = x >> 1
    b = x
    while a < b:
        c = (a + x//a) >> 1
        a,b = c,a
    return b

def midpi(n):
    sq = isqrt(n)
    v = set()
    for i in range(1, sq + 1):
        v.add(i)
        v.add(n//i)
    v = list(v)
    v.sort()
    
    def geti(x):
        if x <= sq:
            return x - 1
        else:
            return len(v) - n//x

    a = 0
    dp = v.copy()
    for p in range(2, sq + 1):
        if dp[geti(p)] != dp[geti(p-1)]:
            a += 1
            for i in range(len(v)-1, -1, -1):
                if v[i] < p*p:
                    break
                dp[i] -= dp[geti(v[i] // p)] - a
    
    return dp[geti(n) - 1]

print(midpi(10**11))



