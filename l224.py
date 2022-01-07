from collections import Counter
l=[1, 2, 2, 3, 4, 4, 5]
result=[i for i,j in Counter(l).items() if j>1]
print(result)