l=[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
d={}
for i in l:
    d[i]=d.get(i,0)+1
a=max(d.values())
for i,j in d.items():
    if a==j:
        print(i)

