l=[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
l1=[]
for i in l:
    for j in i:
        if j not in l1:
            l1.append(j)
        else:
            pass
print(sorted(l1))