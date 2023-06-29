def mobius(n):
    mob = [1]*(n+1)
    prime = [1]*(n+1)

    for i in range(2, n+1):
        if prime[i]:
            for j in range(i+i, n+1, i):
                mob[j]*=1
                prime[j] = 0
            for j in range(i**3, n+1, i**3):
                mob[j] = 0
    return mob

def f(n):
    cap = int(n**(1/3)+1)
    mob = mobius(cap)
    s = n
    for i in range(2, cap+1):
        if mob[i] == 0: continue
        x = 3
        while i**x <= n:
            s += n//(i**x)
            x += 1
    return s
print(f(10**4))
print(mobius(10))