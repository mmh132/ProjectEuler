def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return [x for x in primes if x!=0]
cap = 30
su=[]
cur = 1
k = sieve(cap)
for i in k:
    while cur<cap:cur*=i
    cur//=i
    su.append(cur)
    cur = 1
print(su)