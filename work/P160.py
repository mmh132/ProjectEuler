rv = 1
x = 2**30-1
for i in range(1,10**12+1):
    if i & x == x:
        print (i/10**12)
    rv *= i
    while rv%10 == 0: rv//=10
    rv %= 10**7
print(rv)
