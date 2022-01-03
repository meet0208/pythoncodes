l=[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
l1=[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
def cnt(a,b):
    count=0
    for i in a:
        if b in i:
            count+=1
    return count
print(cnt(l,1))
print(cnt(l1,'A'))