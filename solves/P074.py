#digit factorial chains
def digitfactorial(n):
    rv = 0
    for i in range(len(str(n))):
        rv+=singledigitfactorial(str(n)[i])
    return rv

def singledigitfactorial(n):
    if n == "0":
        return 1
    if n == "1":
        return 1
    if n == "2":
        return 2
    if n == "3":
        return 6
    if n == "4":
        return 24
    if n == "5":
        return 120
    if n == "6":
        return 720
    if n == "7":
        return 5040
    if n == "8":
        return 40320
    if n == "9":
        return 362880

def recLen(curr, size, set):
    stor = digitfactorial(curr)
    if stor in set:
        return size
    else:
        set.append(stor)
        return recLen(stor, size+1, set)
thing = [169]
print(recLen(digitfactorial(169),1,thing))

sum = 0
for i in range(1,1000001):
    thing = [i]
    if recLen(digitfactorial(i),1,thing) == 59:
        sum+=1
print("total: " + str(sum))

    