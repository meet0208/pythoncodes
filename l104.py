l=[1, 1, 3, 4, 4, 5, 6, 7]
l2=[4, 5, 8, 9, 6, 10]
l1=[]
def diff(a):
    l1.clear()
    for i in range(len(a)):
        if len(a)-1!=i:
            l1.append(a[i+1]-a[i])
    return l1
print(diff(l))
print(diff(l2))

