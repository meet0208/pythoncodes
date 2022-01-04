l=[(2, 7), (2, 6), (1, 8), (4, 9)]
result_max = max([abs(x * y) for x, y in l] )
result_min = min([abs(x * y) for x, y in l] )
print((result_max,result_min))