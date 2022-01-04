t=[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
n=int(input('Element position, needs to extract: '))
result=[]
for i in t:
    result.append(i[n])

print(result)