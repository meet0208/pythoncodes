l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
str1='a'
l1=[]
for i in range(0,len(l),2):
    l1.extend(l[i:i+2])
    l1.append(str1)
l1.pop()
print(l1)