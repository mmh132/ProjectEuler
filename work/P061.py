def triangle(n):
    return (n*(n+1))/2
def square(n):
    return n**2
def pentagonal(n):
    return 0.5*(n*(3*n-1))
def hexagonal(n):
    return n*(2*n-1)
def heptagonal(n):
    return 0.5*(5*n-3)*(n)
def octagonal(n):
    return n*(3*n-2)

triangles = []
i = 1
while triangle(i)<1000:
    i+=1
while triangle(i)<10000:
    triangles.append(int(triangle(i)))
    i+=1
print(triangles)

squares = [32**2]
for i in range(33,100):
    squares.append(i**2)
print(squares)

pentagonals = []
i = 1
while pentagonal(i)<1000:
    i+=1
while pentagonal(i)<10000:
    pentagonals.append(int(pentagonal(i)))
    i+=1
print(pentagonals)

hexagonals = []
i = 1
while hexagonal(i)<1000:
    i+=1
while hexagonal(i)<10000:
    hexagonals.append(int(hexagonal(i)))
    i+=1
print(hexagonals)

heptagonals = []
i = 1
while heptagonal(i)<1000:
    i+=1
while heptagonal(i)<10000:
    heptagonals.append(int(heptagonal(i)))
    i+=1
print(heptagonals)

octagonals = []
i = 1
while octagonal(i)<1000:
    i+=1
while octagonal(i)<10000:
    octagonals.append(int(octagonal(i)))
    i+=1
print(octagonals)

end = 0
for i in range (len(octagonals)):
    end = octagonals[i]%100