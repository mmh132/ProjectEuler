memo = dict()
def recbuild(prev, found, bank, size):
    if size == 0: 
        #print(prev) 
        return 1
    #if str(prev) + str(found) + str(bank) + str(size) in memo: return memo[str(prev) + str(found) + str(bank) + str(size)] 
    if found:
        rv = 0
        tmp = bank.copy()
        for k in [i for i in bank if i < prev[-1]]:
            tmp = bank.copy()
            tmp.remove(k)
            rv += recbuild(prev + [k],found,tmp,size-1)
        #memo[str(prev) + str(found) + str(bank) + str(size)] = rv
        return rv
    if not found:
        rv = 0
        tmp = bank.copy()
        for i in bank:
            tmp = bank.copy()
            tmp.remove(i)
            rv += recbuild(prev + [i],i<prev[-1],tmp,size-1)
        #memo[str(prev) + str(found) + str(bank) + str(size)] = rv
        return rv
    print("err")
    return -1
print(str(recbuild([0],False,list(range(1,27)), 6)) + " from " + str(6))