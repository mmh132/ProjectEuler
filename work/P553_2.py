from functools import cache as ccc

@ccc 
def binom(n,k): return binom(n-1,k-1) + binom(n-1, k) if n>k>0 else 1
@ccc
def f(n):
    rv = 2**(n-1)-1
    for i in range(1, n):
        #fix a connected component with exactly i numbers
        rv -= (2**(n-i-1)-1)*f(i)
    return rv
print(f(3))
