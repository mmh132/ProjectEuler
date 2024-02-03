def sumpow(n, k):
    rv = 0
    for i in range(1, n+1):
        rv += (i**k) % n
    print(rv, n, k)
    return rv

def inner(N):
    for k in range(1, 20, 2):
        sumpow(N, k)

def S(N):
    rv = 0
    for n in range(1, N + 1):
        ta = 0
        for k in range(1, N + 1, 2):
            ta += sumpow(n, k)
        ta = ta/n
        rv += ta
    return rv

def test(n, k):
    print([(i**k) % n for i in range(1, n+1)])

b = 3
inner(b**2), inner(b**3), inner(b**4), inner(b**5), inner(b**6), inner(b**8), inner(b**10)

#for squarefree n and any odd k, s(n, k) = n(n-1)//2
#for not squarefree n and any odd k, s(n, k) = n(n-1)//2 with some error.
#s(n, 1) is always choose(n, 2), but for every square it takes one more k for it to stabalize
# for example, 18 = 2^2 3^2 takes one step to stabalize, but 16 = 2^4 takes two

#sumpow(16, 1) = 120, (16, 3) = 96 , (16, 5) = 64 and then constant
#sumpow(16*3, 1) = 1128, (16*3, 3) = 1056, (16*3, 5) = 960 and then constant
#note the differences in the second are 3 times the differences in the first. 