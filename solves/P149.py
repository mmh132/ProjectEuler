def msa(a):
    best = -1
    cs = 0
    for i in a:
        cs = max(i, cs+i)
        best = max(best, cs)
    return best

lfg = [(100003 - 200003*k + 300007*k**3) % 10**6 - 5*10**5 for k in range(1, 56)]
for _ in range(4*10**6 - 55):
    lfg.append( (lfg[-24] + lfg[-55] + 10**6)%10**6 - 5*10**5)

#rows:
br = 0
for i in range(2000):
    br = max(br, msa([lfg[2000*i + k] for k in range(2000)]))

#cols:
for i in range(2000):
    br = max(br, msa([lfg[2000*k + i] for k in range(2000)]))

#diag
for i in range(2000):
    br = max(br, msa([lfg[2000*k + i + k] for k in range(2000 - i)]))

#antidiag
for i in range(2000):
    br = max(br, msa([lfg[2000*k + 2000-1-i-k] for k in range(2000-i)]))

print(br)