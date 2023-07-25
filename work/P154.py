number = 200000
numberof5= [0]*(number+1)
numberof2= [0]*(number+1)
i = 2
tmp = 0
val = 0
while i < len(numberof2):
    tmp = i
    val = 0
    while tmp%2 == 0: tmp//=2; val+=1
    numberof2[i]+=val
    i += 2
facstorer2 = [0]*(number+1)

i = 5
tmp = 0
val = 0
while i < len(numberof5):
    tmp = i
    val = 0
    while tmp%5 == 0: tmp//=5; val+=1
    numberof5[i]+=val
    i += 5
facstorer5 = [0]*(number+1)

for i in range(1,len(facstorer5)):
    facstorer5[i] += facstorer5[i-1] + numberof5[i]
del numberof5
for i in range(1,len(facstorer2)):
    facstorer2[i] += facstorer2[i-1] + numberof2[i]
del numberof2
fives = facstorer5[200000]
twos = facstorer2[200000]
twosub = 0
fivsub = 0
tot = 0
for x in range(0,number+1):
    print(x)
    for y in range(number+1-x):
        twosub = facstorer2[x] + facstorer2[y] + facstorer2[number-x-y]
        fivsub = facstorer5[x] + facstorer5[y] + facstorer5[number-x-y]
        if fives-fivsub >= 12 or twos - twosub >= 12:
            tot += 1
print(tot)

