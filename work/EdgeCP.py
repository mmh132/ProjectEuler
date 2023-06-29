from copy import deepcopy as dc
def add(polya, polyb):
    rv = [0]*max(len(polya), len(polyb))
    for i in range(len(polya)):
        rv[i] += polya[i] % (10**9+7)
    for i in range(len(polyb)):
        rv[i] += polyb[i] % (10**9+7)
   # for i in range(len(rv)):
       # rv[i] %= (10**9+7)
    return rv

def diff(polya, polyb):
    rv = [0]*max(len(polya), len(polyb))
    for i in range(len(polya)):
        rv[i] += polya[i] % (10**9+7)
    for i in range(len(polyb)):
        rv[i] -= polyb[i] % (10**9+7)
    #for i in range(len(rv)):
        #rv[i] %= (10**9+7)
        #if rv[i] < 0: rv[i] += (10**9+7)
    return rv

memo = dict()
def ChromaticPolynom(graph, emp):
    #if graph is edgeless, obviously its options ^ vertices
    if len(graph) == 0: print(emp); return [0]*emp + [1]
    #if str(graph) in memo: return memo[str(graph)]

    #if graph is complete return that
    #otherwise, expansion deletion contract
    #first find the first node in the graph that is connected
    #print("a")
    #print(graph)
    delt = graph.pop(0)
    #print(delt)
    delete = graph.copy()
    #print(delete)
    contract = []
    for i in graph:
        if delt[1] == i[0]:
            contract.append((delt[0], i[1]))
            graph.remove(i)
        if delt[1] == i[1]:
            contract.append((delt[0], i[0]))
            graph.remove(i)
    for i in contract:
        if i[0] == i[1]: contract.remove(i)
    contract += graph
    #print(contract)
    
    rv = diff(ChromaticPolynom(delete, emp), ChromaticPolynom(contract, emp-1))
    #memo[str(graph)] = rv
    return rv

memo2 = dict()
def ChromaticPolynomSet(graph, emp):
    #if graph is edgeless, obviously its options ^ vertices
    if len(graph) == 0: return [0]*emp + [1]
    if (frozenset(graph), emp) in memo: return memo2[(frozenset(graph), emp)]

    #if graph is complete return that
    #otherwise, expansion deletion contract
    #first find the first node in the graph that is connected
    print(graph,emp)
    delt = graph.pop()
    delete = graph.copy()
    contract = set()
    for i in graph:
        if delt[1] == i[0]:
            if delt[0] != i[1]:
                contract.add(tuple(sorted([delt[0], i[1]])))
        elif delt[1] == i[1]:
            if delt[0] != i[0]:
                contract.add(tuple(sorted([delt[0], i[0]])))
        else: 
            contract.add(i)
    
    rv = diff(ChromaticPolynomSet(delete, emp), ChromaticPolynomSet(contract, emp-1))
    memo2[(frozenset(graph), emp)] = rv
    return rv


tester = []
for i in range(1,10):
    for k in range(i+1,10):
        tester.append((i,k))
print(tester)
testerset = set()
for i in tester: testerset.add(i)
print(ChromaticPolynomSet(testerset, 9))