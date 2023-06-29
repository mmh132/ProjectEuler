trinums = []
for i in range(284,100001):trinums.append((i*(i+1))/2)
pentnums = []
for i in range(164,100001):pentnums.append((i*(3*i-1))/2)
hexnums = []
for i in range(143,100001):hexnums.append((i*(2*i-1)))
for i in range(len(hexnums)): 
    if hexnums[i] in trinums and hexnums[i] in pentnums: print(hexnums[i])