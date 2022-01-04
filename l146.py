l=[10, 2, 56]
l1=[10, 20, 4, 5, 'b', 70, 'a']
l2=[10, 20, -4, 5, -70]
def sumlist(a):
    sum=0
    for i in a:
        for j in str(i):
            if j.isdigit():
                sum+=int(j)
    return sum

print(sumlist(l))
print(sumlist(l1))
print(sumlist(l2))