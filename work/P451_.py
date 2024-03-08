N = 2*10**7
cmp, primes, lpf, exp = [0]*(N+1), [], [0]*(N+1), [0]*(N+1)
lpf[1] = 1
for i in range(2, N+1):
    if not cmp[i]:
        primes.append(i)
        lpf[i] = i
        exp[i] = 1
    for j in primes:
        if i*j > N: break
        cmp[i*j] = 1
        if i%j:
            exp[i*j] = 1
            lpf[i*j] = lpf[i]
        else:
            exp[i*j] = exp[i] + 1
            lpf[i*j] = lpf[i]
            break

def factor(n):
    if n == 1: return []
    p, e = lpf[n], exp[n]
    return factor(n//(p**e)) + [(p, e)] 

print(factor(100))