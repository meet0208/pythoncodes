l=[[1, 2, 4], [2, 4, 4], [1, 2]]
result =  [sum(x) for x in zip(*map(lambda x:x+[0]*max(map(len, l)) if len(x)<max(map(len, l)) else x, l))]
print(result)