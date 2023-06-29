from copy import deepcopy as dcop
def isempty(graph):
    for x in graph:
        if x != set(): return False
    return True
memo = dict()
def takechrom(graph, colors):
    #if graph is edgeless, obviously its options ^ vertices
    if isempty(graph): return colors**len(graph)
    if str(graph) in memo: return memo[str(graph)]
    #if graph is complete return that
    #otherwise, expansion deletion contract
    #first find the first node in the graph that is connected

    edremov = 1
    for todel in range(len(graph)-1,-1,-1):
        x = todel
        if len(graph[x]) != 0: break
    
    n1 = x
    n2 = list(graph[x])[0]
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
        if n1 in contract[c]: contract[c].discard(n1); contract[c].add(n2); edremov +=1
    if n2 in contract[n2]: contract[n2].discard(n2)

    #for delete, same edge must be  removed
    #n1 gets all adjacencies except of edge to be removed
    delete[n1].remove(n2)
    #n2 gets all adjacencies except edge to be removes aswell
    delete[n2].remove(n1)

    rv = takechrom(delete,colors) - takechrom(contract,colors)
    memo[str(graph)] = rv
    return rv