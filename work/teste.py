def fact_digit(x):
    p = 0
    while x!=0 :
        p += fact(x%10)
        x//=10
    return p
def fact(x):
    for i in range(2,x):x*=i
    return x

for i in range(10,10**7):
    if fact_digit(i)==i:
        print(i)

print(fact_digit(40585))