MOD = 1_000_000_087
def f(n):
    w = [0]*(n+1)
    s = [1]*(n+1)
    for i in range(2, n+1):
        if w[i] == 0:
            for k in range(i, n+1, i):
                w[k] += 1
    for i in range(2,len(w)):
        if w[i] == 0: w[i] = 1

    for d in range(2, n+1):
        ta = pow(2, w[d], MOD)
        for k in range(d, n+1, d):
            s[k] += ta
            s[k] %= MOD
    print(s)
    rv = 0
    x = 1
    for i in range(1, n+1):
        x *= s[i]
        x %= MOD
        rv += x
        rv %= MOD
    return rv
print(f(10))