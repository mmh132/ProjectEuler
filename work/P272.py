def bf(p, k):
    for i in range(1, p ** k):
        if i * i * i % p ** k == 1:
            print(i)

bf(11, 4)
print(3**5)

#PRODUCT OF 5 PRIMES WITH ARBITRARY EXPONENTS WHO ARE ALL CONGRUENT TO 1 MODULO 3
#ALSO CAN HAVE ARBITRARY NUMBER OF CONGRUENT TO 2 PRIMES, WITH ARBITRARY EXPONENTS

