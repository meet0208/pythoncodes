l=[[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
result = list(set.intersection(*map(set, l)))
print(result)

# or

for i in range(len(l)-2):
    print(list(set(l[i]) & set(l[i+1]) & set(l[i+2])))