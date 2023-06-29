from totientsum import totientsum

memo = dict()
def f(n):
    if n in memo: return memo[n]
    else:
        return totientsum(n)
    
def G(n):
    s = 0
    for i in range(1, n+1):
        s += i*f(n//i)
    return s

print(G(10**11) % 998244353)
