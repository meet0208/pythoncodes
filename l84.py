l=[22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
l=list(map(round,l))
print(min(l))
print(max(l))
number=sorted(list(set(l)))

for i in number:
    print(i*5,end=' ')