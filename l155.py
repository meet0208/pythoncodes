l=[2, 4, 7, 0, 5, 8]
l1=[3, 3, -1, 7]
result=[i+j for (i,j) in zip(l,l1)]+l[len(l1):]
print(result)