
allsets = []
total = [0]
factorial = [1,1,2,6,24,120,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
factorial[17] = 355687428096000
factorial[18] = 6402373705728000
def solnset(setnums,div):
    numzeroes = 0
    while setnums[numzeroes] == 0: numzeroes += 1
    if numzeroes == 0:
        return factorial[18]/div
    else:
        uniquenums = 0
        for i in range(len(setnums)-1): 
            if setnums[i] != setnums[i+1]:uniquenums += 1
        return ((18-uniquenums)*factorial[17])/div
def recbuild(setn, curnum, div):
    setn = setn.copy()
    if curnum == 9:
        if len(setn) == 18:
            total[0] += solnset(setn,div)
        if len(setn) < 18 and len(setn)>14:
            div*=factorial[18-len(setn)]
            for i in range(18-len(setn)):
                setn.append(9)
            total[0] += solnset(setn,div)
        return
    if curnum == 0:
        for i in range(4):
            recbuild(setn,curnum+1,div*factorial[i])
            setn.append(curnum)
    else: 
        for i in range(4):
            recbuild(setn,curnum+1,div*factorial[i])
            setn.append(curnum)
    return
recbuild([],0,1)
print(int(total[0]))