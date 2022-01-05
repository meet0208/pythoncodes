l=[1, 2, 3, 4, 5, 6]
l1=[7, 8, 5, 2, 10, 12]
a=[]
for i in range(len(l)):
    for j in range(len(l1)):
        if l1[j]==l[i]:
            a.append(i)
print(a)
