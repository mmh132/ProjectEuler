from functools import cache

@cache
def f(dl, pd, inc, dec):
    if dl == 0: return 1 if inc and dec else 0
    rv = 0
    for i in range(10):
        rv += f(dl-1, i, i>pd or inc, i<pd or dec)
    return rv

def run(len):
    rv = 10**(len-1)
    for i in range(1, len):
        for k in range(1, 10):
            rv -= f(i-1, k, False, False)
    return rv

print(run(10))

