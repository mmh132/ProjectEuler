from copy import deepcopy as dcop
def isempty(graph):
    for x in graph: 
        if graph[x] != []:
            return False
    return True
    
def removedupes(listin):
    return list(dict.fromkeys(listin))

def iscomplete(graph):
    if len(graph) > 3: return False
    for x in graph:
        if len(graph[x]) != len(graph) - 1: return False
    return True

def numedges(graph):
    edges = [] 
    for x in graph:
        for y in graph[x]:
            if sorted([x,y]) not in edges: edges.append(sorted([x,y]))
    return len(edges)

mem = dict()
def chrompolyedge(edgelist, vertices, colors):
    if len(edgelist) == 0: return colors**vertices
    if vertices*(vertices-1)/2 == len(edgelist):

        rv = 1
        for i in range(vertices):
            rv *= (colors - i)
        return rv
    edgeremov = edgelist[0]
    if str(edgelist) + str(vertices) in mem: return mem[str(edgelist) + str(vertices)]
    n1 = list(edgeremov)[0]
    n2 = list(edgeremov)[1]
    contract = dcop(edgelist)
    delete = dcop(edgelist)

    for i in range(len(edgelist)):
        if n2 in edgelist[i]:
            contract[i].remove(n2)
            contract[i].add(n1)
    ncontract = []
    [ncontract.append(x) for x in contract if x not in ncontract]
    ncontract.pop(0)
    
    delete.pop(0)

    rv = chrompolyedge(delete, vertices, colors) - chrompolyedge(ncontract, vertices - 1, colors)
    mem[str(edgelist) + str(vertices)] = rv
    return rv
memo = dict()
def chromaticpoly(graph, colors, edges):
    #if graph is edgeless, obviously its options ^ vertices
    if isempty(graph): return colors**len(graph)
    if str(graph) in memo: return memo[str(graph)]
    #if graph is complete return that
    if (len(graph)*(len(graph)-1))/2 == edges:
        print("here")
        rv = 1
        for i in range(len(graph)):
            rv *= (colors - i)
        return rv
    #otherwise, expansion deletion contract
    #first find the first node in the graph that is connected

    edremov = 1
    for todel in graph:
        x = todel
        if graph[x] != []: break
    
    n1 = x
    n2 = graph[x][0]
    contract = dcop(graph)
    delete = dcop(graph)

    #for contraction, add all adjacencies of second node to main node, then delete the second

    #add all adjacencies of n2 to n1
    contract[n1] += graph[n2]
    #remove the pointer to itsself
    contract[n1].remove(n1)
    #remove all duplicate pointers
    contract[n1] = removedupes(contract[n1])
    #remove node 2 from the graph
    contract.pop(n2)
    #replace all n2 adjacencies with n1 adjacencies
    for c in contract:
        if n2 in contract[c]: contract[c].remove(n2); contract[c] += [n1]; edremov +=1
        contract[c] = removedupes(contract[c]) 
    while n1 in contract[n1]: contract[n1].remove(n1)

    #for delete, same edge must be  removed

    #n1 gets all adjacencies except of edge to be removed
    delete[n1] = graph[x][1:]
    #n2 gets all adjacencies except edge to be removes aswell
    delete[n2] = [a for a in graph[n2] if a != n1]

    rv = chromaticpoly(delete,colors, edges-1) - chromaticpoly(contract,colors, edges - edremov)
    memo[str(graph)] = rv
    return rv







