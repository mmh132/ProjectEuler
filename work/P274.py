from PEutil import sieve

def dm(p):
    if p == 3 or p == 7: return 0
    q = p//10
    r = p%10
    return (9*q*pow(r, -1, p) + 1) % p

print(dm(113))

out = 0
primes = sieve(10**7)
for p in primes:
    if p < 10: continue
    out += dm(p)
print(out + 6)

#correct sol
print(sum(pow(10, -1, p) for p in sieve(10**7) if 10%p))