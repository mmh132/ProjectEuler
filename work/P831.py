from math import comb, log, exp
import decimal

decimal.getcontext().prec = 80

M = 10
f = [0, decimal.Decimal(0)]
while len(f) < 7*M + 10:
    f.append(f[-1] + decimal.Decimal(len(f)).ln())

tp = decimal.Decimal(0)
for j in range(1, M+1):
    if 7*j >= M:
        if (M-j) & 1: 
            tp -= decimal.Decimal(f[M] - f[j] - f[M-j] + f[7*j+5] - f[M+5] - f[7*j-M]).exp()

        else:
            tp += decimal.Decimal(f[M] - f[j] - f[M-j] + f[7*j+5] - f[M+5] - f[7*j-M]).exp()

print(tp)



