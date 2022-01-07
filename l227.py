import math
l=[2.1, 1.2]
l1=[2.3, 3.4]
def diff(l,l1):
    (a,b)=(set(map(math.floor,l)),set(map(math.floor,l1)))
    return [item for item in l if math.floor(item) not in b] + [item for item in l1 if math.floor(item) not in a]
print(diff(l,l1))