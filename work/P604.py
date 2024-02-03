def lsievetot(n):
    primes, cmp, tot = [],[0]*(n+1),[0]*(n+1)
    tot[1] = 1
    for i in range(2, n+1):
        if not cmp[i]:
            primes.append(i)
            tot[i] = i-1
        for j in primes:
            idx = i*j
            if idx > n: break
            cmp[idx] = True
            if i%j == 0:
                tot[idx] = tot[i]*j
                break
            else:
                tot[idx] = tot[i]*(j-1)
    return tot

def f(n):
    n//=2
    tot = lsievetot(n)
    rv, i = 1, 1
    while n>0:
        rv += tot[i]
        n-= i*tot[i]
        print(i, n, rv)
        i+=1
    if n < 0:
        i -= 1
        n += i*tot[i]
        rv -= tot[i]
        rv += n//tot[i]
        print(i, n, rv)
    return rv*2

print(f(100))
        
