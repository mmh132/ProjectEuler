coins = [1,2,5,10,20,50,100,200]
memo = dict()
def currency(p):
    if p == 0: return 1
    if p<0: return 0
    if p in memo: return memo[p]
    rv = 0
    for i in coins:
        rv += currency(p-i)
    memo[p] = rv
    return rv
print(currency(200))



