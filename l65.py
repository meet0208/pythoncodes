l=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
result = sorted(l, key=lambda x: not x)
print(result)

#or

l=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
l1=[]
a=len(l)
for j in range(a):
    for i in l:
        if i==0:
            l.remove(i)
            l1.append(i)
l.extend(l1)
print(l)