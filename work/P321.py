l = [1,1,0,2,2]
def recrun(l, pls, moves):
    if moves==8:
        if l == [2,2,0,1,1]:
            print(pls)
            return
        else: return
    for i in range(len(l)-1):
        if l[i] != 0 and l[i+1] == 0:
            l[i+1] = l[i]
            l[i] = 0
            recrun(l ,pls+" , "+str(l) ,moves+1)
            l[i] = l[i+1]
            l[i+1] = 0
            
    for i in range(1,len(l)):
        if l[i] != 0 and l[i-1] == 0:
            l[i-1] = l[i]
            l[i] = 0
            recrun(l ,pls+" , "+str(l) ,moves+1)
            l[i] = l[i-1]
            l[i-1] = 0
            
    for i in range(len(l)-2):
        if l[i] != 0 and l[i+1] != 0 and l[i+2] == 0: 
            l[i+2] = l[i]
            l[i] = 0
            recrun(l ,pls+" , "+str(l) ,moves+1)
            l[i] = l[i+2]
            l[i+2] = 0

    for i in range(2,len(l)):
        if l[i] != 0 and l[i-1] != 0 and l[i-2] == 0: 
            l[i-2] = l[i]
            l[i] = 0
            recrun(l ,pls+" , "+str(l) ,moves+1)
            l[i] = l[i-2]
            l[i-2] = 0

recrun(l,"",0)

tri = set([(n*(n+1))//2 for n in range(10000000)])
idxset = set()
n = 0
while len(idxset) < 40:
    n += 1
    if n**2 + 2*n in tri:
        idxset.add(n)
        print(idxset)
print(idxset)