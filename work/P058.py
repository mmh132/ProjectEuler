from math import sqrt
def isprime(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0: return False
    return True
primes = 3
nums = 5
c = 9
inc = 4
while primes/nums > 0.1:
    print(primes,nums)
    for i in range(4):
        c += inc
        if isprime(c): primes += 1
        nums += 1
    inc += 2
print(inc-1)
