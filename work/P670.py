import sys
sys.setrecursionlimit(10000)

def dp(s, l):
    if l == 0:
        return 1 if s in [1,4] else 0
    if l<0: 
        return 0
    if s == 1:
        return 6*dp(4,l-2) + 3*dp(2,l) + 3*dp(3,l) + 3*dp(1,l-1)
    elif s == 2:
        return 2*dp(4,l-1) + 2*dp(3,l-1)
    elif s == 3:
        return 2*dp(4,l-1) + 2*dp(2,l-1)
    else:
        return 2*dp(1,l-1)
    

def realfunky(l):
    x = 0
    x += 4*dp(1,l-1)
    x += 6*dp(2,l-1)
    x += 6*dp(3,l-1)
    x += 6*dp(4,l-1)
    x += 6*dp(4,l-2)
    print(x)

print(realfunky(2))