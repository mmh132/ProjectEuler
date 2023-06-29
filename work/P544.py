from ChromaticPolynomial import ChromaticPolynom
from EdgeCP import ChromaticPolynomSet
def generateGridGraph(h,w):
    tempset = set()
    graph = list()
    for i in range(0,h*w):
        tempset = set()
        if i-w>-1: tempset.add(i-w)
        if i+w<h*w: tempset.add(i+w)
        if i%w != w-1: tempset.add(i+1)
        if i%w != 0: tempset.add(i-1)
        graph.append(tempset)
    return graph
x,y = 5,5
tester = generateGridGraph(x,y)
print(tester)
print([(x + (10**9+7)) % (10**9+7) for x in ChromaticPolynom(tester)])

edgelist = []
for x in range(len(tester)):
    for i in tester[x]:
        edgelist.append((x+1,i+1))
edgeset = set()
for i in edgelist:
    edgeset.add(tuple(sorted(list(i))))
print(edgeset)
print([(x + (10**9+7)) % (10**9+7) for x in ChromaticPolynomSet(edgeset, x*y)])
