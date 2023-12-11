from math import isqrt

def mobius(n):
    mob = list(range(n+1))
    prime = [1]*(n+1)
    for i in range(2, n+1):
        if prime[i]:
            mob[i] *= -1
            for j in range(i+i, n+1, i):
                mob[j]*=-1
                prime[j] = 0
            for j in range(i**2, n+1, i**2):
                mob[j] = 0
    return mob

def g(n):
    rv = 0
    for x in range(1,isqrt(n) + 1):
        rv += isqrt(n-x*x) 
    return rv

def solve(n):
    rv = 0
    mob = mobius(isqrt(n))
    for i in range(1, isqrt(n)+1):
        rv += g(n//(i*i))*mob[i]
    return rv
    
print(solve(10**6))

# from math import isqrt
# def d(n):
# 	rv = 0
# 	for i in range(1, isqrt(n) + 1):
# 		rv += i*(n//i)
# 		rv += (n//i)*(n//i + 1)//2
# 	rv -= isqrt(n)*isqrt(n)*(isqrt(n)+1)//2
# x = int(input())
# while x:
# 	y = int(input)
# 	print(d(y))
# 	x-=1