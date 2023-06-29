from Graph import chromaticpoly as cpoly
from Graph import chrompolyedge as edgepoly
from Graph import numedges as ned
from at2 import takechrom
from finalGraph import takepoly
from ChromaticPolynomial import ChromaticPolynom
from ChromaticPolynomial import eval
from EdgeCP import ChromaticPolynomSet
import time
start_time = time.time()
graph = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
for i in range(0,10**2):
    v = i%10
    w = i**2//10 % 10
    if v == w: continue
    graph[w] += [v]
    graph[v] += [w]
for x in graph:
    graph[x] = [*set(graph[x])]
colors = 5
print(graph)
print(cpoly(graph, colors,ned(graph)))

print("--- %s seconds ---" % (time.time() - start_time))


edgelist = []
for x in graph:
    for i in(graph[x]):
        edgelist.append({x,i})
nlist = []
[nlist.append(x) for x in edgelist if x not in nlist]

start_time1 = time.time()
print(edgepoly(nlist,10,5))
print("--- %s seconds ---" % (time.time() - start_time1))


start_time2 = time.time()
newl = []
for x in graph:
    newl.append(set([a for a in graph[x]]))
print(takechrom(newl, 5))
print("--- %s seconds ---" % (time.time() - start_time2))
print(newl)
start_time3 = time.time()
print(takepoly(newl,5,0))
print("--- %s seconds ---" % (time.time() - start_time3))

start_time4 = time.time()
print(ChromaticPolynom(newl))
print("--- %s seconds ---" % (time.time() - start_time4))

edgeset = set()
for i in edgelist:
    edgeset.add(tuple(sorted(list(i))))

start_time4 = time.time()
print(edgeset)
print(ChromaticPolynomSet(edgeset, 10))
print("--- %s seconds ---" % (time.time() - start_time4))