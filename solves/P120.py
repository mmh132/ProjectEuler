def rmax(a):
    return 2 * a * ((a-1)//2)

print(sum([rmax(i) for i in range(3, 1000 + 1)]))