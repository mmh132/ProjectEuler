from math import sqrt, gcd
import time
start_time = time.time()
def f(L):
    s = 0
    for i in range(3, int(1.42*(sqrt(L))) + 1):
        for k in range(1, i//2 + 1):
            if gcd(i,k) == 1: 
                s += L//i//(i-k)
    return s

def o(L):
    s = 0
    for i in range(3, L):
        for k in range(1, i//2 + 1):
            if gcd(i,k) == 1: 
                s += L//i//(i-k)
    return s

print(f(10**12))

print("--- %s seconds ---" % (time.time() - start_time))