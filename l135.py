l=[1, 1, 2, 3, 3, 4, 4, 5]
result=[(l[i],l[i+1])for i in range(len(l)-1)]
print(result)