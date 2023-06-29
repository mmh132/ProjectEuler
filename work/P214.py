def radsieve(n):
    e = []
    facs = []
    for i in range(n+1): facs.append(e.copy())
    for i in range(2, n+1):
        if facs[i] == []:
            for k in range(i, n+1, i):
                facs[k].append(i)
    return facs

def totsub(n):
    tots = list(range(0,n+1))
    facs = radsieve(n)
    for i in range(2, len(facs)):
        for j in facs[i]:
            tots[i] *= (j-1)/j
        tots[i] = int(tots[i])
    return tots

def chains(size, length):
    tots = totsub(size)
    print("here")
    chains = [0]*(size+1)
    chains[1] = 0
    for i in range(len(tots)):
        chains[i] = 1+chains[tots[i]]
    rv = 0
    for i in range(len(chains)):
        if chains[i] == length:
            if tots[i] == i-1:
                rv += i
    return rv

print(chains(4*10**7, 25))