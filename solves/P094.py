sizecap = 1000000000
def coprime(a,b):
    if a==0:
        return b==1
    return coprime(b%a,a)
def buildtriples(lessthan):
    total = 0
    n = 1
    m = 1
    i = 1
    stor = []
    while 2*(m**2)+2*m*n < lessthan:
        while n<m and 2*(m**2)+2*m*n < lessthan:
            if coprime((m**2-n**2),2*m*n) and coprime((m**2+n**2),2*m*n) and coprime((m**2-n**2),(m**2+n**2)):
                while i*(2*m**2+2*m*n)<lessthan:
                    stor = [i*(m**2-n**2),i*2*m*n,i*(m**2+n**2)]
                    if abs(stor[2]-2*stor[0]) == 1:
                        total += stor[2]*2+2*stor[0]
                    elif abs(stor[2]-2*stor[1]) == 1:
                        total += stor[2]*2+2*stor[1]
                    i+=1
            n+=1
            i=1
        m+=1
        n=1
    return total
print(buildtriples(sizecap))

