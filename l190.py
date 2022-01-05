l=[1, 2, 3, 4, 5, 6]
l1=[3, 6, 8, 9, 10, 6]
result=sorted([i*j for i in l for j in l1],reverse=True)[:3]
print(result)