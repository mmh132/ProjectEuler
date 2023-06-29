from Graph import chrompolyedge as chrompolynomnom
from at2 import takechrom as cpoly
edges = [{1,2}, {2,4}, {3,4}, {1,3}]

print(chrompolynomnom(edges, 4, 4))

tester = [{1,2}, {0,3}, {0,3}, {1,2}]

print(cpoly(tester, 4))