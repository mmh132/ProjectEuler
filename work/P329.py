from math import sqrt

seq = [1,1,1,1,0,0,1,1,1,0,1,1,0,1,0]
frac = [0,0]

def isprime(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0: return False
    return True
prime = [1, 1] + [isprime(i) for i in range(2,501)]


def dp(pos, turn, isval):
    if turn == 15:
        if isval:
            frac[0] += 1
        frac[1] += 1
    want = seq[turn]

    if prime[pos]:
        if pos == 1:
            
    else:

    