def bf(v, l, t):
    if l == t:
        return 1 if len(v) == t else 0
    rv = 0 
    for i in range(max(l-3, 1), min(l+3, t) + 1):
        if i not in v:
            v.add(i)
            rv += bf(v, i, t)
            v.remove(i)
    return rv

print([bf({1}, 1, i) for i in range(17)])

def berlekampMassey(s,mod=0):
	C = [1]
	B = [1]
	L = 0
	m = 1
	b = 1
	
	for n in range(len(s)):
		d = s[n] + sum(C[i] * s[n-i] for i in range(1,L+1))
		if mod: d %= mod
		if d == 0:
			m += 1
			continue
		
		T = C[:]
		coef = d*pow(b,-1,mod) if mod else d//b
		nb = [0]*m + [coef*x % mod if mod else coef*x for x in B]
		C += [0] * (len(nb)-len(C))
		for i in range(len(nb)):
			C[i] -= nb[i]

		if 2*L <= n:
			L = n+1 - L
			B = T
			b = d
			m = 0
		
		m += 1
	
	ret = [-x for x in C[1:]]
	if mod: ret = [x%mod for x in ret]
	return ret

