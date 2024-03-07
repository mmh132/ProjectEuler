from itertools import product
def bf(n):
    rv = 0
    for x in list(product(range(n), repeat = 4)):
        for y in list(product(range(n), repeat = 4)):
            if sum(i*i for i in x) % n == sum(j*j for j in y) % n:
                rv += 1
    return rv

def obf(n):
    rv = 0
    for x in list(product(range(n), repeat = 2)):
        for y in list(product(range(n), repeat = 2)):
            if sum(i*i for i in x) % n == sum(j*j for j in y) % n:
                rv += 1
    return rv

print(bf(4))

print([obf(i)for i in range(10)])