l=[1, 2, 3, 4, 5, 6, 7]
result =   [(x + y) / 2.0 for (x, y) in zip(l[:-1], l[1:])]
print(result)