l=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
d={}
for i in l:
    for j in i:
        d[j]=d.get(j,0)+1
print(d)