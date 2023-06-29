import math
import sys
sys.setrecursionlimit(1000000000)
smemo = {0:290797}
k = 2000000
def s(n):
    if n in smemo: return smemo[n]
    return s(n-1)**2 % 50515093
def p(n):
    return(s(2*n),s(2*n+1))
listvals = []
for i in range(k):
    listvals.append(p(i))
print("done")
listvals.sort(key = lambda a:a[0])
def eval(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
best = 10000000000000000000
storage = 0
for a in range(len(listvals)-1):
    storage = eval(listvals[a],listvals[a+1])
    if storage>best:
        best = storage
print(math.sqrt(best))
listvals.sort(key = lambda a:a[1])
for a in range(len(listvals)-1):
    storage = eval(listvals[a],listvals[a+1])
    if storage>best:
        best = storage
print(math.sqrt(best))