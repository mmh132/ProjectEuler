import time
start_time = time.time()
sizesearch = 10000
def bs(val,l,u):
    if sqsum[(l+u)//2] == val:
        return (l+u)//2
    if sqsum[(l+u)//2] > val:
        return bs(val, l, (l+u)//2)
    if sqsum[(l+u)//2] < val:
        return bs(val, (l+u)//2, u)

sqsum = [1,2,5,6,12,54,56,76,78,111]
print(bs(54,0,len(sqsum)-1))

#squares = [x**2 for x in range(1,sizesearch)]
#sqsum = [(a,b,a+b) for a in squares for b in squares if a!=b]
#sqsum.sort(key = lambda a: a[2])
#for i in range(len(sqsum)):
#    if sqsum[i][2] == sqsum[i][2]:


print("--- %s seconds ---" % (time.time() - start_time))