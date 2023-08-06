# we are defining polynomials as strings such that P[k] = coefficient near x^k

# we use a special function G on a polynomial F(x) = sum(c_i * x^i)(i=0,n)
# that fufills G(F) = sum(c_i * s_i)(i=0, n). G is additive and this scalar
# ie. G(F + H) = G(F) + G(H) and G(kF) = kG(F) for polynomials H, F and scalar k
# we then use the fact that G(x^k) = s_k, and the fact that since, for the characteristic 
# polynomail of the recurrence C = {c_1, c_2 ... c_n}, which we will call 
# P = x^n - sum(c_i * x^(n-i))(i=1, n), it suffices to compute G(x^k mod P)
def solve(c, s, k, mod):
    #c is our recurrence, s is terms, k is term number
    n = len(c)
    a = [c[0]] if n == 1 else [0,1]
    x = 1
    while k > 0:
        if k%2:
            x = mul(x,a,c,n)
        a = mul(a,a,c,n)
        k//=2
    rv = 0
    for i in range(n):
        rv += x[i]*s[i]
    return rv

def mul(a, b, m, n):
    # m is polynomial modulus
    rv = [0]*(len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            rv[i+j] += a[i]*b[j]
    for i in range(len(rv) - 1, len(m)-1, -1):
        for j in range(len(m)-1, -1, -1):
            rv[i-j-1] += rv[i]*m[j]
    return rv[min(len(rv), n):]

print(solve)

def BM(s, mod):
    #c is recurrence, pc is best previous recurrence
    c, pc = list(), list()
    #f is index of failure
    f = -1
    for i in range(len(s)):
        #evaluate c(i), evaluate delta, if its zero then c(i) is right
        delta = s[i]
        for k in range(1, len(c) + 1):
            delta -= c[k-1]*s[i-k]

    pass