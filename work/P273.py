def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return [x for x in primes if x!=0 and x%4 != 3]
print(sieve(150))
def sqsm(n):
    for a in range(1,n):
        for b in range(a,n):
            if a**2+b**2 == n:
                return (a,b)
nice = [sqsm(i) for i in sieve(150) if i != 2]
print(nice)
def mult(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])

tot = [0]
def recbuild(sets, cur, num):
    check = (abs(cur[0]), abs(cur[1]))
    tot[0] += min(check)
    if num == 0: return
    for i in sets:
        reg, inv = i, (i[0], -1*i[1])
        recbuild([x for x in sets if x!= i], mult(cur, reg), num-1)
        recbuild([x for x in sets if x!= i], mult(cur, inv), num-1)
for i in range(1,7):
    recbuild(nice, (1,0), i)
print(tot)
    

    