str=input('Enter a string: ')
print(type(str))
a=[]
for i in str:
    a.append(i)
b=tuple(a)
print(b,type(b))