l=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
n=int(input('enter index: '))
def rec(a,b):
    l1=[]
    for i in a:
        l1.append(i[b])
    return l1
print(rec(l,n))
