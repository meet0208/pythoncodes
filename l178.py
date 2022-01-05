l=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
str1=20
l1=[]
for i in range(0,len(l),4):
    l1.extend(l[i:i+4])
    l1.append(str1)
l1.pop()
print(l1)