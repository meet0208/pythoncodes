str1='w3resource'
d={}
for i in str1:
    d[i]=d.get(i,0)+1
print(d)