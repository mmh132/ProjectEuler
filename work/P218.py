from math import gcd as g
def paritytest(a,b):
    list = [a%2, b%2]
    if sorted(list) == [0,1]: return True
    return False
def coprime(a,b):
    if a==0:
        return b==1
    return coprime(b%a,a)
def buildtriples(lessthan):
    tripleset = []
    n = 1
    m = 1
    i = 1
    temp = 2*(m**2)+2*m*n
    stor = []
    while temp < lessthan:
        while n<m and temp < lessthan:
            if g(m,n)==1 and paritytest(m,n):
                stor = [(m**2-n**2),2*m*n,(m**2+n**2)]
                stor = sorted(stor)
                tripleset.append(stor) 
            temp = 2*(m**2)+2*m*n
            n+=1
            i=1
        m+=1
        n=1
    return tripleset
thing = buildtriples(10**7)
print(len(thing))