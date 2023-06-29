from math import gcd 
def digcancelling(num, den):
    if num%10 == den%10 == 0: return False
    if len(set(str(num)).intersection(set(str(den)))) == 0: return False
    toremove = list(set(str(num)).intersection(set(str(den))))[0]
    newn = str(num).replace(toremove,"",1)
    newd = str(den).replace(toremove,"",1)
    if newd == "0": return False
    return (num/den) == int(newn)/int(newd)
print(digcancelling(30,50))
print(digcancelling(79,50))
print(digcancelling(49,98))

num = 1
den = 1
for i in range(10,100):
    for d in range(i+1, 100):
        if digcancelling(i,d):
            num*=i
            den*=d
            print("here")
g = gcd(num,den)
print(den/g)
