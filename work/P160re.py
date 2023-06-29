def things(b, n):
    rv = 0
    exp = b
    while exp<n:
        rv += n//exp
        exp*=b
    return rv
f = things(5, 10**6+1)
t = f
rv = 1
for i in range(1,10**6+1):
    x = i
    while x%5==0 and f>0: x//=5; f-=1
    while x%2==0 and t>0: x//=2; t-=1
    rv*=x
    rv%= 10**7

print(pow(rv, 10**6, 10**7))
