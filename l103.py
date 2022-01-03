l=[1, 1, 3, 4, 4, 5, 6, 7]
l1=[]
l2=[]

for i in l:
    if i not in l1:
        l1.append(i)
    else:
        l2.append(i)
print(l2)

#or

from itertools import groupby

def extract_elements(nums, n):
    result = [i for i, j in groupby(nums) if len(list(j)) == n]
    return result

nums1 = [1, 1, 3, 4, 4, 5, 6, 7]
n = 2
print(extract_elements(nums1,n))