num=[1,1,2,3,5,1,2,3,5,6,2]
d=dict()
for i in num:
    d[i]=d.get(i,0)+1
print(sum(d.values()))

# or

from collections import Counter
num = [2,2,4,6,6,8,6,10,4]
print(sum(Counter(num).values()))