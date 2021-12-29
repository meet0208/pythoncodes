t=[(1, 2), (2, 3), (3, 4)]
t1=[(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
l=[]
def convert(lst):
    l.clear()
    for i in lst:
        l.append(list(i))
    return l

print(convert(t))
print(convert(t1))