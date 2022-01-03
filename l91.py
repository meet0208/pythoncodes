l=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
def max_l(a):
    max_length = max(len(i) for i in a)
    max_list = max(a,key=len)
    return (max_length,max_list)
def min_l(b):
    min_length = min(len(i) for i in b)
    min_list = max(b, key=len)
    return (min_length,min_list)

print(max_l(l))
print(min_l(l))
