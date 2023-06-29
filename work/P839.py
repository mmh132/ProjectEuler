def issorted(l):
    for i in range(len(l)-1):
        if l[i]>l[i+1]: return False
    return True
def sort(l):
    s = 0
    while issorted(l) == False:
        for i in range(len(l)-1):
            a,b = l[i],l[i+1]
            if a>b:
                if (a-b) % 2 == 0:
                    l[i] -= (a-b)//2
                    l[i+1] += (a-b)//2
                    s += (a-b)//2
                else: 
                    l[i] -= (a-b+1)//2
                    l[i+1] += (a-b+1)//2
                    s += (a-b+1)//2
            print(l)
    print(s)
inp = 6
beans = [290797]
for i in range(inp-1):
    beans.append((beans[-1]**2)%50515093)
sort(beans)

sort([5,5,6,2])