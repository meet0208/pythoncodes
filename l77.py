l=[[2, 1], 2, 3, [2, 4], 5, 1]
l1=[]
def decode(a):
    for i in  a:
        if isinstance(i,list):
            for j in range(len(i)):
                l1.append(i[1])
        else:
            l1.append(i)
    return l1
print(decode(l))