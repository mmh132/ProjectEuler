f1=0
f2=1
fcur=f1+f2
curridx = 2
modulo = 1307674368000
n=(10**15)%modulo
sum = n+n**2
def ntokmod(n,k):
    n=n%modulo
    return (n**k)%modulo

while curridx<10**15:
    f1=f2
    f2=fcur
    fcur = (f1+f2)%modulo
    curridx+=1
    
print(fcur)
sum = sum%modulo


print(sum)


