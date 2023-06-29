import sys
sys.setrecursionlimit(100000)
def g(a,x):
    if x<a: return 1
    return g(a, x-1) + g(a, x-a)
def G(x): return g(x**0.5, x)

print(G(10**3))