my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
l=[]
for value in my_dict.values():
    l.append(value)
l.sort(reverse=True)
l1=[]
l=l[:3]
for i,j in my_dict.items():
    if j in l:
       l1.append(i)
print(l1)