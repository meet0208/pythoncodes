l=[[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
d={}
for i in l:
    d[tuple(i)]=d.get(tuple(i),0)+1
print(d)