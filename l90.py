l=[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
l1 = [[2, 4], [[6,8], [4,5,8]], [10, 12, 14]]

def cnt(a):
    count = 0
    for i in a:
        count+=1
    return count
print(cnt(l))
print(cnt(l1))

#or

def cont(a):
    return len(a)
print(cont(l))
print(cont(l1))
