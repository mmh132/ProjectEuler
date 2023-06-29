size = 1000000
numbers = list(range(1,size+1))
sumdivisors = []
for i in range(len(numbers)):
    sumdivisors.append(0)

for n in range(1,int(size/2)+1):
    for i in range(2*n,len(numbers),n):
            sumdivisors[i-1] += n

def bestchain(curr, size, start):
    if curr>1000000 or size>100:
        return -1
    if curr == 0 or curr == 1 or curr == sumdivisors[curr-1]:
        return -1
    if curr == start and size != 0:
        return size
    else:
        return bestchain(sumdivisors[curr-1], size+1, start)    

currbest = 0
stor = 0
for i in range(1,size+1):
    
    stor = bestchain(i,0,i)
    if stor > currbest:
        currbest = stor
        print(i)

