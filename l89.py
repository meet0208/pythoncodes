list1 = [[1, 3], [5, 7], [9, 11]]
list2 = [[2, 4], [6, 8], [10, 12, 14]]
l2=[]
for (i,j) in zip(list1,list2):
    l2.append((i+j))
print(l2)