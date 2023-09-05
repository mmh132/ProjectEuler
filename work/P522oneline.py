f,m,n = [1,1], 135707531, 12344321
for i in range(2, n+1): f.append(f[-1]*i % m)
print((f[n]*pow(f[n-1],-1,m)*pow(f[1],-1,m)*pow(n-2, n-1, m)*(n-1) + sum(f[n]*pow(k,-1,m)*pow(f[n-k],-1,m)*pow(n-k-1,n-k,m) % m for k in range(2, n-1))) % m)