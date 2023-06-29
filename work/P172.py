allsets = []
total = [0]
factorial = [1,1,2,6,24,120,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
factorial[17] = 355687428096000
factorial[18] = 6402373705728000
def solnset(setnums):
    numzeroes = 0
    while setnums[numzeroes] == 0: numzeroes += 1
    absnum = [1]
    ptr = 0
    for i in range(numzeroes, len(setnums)-1):
        if setnums[i] == setnums[i+1]:
            absnum[ptr] += 1
        else:
            ptr+=1
            absnum.append(1)
    div = 1
    if numzeroes == 0:
        for i in range(len(absnum)):
            div*=factorial[absnum[i]]
        return factorial[18]/div
    else:
        total = 0
        for k in range(len(absnum)):
            absnum[k]-=1
            for i in range(len(absnum)):
                div*=factorial[absnum[i]]
            total += factorial[17]/(div*factorial[numzeroes])
            absnum[k]+=1
            div = 1
        return total 
def recbuild(setn, curnum):
    setn = setn.copy()
    if curnum == 9:
        if len(setn) == 18:
            total[0] += solnset(setn)
            allsets.append(setn)
        if len(setn) < 18 and len(setn)>14:
            for i in range(18-len(setn)):
                setn.append(9)
            total[0] += solnset(setn)
            allsets.append(setn)
        return
    for i in range(4):
        recbuild(setn,curnum+1)
        setn.append(curnum)
recbuild([],0)
print(int(total[0]))

