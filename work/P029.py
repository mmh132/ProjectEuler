nnums = []
stor = 0
for a in range(2,101):
    for b in range(2,101):
        stor = a**b
        if stor not in nnums:
            nnums.append(stor)
print(len(nnums))