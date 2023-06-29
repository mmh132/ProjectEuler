from Graph import chromaticpoly as cpnom
from Graph import numedges as ned
from ChromaticPolynomial import ChromaticPolynom

typea = {1:[2,3,6], 2: [1,3,7], 3: [1,2,4], 4: [3,5], 5: [4,6,7], 6:[1,5,7], 7: [6,5,2]}
typeb = {1:[2,3,6], 2: [1,3,7], 3: [1,2,4], 4: [3,5], 5: [4,6,7], 6:[1,5], 7: [5,2]}

def N(a,b,c, mod):
    rv = pow(cpnom(typea, c,ned(typea))//(c*(c-1)),a,mod) * pow(cpnom(typeb, c,ned(typea))//(c*(c-1)),b,mod)
    rv = rv*c*(c-1)
    perms = 242519269720337121015504 # 100 choose 25
    return rv*perms % 10**8
print(N(25,75,1984,10**8))




ta = []
for x in typea:
    ta.append(set([a-1 for a in typea[x]]))

tb = []
for x in typeb:
    tb.append(set([a-1 for a in typeb[x]]))

print(ChromaticPolynom(ta))
print(ChromaticPolynom(tb))