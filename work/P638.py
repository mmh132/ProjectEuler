
def prod(a,b,m): return (a[0]*b[1] % m, b[0]*a[1] % m)
def C(a,b,k):
    if a == 0: return (1,1)
    return prod(((k**(b+1)-1), k**a-1) , C(a-1,b+1,k) , (10**9+7))
def modinv(a,c):
    for b in range(1,c):
        if a*b % c == 1: return b
def f(a,b,k,m):
    inp = C(a,b,k)
    n = inp[0]
    d = inp[1]
    return n * modinv(d,m) % m
print(f(15,10,3,10**9+7))
    

