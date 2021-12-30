from collections import defaultdict
l=['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
l1=[1, 2, 2, 3]

d=defaultdict(set)
for i,j in zip(l,l1):
   d[i]=j
print(d)
