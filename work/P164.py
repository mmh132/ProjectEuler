memo = []
def recbuild(diga, digb, iters):
    if iters == 19: return 1
    for i in range(len(memo)): 
        if memo[i][0] == iters and memo[i][1] == diga and memo[i][2] == digb: return memo[i][3]
    rv = 0
    for i in range(9-(diga+digb)+1): rv+=recbuild(digb,i,iters+1)
    memo.append([iters,diga,digb,rv])
    return rv
print(sum(recbuild(0,i,0) for i in range(1,10)))