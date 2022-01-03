l=[1, 1, 3, 4, 5, 6, 7]
l1=[0, 1, 2, 3, 4, 5, 7]
l2=[0, 1, 2, 3, 4, 5, 7]
result=[]
for i,j,k in zip(l,l1,l2):
    if (i==j==k):
        result.append(i)
print(result)