from math import sqrt as sqrt
def sieve(size):
    numbers = list(range(2,size+1))
    for ptr in range(0,int(sqrt(size))+1):
        if numbers[ptr] != 0:
            for k in range(ptr + numbers[ptr], len(numbers), numbers[ptr]):
                numbers[k] = 0
    primes = [x for x in numbers if x!=0]
    return primes
def floorlog(num, n):
    i = 1
    stor = num
    while stor < n:
        stor*=num
        i+=1
    return i-1
def mindivby1ton(n):
    primes = sieve(n)
    rv = 1
    for i in primes:
        rv*=(i**floorlog(i,n))
    return rv
print(mindivby1ton(1000000) % (10**9 + 7))