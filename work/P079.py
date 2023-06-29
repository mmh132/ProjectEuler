numbers = """319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716"""
attempts = numbers.splitlines()
print(attempts)
filtered = []
for i in range(len(attempts)):
    if attempts[i] not in filtered:
        filtered.append(attempts[i])
print(filtered)
filtered = sorted(filtered)
chars = []
for i in filtered:
    for k in list(i):
        if k not in chars: chars.append(k)
print(chars)