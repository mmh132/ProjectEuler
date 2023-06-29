def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return [x for x in primes if x!= 0]
primes = sieve(100000000)
def rev(n):
    if str(n) == str(n)[::-1]: return False
    return int(str(n)[::-1]) in squares
squares = [x**2 for x in primes]
summed, ctr = 0,0
for i in squares:
    if rev(i) and ctr<51:
        ctr+=1
        summed+=i
        print(i)
print(summed)