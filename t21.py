t=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
b=[]
for i in t:
    a=i[:-1]+(100,)
    b.append(a)
print(b)