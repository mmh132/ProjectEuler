from itertools import chain, combinations

def powerset(iterable):
    xs = list(iterable)
    return chain.from_iterable(combinations(xs,n) for n in range(1,len(xs)+1))

def f(n):
    s = [1, 2, 3]
    while len(s) < n:
        s.append(s[-1] + s[-3])
    rv = 2**n 
    for i in powerset(s):
        if max(i) * 2 >= sum(i):
            rv -= 1
    return rv - 1

print([0,0,0] + [f(n) for n in range(4, 13)])

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
N = 23
print(berlekampMassey( [f(n) for n in range(4, N)]))