import itertools
l=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else: pass
print(l1)

#or

l.sort()
new_num = list(num for num,_ in itertools.groupby(l))
print("New List", new_num)