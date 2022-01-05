l=[1, None, 5, 4, None, 0, None, None]
l1=[]
for i in range(len(l)):
    if l[i]==None:
        l1.append(i)
print(l1)