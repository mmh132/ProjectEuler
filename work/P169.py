cap = 10**20
powers = []
memo = dict()
i = 0
while 2**i<cap: powers.append(2**i); i+=1
def recbuild(number, pow):
    if number > powers[pow]*4: return 0
    if number == 0: return 1
    if number < 0 or pow == -1: return 0
    if (number,pow) in memo: return memo[(number,pow)]
    rv = 0
    for i in range(3):
        rv += recbuild(number-powers[pow]*i, pow-1)
    memo[(number,pow)] = rv
    return rv
print(recbuild(cap, i-1))