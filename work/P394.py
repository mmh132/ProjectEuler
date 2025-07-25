import sys
sys.setrecursionlimit(100_000)

CUTOFF = 2
LIM = 1000

def guess(x, k):
    if 1-x < CUTOFF: return k
    o = (1 - (1/(1-x) * CUTOFF))**2 
    return (1-o) * k + o*guess(x + 2/3 * (1-x)*(1-CUTOFF), k+1)

print(guess(0, 0))


def guess(cutoff, k):
    #if cutoff >= 1: return k
    o = (1 - 1 / cutoff)**2
    if k > LIM: return (1-o) * k
    cutoff = 1 / (1 - (2/3) * (1 - cutoff))
    return (1-o) * k + o * guess(cutoff, k+1)

print(guess(CUTOFF, 0))