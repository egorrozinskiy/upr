inp = open("int_data.txt")
file = str(inp.read())
file = file[:-1]
counts = []
ch = list(map(int,file.split(" ")))
for i in range(max(ch)+1):
    counts.append(ch.count(ch[i]))
print('kol-vo ',i,'rav:',ch.count(ch[i]))
print ('chasto:',counts.index(max(counts)))
print ('redko:',counts.index(min(counts)))
print ('razlichnie:',(101-counts.count(0)))