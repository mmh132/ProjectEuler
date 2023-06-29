from Graph import chromaticpoly
from Graph import chrompolyedge as edgepoly
from at2 import takechrom 
from finalGraph import takepoly
trigraph = {1: [2], 2: [1,3,4], 3: [2,5], 4: [2,6], 5: [3,7,8], 6: [4,8,9], 7: [5,10], 8: [5,6,11],
9: [6,12], 10: [7,13,14], 11: [8,14,15], 12: [9,15,16], 13: [10,17], 14: [10,11,18], 15: [11,12,19], 
16: [12,20], 17: [13,21,22], 18: [14,22,23], 19: [15,23,24], 20: [16,24,25], 21: [17,26], 22: [17,18,27],
23: [18,19,28], 24: [19,20,29], 25: [20,30], 26: [21,31,32], 27: [22,32,33], 28: [23,33,34], 
29: [24,34,35], 30: [25,35,36], 31: [26,37], 32: [26,27,38], 33: [27,28,39], 34: [28,29,40],
35: [29,30,41], 36: [30,42], 37: [31,43,44], 38: [32,44,45], 39: [33,45,46], 40: [34,46,47],
41: [35,47,48], 42: [36,48,49], 43: [37,50], 44: [37,38,51], 45: [38,39,52], 46: [39,40,53],
47: [40,41,54], 48: [41,42,55], 49: [42,56], 50: [43,57,58], 51: [44,58,59], 52: [45,59,60],
53: [46,60,61], 54: [47,61,62], 55: [48,62,63], 56: [49,63,64], 57: [50], 58: [50,51], 59:[51,52],
60: [52,53], 61: [53,54], 62: [54,55], 63: [55,56], 64: [56]}

#triangletest = {'A': ['B', 'C'], 'B':['A','C'], 'C':['A','B']}
#print(str(triangletest))
#print(chromaticpoly(triangletest, 3))
#print(chromaticpoly(trigraph, 3))
#edgelist = []
#for x in trigraph:
    #for i in(trigraph[x]):
        #edgelist.append({x,i})
#nlist = []
#[nlist.append(x) for x in edgelist if x not in nlist]
#print(nlist)
#print(edgepoly(nlist, 64, 3))
import time
start_time = time.time()
newl = []
for x in trigraph:
    newl.append(set([a-1 for a in trigraph[x]]))
#print(newl)
print(takechrom(newl, 3))

print("--- %s seconds ---" % (time.time() - start_time))

start_time1 = time.time()
print(takepoly(newl,3,0))
print("--- %s seconds ---" % (time.time() - start_time1))