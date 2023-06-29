import copy
import time
start_time = time.time()
memo = dict()
x,y = 9,12
band = [0,0,0]
inp = []
for i in range(x): inp.append(band.copy())
def recbuild(row, depth):
    if depth == 0:
        if [x[0] for x in row] == [0]*len(row): 
            return 1
        return 0
    if 0 not in [a[0] for a in row]: 
        return recbuild([x[-2:]+[0] for x in row], depth-1)
    if (str(row),depth) in memo:
        return memo[(str(row),depth)]
    rv = 0
    temp = copy.deepcopy(row)
    x = -1
    for k in range(len(row)):
        if row[k][0] == 0 and x == -1: x = k
    if x+2 < len(row) and row[x+1][0] == row[x+2][0] == 0:
        temp = copy.deepcopy(row)
        temp[x][0] += 1
        temp[x+1][0] +=1
        temp[x+2][0] +=1
        rv += recbuild(temp,depth)
    if row[x][1] == row[x][2] == 0:
        temp = copy.deepcopy(row)
        temp[x][0] += 1
        temp[x][1] += 1
        temp[x][2] += 1
        rv += recbuild(temp,depth)
    if x + 1 < len(row) and row[x+1][0] == 0:
        if row[x+1][1] == 0:
            temp = copy.deepcopy(row)
            temp[x][0] += 1
            temp[x+1][0] += 1
            temp[x+1][1] += 1
            rv += recbuild(temp,depth)
        if row[x][1] == 0:
            temp = copy.deepcopy(row)
            temp[x][0] += 1
            temp[x][1] += 1
            temp[x+1][0] += 1
            rv += recbuild(temp,depth)
    if x + 1 < len(row) and row[x][1] == row[x+1][1] == 0:
        temp = copy.deepcopy(row)
        temp[x][0] += 1
        temp[x][1] += 1
        temp[x+1][1] +=1
        rv += recbuild(temp,depth)
    if x!= 0 and row[x-1][1] == row[x][1] == 0:
        temp = copy.deepcopy(row)
        temp[x][0] += 1
        temp[x][1]+=1
        temp[x-1][1] +=1
        rv += recbuild(temp,depth)
    memo[(str(row),depth)] = rv
    return rv
print(recbuild(inp,y))
print("--- %s seconds ---" % (time.time() - start_time))
