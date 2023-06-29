import math
combos = []
def choosesets(cfrom, nchoose, out):
    if nchoose == 0:
        combos.append(out)
    else:
        storein = cfrom[:]
        storeout = out[:]
        for i in range(len(cfrom)):
            storein.pop(0)
            storeout.append(cfrom[i])
            choosesets(storein,nchoose-1,storeout)
            storeout = out[:]

def pentagonal(n):
    return n*(3*n-1)/2

nums = []
for i in range(1,3000):
    nums.append(pentagonal(i))
out = []
print("built nums")
choosesets(nums,2,out)
check = []
print("built sets")
for i in range(len(combos)):
    print(i)
    check = combos[i]
    if abs(check[0]-check[1]) in nums:
        if check[0]+check[1] in nums:
            print(combos[i])
            break
print("done")

