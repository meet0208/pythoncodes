list1 = [220, 330, 500]
list2 = [12, 17, 21]
l1,l2=[],[]
for x in list1:
    if x>=200:
        l1.append(x)
for y in  list2:
    if y>=20:
        l2.append(y)
print(l1, l2)

#or


print(all(x>=200 for x in list1))
print(all(x>=20 for x in list1))

