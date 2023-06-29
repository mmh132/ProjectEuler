u=1
up=2


a=0
for k in range(100):
    print(u)
    upp=u+up
    u=up
    up=upp
    if upp<4000000 and up%2==0:
        a= a+up
print(a)

tot = 0
f1,f2,f3 = 0,0,1
while f3 < 4000000:
    f1 = f2
    f2 = f3
    f3 = f1+f2
    if f3%2 == 0: tot += f3
print(tot)