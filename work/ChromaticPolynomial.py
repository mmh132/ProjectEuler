from copy import deepcopy as dcop

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

def eval(poly, x, mod):
    rv = 0
    for i in range(len(poly)):
        rv += poly[i]*pow(x,i,mod)
        rv %= mod
    return rv

def isempty(graph):
    for x in graph:
        if x != set(): return False
    return True
memo = dict()


def ChromaticPolynom(graph):
    #if graph is edgeless, obviously its options ^ vertices
    if isempty(graph): return [0]*len(graph) + [1]
    if str(graph) in memo: return memo[str(graph)]

    #if graph is complete return that
    #otherwise, expansion deletion contract
    #first find the first node in the graph that is connected
    n1 = 0
    for todel in range(len(graph)-1,-1,-1):
        n1 = todel
        if len(graph[n1]) != 0: break
    
    n2 = list(graph[n1])[0]
    contract = dcop(graph)
    delete = dcop(graph)

    #for contraction, add all adjacencies of second node to main node, then delete the second

    #add all adjacencies of n2 to n1
    contract[n2] = contract[n1].union(graph[n2])
    #remove the pointer to itsself
    contract[n2].discard(n2)
    #remove all duplicate pointers
    #remove node 2 from the graph
    contract.pop(n1)
    #replace all n2 adjacencies with n1 adjacencies
    for c in range(len(contract)):
        if n1 in contract[c]: contract[c].discard(n1); contract[c].add(n2)
    if n2 in contract[n2]: contract[n2].discard(n2)
    
    #for delete, same edge must be  removed
    #n1 gets all adjacencies except of edge to be removed
    delete[n1].remove(n2)
    #n2 gets all adjacencies except edge to be removes aswell
    delete[n2].remove(n1)

    rv = diff(ChromaticPolynom(delete), ChromaticPolynom(contract))
    memo[str(graph)] = rv
    return rv

