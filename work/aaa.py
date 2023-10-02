for i in range(100):
    for j in range(100):
        for k in range(100):
            if i*i + j*j == k*k:
                if i-j == -1 or j-k == -1:
                    print(i,j,k)