def cds(sum, digits, left, mod):
    if left == 0: return sum
    for i in range(1,min(left+1, 10)):
        sum += cds(sum + i * pow(10, digits, mod) % mod, digits + 1, left-i, mod)
    return sum

print(cds(0, 0, 5, 100000))