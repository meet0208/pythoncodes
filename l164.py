l=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
l1=[]
for i in l:
    if i%2==0 and i>45:
        l1.append(i)
print(len(l1))