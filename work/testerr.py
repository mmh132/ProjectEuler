from math import gcd
ct = 0
for i in range(1, 1000+1):
    for j in range(i+1, 1000+1):
        if i*j == gcd(i,j)**3:
            print(i,j,gcd(i,j),3)
            ct += 1
print(ct)