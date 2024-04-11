from functools import cache

def mex(s):
    i = 0
    while i in s:
        i += 1
    return i



@cache
def g(u):
    if u == 0: return 0
    l = [g(u-i) for i in [1,3] if i <=u]
    return mex(set(l))


for i in range(1, 100):
    print(i, g(i))