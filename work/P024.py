permutation = []
def permutations(inset, outset):
    if len(inset) == 0:
        permutation.append(outset)
    else:
        tempset = []
        tempout = []
        for i in range(len(inset)):
            tempset = inset[:]
            tempout = outset[:]
            tempout.append(tempset[i])
            tempset.pop(i)
            permutations(tempset, tempout)

thing = [0,1,2,3,4,5,6,7,8,9]
permutations(thing, [])
print(permutation[999999])
