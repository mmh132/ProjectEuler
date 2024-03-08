p, q, r = 10**6, 10**7, 10**8
#p, q, r = 4, 4, 44
MOD, K = 10**9 + 7, p+q+r

f = [1,1]
for i in range(2, K+1):
    f.append((f[-1]*i) % MOD)

finv = [pow(f[-1], -1, MOD)]
k = K
while k>0:
    finv.append((finv[-1]*k) % MOD)
    k -= 1
finv.reverse()

def comb(n, k):
    if k < 0 or k > n: return 0
    return (f[n]*finv[n-k]*finv[k]) % MOD

def w(a, b, c):
    rv = 0
    for tr in range(1, 2*min(a, b) + 1):
        A = (tr+1)//2 + (1 if not tr&1 else 0)
        B = (tr+1)//2
        #we have al a's to place in A holes
        # same for b's
        # then for c's we have tr + 2 transition holes
        # as well as al a-holes, and bl b-holes
        rv += comb(a - 1, A - 1)*comb(b - 1, B - 1)*comb(c - 2*tr + a + b, a + b)
        A = (tr+1)//2 
        B = (tr+1)//2 + (1 if not tr&1 else 0)
        #we have al a's to place in A holes
        # same for b's
        # then for c's we have tr + 2 transition holes
        # as well as al a-holes, and bl b-holes
        rv += comb(a - 1, A - 1)*comb(b - 1, B - 1)*comb(c - 2*tr + a + b, a + b)
    return rv % (10**9 + 7)

print(w(p,q,r))