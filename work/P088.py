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
    if n in primes: return [1]
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
    return sols
i = 3
solsi = 1
kcur = list(range(2,12001))
answers = []
while kcur!=list():
    i+=1
    print(len(kcur))
    solsi = prodsum(i, kcur)
    if [x for x in solsi if x in kcur and x<12001] != list(): 
        answers.append(i)
        kcur = [x for x in kcur if x not in solsi]
answers = [*set(answers)]
print(answers)
print(sum(answers))




