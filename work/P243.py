def factor(n):
    rv = []
    i = 2
    while n != 1:
        while n%i == 0: rv.append(i); n//=i
        i+=1
    print(rv)
    return rv

def tot(n, facs):
    for i in facs:
        n *= (i-1)
        n /= i
    return int(n)

def compare(n, d):
    return n*94744<15499*d


for i in range(2*3*5*7*11*13,10**10,2):
    a = factor(i)
    if compare(tot(i,a), i-1):
        print(i)
        break