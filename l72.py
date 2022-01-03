l= [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
l1=[]
def flatten(a):
    for i in a:
        if isinstance(i,list):
            for y in i:
                l1.append(y)
        else:
            l1.append(i)
    return l1

print(flatten(l))