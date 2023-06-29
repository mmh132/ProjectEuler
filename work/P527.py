
def r(t): 
    if t in [0,1]: return 0
    if t % 2 == 0:
        return 1 + (1 + ((r(t/2) + r((t-1)//2)))*(t-1))/t
    else:
        return 1 + (1 + r(t//2)*2*(t-1))/t
def b(t):
    if t == 0: return 0
    div = t
    rv = 0
    i = 1
    while t>0:
        if t-2**(i-1)>0:
            rv+=(2**(i-1))*i
            t-=2**(i-1)
        else:
            rv+=t*i
            t = 0
        i+=1
    return rv/div
print(r(6))