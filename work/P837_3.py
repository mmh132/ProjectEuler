from math import comb
MOD = 1234567891
M, N = 123456789,987654321
fac = [1,1]
while len(fac) < M+N:
    fac.append(fac[-1]*len(fac) % MOD)
print("done")

def g(n):
    flip = ((n%6)//3==1)
    rv = (pow(2,n,3*MOD)//3)%MOD
    if n%3 == 0:
        return rv + (0 if flip else 1)
    if n%3 == 1:
        return rv + (1 if flip else 0)
    if n%3 == 2:
        return rv + (0 if flip else 1)
def f(m,n):
    rv = 0
    # ab is ab+ba
    for ab in range(min(m,n)+1):
        if ab%10001 == 0: print(ab*100/n)
        # number aa blocks
        a = (m-ab)
        # number bb blocks
        b = (n-ab)
        if a&1 or b&1: continue
        a//=2
        b//=2
        rv += g(ab)*fac[a+b+ab]*pow(fac[a],-1,MOD)*pow(fac[b], -1, MOD)*pow(fac[ab], -1, MOD)
        rv %= MOD
    return rv
print(f(N,M))


def test(n):
    zero,one,two = 0,0,0
    for i in range(n+1):
        if i%3 == 0:
            zero += comb(n,i)
        if i%3 == 1:
            one += comb(n,i)
        if i%3 == 2:
            two += comb(n,i)
    print(n,n%3,zero,one,two, (2**n)//3)

def test2(n):
    rv = 0
    for x in range(-n%3, n+1, 3):
        rv += comb(n,x)
    return rv

# for i in range(10):
#     print(g(i), test2(i))
#for i in range(0, 15):test(i)
