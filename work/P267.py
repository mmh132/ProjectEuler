def bt(f):
    p = 0
    for i in range(1001):
        if pow(1+2*f, i)*pow(1-f, 1000-i) >= 1_000_000_000: p = 1000-i; break
    return p/1000
print(bt(1/4))

def rb(depth, curpow, curnum):
    if depth == 0: return curnum
    i = 0
    while bt(curnum + i*pow(10, -1*curpow)) <= bt(curnum + (i+1)*pow(10, -1*curpow)): i+=1
    return rb(depth-1, curpow+1, curnum + i*pow(10, -1*curpow))
magicnum = rb(15,1,0)
print(magicnum)
print(bt(magicnum))