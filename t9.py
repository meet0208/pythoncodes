t=(1,2,3,4,2,41,1)
d=dict()
for i in t:
    d[i]=d.get(i,0)+1
print(d)
for j,k in d.items():
    if k>=2:
        print(j)