from math import sqrt
def buildtriples(lessthan):
    tripleset = []
    n = 1
    m = 1
    i = 1
    stor = []
    while 2*(m**2)+2*m*n < lessthan:
        while n<m and 2*(m**2)+2*m*n < lessthan:
            if sorted([m%2,n%2]) == [0,1]:
                    if abs((m**2-n**2)-2*m*n) == 1:
                        print( [(m**2-n**2),2*m*n,(m**2+n**2)], " with m,n being ", m , n  )
                    stor = sorted(stor)
                    tripleset.append(stor) 
                    i+=1
            n+=1
            i=1
        m+=1
        n=1
    return tripleset
#buildtriples(100000000)

sequence = [1,2]
for i in range(10):
     sequence.append(sequence[-1]*2+sequence[-2])
print(sequence)

def hype(sub):
    m=2
    n=1
    psum = 0
    while 2*m**2 + 2*m*n < sub:
        psum += 2*m**2 + 2*m*n
        m+=1
        n+=1
    return psum
def nohype(sub):
    recurrence = [1,2]
    m,n = recurrence[-1],recurrence[-2]
    psum = 0
    other = []
    while 2*m**2 + 2*m*n < sub:
        psum += (2*m**2 + 2*m*n) 
        other.append(2*m**2 + 2*m*n) 
        recurrence.append(recurrence[-1]*2 + recurrence[-2])
        recurrence.pop(0)
        m,n = recurrence[-1],recurrence[-2]

    return other
def nohype2(sub):
    recurrence = [1,2]
    m,n = recurrence[-1],recurrence[-2]
    psum = 0
    while 2*m**2 + 2*m*n < sub:
        psum += 2*m**2 + 2*m*n
        recurrence.append(recurrence[-1]*2 + recurrence[-2])
        recurrence.pop(0)
        m,n = recurrence[-1],recurrence[-2]
    return psum
#print(hype(10**(10)) + nohype(10**(10))-3-4-5)
#print(nohype(10**(10**10)) % 1234567891)

def fasthype(n):
    cap = int((1+sqrt(1+4*n))/(4))
    tot = 0
    for i in range(2,cap+1): tot += 4*i**2-2*i
    return tot
def fasterhype(n):
    cap = int((1+sqrt(1+4*n))/(4))
    return ((4*pow(cap,3,1234567891) + 3*pow(cap,2,1234567891) - (cap%1234567891)))/3-2

print(fasterhype(10**(10**10)))
seq = []
for i in range(1,20): seq.append(4*i**2-2*(i)); print(sum(seq))

#print(nohype(100000000))
#print(hype(100) + sum(nohype(100)))
#print(hype(100) + nohype2(100))