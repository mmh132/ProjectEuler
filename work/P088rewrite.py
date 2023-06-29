def primefactorn(n):
    fac = []
    i = 2
    while n!= 1:
        while n%i == 0: n//=i; fac.append(i)
        i+=1
    return fac
def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return primes
asd = sieve(30000)
primes = []
for i in range(len(asd)): 
    if asd[i] != 0: primes.append(asd[i])
def prodsum(n, cur):
    if n in primes: return 1
    facs = primefactorn(n)
    sols = []
    def recsimplifier(listed, n):
        if len(listed) == 2:
            if n-sum(listed)+len(listed) < 12000:
                sols.append(n-sum(listed)+len(listed))
            return
        if n-sum(listed)+len(listed) < 12000:
            sols.append(n-sum(listed) + len(listed))
            for i in range(len(listed)-1):
                recsimplifier(listed[:i] + [listed[i]*listed[i+1]] + listed[i+2:],n)
    recsimplifier(facs,n)
    sols = [*set(sols)]
    while cur in sols: cur +=1
    return cur
i = 3
solsi = 1
kcur = 2
answers = []
while kcur < 12001:
    i+=1
    print(i)
    solsi = prodsum(i, kcur)
    if solsi>kcur: 
        answers.append(i)
        kcur = solsi
answers = [*set(answers)]
print(answers)
print(sum(answers))
