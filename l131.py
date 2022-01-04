l=[1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
d={}
for i in l:
    d[i]=d.get(i,0)+1
print(list((d.keys())),list(d.values()))