fibseq = []
for i in range(1,56):
    fibseq.append((100003 - 200003*i + 300007*i**3)%1000000)
fibseq.append((fibseq[-24] + fibseq[-55])%1000000)
print(len(fibseq))