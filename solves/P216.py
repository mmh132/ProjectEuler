from PrimeUtil import MillerRabin64

t = 0
for i in range(2,5*10**7+1):
    if i%10_000 == 0: print((100*i)/(5*10**7))
    if MillerRabin64(2*i**2-1):
        t+=1
print(t)
