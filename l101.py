l=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
l1=[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
result=sorted(l,key=sum)
print(result)
result1=sorted(l1,key=sum)
print(result1)