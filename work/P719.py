def splittable(n,toreach):
    if toreach<0 or len(n) == 0: return False
    if int(n) == toreach: return True
    for i in range(1,len(str(toreach))+1):
        if splittable(n[i:], toreach-int(n[:i])):
            return True
    return False
sum = 0
squares = [str(i**2) for i in range(10**6+1)]
kekr=0
for i in range(len(squares)):
    if kekr == 50:
        #print(i/10**6)
        kekr = 0
    else: kekr+=1
    if splittable(squares[i],i):
        sum += int(squares[i])
print(sum-1)




