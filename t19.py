l = [(1,2),(1,5), (3,4), (8,9)]
d={}
for a,b in l:
    d.setdefault(a,[]).append(b)
print(d)