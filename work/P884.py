from functools import cache

# 0 1 2 3 4 5 6 7 8 9 10
# 0 0 1 2 3 4 5 6 0 1 2

#subtract 1 from 1->7, subtract 8 from 8 -> 10
@cache
def S(n):
    if n < 2: return 0
    rv, i = n-1, 1
    while i*i*i < n:
        l = (i+1)**3
        if l >= n: l = n
        rv += S(l - i**3)
        i += 1
    return rv

print(S(10**17))
    
