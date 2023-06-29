from math import sqrt

def hilbertfactor(n):
    facs = []
    for i in range(5, n, 4):
        while n%i == 0: 
            n//=i
            if i in facs: return False
            facs.append(i)
    return True

def modifiedMobius(n):
    prime = [1] * (n + 1)
    mobius = [1] * (n + 1)

    for i in range(5, n + 1, 4):
        if not prime[i]:
            continue
        mobius[i] = -1
        for j in range(i+4*i, n+1, 4*i):
            prime[j] = 0
            mobius[j] *= -1
        for j in range(i**2, n+1, 4*i**2):
            mobius[j] = 0
    
    return mobius

def sqfree(sub):
    sqsub = int(sqrt(sub))
    mMob = modifiedMobius(sqsub)
    s = (sub-1)//4 + 1
    for i in range(5, sqsub+1, 4):
        x = (sub // (i*i))
        s += mMob[i]*((x-1)//4 + 1)
    return s

print(sqfree(10**7))
# print(hilbertfactor(6237))
# a = modifiedMobius(10000)
# for i in range(5, 10001, 4):
#     if a[i] == 0 and hilbertfactor(i) == True:
#         print(i, "thinks square, is squarefree")
#     if a[i] != 0 and hilbertfactor(i) == False:
#         print(i, "thinks squarefree, has square")

# print(hilbertfactor(441))