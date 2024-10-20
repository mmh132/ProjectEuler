# find the shortest linear recurrence which matches s
def polymul(a,b,mod=0):
	c = [0] * (len(a)+len(b)-1)
	for i in range(len(a)):
		for j in range(len(b)):
			c[i+j] += a[i] * b[j]
			if mod: c[i+j] %= mod
	return c

def berlekamp_massey(arr):
    # 返り値は数列の後ろに掛けるやつが前（伝われ）
    n = len(arr)
    bs = [1]
    cs = [1]
    y = 1
    for ed in range(1, n+1):
        len_cs, len_bs = len(cs), len(bs)
        x = sum(c * arr[ed-len_cs+i] % mod for i, c in enumerate(cs)) % mod
        bs.append(0)
        len_bs += 1
        if x == 0:
            continue
        freq = x * pow(y, mod-2, mod) % mod
        if len_cs < len_bs:
            tmp = cs[:]
            cs = [0] * (len_bs - len_cs) + cs
            cs = [(c-b*freq)%mod for c, b in zip(cs, bs)]
            bs = tmp
            y = x
        else:
            for i, b in enumerate(reversed(bs), 1):
                cs[-i] = (cs[-i] - freq * b) % mod
    return [-c % mod for c in cs[-2::-1]]

# find the kth term of a linear recurrence with coefficients c, initial values s, and starting index k0
def linearRecurrence(c,s,k0,k,mod=0):
	def mul(a,b):
		ret = polymul(a,b,mod)
		for i in range(len(ret)-1,n-1,-1):
			for j in range(n-1,-1,-1):
				ret[i-j-1] += ret[i] * c[j]
				if mod: ret[i-j-1] %= mod
		return ret[:n]

	n = len(c)
	assert len(c) <= len(s)

	a = [c[0]] if n == 1 else [0,1]
	x = [1]
	k -= k0
	while k:
		if k % 2: x = mul(x,a)
		a = mul(a,a)
		k //= 2
	x = x[:n] + [0] * (n - len(x))

	ret = 0
	for i in range(n):
		ret += x[i] * s[i]
		if mod: ret %= mod
	return ret

# find the kth term of a linear recurrence with initial values s and starting index k0
def linearExtend(s,k0,k,mod=0):
	return linearRecurrence(berlekampMassey(s,mod),s,k0,k,mod)


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
N = 20
print(berlekampMassey([bf({1}, 1, i) for i in range(N)]))
