def ispalindrome(n):
    if str(n) != str(n)[::-1]:
        return False
    binary = str(bin(n))[2:]
    if str(binary) != str(binary)[::-1]:
        return False
    return True

sum = 0
for i in range(1,1000000):
    if ispalindrome(i): sum+=i
print(sum)