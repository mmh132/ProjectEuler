inset = [pow(i,i,250) for i in range(1,250251)]
coeffs = [0]*(251)
cop = coeffs.copy()
coeffs[0] = 1
for v in range(len(inset)):
    i = inset[v]
    cop = coeffs.copy()
    for k in range(len(coeffs)):
        if cop[k] != 0:
            coeffs[(k+i) % 250] = (coeffs[(k+i) % 250] + cop[k]) % 10**16
print(coeffs[0]%10**16-1)