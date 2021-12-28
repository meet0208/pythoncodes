def min_max(a):
    min=a[0]
    max=a[0]
    for j in a:
        if j<min:
            min=j
        elif j>max:
            max=j
    return min,max

a=[]
b=int(input('Range: '))
for i in range(0,b):
    x=int(input(''))
    a.append(x)
print(min_max(a))
