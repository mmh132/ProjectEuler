N, MOD = 12344321, 135707531

# der = [1,0]
# for i in range(2, N+1):
#     x = (der[-1] + der[-2])*(i-1)
#     x %= MOD
#     der.append(x)
# print(der)
fac = [1,1]
for i in range(2, N+1):
    fac.append(fac[-1]*i % MOD)

c = [fac[N]*pow(fac[N-k],-1, MOD)*pow(fac[k],-1, MOD) % MOD for k in range(N+1)]

out = c[1]*pow(N-1-1, N-1, MOD)*pow(N-1,1,MOD)

# for k in range(1, N-1):
#     x = c[k]*pow(N-k-1, N-k, MOD)*pow(N-k,k,MOD)
#     print(N,k,x)
#     x %= MOD
#     out = (out + x) % MOD

for k in range(2, N-1):
    x = c[k]*fac[k-1]*pow(N-k-1,N-k,MOD)
    x %= MOD
    out = (out + x) % MOD

print(out)


# out = 0
# for k in range(1, N//2+1):
#     x = c[2*k]*pow(N-k, N-2*k, MOD)
#     print(k,x)
#     x %= MOD
#     out = (out + x) % MOD

# print(out)

# for k in range(1, N-1):
#     x = k*c[k]*der[N-k]*pow(N-k, k, MOD)
#     print(N,k,x)
#     x %= MOD
#     out = (out + x) % MOD

# print(out)

# for k in range(1, N-1):
#     x = c[k]*fac[N-k-1]*pow(N-k,k,MOD)
#     print(k,x)
#     x %= MOD
#     out = (out - x) % MOD

# print(out - fac[N-1] % MOD)

