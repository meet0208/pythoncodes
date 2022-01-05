l=[[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
result=set(l[0]).intersection(*l)
print(list(result))