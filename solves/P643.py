from totientsum import totientsum

def f(n, mod):
    x = 1
    rv = 0
    while 2**x < n:
        rv += totientsum(n//(2**x)) - 1
        rv %= mod
        x += 1
    return rv

print(f(10**11, 10**9+7))