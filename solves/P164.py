memo = dict()
def recbuild(diga, digb, iters):
    if iters == 19: return 1
    if (diga,digb,iters) in memo: return memo[(diga,digb,iters)]
    rv = 0
    for i in range(9-(diga+digb)+1): rv+=recbuild(digb,i,iters+1)
    memo[(diga,digb,iters)] = rv
    return rv
print(sum(recbuild(0,i,0) for i in range(1,10)))