min = 1504170715041707
mod = 4503599627370517
cur = min
sum = min
while min != 0:
    if cur<min: sum += cur; min = cur; print(str(cur) + " added to make " + str(sum))
    cur += 1504170715041707
    if cur>mod: cur-= mod
print(sum)
