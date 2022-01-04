l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
l1=[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
result=[[n for n in lst if n in l] for lst in l1]
print(result)
